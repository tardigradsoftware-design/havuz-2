#!/usr/bin/env python3
"""Validate every JSON artifact under metadata/ against schemas/.

Also checks registry-level invariants that a per-record schema cannot express:
  * unique slugs / ids
  * no record with fetch_ok == false is presented as verified
  * archived repositories are never marked production_ready
  * records past expires_at are reported (warning, not error)
  * quarantine files stay out of the retrieval index

Usage:
    python3 scripts/validate/validate_json.py
    python3 scripts/validate/validate_json.py --strict
"""
from __future__ import annotations

import argparse
import json
import sys
import warnings
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
warnings.filterwarnings("ignore", category=DeprecationWarning)

from lib import frontmatter as fm  # noqa: E402

TODAY = date.today()

# (path, item-schema, list key, unique key) — or (path, container-schema, None, None)
# for files whose schema describes the whole document rather than each record.
TARGETS = [
    ("metadata/repositories.json", "repository.schema.json", "repositories", "slug"),
    ("metadata/sources-papers.json", "source.schema.json", "sources", "id"),
    ("metadata/tools.json", "mcp.schema.json", "tools", "id"),
    ("metadata/skills.json", "skill.schema.json", "skills", "name"),
    ("metadata/evaluations.json", "evaluation.schema.json", "evaluations", "id"),
    ("metadata/sources.json", "source.schema.json", "sources", "id"),
    ("metadata/agents.json", "agent.schema.json", "agents", "name"),
    ("metadata/workflows.json", "workflow.schema.json", "workflows", "name"),
    ("metadata/models.json", "model.schema.json", "models", "id"),
    ("metadata/datasets.json", "dataset.schema.json", "datasets", "id"),
    ("metadata/prompts.json", "prompt.schema.json", "prompts", "id"),
    ("scripts/update/seeds.json", "seeds.schema.json", None, None),
]

QUARANTINED = ["metadata/pending-paper-candidates.json", "metadata/unresolved-seeds.json"]


# Keys that scripts/generate-index/extract_registries.py adds to every record it emits.
# They are generator bookkeeping (where the record came from, how big it is, what it contains),
# not content, so the content schemas do not — and should not — describe them. Stripping this
# explicit allowlist before validation keeps the schemas honest about *content* while still
# rejecting any other unknown key, including a mistyped annotation such as `_headingz`.
BUILD_ANNOTATIONS = frozenset({"_path", "_tokens", "_headings"})


def strip_annotations(rec: Dict[str, Any]) -> Dict[str, Any]:
    """Return the record without generator bookkeeping keys."""
    return {k: v for k, v in rec.items() if k not in BUILD_ANNOTATIONS}


