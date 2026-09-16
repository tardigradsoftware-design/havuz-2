#!/usr/bin/env python3
"""Validate YAML frontmatter across the repository.

Checks, in order:
  1. every governed Markdown file HAS frontmatter
  2. the frontmatter parses as a YAML mapping
  3. it validates against the JSON Schema for its directory
  4. `id` values are unique repository-wide and match the file location
  5. `updated` / `verified_at` are real dates and not in the future
  6. declared `sources[]` have url + type + verified_at
  7. semantic-chunk headings exist when `sections:` is declared
  8. token budget (AGENTS.md §4.3)

Exit code 1 on any error. Warnings do not fail the build.

Usage:
    python3 scripts/validate/validate_frontmatter.py            # all
    python3 scripts/validate/validate_frontmatter.py --strict   # warnings become errors
    python3 scripts/validate/validate_frontmatter.py --path knowledge/frontend
"""
from __future__ import annotations

import argparse
import re
import sys
import warnings
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
warnings.filterwarnings("ignore", category=DeprecationWarning)

from lib import frontmatter as fm  # noqa: E402

TODAY = date.today()

TOKEN_BUDGET = {
    "skills": 2500,
    "knowledge": 3000,
    "agents": 1500,
    "patterns": 1200,
    "workflows": 2000,
    "prompts": 2500,
    "evaluations": 2000,
}

DATE_FIELDS = ("updated", "verified_at", "expires_at", "last_test_run")


def top_dir(rel: str) -> str:
    return rel.split("/")[0]


def check_dates(rel: str, data: Dict) -> List[str]:
    errs = []
    for f in DATE_FIELDS:
        v = data.get(f)
        if v is None:
            continue
        if isinstance(v, (datetime, date)):
            d = v if isinstance(v, date) else v.date()
        else:
            try:
                d = datetime.strptime(str(v), "%Y-%m-%d").date()
            except ValueError:
                errs.append(f"{f}: '{v}' is not YYYY-MM-DD")
                continue
        # expires_at is *required* to be in the future — that is what a review window is.
        if d > TODAY and f != "expires_at":
            errs.append(f"{f}: {d.isoformat()} is in the future")
    va, ex = data.get("verified_at"), data.get("expires_at")
    if isinstance(va, (date, datetime)) and isinstance(ex, (date, datetime)):
        if (ex if isinstance(ex, date) else ex.date()) < (va if isinstance(va, date) else va.date()):
            errs.append("expires_at is before verified_at")
    return errs


def check_sources(rel: str, data: Dict) -> List[str]:
    errs = []
    for i, s in enumerate(data.get("sources") or []):
        if not isinstance(s, dict):
            errs.append(f"sources[{i}]: not a mapping")
            continue
        if not s.get("url"):
            errs.append(f"sources[{i}]: missing url")
        elif not re.match(r"^https?://", str(s["url"])):
            errs.append(f"sources[{i}]: url must be absolute http(s): {s['url']}")
        if not s.get("type"):
            errs.append(f"sources[{i}]: missing type")
        if not s.get("verified_at"):
            errs.append(f"sources[{i}]: missing verified_at (an undated citation is not a citation)")
    return errs


def check_sections(rel: str, data: Dict, body: str) -> List[str]:
    errs = []
    declared = data.get("sections")
    if not declared:
        return errs
    anchors = {"#" + fm.slugify(h) for lvl, h in fm.headings(body)}
    for i, s in enumerate(declared):
        if not isinstance(s, dict) or "anchor" not in s:
            continue
        if s["anchor"] not in anchors:
            errs.append(f"sections[{i}]: anchor {s['anchor']} has no matching heading")
    return errs


def check_budget(rel: str, data: Dict, body: str) -> List[str]:
    warn = []
    budget = TOKEN_BUDGET.get(top_dir(rel))
    if not budget:
        return warn
    n = fm.estimate_tokens(body)
    if n > budget * 1.35:
        warn.append(f"body ≈{n} tokens exceeds the {budget} budget by >35% — split into references/")
    declared = data.get("estimated_tokens")
    if declared and abs(int(declared) - n) > max(400, n * 0.35):
        warn.append(f"estimated_tokens={declared} but measured ≈{n}")
    return warn


def expected_id(rel: str) -> str:
    p = Path(rel)
    stem = p.stem
    if stem in ("SKILL",):
        return p.parent.name
    if stem in ("AGENT", "WORKFLOW"):
        return p.parent.name
    if stem == "README":
        return p.parent.name
    return stem


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--path", default=None)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    files = fm.iter_markdown(ROOT)
    if args.path:
        files = [f for f in files if args.path in f.relative_to(ROOT).as_posix()]

    errors: List[str] = []
    warns: List[str] = []
    ids: Dict[str, List[str]] = defaultdict(list)
    governed = missing = 0

    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        doc = fm.parse(f)
        if not fm.requires_frontmatter(rel):
            continue
        governed += 1
        if not doc.raw_front:
            missing += 1
            errors.append(f"{rel}: missing frontmatter (expected schema {doc.schema})")
            continue
        if doc.parse_error:
            errors.append(f"{rel}: {doc.parse_error}")
            continue
        for e in fm.validate(doc):
            errors.append(f"{rel}: {e}")
        for e in check_dates(rel, doc.data):
            errors.append(f"{rel}: {e}")
        for e in check_sources(rel, doc.data):
            errors.append(f"{rel}: {e}")
        for e in check_sections(rel, doc.data, doc.body):
            errors.append(f"{rel}: {e}")
        for w in check_budget(rel, doc.data, doc.body):
            warns.append(f"{rel}: {w}")
        if doc.data.get("id"):
            ids[str(doc.data["id"])].append(rel)
            exp = expected_id(rel)
            if doc.data["id"] != exp and top_dir(rel) in ("skills", "agents", "workflows"):
                warns.append(f"{rel}: id '{doc.data['id']}' does not match folder '{exp}'")
        if doc.data.get("confidence") == "high" and not (doc.data.get("sources")):
            warns.append(f"{rel}: confidence 'high' with no sources[] — downgrade or cite")
        # An evidence level caps the confidence a document may claim. Enforced as an
        # error, corpus-wide, so a claim can never outstate the evidence behind it.
        # The table lives in scripts/lib/frontmatter.py next to the schema defs it is
        # derived from, and README.md documents the same rule in prose.
        cap_err = fm.confidence_cap_error(doc.data.get("evidence_level"),
                                          doc.data.get("confidence"))
        if cap_err:
            errors.append(f"{rel}: {cap_err}")
        if doc.data.get("claim_type") == "fact" and not doc.data.get("sources"):
            errors.append(f"{rel}: claim_type 'fact' requires at least one source")

    for i, paths in ids.items():
        if len(paths) > 1:
            errors.append(f"duplicate id '{i}' in: {', '.join(paths)}")

    if not args.quiet:
        print(f"Governed markdown files : {governed}")
        print(f"Missing frontmatter     : {missing}")
        print(f"Unique ids              : {len(ids)}")
        print(f"Errors                  : {len(errors)}")
        print(f"Warnings                : {len(warns)}")
    for e in errors[:120]:
        print("  ERROR  " + e)
    if len(errors) > 120:
        print(f"  … and {len(errors)-120} more errors")
    if not args.strict:
        for w in warns[:60]:
            print("  warn   " + w)
        if len(warns) > 60:
            print(f"  … and {len(warns)-60} more warnings")
    else:
        for w in warns[:120]:
            print("  ERROR  " + w)
        errors.extend(warns)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
