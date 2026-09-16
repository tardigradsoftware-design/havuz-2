#!/usr/bin/env python3
"""Recompute every headline corpus statistic and check the documents that assert it.

The numbers in `README.md`'s statistics block are generated, so they cannot drift. The numbers
in *prose* can: `REVIEW-REPORT.md` §15 states measurements by hand, README's own narrative
sections restate counts outside the generated block, and a pull-request description restates them
again. Three of those went stale during Phase 5 alone — README claimed "333 test cases" long
after the corpus reached 1108, its generated block counted `cases.md` *files* under the label
"Skill test cases" and printed 50, and a PR description still said "35 MCP servers" and "15
UNVERIFIED" after H-3 and H-8 had changed both.

A stale count in a document that exists to be trusted is the same defect this repository's
validators were built for, so it gets the same treatment: one source of truth, recomputed, and a
check that fails when an assertion disagrees with it.

This script owns the *computation*. Anything that needs a corpus count should import
`corpus_stats()` rather than re-deriving it, so there is one answer.

Run: python3 scripts/validate/check_release_claims.py
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from lib import frontmatter as fm  # noqa: E402


def _meta(name: str, key: str) -> List[Dict[str, Any]]:
    p = ROOT / "metadata" / name
    if not p.exists():
        return []
    data = json.loads(p.read_text())
    return data.get(key) or []


def _evaluation_records() -> int:
    p = ROOT / "metadata" / "evaluations.json"
    if not p.exists():
        return 0
    d = json.loads(p.read_text(encoding="utf-8"))
    if isinstance(d, list):
        return len(d)
    return len(d.get("evaluations", []))


def corpus_stats() -> Dict[str, Any]:
    """Every headline statistic, recomputed from source data.

    Counts come from the registries and the files on disk, never from a document, so a document
    that disagrees with this is the thing that is wrong.
    """
    repos = _meta("repositories.json", "repositories")
    tools = _meta("tools.json", "tools")
    index = _meta("index.json", "entries") or _meta("index.json", "items")
    sources = _meta("sources.json", "sources")

    md = [f.relative_to(ROOT).as_posix() for f in fm.iter_markdown(ROOT)]

    def count(pred) -> int:
        return sum(1 for rel in md if pred(rel))

    # Cases, not files: the distinction README's generated block once got wrong by 22x.
    cases = 0
    for rel in md:
        if rel.startswith("skills/") and rel.endswith("/tests/cases.md"):
            cases += len(re.findall(r"(?m)^## Case \d+",
                                    (ROOT / rel).read_text(encoding="utf-8", errors="replace")))

    kinds = collections.Counter(t.get("registry_kind") for t in tools)
    tiers = collections.Counter(r.get("tier") for r in repos)
    risk = collections.Counter(r.get("license_risk") for r in repos)

    return {
        "repositories": len(repos),
        "repository_cards": count(lambda r: r.startswith("repositories/")
                                  and not r.endswith("README.md")),
        "skills": count(lambda r: re.fullmatch(r"skills/[^/]+/SKILL\.md", r)),
        "skill_test_cases": cases,
        "skill_case_files": count(lambda r: r.startswith("skills/")
                                  and r.endswith("/tests/cases.md")),
        "knowledge_articles": count(lambda r: r.startswith("knowledge/")
                                    and not r.endswith("README.md")),
        "agents": count(lambda r: r.endswith("/AGENT.md")),
        "workflows": count(lambda r: r.endswith("/WORKFLOW.md")),
        "mcp_entries": len(tools),
        "mcp_servers": kinds.get("server", 0),
        "mcp_not_servers": len(tools) - kinds.get("server", 0),
        "mcp_kinds": dict(kinds),
        "index_entries": len(index),
        "evaluation_records": _evaluation_records(),
        "index_files": len(list((ROOT / "indexes").glob("*.md"))),
        "schemas": len(list((ROOT / "schemas").glob("*.json"))),
        "verified_papers": sum(1 for s in sources if s.get("type") == "research-paper"),
        "tiers": dict(tiers),
        "no_license": risk.get("no-license-do-not-redistribute", 0),
        "custom_license": risk.get("custom-license-review-before-vendoring", 0),
        "fetch_failures": sum(1 for r in repos if not r.get("fetch_ok", True)),
        "archived": sum(1 for r in repos if r.get("archived")),
    }


# Assertions written in prose, as (label, regex over the document, expected value from stats).
# Each is a claim a reader would act on, so each is worth pinning. Deliberately few: a check
# that asserts everything becomes a maintenance burden and stops being run.
def prose_claims(s: Dict[str, Any]) -> List[Tuple[str, str, Any, bool]]:
    """Hand-written counts, as `(file, pattern, expected, required)`.

    `required` matters as much as the comparison. A claim whose pattern stops matching — because
    a table row was renamed, say — must fail rather than be skipped, or the check passes
    vacuously and looks green while asserting nothing. That is exactly how the first version of
    this function came to verify no README row at all: it labelled them `"README"` while the
    documents were keyed `"README.md"`, so every lookup missed and every claim was silently
    skipped.
    """
    return [
        ("README.md", r"\| Skill test cases \| \*\*(\d+)\*\*", s["skill_test_cases"], True),
        ("README.md", r"\| MCP servers \| \*\*(\d+)\*\*", s["mcp_servers"], True),
        ("README.md", r"\| MCP registry entries \(incl\. (\d+) that are not servers\) \| \*\*(\d+)\*\* \|",
         (s["mcp_not_servers"], s["mcp_entries"]), True),
        ("README.md", r"\| Knowledge articles \| \*\*(\d+)\*\*", s["knowledge_articles"], True),
        ("README.md", r"\| Verified GitHub repositories \| \*\*(\d+)\*\*", s["repositories"], True),
        ("README.md", r"\| Retrieval index entries \| \*\*(\d+)\*\*", s["index_entries"], True),
        ("README.md", r"\| Skills \| \*\*(\d+)\*\* \|", s["skills"], True),
        ("README.md", r"\| Agent roles \| \*\*(\d+)\*\* \|", s["agents"], True),
        ("README.md", r"\| Workflows \| \*\*(\d+)\*\* \|", s["workflows"], True),
        # README's narrative restates the case count outside the generated block, and must carry
        # the not-executed qualifier next to it.
        ("README.md", r"\*\*([\d,]+) cases across (\d+)\s*\n?skills",
         (f"{s['skill_test_cases']:,}", str(s["skills"])), True),
        ("README.md", r"authored specifications, not executed results", None, True),
        ("README.md", r"No effectiveness claim is made", None, True),
        # §15 is the authoritative current measurement; it must match the recomputation.
        ("REVIEW-REPORT.md", r"\*\*(\d+)\*\* skill directories are now verified", s["skills"], True),
        ("REVIEW-REPORT.md", r"server (\d+) / sdk (\d+) / tooling (\d+) / catalog (\d+) / "
                             r"registry (\d+) / unproven (\d+)",
         (s["mcp_kinds"].get("server", 0), s["mcp_kinds"].get("sdk", 0),
          s["mcp_kinds"].get("tooling", 0), s["mcp_kinds"].get("catalog", 0),
          s["mcp_kinds"].get("registry", 0), s["mcp_kinds"].get("unproven", 0)), True),
        ("REVIEW-REPORT.md", r"\*\*(\d+) of 401\*\* descriptions", None, False),
    ]


def check_prose(s: Dict[str, Any]) -> List[str]:
    """Verify hand-written counts against the recomputation."""
    errs: List[str] = []
    docs = {name: (ROOT / f"{name}").read_text(encoding="utf-8", errors="replace")
            for name in ("README.md", "REVIEW-REPORT.md") if (ROOT / f"{name}").exists()}

    for doc, pattern, expected, required in prose_claims(s):
        text = docs.get(doc)
        if text is None:
            if required:
                errs.append(f"{doc}: not found, but {len([1 for d, _, _, r in prose_claims(s) if d == doc and r])} "
                            f"required claims depend on it")
            continue
        m = re.search(pattern, text)
        if not m:
            if required:
                errs.append(f"{doc}: no longer makes the claim /{pattern[:60]}/ — either the "
                            f"wording changed or the claim was removed. Update this checker "
                            f"deliberately; do not let it pass by going quiet.")
            continue
        if expected is None:
            continue                      # presence is the assertion (e.g. a required qualifier)
        got = m.group(1) if m.lastindex == 1 else tuple(m.groups())
        want = expected if isinstance(expected, tuple) else (expected,)
        got_t = got if isinstance(got, tuple) else (got,)

        def norm(seq):
            return tuple(str(v).replace(",", "").strip() for v in seq)

        if norm(got_t) != norm(want):
            errs.append(f"{doc}: asserts {got_t} where the data says {tuple(str(x) for x in want)} "
                        f"(pattern /{pattern[:50]}/)")
    return errs


def check_registry_split(s: Dict[str, Any]) -> List[str]:
    """§15's kind split and the README/indexes must describe the same registry."""
    errs: List[str] = []
    doc = ROOT / "REVIEW-REPORT.md"
    if not doc.exists():
        return errs
    text = doc.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"server (\d+) / sdk (\d+) / tooling (\d+) / catalog (\d+) / registry (\d+) / "
                  r"unproven (\d+)", text)
    if m:
        stated = dict(zip(("server", "sdk", "tooling", "catalog", "registry", "unproven"),
                          (int(g) for g in m.groups())))
        for k, v in stated.items():
            if s["mcp_kinds"].get(k, 0) != v:
                errs.append(f"REVIEW-REPORT.md: registry kind '{k}' stated as {v}, "
                            f"data says {s['mcp_kinds'].get(k, 0)}")
        if sum(stated.values()) != s["mcp_entries"]:
            errs.append(f"REVIEW-REPORT.md: kind split sums to {sum(stated.values())}, "
                        f"registry holds {s['mcp_entries']} entries")

    # The distinction has to be stated consistently wherever the registry is summarised.
    for rel, needle in (("indexes/mcp.md", str(s["mcp_servers"])),
                        ("README.md", str(s["mcp_servers"]))):
        p = ROOT / rel
        if p.exists() and needle not in p.read_text(encoding="utf-8", errors="replace"):
            errs.append(f"{rel}: does not state {needle} MCP servers anywhere — the "
                        f"server/entry distinction is missing where the registry is summarised")
    return errs


