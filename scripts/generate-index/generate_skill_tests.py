#!/usr/bin/env python3
"""Generate skills/<name>/tests/cases.md from each skill's own body text.

Why this script exists
----------------------
The first version of the test corpus interpolated skill-specific text into the
GIVEN line and then attached one of four boilerplate THEN/FAIL IF pairs. That
produced 333 cases with 4 distinct failure conditions — a suite that could detect
a skill being selected when it should not have been, and nothing else. It also
violated skills/AGENTS.md rule 3 in terms: "never from a generic template. A case
that would pass for any skill is not a case."

This version derives every clause from the skill's own prose:

  Applies   <- Purpose + Workflow step titles + Quality Checklist items
  Declines  <- each "When NOT to Use" exclusion, with the alternative it names
  Detects   <- each Failure Modes row (table) or entry (aligned block), with its
               own detection signal and its own documented response
  Avoids    <- each Anti-Patterns entry, with the consequence that entry states

THEN and FAIL IF quote that material verbatim, so a case asserts something
different for every skill by construction rather than by rewording. A FAIL IF
that names "retrieval metrics good, faithfulness poor" cannot pass for a skill
about threat modelling, and that is the property the previous corpus lacked.

Self-verification
-----------------
The script measures what it produced and refuses to write output that is not
skill-specific: distinctness of THEN and FAIL IF across the whole corpus must be
at or above --min-distinct (default 0.95), and no single FAIL IF may be shared by
more than --max-share skills (default 1). Run with --report to print the
measurement without writing.

Usage:
    python3 scripts/generate-index/generate_skill_tests.py            # write
    python3 scripts/generate-index/generate_skill_tests.py --report   # measure only
    python3 scripts/generate-index/generate_skill_tests.py --check    # CI: no drift + distinctness
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"


# --------------------------------------------------------------------------
# section extraction
# --------------------------------------------------------------------------

def section(body: str, heading: str) -> str:
    """Return the text of `## heading`, up to the next `## ` heading."""
    m = re.search(rf"(?ms)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", body)
    return m.group(1) if m else ""


def unwrap_fenced(text: str) -> str:
    """Strip a single ```text fence if present, keeping inner line structure."""
    m = re.search(r"(?ms)^```[a-z]*\n(.*?)^```", text)
    return m.group(1) if m else text


def collapse(text: str) -> str:
    return " ".join(str(text).split())


def clip(text: str, limit: int = 220) -> str:
    """Trim to a sentence-ish boundary so quoted material stays readable."""
    t = collapse(text)
    if len(t) <= limit:
        return t
    cut = t[:limit]
    for sep in ("; ", ". ", ", "):
        i = cut.rfind(sep)
        if i > limit * 0.5:
            return cut[:i + 1].rstrip()
    return cut.rsplit(" ", 1)[0] + "…"


# --------------------------------------------------------------------------
# parsers — each returns skill-specific material, never invented content
# --------------------------------------------------------------------------

def parse_marked_items(text: str) -> List[str]:
    """Parse a `✗ item` list, joining indented continuation lines."""
    out: List[str] = []
    for raw in unwrap_fenced(text).splitlines():
        if not raw.strip():
            continue
        if raw.lstrip().startswith("✗"):
            out.append(raw.lstrip()[1:].strip())
        elif out and (raw[:1].isspace() or not raw.lstrip().startswith(("□", "|", "-"))):
            out[-1] += " " + raw.strip()
    return [collapse(o) for o in out if collapse(o)]


def split_claim(item: str) -> Tuple[str, str]:
    """Split `condition. alternative/reason.` into its two halves.

    Returns (condition, rest). If there is no second sentence, rest is empty and
    the caller must not fabricate one.
    """
    m = re.match(r"^(.*?[.!?])\s+(.*)$", item)
    if not m:
        return item, ""
    return m.group(1).strip(), m.group(2).strip()


def parse_checklist(text: str) -> List[str]:
    out: List[str] = []
    for raw in unwrap_fenced(text).splitlines():
        s = raw.strip()
        if s.startswith("□"):
            out.append(collapse(s[1:].strip()))
        elif s.startswith(("-", "*")) and out:
            out.append(collapse(s.lstrip("-* ").strip()))
    return [o for o in out if o]


def parse_workflow_steps(text: str) -> List[str]:
    """Return the imperative titles of numbered workflow steps."""
    titles: List[str] = []
    for raw in unwrap_fenced(text).splitlines():
        m = re.match(r"^\s*(\d+)\.\s+(.+?)\.\s{2,}", raw)
        if m:
            titles.append(collapse(m.group(2)))
            continue
        m = re.match(r"^\s*(\d+)\.\s+([A-Z][A-Z0-9 ,/'\-]{3,})\s*$", raw)
        if m:
            titles.append(collapse(m.group(2)))
    return titles


def parse_failure_modes(text: str) -> List[Dict[str, str]]:
    """Failure modes appear in two shapes; both are parsed.

    Table:    | Failure | Detection | Response |
    Aligned:  NAME       description
              (continuation lines indented to the description column)
    """
    rows: List[Dict[str, str]] = []
    lines = text.splitlines()
    table = [l for l in lines if l.strip().startswith("|")]
    if len(table) >= 3:
        for l in table:
            cells = [collapse(c) for c in l.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            if re.match(r"^[-: ]+$", cells[0]) or cells[0].lower().startswith("failure"):
                continue
            rows.append({
                "kind": "table",
                "failure": cells[0],
                "detection": cells[1] if len(cells) > 1 else "",
                "response": cells[2] if len(cells) > 2 else "",
            })
        return rows

    current: Optional[Dict[str, str]] = None
    for raw in unwrap_fenced(text).splitlines():
        if not raw.strip():
            continue
        m = re.match(r"^([A-Z0-9][A-Z0-9 ,/'&\-\(\)]{2,}?)\s{2,}(.+)$", raw)
        if m:
            if current:
                rows.append(current)
            current = {"kind": "aligned", "failure": collapse(m.group(1)),
                       "detection": "", "response": collapse(m.group(2))}
        elif current:
            current["response"] += " " + collapse(raw)
    if current:
        rows.append(current)
    return rows


def parse_anti_patterns(text: str) -> List[Dict[str, str]]:
    """`✗ NAME.   consequence` -> {name, consequence}."""
    out: List[Dict[str, str]] = []
    for item in parse_marked_items(text):
        m = re.match(r"^(.{2,70}?)\.\s{2,}(.+)$", item)
        if m:
            out.append({"name": collapse(m.group(1)), "consequence": collapse(m.group(2))})
            continue
        cond, rest = split_claim(item)
        if rest:
            out.append({"name": cond.rstrip("."), "consequence": rest})
        else:
            out.append({"name": cond.rstrip("."), "consequence": ""})
    return out


# --------------------------------------------------------------------------
# case construction — every clause quotes the skill's own text
# --------------------------------------------------------------------------

def q(s: str) -> str:
    """Quote material so it is visibly the skill's wording, not the harness's."""
    return '"' + s.strip().strip('"') + '"'


def build_cases(name: str, body: str) -> List[Dict[str, str]]:
    cases: List[Dict[str, str]] = []
    purpose = collapse(section(body, "Purpose"))
    checklist = parse_checklist(section(body, "Quality Checklist"))
    steps = parse_workflow_steps(section(body, "Workflow"))
    exclusions = parse_marked_items(section(body, "When NOT to Use"))
    failures = parse_failure_modes(section(body, "Failure Modes"))
    antis = parse_anti_patterns(section(body, "Anti-Patterns"))

    # ---- 1. Applies -------------------------------------------------
    if checklist:
        first, last = checklist[0], checklist[-1]
        mid = checklist[len(checklist) // 2] if len(checklist) > 2 else checklist[-1]
        then_parts = []
        if steps:
            then_parts.append(f"the workflow runs in its stated order — {q(clip(steps[0], 70))} "
                              f"through to {q(clip(steps[-1], 70))}")
        then_parts.append(f"and before delivery these specific conditions hold: {q(clip(first))}; "
                          f"{q(clip(mid))}; {q(clip(last))}")
        fail_parts = [f"{q(clip(first))} is false", f"{q(clip(last))} is false"]
        if steps:
            fail_parts.append(f"the result is delivered before {q(clip(steps[-1], 70))} has run")
        else:
            fail_parts.append(f"{q(clip(mid))} is false")
        cases.append({
            "label": "Applies to the task it was written for",
            "given": f"A task inside this skill's stated purpose: {clip(purpose, 240)}",
            "when": f"the agent executes `{name}` end to end on that task",
            "then": "; ".join(then_parts),
            "fail": ", or ".join(fail_parts),
        })

    # ---- 2. Declines (one per exclusion) ----------------------------
    for item in exclusions:
        cond, alt = split_claim(item)
        if not cond:
            continue
        then = (f"the skill is not selected, and what is done instead is what this exclusion "
                f"names: {q(clip(alt, 200))}" if alt else
                f"the skill is not selected, because this task is the excluded case {q(clip(cond, 160))}, "
                f"and the reason given is that exclusion rather than a generic decline")
        fail = (f"the skill is run on a task where {q(clip(cond, 150))}, and the consequence that "
                f"exclusion states follows — {q(clip(alt, 150))}" if alt else
                f"the skill is run on a task where {q(clip(cond, 150))}")
        fail += f"; or `{name}` is declined without naming that exclusion"
        cases.append({
            "label": f"Declines: {clip(cond, 78)}",
            "given": f"A task that looks like a match but is this skill's excluded case: {clip(cond, 170)}",
            "when": f"the agent considers `{name}` for that task",
            "then": then,
            "fail": fail,
        })

    # ---- 3. Detects (one per failure mode) --------------------------
    for fm in failures:
        failure = fm["failure"]
        if fm["kind"] == "table":
            det, resp = fm.get("detection", ""), fm.get("response", "")
            then = (f"the failure is caught by its documented detection signal — {q(clip(det, 170))} — "
                    f"and the response applied is the documented one: {q(clip(resp, 190))}")
            fail = (f"{q(clip(failure, 120))} reaches the output because {q(clip(det, 130))} was never "
                    f"checked; or it is caught but the response taken is not {q(clip(resp, 150))}")
        else:
            desc = fm.get("response", "")
            then = (f"{q(clip(failure, 90))} is recognised as a failure of this skill rather than "
                    f"accepted as a result, because the skill states what it looks like: "
                    f"{q(clip(desc, 190))}")
            fail = (f"{q(clip(failure, 90))} appears in the work and is reported as complete — "
                    f"specifically {q(clip(desc, 170))}")
        cases.append({
            "label": f"Detects: {clip(failure, 78)}",
            "given": f"A run of this skill in which the known failure mode is present: {clip(failure, 150)}",
            "when": f"the agent executes `{name}` and reaches the point where this failure occurs",
            "then": then,
            "fail": fail,
        })

    # ---- 4. Avoids (one per anti-pattern) ---------------------------
    for ap in antis:
        nm, cons = ap["name"], ap["consequence"]
        then = (f"{q(clip(nm, 90))} is absent from the output, and the work shows it was ruled out "
                f"for the reason this skill gives: {q(clip(cons, 190))}" if cons else
                f"{q(clip(nm, 90))} is absent from the output, and the work shows the alternative "
                f"this skill prescribes was chosen deliberately")
        fail = (f"{q(clip(nm, 90))} appears in the output — that is, {q(clip(cons, 170))}" if cons else
                f"{q(clip(nm, 90))} appears in the output")
        fail += (f"; or it is absent by accident, with nothing in `{name}` having ruled it out"
                 if cons else
                 f"; or it is absent by accident, with nothing in `{name}` having ruled it out")
        cases.append({
            "label": f"Avoids: {clip(nm, 78)}",
            "given": (f"A situation that invites the anti-pattern {q(clip(nm, 90))}"
                      + (f", whose stated consequence is: {clip(cons, 170)}" if cons else "")),
            "when": f"the agent applies `{name}` in that situation",
            "then": then,
            "fail": fail,
        })

    return cases


HEADER = """# Test cases — `{name}`

Every clause below is derived from this skill's own body text. Nothing here is a
generic control that would read the same for a different skill:

| Case kind | Derived from | What it asserts |
|---|---|---|
| Applies | Purpose, Workflow step titles, Quality Checklist items | the named checklist conditions hold and the named steps ran |
| Declines | each `When NOT to Use` exclusion | the exclusion is honoured and the alternative it names is used |
| Detects | each `Failure Modes` entry, with its own detection signal and response | the failure is caught by that signal and answered by that response |
| Avoids | each `Anti-Patterns` entry, with the consequence it states | the anti-pattern is absent for the reason this skill gives |

Quoted text is the skill's own wording. A case whose quoted material could be
lifted from another skill is a defect and should be reported, not relaxed.

Regenerate: `python3 scripts/generate-index/generate_skill_tests.py`
Measure distinctness: `python3 scripts/generate-index/generate_skill_tests.py --report`

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

"""


def render(name: str, cases: List[Dict[str, str]]) -> str:
    out = [HEADER.format(name=name)]
    for i, c in enumerate(cases, 1):
        out.append(f"## Case {i} — {c['label']}\n")
        out.append("```text")
        out.append(f"GIVEN    {c['given']}")
        out.append(f"WHEN     {c['when']}")
        out.append(f"THEN     {c['then']}")
        out.append(f"FAIL IF  {c['fail']}")
        out.append("```\n")
    return "\n".join(out).rstrip() + "\n"


