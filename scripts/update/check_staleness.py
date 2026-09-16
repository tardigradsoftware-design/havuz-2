#!/usr/bin/env python3
"""Freshness report: what in this repository has expired and must be re-verified.

Reads every record carrying `expires_at` / `verified_at` (Markdown frontmatter and
metadata/*.json) and buckets it:

    EXPIRED       past expires_at — re-verify before acting
    DUE SOON      expires within --window days
    NO EXPIRY     verified_at present but no expiry policy applied
    NEVER CHECKED no verified_at at all — worst case

Usage:
    python3 scripts/update/check_staleness.py
    python3 scripts/update/check_staleness.py --window 14 --json metadata/staleness.json
    python3 scripts/update/check_staleness.py --fail-on expired   # CI gate
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402
from lib.scoring import expires_for  # noqa: E402

TODAY = date.today()

JSON_TARGETS = [
    ("metadata/repositories.json", "repositories", "slug"),
    ("metadata/sources-papers.json", "sources", "title"),
    ("metadata/tools.json", "tools", "name"),
    ("metadata/skills.json", "skills", "name"),
    ("metadata/evaluations.json", "evaluations", "id"),
    ("metadata/sources.json", "sources", "title"),
]


def as_date(v: Any):
    if v is None:
        return None
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, date):
        return v
    try:
        return datetime.strptime(str(v)[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def collect() -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for f in fm.iter_markdown(ROOT):
        rel = f.relative_to(ROOT).as_posix()
        if rel.startswith(("indexes/", "repositories/", ".github/")):
            continue
        d = fm.parse(f)
        if not d.data:
            continue
        rows.append({"where": rel, "what": d.data.get("id") or d.data.get("title") or rel,
                     "kind": "document", "verified_at": as_date(d.data.get("verified_at")),
                     "expires_at": as_date(d.data.get("expires_at")),
                     "status": d.data.get("status"), "confidence": d.data.get("confidence")})
    for rel, listkey, namekey in JSON_TARGETS:
        p = ROOT / rel
        if not p.exists():
            continue
        blob = json.loads(p.read_text())
        for r in blob.get(listkey, []):
            rows.append({"where": rel, "what": r.get(namekey) or r.get("id") or "?",
                         "kind": "record", "verified_at": as_date(r.get("verified_at")),
                         "expires_at": as_date(r.get("expires_at")),
                         "status": r.get("status"), "confidence": r.get("confidence")})
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--window", type=int, default=30)
    ap.add_argument("--json", default=None)
    ap.add_argument("--fail-on", choices=["expired", "never", "none"], default="none")
    ap.add_argument("--max-expired", type=int, default=100000)
    args = ap.parse_args()

    rows = collect()
    expired, soon, no_expiry, never = [], [], [], []
    horizon = TODAY + timedelta(days=args.window)
    for r in rows:
        if r["verified_at"] is None:
            never.append(r)
        elif r["expires_at"] is None:
            no_expiry.append(r)
        elif r["expires_at"] < TODAY:
            expired.append(r)
        elif r["expires_at"] <= horizon:
            soon.append(r)

    print(f"Records scanned        : {len(rows)}")
    print(f"EXPIRED                : {len(expired)}")
    print(f"DUE within {args.window} days      : {len(soon)}")
    print(f"NO EXPIRY POLICY       : {len(no_expiry)}")
    print(f"NEVER VERIFIED         : {len(never)}")

    def show(title, items, n=25):
        if not items:
            return
        print(f"\n{title}")
        for r in items[:n]:
            print(f"  {str(r['expires_at'] or r['verified_at'] or '—'):12} {r['where'][:44]:46} {str(r['what'])[:52]}")
        if len(items) > n:
            print(f"  … and {len(items)-n} more")

    show("EXPIRED — re-verify before acting:", sorted(expired, key=lambda r: r["expires_at"]))
    show("NEVER VERIFIED — no verified_at:", never)
    show("NO EXPIRY POLICY:", no_expiry, 10)

    if args.json:
        out = {"generated_at": TODAY.isoformat(), "window_days": args.window,
               "counts": {"expired": len(expired), "due_soon": len(soon),
                          "no_expiry": len(no_expiry), "never_verified": len(never)},
               "expired": [{**r, "verified_at": str(r["verified_at"]),
                            "expires_at": str(r["expires_at"]),
                            "days_overdue": (TODAY - r["expires_at"]).days} for r in expired],
               "never_verified": [{**r, "verified_at": None, "expires_at": None} for r in never]}
        p = ROOT / args.json
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=2, default=str) + "\n")
        print(f"\nWrote {args.json}")

    if args.fail_on == "expired" and len(expired) > args.max_expired:
        print(f"\nFAIL: {len(expired)} expired records exceed --max-expired={args.max_expired}")
        return 1
    if args.fail_on == "never" and never:
        print(f"\nFAIL: {len(never)} records have no verified_at")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
