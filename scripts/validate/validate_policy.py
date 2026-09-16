#!/usr/bin/env python3
"""Policy validator — the guardrails that keep this repository honest and legal.

Checks:
  1. SECRET SHAPES      no credential-looking strings anywhere in tracked files
  2. COLLECTION ETHICS  no private chain-of-thought, leaked system prompts, PII,
                        or vendored private-repository content
  3. LICENSE POLICY     no vendored code from a repository whose license is NONE
  4. HALLUCINATION FIREWALL  no "latest/best/current" superlative asserted without
                        verified_at nearby
  5. QUARANTINE         experimental/ and pending-* files are not referenced as
                        authoritative from core knowledge
  6. GENERATED FILES    metadata/ + indexes/ carry a generator marker

Usage:
    python3 scripts/validate/validate_policy.py
    python3 scripts/validate/validate_policy.py --strict
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402
from lib.exclusions import load_exclusions  # noqa: E402
from lib.sanitize import any_injection_marks, untrusted  # noqa: E402

SECRET_PATTERNS = {
    "github_pat": re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    "github_oauth": re.compile(r"\bghp_[A-Za-z0-9]{30,}"),
    "github_fine": re.compile(r"\bgho_[A-Za-z0-9]{30,}"),
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}"),
    "anthropic_key": re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{20,}"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "slack_token": re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}"),
    "private_key_block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "google_api_key": re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    "stripe_secret": re.compile(r"\bsk_live_[A-Za-z0-9]{16,}"),
    "jwt": re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"),
    "supabase_service": re.compile(r"\bsbp_[A-Za-z0-9]{20,}"),
    "npm_token": re.compile(r"\bnpm_[A-Za-z0-9]{30,}"),
    "huggingface_token": re.compile(r"\bhf_[A-Za-z0-9]{20,}"),
}

# Strings that indicate forbidden content rather than discussion *about* it.
FORBIDDEN = [
    (re.compile(r"(?i)\bBEGIN (?:PRIVATE )?CHAIN[- ]OF[- ]THOUGHT\b"), "private chain-of-thought dump"),
    (re.compile(r"(?i)<\s*(?:hidden|secret|internal)[-_ ]?(?:cot|reasoning|thought)\s*>"),
     "private reasoning block"),
    (re.compile(r"(?i)leaked system prompt(?: of| for)?\s*[:=]?\s*\n\s*[\"']?(you are|assistant)"),
     "leaked system prompt content"),
    (re.compile(r"(?i)\bpassword\s*[:=]\s*['\"][^'\"]{6,}['\"]"), "hardcoded password"),
    (re.compile(r"(?i)\bapi[_-]?key\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}['\"]"), "hardcoded API key"),
    (re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), "US SSN-shaped PII"),
    (re.compile(r"(?i)\bprivate (?:repository|repo) (?:contents?|source)\b\s*:"), "private repo content"),
]

# Discussion ABOUT these topics is allowed and expected; only reproduction is banned.
ALLOWED_DISCUSSION = re.compile(
    r"(?i)(never|do not|don't|must not|forbidden|excluded|policy|prohibited|risk|attack|defend|"
    r"detection|guardrail|threat|avoid)")

SUPERLATIVE = re.compile(r"(?i)\b(the\s+)?(latest|newest|current(?:ly)?\s+best|best|fastest|"
                         r"most\s+popular|state[- ]of[- ]the[- ]art|sota)\b")
VERIFIED_NEAR = re.compile(r"(?i)(verified_at|verified\s+\d{4}-\d{2}-\d{2}|stars_checked_at|"
                             r"as of \d{4}-\d{2}-\d{2}|\d{4}-\d{2}-\d{2})")


def tracked_files() -> List[Path]:
    try:
        out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=ROOT,
                             capture_output=True, text=True, timeout=60)
        files = [ROOT / line for line in out.stdout.splitlines() if line]
        return [f for f in files if f.exists() and f.is_file()]
    except Exception:
        skip = {".git", ".cache", "node_modules", ".venv", "__pycache__"}
        return [p for p in ROOT.rglob("*")
                if p.is_file() and not any(s in p.parts for s in skip)]


# ---------------------------------------------------------------------------
# The license hard override, applied to markdown and not only to code (H-5)
# ---------------------------------------------------------------------------

LICENSE_RISKS = ("no-license-do-not-redistribute", "custom-license-review-before-vendoring")

# Naming a repository is not vendoring it. These paths exist to name repositories, so a
# mention there is the file doing its job; scanning them produced most of the warnings that
# trained reviewers to ignore this check. This is one list rather than an allow-and-a-deny:
# a second "relevant paths" filter would have excluded README.md for saving three warnings,
# and two lists describing one rule is how a control becomes hard to reason about.
# Everything not listed here warns, and the vendoring-shaped error below applies to every
# path without exception, so this exemption cannot hide copied content.
LICENSE_MENTION_OK = (
    "scripts/",                 # generators and validators must name what they process
    "tests/",                   # regression tests name the records they assert on
    "metadata/",                # the registry itself is the source of truth
    "indexes/",                 # generated listings
    "repositories/",            # generated cards and category tables render the registry
    "CHANGELOG.md",             # the record of decisions has to be able to name them
    "REVIEW-REPORT.md",         # so does the record of what was found and fixed
)


# A fenced block at least this long, attributed to the named repository, is the shape of
# copied content rather than a passing reference. Both numbers are deliberately conservative:
# the error has to be worth stopping a build over.
VENDOR_BLOCK_MIN_LINES = 15
VENDOR_ATTRIBUTION_LINES = 3

FENCE = re.compile(r"^\s*(```|~~~)\s*([A-Za-z0-9_+.#-]*)")

# Prose fences are not candidates for vendored content — see vendored_block_at. A bare fence
# still is: pasted code and output samples both use one, and copied content is far more likely
# to arrive unlabeled than to announce itself as `text`.
PROSE_FENCE_LANGS = {"text", "txt", "plaintext", "plain", "prose"}

# Wording that establishes a passage is *stating* the no-copy rule rather than breaking it.
STATES_NO_COPY = re.compile(
    r"(?i)(do not (?:copy|vendor|redistribute)|never (?:copy|vendor|redistribute)|"
    r"reference[- ]only|link only|no license|license:? *null|licen[cs]e risk|"
    r"respect(?:ing)? the (?:upstream )?licen[cs]e|do-not-redistribute|review-before-vendoring)")


def load_license_risks() -> Dict[str, str]:
    """`slug -> license_risk` for every repository whose license carries a consequence.

    Read from the registry rather than from the cards, because the registry is the source of
    truth the cards are generated from. Checking the cards against their own content would
    only prove the generator is self-consistent.
    """
    out: Dict[str, str] = {}
    reg = ROOT / "metadata" / "repositories.json"
    if not reg.exists():
        return out
    for r in json.loads(reg.read_text()).get("repositories", []):
        risk = r.get("license_risk")
        slug = r.get("slug")
        if slug and risk in LICENSE_RISKS:
            out[str(slug)] = str(risk)
    return out


def fenced_blocks(text: str) -> List[Tuple[int, int, str]]:
    """(first_line, last_line, language) of every fenced block, lines 0-indexed.

    An unterminated fence is ignored rather than swallowed to end-of-file: a card that ends
    mid-fence is a different defect, and treating the rest of the document as copied code
    would turn one broken fence into a vendoring accusation.
    """
    spans: List[Tuple[int, int, str]] = []
    open_at = None
    lang = ""
    for i, line in enumerate(text.splitlines()):
        m = FENCE.match(line)
        if m:
            if open_at is None:
                open_at, lang = i, m.group(2).lower()
            else:
                spans.append((open_at, i, lang))
                open_at = None
    return spans


def vendored_block_at(text: str, slug_rx) -> Optional[Tuple[int, int, int, str]]:
    """A long code fence the named repository is *attributed to*, or None.

    Proximity alone is not evidence of copying. Treating it as such accused
    `skills/database-design/SKILL.md` of vendoring `pgvector/pgvector` because the skill
    mentions it in one paragraph and carries its own original modelling rules 30 lines away.
    An error that cries vendoring on original work gets argued with once and then ignored, so
    the signal has to be attribution: the slug appears inside the fence (the way a copied
    header comment survives), or in the prose immediately around it (the way "adapted from X"
    is actually written).

    Two further exclusions, both learned from false positives on the committed corpus:

      * **prose fences are not candidates.** This repository sets authored prose in aligned
        ```text blocks. `knowledge/agent-skills/skill-format.md` states its authoring rules
        that way, and rule 4 is "Never copy external content … (anthropics/skills,
        openai/skills) — they are reference-only." Reading that as vendoring inverts the
        finding: the passage is the policy being stated, in the file that states it.
      * **a passage that states the no-copy rule is compliance, not violation.** Failing the
        build over the sentence that enforces the policy would remove the incentive to write
        it, which is the opposite of what the override is for.
    """
    lines = text.splitlines()
    best = None
    for start_ln, end_ln, lang in fenced_blocks(text):
        if lang in PROSE_FENCE_LANGS:
            continue
        inner = end_ln - start_ln - 1
        if inner < VENDOR_BLOCK_MIN_LINES:
            continue
        lo = max(0, start_ln - VENDOR_ATTRIBUTION_LINES)
        hi = min(len(lines), end_ln + VENDOR_ATTRIBUTION_LINES + 1)
        inside = next((lines[i].strip() for i in range(start_ln + 1, end_ln)
                       if slug_rx.search(lines[i])), "")
        adjacent = "" if inside else next(
            (lines[i].strip() for i in range(lo, hi)
             if not (start_ln <= i <= end_ln) and slug_rx.search(lines[i])), "")
        if not (inside or adjacent):
            continue
        if STATES_NO_COPY.search("\n".join(lines[lo:hi])):
            continue
        where = ("inside the block" if inside
                 else f"within {VENDOR_ATTRIBUTION_LINES} lines of the block")
        if best is None or inner > best[2]:
            best = (start_ln, end_ln, inner, f"{where}: {(inside or adjacent)[:90]}")
    if not best:
        return None
    s, e, inner, attribution = best
    return s, e, inner, attribution


def card_path_for(slug: str, category: str) -> str:
    return f"repositories/{category}/{slug.replace('/', '--').lower()}.md"


def check_license_policy(files: List[Path], risks: Dict[str, str]) -> Tuple[List[str], List[str]]:
    """Enforce the license override on prose, not only on source code.

    The override always worked in the data: every no-license record carried
    `license_risk: no-license-do-not-redistribute`. What did not work was the enforcement.
    The old check matched the repository *name* alone, so it fired on every script that used
    the word "skills", and it scanned only `.ts/.js/.py/.go/.rs` — while the realistic
    vendoring target in this repository is a **markdown article** copying prose or a skill.
    A warning that is 90% noise and blind to the actual risk is worse than no warning,
    because it is read once and then skipped.

    Two severities, because they are two different situations:

      * a **mention** of a risky repository in prose is a warning. Naming `anthropics/skills`
        in order to say "do not copy this" is legitimate and necessary.
      * a mention sitting next to a long fenced code block is an **error**. That is the shape
        of vendored content, and the override exists to prevent exactly that.
    """
    errs: List[str] = []
    warns: List[str] = []
    if not risks:
        return errs, warns

    categories: Dict[str, str] = {}
    reg = ROOT / "metadata" / "repositories.json"
    if reg.exists():
        for r in json.loads(reg.read_text()).get("repositories", []):
            if r.get("slug"):
                categories[str(r["slug"])] = str(r.get("category") or "")

    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        if f.suffix in (".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".woff", ".woff2"):
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        lines = text.splitlines()
        mention_ok = rel.startswith(LICENSE_MENTION_OK)

        for slug, risk in risks.items():
            # A card naming the repository it is *about* is not a vendoring risk, and the card
            # is required to carry the policy marker — checked separately below.
            if rel == card_path_for(slug, categories.get(slug, "")):
                continue
            rx = re.compile(rf"(?i)(?<![\w/.-]){re.escape(slug)}(?![\w/-])")
            if not rx.search(text):
                continue

            block = vendored_block_at(text, rx)
            if block:
                start, end, inner, attribution = block
                errs.append(
                    f"{rel}: attributes a {inner}-line code block (lines {start + 1}-{end + 1}) to "
                    f"'{slug}', whose license is {risk} — {attribution}. That is the shape of "
                    f"vendored content, and this repository does not redistribute from a "
                    f"repository whose license carries that consequence. Replace the block with "
                    f"a link and a summary written here.")
            elif not mention_ok:
                warns.append(
                    f"{rel}: names '{slug}', whose license is {risk}. A reference and a link "
                    f"are fine; copying content from it is not.")
    return errs, warns


def check_cards_state_license_policy(risks: Dict[str, str]) -> Tuple[List[str], List[str]]:
    """Every card for a risky repository must state the policy in the markdown itself.

    The generator emits `license_risk` into the card frontmatter and a banner above the fold.
    This check is what keeps that true: a generator change, a hand edit to a "GENERATED — DO
    NOT EDIT" file, or a card written before the rule existed would otherwise leave the
    policy in the data file only, where nobody reading the card would see it.
    """
    errs: List[str] = []
    reg = ROOT / "metadata" / "repositories.json"
    if not reg.exists():
        return errs, []
    categories = {str(r["slug"]): str(r.get("category") or "")
                  for r in json.loads(reg.read_text()).get("repositories", []) if r.get("slug")}
    for slug, risk in sorted(risks.items()):
        rel = card_path_for(slug, categories.get(slug, ""))
        card = ROOT / rel
        if not card.exists():
            errs.append(f"{rel}: no card exists for '{slug}', so its {risk} license policy is "
                        f"stated nowhere a reader would see it")
            continue
        text = card.read_text(encoding="utf-8", errors="replace")
        if f"license_risk: {risk}" not in text:
            errs.append(f"{rel}: frontmatter does not carry `license_risk: {risk}` — the "
                        f"override is recorded in metadata/repositories.json but not in the "
                        f"card, so the policy is invisible to anyone reading the markdown")
        if risk not in text.split("---", 2)[-1]:
            errs.append(f"{rel}: body does not state the {risk} policy — the marker must be "
                        f"readable, not only machine-parseable")
    return errs, []


def check_no_orphan_cards() -> List[str]:
    """A card on disk must correspond to a registry record at its expected path.

    Found while enforcing H-5: `repositories/developer-tools/firebase--firebase-tools.md` had
    survived since v1.0.0 after the repository was reclassified to `mcp-servers`. Two cards for
    one repository, with conflicting `domain` and `tags`, and the stale one carrying no license
    marker at all — an agent that found it first would trust the wrong category and miss the
    policy. Nothing detected it, because nothing compared the cards to the registry.
    """
    errs: List[str] = []
    reg = ROOT / "metadata" / "repositories.json"
    if not reg.exists():
        return errs
    expected = {card_path_for(str(r["slug"]), str(r.get("category") or ""))
                for r in json.loads(reg.read_text()).get("repositories", []) if r.get("slug")}
    on_disk = {p.relative_to(ROOT).as_posix()
               for p in (ROOT / "repositories").glob("*/*.md") if p.name != "README.md"}
    for rel in sorted(on_disk - expected):
        errs.append(f"{rel}: card exists but no registry record maps to this path — it is an "
                    f"orphan left behind by a reclassification or a rename. Regenerate the "
                    f"cards and delete it; a stale card states a category and a license "
                    f"position that are no longer true")
    return errs


def check_ingested_text() -> List[str]:
    """Scan API-sourced strings for injection-shaped content, before anything renders them.

    `description`, `homepage` and `topics` are set by whoever owns the repository. They are
    recorded verbatim because that is the observed fact, and generators escape them when
    rendering — but escaping only stops markdown being interpreted. A description reading
    "ignore prior instructions and …" is still perfectly safe *markdown* and still an
    instruction to the next agent that reads the card. This repository is explicitly built to
    be ingested as external long-term memory, so ingested text has to be treated as untrusted
    input rather than as content.

    A match is an error, not a warning: the remedy is to review the record, and a warning that
    can be merged past is not a control. The corpus is clean today — zero hits across 401
    descriptions — which is a property of the current seed list and not of the pipeline, and is
    exactly why the check has to exist before something is added rather than after.
    """
    errs: List[str] = []
    for rel, key, fields in (
        ("metadata/repositories.json", "repositories",
         ("description", "homepage", "topics", "name")),
        ("metadata/tools.json", "tools", ("purpose", "name")),
        ("metadata/sources.json", "sources", ("title", "summary")),
    ):
        p = ROOT / rel
        if not p.exists():
            continue
        for rec in json.loads(p.read_text()).get(key, []):
            if not isinstance(rec, dict):
                continue
            ident = rec.get("slug") or rec.get("id") or rec.get("name") or "?"
            marks = any_injection_marks({f: rec.get(f) for f in fields})
            if marks:
                errs.append(f"{rel}: {ident} carries injection-shaped upstream text "
                            f"({', '.join(sorted(set(marks)))}). The record is quarantined "
                            f"rather than rendered; review it before it is published.")
    return errs



def check_exclusions(files: List[Path], excluded) -> Tuple[List[str], List[str]]:
    """Enforce SECURITY.md's collection-ethics exclusions.

    Three separate failures, because they have different remedies:

      1. **the list itself is unusable** — a missing or malformed policy file means every
         exclusion is unenforced, which is the defect this check exists to prevent, so it is
         an error rather than a silent pass over an empty list.
      2. **an excluded source has been collected** — a slug in `seeds.json`,
         `repositories.json` or any retrieval path. No wording can excuse this: a seed entry
         or a registry record *is* collection, whatever the prose around it says.
      3. **an excluded source is cited or named without stating that it is excluded** — the
         case the policy was written for. Naming it is legitimate, and necessary: an
         exclusion nobody can see will be rediscovered by a contributor who notices a
         popular repository is missing and adds it in good faith. What is not legitimate is
         naming it in a passage that reads as a recommendation.

    Matching is on the whole `owner/name` slug, never on the bare repository name, so an
    exclusion cannot implicate every file that happens to use a common word.
    """
    errs: List[str] = []
    warns: List[str] = []

    if excluded.load_error:
        for line in excluded.load_error.strip().splitlines():
            errs.append(f"exclusion policy: {line.strip()}")
    if excluded.is_empty():
        errs.append("exclusion policy: metadata/excluded-sources.json declares no exclusions — "
                    "SECURITY.md states hard exclusions, so an empty list means they are "
                    "unenforced rather than satisfied")
        return errs, warns

    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        if excluded.is_policy_file(rel):
            continue                       # the policy document is allowed to name them
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        hits = excluded.slug_in(text)
        ingestion = excluded.is_ingestion_path(rel)
        for slug in hits:
            if ingestion:
                errs.append(f"{rel}: contains the excluded source '{slug}' on an ingestion or "
                            f"retrieval path — this is collection, and no wording excuses it. "
                            f"Remove it; the exclusion itself is recorded in "
                            f"knowledge/security/llm-security/excluded-sources.md")
            elif not excluded.passage_states_exclusion(text, slug):
                errs.append(f"{rel}: names the excluded source '{slug}' in a passage that does "
                            f"not state the exclusion. Naming it is allowed — that is how a "
                            f"contributor avoids rediscovering it — but the passage must say it "
                            f"is excluded, not recommend it")

        for pat, matched in excluded.pattern_hits(text):
            if ingestion:
                errs.append(f"{rel}: matches excluded-content pattern '{pat.get('id')}' "
                            f"('{matched}') on an ingestion or retrieval path")
            elif pat.get("requires_nearby_exclusion_wording") and \
                    not excluded.passage_states_exclusion(text, matched):
                warns.append(f"{rel}: matches excluded-content pattern '{pat.get('id')}' "
                             f"('{matched}') without stating the exclusion nearby")

    # A citation is collection by reference: an artifact whose sources block points at an
    # excluded source is relying on it, whatever the body text says.
    errs += check_excluded_citations(excluded)
    return errs, warns


def check_excluded_citations(excluded) -> List[str]:
    """Reject any artifact whose `sources` block cites an excluded source."""
    errs: List[str] = []
    slugs = [s.lower() for s in excluded.slugs]
    if not slugs:
        return errs

    def cited(value: Any) -> bool:
        s = str(value or "").lower()
        return any(slug in s for slug in slugs)

    for f in fm.iter_markdown(ROOT):
        rel = f.relative_to(ROOT).as_posix()
        if fm.is_exempt(rel):
            continue
        doc = fm.parse(f, ROOT)
        for src in (doc.data or {}).get("sources") or []:
            if not isinstance(src, dict):
                continue
            for field in ("url", "repository", "title", "organization"):
                if cited(src.get(field)):
                    errs.append(f"{rel}: sources[] cites the excluded source "
                                f"{src.get(field)!r} (field '{field}')")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    errors: List[str] = []
    warns: List[str] = []
    files = tracked_files()
    print(f"Scanning {len(files)} tracked files…")

    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        if f.suffix in (".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".woff", ".woff2"):
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        low = text.lower()

        # 1. secrets
        for name, pat in SECRET_PATTERNS.items():
            for m in pat.finditer(text):
                s = m.group(0)
                if "<" in s or "YOUR" in s.upper() or "xxxx" in s.lower() or "example" in low[max(0, m.start()-80):m.start()]:
                    continue
                errors.append(f"{rel}: possible {name} secret ({s[:8]}…{s[-4:]})")

        # 2. forbidden collection
        for pat, label in FORBIDDEN:
            for m in pat.finditer(text):
                ctx = text[max(0, m.start() - 200):m.end() + 200]
                if ALLOWED_DISCUSSION.search(ctx):
                    continue
                errors.append(f"{rel}: forbidden content — {label}")

        # 4. hallucination firewall: superlatives need a date
        #
        # Generated artifacts are skipped, and the skip loses no coverage: a generated
        # file quotes a governed source, and that source is scanned here in its own
        # right. Flagging the copy as well as the original only doubles the count for
        # one underlying unverified claim — which is exactly what happened when
        # skills/*/tests/cases.md started quoting skill prose verbatim.
        if f.suffix == ".md" and "experimental/" not in rel and not fm.is_generated(rel):
            lines = text.splitlines()
            for i, line in enumerate(lines):
                if line.strip().startswith(("```", "|", "<!--")):
                    continue
                if SUPERLATIVE.search(line):
                    window = "\n".join(lines[max(0, i - 3):i + 4])
                    if not VERIFIED_NEAR.search(window):
                        warns.append(f"{rel}:{i+1}: superlative without a nearby verification date — "
                                     f"'{line.strip()[:70]}'")

        # 5. quarantine must not be cited as authoritative
        if f.suffix == ".md" and not rel.startswith(("experimental/", "knowledge/ai-engineering/")):
            if re.search(r"pending-paper-candidates\.json", text) and not re.search(r"(?i)(quarantin|pending|do not cite|not verified)", text):
                warns.append(f"{rel}: references the paper quarantine file without saying it is unverified")

    # 6. generated files must declare their generator
    for rel in ["metadata/repositories.json", "metadata/index.json", "metadata/tools.json",
                "metadata/skills.json", "metadata/evaluations.json", "metadata/sources.json"]:
        p = ROOT / rel
        if not p.exists():
            continue
        head = p.read_text()[:400]
        if "generat" not in head.lower():
            errors.append(f"{rel}: generated file lacks a generator/generated_at marker")

    # 8. ingested text is untrusted input, not content
    ingested = check_ingested_text()
    errors += ingested
    print(f"Ingested text: {0 if not ingested else len(ingested)} records carrying "
          f"injection-shaped upstream strings")

    # 7. the license hard override, applied to markdown and not only to code
    risks = load_license_risks()
    e7, w7 = check_license_policy(files, risks)
    errors += e7
    warns += w7
    e7b, _ = check_cards_state_license_policy(risks)
    errors += e7b
    errors += check_no_orphan_cards()
    if risks:
        print(f"License policy: {len(risks)} repositories carry a license consequence "
              f"({sum(1 for v in risks.values() if v == 'no-license-do-not-redistribute')} "
              f"do-not-redistribute, "
              f"{sum(1 for v in risks.values() if v == 'custom-license-review-before-vendoring')} "
              f"review-before-vendoring); {len(e7)} vendoring-shaped references, "
              f"{len(e7b)} cards not stating it, {len(w7)} prose mentions")

    # 6. collection ethics: SECURITY.md's hard exclusions, enforced
    excluded = load_exclusions()
    e6, w6 = check_exclusions(files, excluded)
    errors += e6
    warns += w6
    if not excluded.is_empty() and not excluded.load_error:
        print(f"Exclusions: {len(excluded.slugs)} declared, "
              f"{len(e6)} violations across {len(files)} tracked files")

    for p in sorted((ROOT / "indexes").glob("*.md")):
        head = p.read_text()[:400]
        if "GENERATED" not in head and "generated" not in head:
            errors.append(f"indexes/{p.name}: generated file lacks a GENERATED marker")

    if args.strict:
        errors += warns
        warns = []

    print(f"Errors: {len(errors)}   Warnings: {len(warns)}")
    for e in errors[:60]:
        print("  ERROR  " + e)
    if len(errors) > 60:
        print(f"  … and {len(errors)-60} more")
    for w in warns[:40]:
        print("  warn   " + w)
    if len(warns) > 40:
        print(f"  … and {len(warns)-40} more warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