def tier_assertions(text: str, line_offset: int = 0) -> List[Tuple[int, int]]:
    """The `N UNVERIFIED` claims a document actually *asserts*, as `(line, n)`.

    Two exclusions, both of which matter:

    * **Text inside inline code spans is naming the label, not asserting it.** This changelog has
      to be able to say "`15 UNVERIFIED` is now `15 NO-LICENSE`" — that sentence is the correction
      being recorded, and flagging it would make the fix unrecordable. Code spans are blanked to
      spaces of equal length so line and column numbers stay accurate.
    * **`0 UNVERIFIED` is a true statement about this corpus.** There are no fetch failures here,
      so a section reporting zero unverified records is asserting the current state correctly and
      must not be treated as a stale label.

    Without these, the check fires on the sentences that document the fix and stays quiet about
    nothing — which is how a validator gets ignored.
    """
    masked = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), text)
    out: List[Tuple[int, int]] = []
    for m in re.finditer(r"(\d+)\s+UNVERIFIED", masked):
        n = int(m.group(1))
        if n == 0:
            continue
        out.append((masked[:m.start()].count("\n") + 1 + line_offset, n))
    return out


def check_tier_semantics(s: Dict[str, Any]) -> List[str]:
    """No document may call the no-license tier `UNVERIFIED`.

    H-3 separated the two. `UNVERIFIED` means the fetch failed; the no-license tier is
    `NO-LICENSE`. A document that still says "15 UNVERIFIED" is repeating the conflation the
    fix removed — and there are 0 fetch failures in this corpus, so any `UNVERIFIED` count
    asserted as non-zero is wrong on its face.
    """
    errs: List[str] = []
    for rel in ("README.md", "REVIEW-REPORT.md", "CHANGELOG.md"):
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        offset = 0
        if rel == "CHANGELOG.md":
            # Only the current version section asserts the present state. A changelog entry for a
            # released version is a historical record of what that version contained, and
            # rewriting `15 UNVERIFIED` to `NO-LICENSE` inside the 1.0.0 section would falsify
            # it — that label really was what 1.0.0 shipped. Past sections are instead required
            # to carry a note saying so; see check_historical_sections_are_marked().
            heads = [m.start() for m in re.finditer(r"(?m)^## \[", text)]
            if len(heads) > 1:
                offset = text[:heads[0]].count("\n")
                text = text[heads[0]:heads[1]]
        for line, n in tier_assertions(text, offset):
            if n != s["tiers"].get("UNVERIFIED", 0):
                errs.append(f"{rel}:{line}: asserts '{n} UNVERIFIED' but the registry has "
                            f"{s['tiers'].get('UNVERIFIED', 0)}; the {s['no_license']} "
                            f"no-license records are tier NO-LICENSE (see H-3)")
    return errs


