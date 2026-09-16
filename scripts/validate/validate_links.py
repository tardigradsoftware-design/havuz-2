#!/usr/bin/env python3
"""Link validation.

  --internal   every relative Markdown link / image / frontmatter path resolves to a
               real file inside the repository, and every heading anchor exists
  --external   every http(s) URL is reachable (HEAD, then GET fallback), with retries
               and a known-flaky allowlist so transient outages do not fail CI

Broken internal links are a hard error: they break agent retrieval.
Broken external links fail only after repeated failure, per SECURITY/brief §81.

Usage:
    python3 scripts/validate/validate_links.py --internal
    python3 scripts/validate/validate_links.py --external --timeout 20
    python3 scripts/validate/validate_links.py --internal --external
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402

MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
RAW_URL = re.compile(r"(?<!\()(?<![\w/\"])https?://[^\s)>\]\"'`]+")
ALLOWLIST = ROOT / "scripts" / "validate" / "link-allowlist.json"

SKIP_DIRS = {".git", ".cache", "node_modules", ".venv", "__pycache__"}

# Domains that block HEAD/bot requests but are known-good references.
SOFT_DOMAINS = {
    "x.com", "twitter.com", "linkedin.com", "medium.com", "reddit.com",
    "news.ycombinator.com", "scholar.google.com", "openai.com", "anthropic.com",
}


def load_allowlist() -> Dict[str, str]:
    if ALLOWLIST.exists():
        try:
            return json.loads(ALLOWLIST.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def strip_code(body: str) -> str:
    out, fence = [], False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if not fence:
            out.append(line)
    return "\n".join(out)


def collect_internal() -> Tuple[List[str], List[str], Set[str]]:
    errors, warns = [], []
    external: Set[str] = set()
    anchors: Dict[str, Set[str]] = {}

    docs = []
    for f in fm.iter_markdown(ROOT):
        if any(p in SKIP_DIRS for p in f.parts):
            continue
        docs.append(fm.parse(f))
    for d in docs:
        anchors[d.rel] = {"#" + fm.slugify(h) for _, h in fm.headings(d.body)}

    for d in docs:
        text = strip_code(d.raw_front + "\n" + d.body)
        for target in MD_LINK.findall(text):
            if target.startswith(("mailto:", "#")):
                if target.startswith("#") and target not in anchors[d.rel]:
                    errors.append(f"{d.rel}: anchor {target} not found in this file")
                continue
            if re.match(r"^https?://", target):
                external.add(target.split("#")[0].rstrip(").,;"))
                continue
            path_part, _, frag = target.partition("#")
            if path_part:
                resolved = (d.path.parent / path_part).resolve()
                try:
                    rel = resolved.relative_to(ROOT.resolve()).as_posix()
                except ValueError:
                    errors.append(f"{d.rel}: link escapes the repository -> {target}")
                    continue
                if not resolved.exists():
                    errors.append(f"{d.rel}: broken internal link -> {target}")
                elif frag and rel in anchors and ("#" + frag) not in anchors[rel]:
                    warns.append(f"{d.rel}: anchor #{frag} not found in {rel}")
        for u in RAW_URL.findall(text):
            external.add(u.rstrip(").,;>"))

    # frontmatter paths (sources[].repository, related, requires)
    for d in docs:
        for k in ("related_skills", "requires"):
            for v in d.data.get(k) or []:
                if not (ROOT / "skills" / str(v) / "SKILL.md").exists():
                    warns.append(f"{d.rel}: {k} '{v}' has no skills/{v}/SKILL.md")
    return errors, warns, external


def check_url(url: str, timeout: int, retries: int = 2) -> Tuple[str, int, str]:
    if any(dom in url for dom in SOFT_DOMAINS):
        return url, 0, "skipped:soft-domain"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; havuz-kb-linkcheck/1.0)",
               "Accept": "*/*"}
    last = 0
    for attempt in range(retries + 1):
        for method in ("HEAD", "GET"):
            req = urllib.request.Request(url, headers=headers, method=method)
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return url, r.status, "ok"
            except urllib.error.HTTPError as e:
                last = e.code
                if e.code in (405, 501, 403) and method == "HEAD":
                    continue
                if e.code in (429, 500, 502, 503, 504):
                    time.sleep(2 + 3 * attempt)
                    break
                return url, e.code, "http-error"
            except Exception as e:
                last = -1
                if attempt < retries:
                    time.sleep(1 + 2 * attempt)
                    break
                return url, -1, f"exception:{type(e).__name__}"
        else:
            continue
        continue
    return url, last, "failed-after-retries"


def collect_external() -> Tuple[List[str], List[str]]:
    errors, warns = [], []
    urls: Set[str] = set()
    for f in fm.iter_markdown(ROOT):
        if any(p in SKIP_DIRS for p in f.parts):
            continue
        d = fm.parse(f)
        text = strip_code(d.raw_front + "\n" + d.body)
        for t in MD_LINK.findall(text) + RAW_URL.findall(text):
            if re.match(r"^https?://", t):
                urls.add(t.split("#")[0].rstrip(").,;>\"'"))
    for p in (ROOT / "metadata").glob("*.json"):
        txt = p.read_text(errors="replace")
        for u in re.findall(r'"(https?://[^"]+)"', txt):
            urls.add(u.rstrip(").,;"))
    urls = {u for u in urls if "localhost" not in u and "127.0.0.1" not in u}
    allow = load_allowlist()
    todo = sorted(u for u in urls if u not in allow)
    print(f"Checking {len(todo)} external URLs ({len(urls)-len(todo)} allowlisted)…")
    failures: Dict[str, List[str]] = defaultdict(list)
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(check_url, u, 20): u for u in todo}
        done = 0
        for fut in cf.as_completed(futs):
            url, status, why = fut.result()
            done += 1
            if done % 50 == 0:
                print(f"  {done}/{len(todo)}")
            if why.startswith("ok") or why.startswith("skipped") or status in (200, 203, 204, 206, 301, 302, 401, 403):
                continue
            failures[url].append(f"{status} {why}")
    for url, reasons in sorted(failures.items()):
        if url in allow:
            warns.append(f"{url}: allowlisted ({allow[url]})")
        else:
            errors.append(f"{url}: {reasons[0]}")
    return errors, warns


# Documents read first by a human or an agent. A path asserted here that does not
# exist is a claim about the repository that is simply false, and markdown-link
# checking alone does not catch it: prose paths are usually backticked, not linked,
# and a link to a *parent* directory resolves happily while the specific file named
# in the sentence does not exist.
PROSE_DOCS = ["README.md", "AGENTS.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md"]

# A token is treated as a repository path only when its first segment is a real
# top-level entry. That keeps GitHub slugs (`anthropics/skills`), package names
# (`@playwright/mcp`) and dotted identifiers out of the check without an allowlist.
PATHISH = re.compile(r"^[A-Za-z0-9_.\-]+(?:/[A-Za-z0-9_.\-]+)+/?$")

# Path segments that stand for a value the reader supplies. A path containing one
# documents a convention rather than asserting a location, so it is not checked.
PLACEHOLDER_SEGMENTS = {
    "YYYY", "MM", "DD", "NN", "XX", "ID", "SLUG", "NAME", "DATE", "TYPE",
    "CATEGORY", "DOMAIN", "TOPIC", "OWNER", "REPO", "KEBAB", "NUM",
}

# A changelog must be able to name a path in order to record that the path was
# falsely claimed and has been removed. Such a passage denies existence rather than
# asserting it, so it is not a broken claim. The marker has to appear in the same
# paragraph as the path, which keeps the exemption narrow enough to be useful and
# wide enough to match how a correction is actually written: the false claim and its
# denial are usually adjacent sentences, not one sentence.
NON_EXISTENCE_MARKER = re.compile(
    r"(?i)(does not exist|do(?:es)?n't exist|never existed|non-?existent|not built|"
    r"no longer|removed|was claimed|is gone|does not produce|not produced)")


def collect_prose_paths() -> Tuple[List[str], List[str]]:
    """Assert that every repository path named in the entry documents exists."""
    errs: List[str] = []
    warns: List[str] = []
    top = {q.name for q in ROOT.iterdir() if not q.name.startswith(".")}
    checked = 0
    for rel in PROSE_DOCS:
        doc = ROOT / rel
        if not doc.exists():
            continue
        text = doc.read_text(encoding="utf-8", errors="replace")
        # backticked spans and markdown link targets; both are assertions about paths
        tokens: List[str] = re.findall(r"`([^`\n]+)`", text)
        tokens += [m for m in re.findall(r"\]\(([^)\s]+)\)", text)]
        # Paragraph containing each token, for the non-existence exemption.
        paragraphs = re.split(r"\n\s*\n", text)

        def paragraph_of(token: str) -> str:
            """The paragraph holding this token, with code spans removed.

            Stripping backticked text matters: the denial has to be in prose. A
            filename that merely *contains* a marker word — `metadata/nonexistent.json`
            — is not a statement that anything is missing, and letting it exempt its
            own paragraph would hide real broken claims sitting next to it.
            """
            for para in paragraphs:
                if token in para:
                    return re.sub(r"`[^`]*`", " ", para)
            return ""

        for raw in tokens:
            tok = raw.split("#")[0].strip()
            if not tok or tok.startswith(("http://", "https://", "mailto:")):
                continue
            if any(c in tok for c in "*<>{}| "):     # globs and placeholders are not claims
                continue
            # A documented naming convention is not a claim that the path exists:
            # `research-archive/YYYY/MM/` describes a shape future runs will fill.
            if any(seg in PLACEHOLDER_SEGMENTS for seg in tok.split("/")):
                continue
            if NON_EXISTENCE_MARKER.search(paragraph_of(raw)):
                continue          # the passage says this path is absent, not present
            if not PATHISH.match(tok):
                continue
            if tok.split("/")[0] not in top:          # not a repository path
                continue
            checked += 1
            if not (ROOT / tok).exists():
                errs.append(f"{rel}: names the path '{tok}' which does not exist — "
                            f"either create it or stop asserting it")
    errs.extend(_skill_test_cases_exist())

    if checked:
        print(f"Prose paths: {checked} repository paths named in "
              f"{', '.join(PROSE_DOCS)} checked")
    return errs, warns


def _skill_test_cases_exist() -> List[str]:
    """Enforce the README's claim that every skill has generated test cases.

    Naming the path as `skills/<skill>/tests/cases.md` describes a convention, and the
    prose-path check deliberately does not treat a placeholder segment as a claim about a
    location — so the convention would otherwise be asserted with nothing holding it up.
    Checking it here is stronger than the prose check was: the sentence promises *every*
    skill has cases, and this fails if any single skill directory is missing them.
    """
    errs: List[str] = []
    skills = ROOT / "skills"
    if not skills.is_dir():
        return errs
    dirs = sorted(q for q in skills.iterdir() if q.is_dir() and not q.name.startswith("."))
    missing = [q.name for q in dirs if not (q / "tests" / "cases.md").is_file()]
    if missing:
        errs.append(
            f"README.md claims every skill has tests/cases.md, but {len(missing)} of "
            f"{len(dirs)} skill directories are missing it: {', '.join(missing[:8])}"
            + ("…" if len(missing) > 8 else "")
            + " — run `python scripts/generate-index/generate_skill_tests.py`"
        )
    elif dirs:
        print(f"Skill test cases: all {len(dirs)} skill directories have tests/cases.md")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--internal", action="store_true")
    ap.add_argument("--external", action="store_true")
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--write-allowlist", action="store_true",
                    help="record current external failures in the allowlist with a reason")
    args = ap.parse_args()
    if not args.internal and not args.external:
        args.internal = True

    errors: List[str] = []
    warns: List[str] = []

    if args.internal:
        e, w, ext = collect_internal()
        errors += e
        warns += w
        print(f"Internal: {len(e)} errors, {len(w)} warnings, {len(ext)} external URLs discovered")
        e2, w2 = collect_prose_paths()
        errors += e2
        warns += w2
    if args.external:
        e, w = collect_external()
        errors += e
        warns += w
        print(f"External: {len(e)} errors, {len(w)} warnings")

    for e in errors[:100]:
        print("  ERROR  " + e)
    if len(errors) > 100:
        print(f"  … and {len(errors)-100} more")
    for w in warns[:40]:
        print("  warn   " + w)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