def measure(all_cases: Dict[str, List[Dict[str, str]]]) -> Dict[str, Any]:
    total = sum(len(v) for v in all_cases.values())
    then_c = Counter(c["then"] for v in all_cases.values() for c in v)
    fail_c = Counter(c["fail"] for v in all_cases.values() for c in v)
    given_c = Counter(c["given"] for v in all_cases.values() for c in v)
    when_c = Counter(c["when"] for v in all_cases.values() for c in v)
    # how many distinct skills share each FAIL IF
    share: Dict[str, set] = defaultdict(set)
    for skill, v in all_cases.items():
        for c in v:
            share[c["fail"]].add(skill)
    return {
        "total": total,
        "skills": len(all_cases),
        "distinct": {"given": len(given_c), "when": len(when_c),
                     "then": len(then_c), "fail": len(fail_c)},
        "top_fail": fail_c.most_common(3),
        "top_then": then_c.most_common(3),
        "max_skills_sharing_a_fail_if": max((len(v) for v in share.values()), default=0),
        "then_ratio": len(then_c) / total if total else 0,
        "fail_ratio": len(fail_c) / total if total else 0,
        "per_skill": {k: len(v) for k, v in sorted(all_cases.items())},
    }


def set_frontmatter_count(skill_md: Path, n: int) -> bool:
    t = skill_md.read_text()
    new = re.sub(r"(?m)^tests:\s*\d+\s*$", f"tests: {n}", t, count=1)
    if new == t:
        if re.search(r"(?m)^tests:", t):
            return False
        new = re.sub(r"(?m)^(updated:.*)$", rf"tests: {n}\n\1", t, count=1)
    if new != t:
        skill_md.write_text(new)
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true", help="measure only, write nothing")
    ap.add_argument("--check", action="store_true", help="CI mode: no drift + distinctness gates")
    ap.add_argument("--min-distinct", type=float, default=0.95,
                    help="minimum distinct-THEN and distinct-FAIL IF ratio across the corpus")
    ap.add_argument("--max-share", type=int, default=1,
                    help="maximum number of skills that may share one FAIL IF string")
    args = ap.parse_args()

    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
    all_cases: Dict[str, List[Dict[str, str]]] = {}
    unparsed: List[str] = []
    for d in skill_dirs:
        name = d.name
        body = (d / "SKILL.md").read_text()
        body = re.sub(r"\A---.*?^---\s*\n", "", body, flags=re.DOTALL | re.MULTILINE)
        cases = build_cases(name, body)
        if len(cases) < 3:
            unparsed.append(f"{name} ({len(cases)} cases)")
        all_cases[name] = cases

    m = measure(all_cases)
    drift = []
    for name, cases in all_cases.items():
        p = SKILLS / name / "tests" / "cases.md"
        want = render(name, cases)
        if not p.exists() or p.read_text() != want:
            drift.append(name)
        skill_md = SKILLS / name / "SKILL.md"
        fm = re.search(r"(?m)^tests:\s*(\d+)\s*$", skill_md.read_text())
        if fm and int(fm.group(1)) != len(cases):
            drift.append(f"{name} (frontmatter tests: {fm.group(1)} != {len(cases)})")

    print(f"skills                    : {m['skills']}")
    print(f"cases generated           : {m['total']}")
    print(f"per-skill min / max       : {min(m['per_skill'].values())} / {max(m['per_skill'].values())}")
    print(f"distinct GIVEN            : {m['distinct']['given']:>4} / {m['total']}")
    print(f"distinct WHEN             : {m['distinct']['when']:>4} / {m['total']}")
    print(f"distinct THEN             : {m['distinct']['then']:>4} / {m['total']}  ratio {m['then_ratio']:.3f}")
    print(f"distinct FAIL IF          : {m['distinct']['fail']:>4} / {m['total']}  ratio {m['fail_ratio']:.3f}")
    print(f"max skills sharing a FAIL IF: {m['max_skills_sharing_a_fail_if']}")
    if unparsed:
        print(f"skills with <3 parsed cases: {', '.join(unparsed)}")

    ok = True
    if m["then_ratio"] < args.min_distinct:
        print(f"FAIL: THEN distinctness {m['then_ratio']:.3f} < {args.min_distinct}")
        ok = False
    if m["fail_ratio"] < args.min_distinct:
        print(f"FAIL: FAIL IF distinctness {m['fail_ratio']:.3f} < {args.min_distinct}")
        ok = False
    if m["max_skills_sharing_a_fail_if"] > args.max_share:
        print(f"FAIL: one FAIL IF is shared by {m['max_skills_sharing_a_fail_if']} skills "
              f"(max {args.max_share}) — that assertion is generic")
        for txt, n in m["top_fail"]:
            if n > 1:
                print(f"        {n}x  {txt[:110]}")
        ok = False
    if unparsed:
        print(f"FAIL: {len(unparsed)} skills yielded fewer than 3 cases — parser missed a section shape")
        ok = False

    if args.report:
        print("\nmost common THEN:")
        for txt, n in m["top_then"]:
            print(f"  {n}x  {txt[:130]}")
        print("\nmost common FAIL IF:")
        for txt, n in m["top_fail"]:
            print(f"  {n}x  {txt[:130]}")
        return 0 if ok else 1

    if args.check:
        if drift:
            print(f"FAIL: {len(drift)} files out of sync with the generator:")
            for d in drift[:12]:
                print(f"        {d}")
            ok = False
        print("distinctness gates: " + ("pass" if ok else "FAIL"))
        return 0 if ok else 1

    if not ok:
        print("\nrefusing to write output that is not skill-specific", file=sys.stderr)
        return 1

    for name, cases in all_cases.items():
        p = SKILLS / name / "tests" / "cases.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(render(name, cases))
        set_frontmatter_count(SKILLS / name / "SKILL.md", len(cases))
    print(f"\nwrote {len(all_cases)} cases.md files, {m['total']} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
