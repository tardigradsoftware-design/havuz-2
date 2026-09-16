#!/usr/bin/env python3
"""Validate every JSON artifact under metadata/ against schemas/.

Also checks registry-level invariants that a per-record schema cannot express:
  * unique slugs / ids
  * no record with fetch_ok == false is presented as verified
  * archived repositories are never marked production_ready
  * tier labels mean what they say: UNVERIFIED only when the fetch actually failed,
    NO-LICENSE only when no license was detected
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
    # Authored policy data rather than a generated registry, but schema-checked like the
    # rest: an exclusion record that cannot be parsed cannot be enforced.
    ("metadata/excluded-sources.json", "excluded-source.schema.json", "exclusions", "slug"),
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
        # A tier label is a claim about a fact, so both directions are checked. These two
        # were conflated once: every record in the UNVERIFIED tier had fetch_ok == true and
        # merely lacked a license, so the label told readers the metadata was unreliable
        # when it was fine, and hid the signal that actually mattered.
        errs += tier_semantics_errors(rec, rel, i, key)
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



# Tiers decided by the score alone, which a missing license must override.
SCORE_BAND_TIERS = ("S", "A", "B", "C", "EXPERIMENTAL")


def tier_semantics_errors(rec: Dict[str, Any], rel: str, i: int, key: str) -> List[str]:
    """Check that a tier label is backed by the fact it names.

    `UNVERIFIED` is an epistemic claim — the record could not be checked against its
    source. `NO-LICENSE` is a legal one — the record was checked and no license was
    published. They are not degrees of the same thing and must not stand in for each
    other, in either direction:

      * `UNVERIFIED` on a record whose fetch succeeded asserts a failure that did not
        happen, and invites a reader to discard metadata that is sound.
      * a record with no license sitting in a score band (`S`/`A`/`B`/`C`) presents it as
        an adoption candidate, which is what `license_risk` exists to prevent.
      * `NO-LICENSE` on a record that does have a license would prohibit redistribution
        of something freely redistributable.

    Only records that carry the underlying facts are judged. A derived record such as an
    MCP registry entry inherits its tier and does not repeat `fetch_ok`, so it is checked
    against the license fields it does carry and otherwise left alone.
    """
    out: List[str] = []
    tier = rec.get("tier")
    if tier not in ("UNVERIFIED", "NO-LICENSE"):
        # Still catch a no-license record left in a band the score alone decided.
        # EXPERIMENTAL is included because tier_for() tests the license before the score
        # bands: an unlicensed repository at score 2.0 is NO-LICENSE, not EXPERIMENTAL.
        # ARCHIVED is excluded because a frozen repository stays ARCHIVED whether or not
        # it has a license, and DEPRECATED because nothing in the model emits it.
        if tier in SCORE_BAND_TIERS and _license_absent(rec):
            out.append(f"{rel}[{i}] {rec.get(key)}: tier {tier} but no license was "
                       f"detected — expected NO-LICENSE")
        return out

    if tier == "UNVERIFIED":
        if rec.get("fetch_ok") is True:
            out.append(f"{rel}[{i}] {rec.get(key)}: tier UNVERIFIED but fetch_ok is true — "
                       f"the metadata was verified; if the finding was a missing license the "
                       f"tier is NO-LICENSE")
        return out

    # tier == "NO-LICENSE"
    if rec.get("fetch_ok") is False:
        out.append(f"{rel}[{i}] {rec.get(key)}: tier NO-LICENSE but fetch_ok is false — an "
                   f"unverified record cannot claim to have verified the absence of a license")
    if _spdx_license(rec):
        out.append(f"{rel}[{i}] {rec.get(key)}: tier NO-LICENSE but license is "
                   f"{rec.get('license')!r}")
    return out


def _license_absent(rec: Dict[str, Any]) -> bool:
    """True only when the record *positively states* that no license was detected.

    Deliberately narrow. `license: null` does not mean "no license": in
    `metadata/repositories.json` the vocabulary is `"NONE"` for none-detected and
    `"NOASSERTION"` for a license the SPDX list does not recognise, but
    `metadata/tools.json` collapses both of those to `null`. Treating `null` as absence
    therefore accused six custom-licensed MCP entries of being unlicensed and demanded
    they leave tier `A`, where `A` is exactly right — a non-SPDX license caps the tier at
    `A` rather than removing it. The two signals that are unambiguous in every registry
    are `license_risk: no-license-do-not-redistribute` and the literal string `"NONE"`.
    """
    if rec.get("license_risk") == "no-license-do-not-redistribute":
        return True
    return rec.get("license") == "NONE"


def _spdx_license(rec: Dict[str, Any]) -> bool:
    """True when the record names an actual SPDX-recognised license."""
    lic = rec.get("license")
    return bool(lic) and str(lic) not in ("NONE", "NOASSERTION", "null")


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