def validate_records(rel: str, schema_name: str, records: List[Dict[str, Any]], key: str,
                     strict: bool) -> tuple[List[str], List[str]]:
    errs, warns = [], []
    schema = fm.load_schema(schema_name)
    store = {}
    for f in (ROOT / "schemas").glob("*.json"):
        s = json.loads(f.read_text())
        if "$id" in s:
            store[s["$id"]] = s
        store[f.name] = s
    resolver = fm.RefResolver(base_uri=f"file://{ROOT/'schemas'}/", referrer=schema, store=store)
    validator = fm.jsonschema.Draft202012Validator(schema, resolver=resolver)

    seen = Counter()
    for i, rec in enumerate(records):
        for e in validator.iter_errors(strip_annotations(rec)):
            loc = "/".join(str(p) for p in e.path) or "(root)"
            errs.append(f"{rel}[{i}] {rec.get(key, '?')}: {loc}: {e.message[:200]}")
        if rec.get(key):
            seen[str(rec[key])] += 1
        # registry invariants
        if "archived" in rec and rec.get("archived") and rec.get("production_ready"):
            errs.append(f"{rel}[{i}] {rec.get(key)}: archived but production_ready=true")
        if rec.get("fetch_ok") is False and rec.get("evidence_level") == "verified-github-api":
            errs.append(f"{rel}[{i}] {rec.get(key)}: fetch failed but marked verified")
        if rec.get("status") == "ARCHIVED" and rec.get("tier") not in ("ARCHIVED", None):
            warns.append(f"{rel}[{i}] {rec.get(key)}: status ARCHIVED but tier {rec.get('tier')}")
        if rec.get("stars") and rec.get("stars_checked_at") is None:
            errs.append(f"{rel}[{i}] {rec.get(key)}: stars without stars_checked_at")
        exp = rec.get("expires_at")
        if exp:
            try:
                d = datetime.strptime(str(exp)[:10], "%Y-%m-%d").date()
                if d < TODAY:
                    warns.append(f"{rel}[{i}] {rec.get(key)}: expired {d.isoformat()} — re-verify")
            except ValueError:
                errs.append(f"{rel}[{i}] {rec.get(key)}: bad expires_at '{exp}'")
    for k, n in seen.items():
        if n > 1:
            errs.append(f"{rel}: duplicate {key} '{k}' ({n}x)")
    return errs, warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    errors: List[str] = []
    warns: List[str] = []
    total = 0

    for rel, schema_name, listkey, keyfield in TARGETS:
        p = ROOT / rel
        if not p.exists():
            warns.append(f"{rel}: absent (not yet generated)")
            continue
        try:
            blob = json.loads(p.read_text())
        except json.JSONDecodeError as e:
            errors.append(f"{rel}: invalid JSON — {e}")
            continue
        if listkey is None:
            # container schema: validate the whole document
            schema = fm.load_schema(schema_name)
            store = {}
            for f in (ROOT / "schemas").glob("*.json"):
                js = json.loads(f.read_text())
                if "$id" in js:
                    store[js["$id"]] = js
                store[f.name] = js
            resolver = fm.RefResolver(base_uri=f"file://{ROOT/'schemas'}/", referrer=schema, store=store)
            e = [f"{rel}: {'/'.join(map(str, x.path)) or '(root)'}: {x.message[:180]}"
                 for x in fm.jsonschema.Draft202012Validator(schema, resolver=resolver).iter_errors(blob)]
            errors += e
            n = len(blob.get("seeds", []) or [])
            total += n
            print(f"  {rel:42} {n:>4} records  {len(e)} errors  0 warnings")
            continue
        recs = blob.get(listkey) if isinstance(blob, dict) else None
        if recs is None:
            errors.append(f"{rel}: no '{listkey}' array")
            continue
        total += len(recs)
        e, w = validate_records(rel, schema_name, recs, keyfield, args.strict)
        errors += e
        warns += w
        print(f"  {rel:42} {len(recs):>4} records  {len(e)} errors  {len(w)} warnings")

    # every metadata/*.json must at least parse
    for p in sorted((ROOT / "metadata").glob("*.json")):
        try:
            json.loads(p.read_text())
        except json.JSONDecodeError as e:
            errors.append(f"metadata/{p.name}: invalid JSON — {e}")

    # quarantine files must be labelled and excluded from the index
    for rel in QUARANTINED:
        p = ROOT / rel
        if not p.exists():
            continue
        blob = json.loads(p.read_text())
        if not any(k.startswith("_") or k in ("reason", "status") for k in blob):
            warns.append(f"{rel}: quarantine file should carry a leading _warning/_comment key")
        idx = ROOT / "metadata" / "index.json"
        if idx.exists():
            try:
                blob_idx = json.loads(idx.read_text())
            except json.JSONDecodeError:
                blob_idx = {}
            leaked = [e for e in blob_idx.get("entries", [])
                      if Path(rel).name in json.dumps(e)]
            if leaked:
                errors.append(f"{rel}: {len(leaked)} quarantined records leaked into metadata/index.json")

    if args.strict:
        errors += warns
        warns = []

    print(f"\nTotal records validated: {total}")
    print(f"Errors: {len(errors)}   Warnings: {len(warns)}")
    for e in errors[:80]:
        print("  ERROR  " + e)
    if len(errors) > 80:
        print(f"  … and {len(errors)-80} more")
    for w in warns[:40]:
        print("  warn   " + w)
    if len(warns) > 40:
        print(f"  … and {len(warns)-40} more warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