def check_evaluation_claims(s: Dict[str, Any]) -> List[str]:
    """README's "the model is not validated" argument rests on there being no evaluation data.

    That argument is only sound while the claim underneath it is true, and the claim is easy to
    break in the good direction: the moment someone authors evaluation records, "nobody has
    measured whether the weights predict usefulness" stops being accurate and the scoring section
    has to be rewritten. So the count is asserted here rather than left to memory.

    The README says `evaluations/` holds seven scaffolded domain READMEs and zero records. Both
    halves are checked — the scaffold count because "seven" is a specific number in prose, the
    record count because it is the load-bearing one.
    """
    errs: List[str] = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
    stubs = sorted((ROOT / "evaluations").glob("*/README.md")) if (ROOT / "evaluations").exists() else []
    m = re.search(r"`evaluations/` holds (\w+) scaffolded\s*\n?domain READMEs and \*\*(\w+) evaluation records\*\*", readme)
    if not m:
        # Required, not optional. The whole "not validated" argument in README's scoring section
        # depends on this sentence; if the sentence is deleted the argument loses its evidence and
        # the check must say so rather than pass because it found nothing to compare.
        errs.append("README.md: the scoring section no longer states how many scaffolded "
                    "evaluation READMEs and evaluation records exist, so its 'not validated' "
                    "argument is unsupported. Restore the claim or update this checker "
                    "deliberately.")
        return errs
    words = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7}
    said_stubs = words.get(m.group(1).lower(), None)
    said_records = words.get(m.group(2).lower(), None)
    if said_stubs is None or said_records is None:
        errs.append(f"README.md: the evaluations claim uses numbers this checker cannot read "
                    f"({m.group(1)!r}, {m.group(2)!r}) — spell them as words it knows")
        return errs
    if said_stubs != len(stubs):
        errs.append(f"README.md: says {said_stubs} scaffolded evaluation READMEs, found {len(stubs)}")
    if said_records != s["evaluation_records"]:
        errs.append(f"README.md: says {said_records} evaluation records, metadata has "
                    f"{s['evaluation_records']} — if records now exist, the scoring section's "
                    f"'not validated' argument must be re-examined, not just this number")
    return errs


