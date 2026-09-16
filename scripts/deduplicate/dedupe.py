#!/usr/bin/env python3
"""Duplicate / near-duplicate detection across the knowledge base.

Duplicate knowledge is a defect: it drifts, contradicts itself, and doubles the
token cost of retrieval. This tool reports overlapping content so it can be
extracted into one canonical location and linked.

Method (cheap, deterministic, no model calls):
  1. shingle each document into k-token n-grams (k=8, normalised)
  2. compare Jaccard similarity between documents that share >=1 tag or domain
  3. report pairs above --threshold (default 0.30)
  4. also report exact duplicate *headings* across files — the usual sign that two
     documents cover the same ground

Usage:
    python3 scripts/deduplicate/dedupe.py --report
    python3 scripts/deduplicate/dedupe.py --threshold 0.4 --json metadata/duplicates.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402

STOP = set("""a an the and or but if then else of to in on for with without from by at as is are was were be
been being this that these those it its their there here we you i not no yes can could should would will may
might must have has had do does did done more most less least than into over under between within each every
any all some such only also very just now new old first second third""".split())

WORD = re.compile(r"[a-z0-9][a-z0-9._+-]*")


def tokens(body: str) -> List[str]:
    body = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)
    body = re.sub(r"`[^`]*`", " ", body)
    body = re.sub(r"!?\[[^\]]*\]\([^)]*\)", " ", body)
    body = re.sub(r"^#{1,6}\s+", " ", body, flags=re.MULTILINE)
    out = []
    for w in WORD.findall(body.lower()):
        if w not in STOP and len(w) > 2:
            out.append(w)
    return out


def shingles(toks: List[str], k: int = 8) -> Set[str]:
    if len(toks) < k:
        return {" ".join(toks)} if toks else set()
    return {" ".join(toks[i:i + k]) for i in range(0, len(toks) - k + 1, 2)}


def jaccard(a: Set[str], b: Set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    return inter / (len(a) + len(b) - inter)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=float, default=0.30)
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--json", default=None)
    ap.add_argument("--k", type=int, default=8)
    args = ap.parse_args()

    docs = []
    for f in fm.iter_markdown(ROOT):
        rel = f.relative_to(ROOT).as_posix()
        if rel.startswith(("indexes/", "repositories/", ".github/")):
            continue
        d = fm.parse(f)
        toks = tokens(d.body)
        if len(toks) < 60:
            continue
        docs.append({
            "rel": rel, "shingles": shingles(toks, args.k),
            "tags": set(map(str, d.data.get("tags") or [])),
            "domain": d.data.get("domain") or d.data.get("category") or "",
            "heads": {fm.slugify(h) for _, h in fm.headings(d.body)},
            "ntok": len(toks),
        })

    print(f"Indexed {len(docs)} documents ({sum(d['ntok'] for d in docs)} tokens)")

    pairs: List[Tuple[float, str, str]] = []
    for i in range(len(docs)):
        a = docs[i]
        for j in range(i + 1, len(docs)):
            b = docs[j]
            if not (a["tags"] & b["tags"]) and a["domain"] != b["domain"]:
                continue
            s = jaccard(a["shingles"], b["shingles"])
            if s >= args.threshold:
                pairs.append((s, a["rel"], b["rel"]))

    # duplicate headings across files (strong signal of topical overlap)
    head_map: Dict[str, List[str]] = defaultdict(list)
    for d in docs:
        for h in d["heads"]:
            if len(h) > 6 and h not in ("overview", "references", "examples", "when-to-use",
                                        "quality-checklist", "failure-modes", "anti-patterns",
                                        "related-skills", "evaluation-criteria", "workflow",
                                        "inputs", "outputs", "validation", "purpose"):
                head_map[h].append(d["rel"])
    dup_heads = {h: v for h, v in head_map.items() if len(v) > 2}

    pairs.sort(reverse=True)
    print(f"\nNear-duplicate pairs above {args.threshold}: {len(pairs)}")
    for s, x, y in pairs[:40]:
        print(f"  {s:.2f}  {x}\n        {y}")
    if len(pairs) > 40:
        print(f"  … and {len(pairs)-40} more")
    print(f"\nHeadings repeated in >2 files: {len(dup_heads)}")
    for h, v in sorted(dup_heads.items(), key=lambda kv: -len(kv[1]))[:20]:
        print(f"  {h}  ({len(v)} files)")

    if args.json:
        out = {"threshold": args.threshold, "documents": len(docs),
               "pairs": [{"similarity": round(s, 4), "a": x, "b": y} for s, x, y in pairs],
               "repeated_headings": {h: v for h, v in dup_heads.items()}}
        p = ROOT / args.json
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=2) + "\n")
        print(f"\nWrote {args.json}")

    if args.report:
        return 0
    return 1 if pairs else 0


if __name__ == "__main__":
    raise SystemExit(main())