def check_category_vs_registry(s: Dict[str, Any]) -> List[str]:
    """A repository category named after servers must not read as a server count.

    The corpus files 35 repositories under the seed-list category `mcp-servers` while the
    registry classifies 26 of its 35 entries as servers. Those numbers measure different things
    on different axes and are not expected to agree — but printed on one page without a word,
    they invite a reader to reconcile them and conclude one is wrong. So if the generated
    category table contains an MCP-named category, the clarification has to be there too.
    """
    errs: List[str] = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
    m = re.search(r"(?m)^\| `mcp-servers` \| (\d+) \|$", readme)
    if not m:
        return errs
    cat_n = int(m.group(1))
    if "repository-corpus category" not in readme:
        errs.append(f"README.md: the category table lists `mcp-servers` = {cat_n} with no note that "
                    f"this is a seed-list repository category, while the registry reports "
                    f"{s['mcp_servers']} servers of {s['mcp_entries']} entries — a reader cannot "
                    f"tell which number counts servers")
    # the note has to carry the same split the data does, or it explains one number and asserts
    # a different one
    note = re.search(r"\*\*(\d+) servers\*\* and \*\*(\d+) entries that are not servers\*\*, out of (\d+)", readme)
    if note:
        got = tuple(int(g) for g in note.groups())
        want = (s["mcp_servers"], s["mcp_entries"] - s["mcp_servers"], s["mcp_entries"])
        if got != want:
            errs.append(f"README.md: the category note asserts {got} where the registry says {want}")
    return errs


def check_historical_sections_are_marked() -> List[str]:
    """A released-version changelog section that repeats a superseded label must say it is historical.

    Scoping the tier check to the current section is only safe if a reader cannot mistake the old
    sections for current state. So each released section that still names `UNVERIFIED` has to
    carry a note pointing at the change that superseded it. This is the same discipline
    REVIEW-REPORT.md uses for its own layers: history is preserved verbatim and labelled, never
    silently rewritten.
    """
    errs: List[str] = []
    p = ROOT / "CHANGELOG.md"
    if not p.exists():
        return errs
    text = p.read_text(encoding="utf-8", errors="replace")
    heads = [m.start() for m in re.finditer(r"(?m)^## \[", text)]
    for i, start in enumerate(heads[1:], start=1):           # skip the current section
        end = heads[i + 1] if i + 1 < len(heads) else len(text)
        section = text[start:end]
        title = section.splitlines()[0]
        if tier_assertions(section) and "historical" not in section.lower():
            errs.append(f"CHANGELOG.md {title}: restates a superseded tier label but is not "
                        f"marked historical — a reader could take it for the current state")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    s = corpus_stats()
    errs = (check_prose(s) + check_registry_split(s) + check_tier_semantics(s)
            + check_historical_sections_are_marked()
            + check_category_vs_registry(s)
            + check_evaluation_claims(s))

    if not args.quiet:
        print("Corpus statistics, recomputed from source data:")
        for k in ("repositories", "repository_cards", "skills", "skill_test_cases",
                  "knowledge_articles", "agents", "workflows", "mcp_entries", "mcp_servers",
                  "mcp_not_servers", "index_entries", "index_files", "schemas",
                  "verified_papers", "no_license", "custom_license", "archived",
                  "fetch_failures"):
            print(f"  {k:22} {s[k]}")
        print(f"  {'mcp_kinds':22} {s['mcp_kinds']}")
        print(f"  {'tiers':22} {s['tiers']}")

    if errs:
        print(f"\nErrors: {len(errs)}")
        for e in errs:
            print(f"  ERROR  {e}")
        return 1
    print("\nOK: every prose count checked agrees with the recomputed statistics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
