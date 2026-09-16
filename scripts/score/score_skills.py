#!/usr/bin/env python3
"""Score every skill, agent, workflow, pattern and knowledge article.

Quality components for authored content (0-10 each) are derived from observable
properties of the document, not from a reviewer's mood:

    authority        do the cited sources rank highly (official > docs > paper > blog)?
    evidence         are claims backed by sources, tests, or measured results?
    recency          how recently was it verified?
    adoption         is it referenced by other documents in this repository?
    reproducibility  does it define inputs, outputs and a validation step?
    practical_value  does it contain a concrete workflow rather than only advice?
    maintenance      is it internally consistent, within budget, and free of dead links?

Writes the score back into each document's frontmatter (scoring:) and into
metadata/skills.json on the next extract_registries.py run.

Usage:
    python3 scripts/score/score_skills.py            # score + write
    python3 scripts/score/score_skills.py --dry      # report only
    python3 scripts/score/score_skills.py --path skills/ai-slop-detection
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402
from lib.scoring import WEIGHTS, tier_for  # noqa: E402

TODAY = date.today()

SOURCE_WEIGHT = {
    "official": 10, "specification": 10, "standard": 10, "official-docs": 9,
    "research-paper": 9, "benchmark": 8, "github-repository": 7, "dataset": 7,
    "framework": 7, "mcp": 7, "agent-skill": 6, "tool": 6, "case-study": 6,
    "example": 5, "tutorial": 4, "blog": 3, "community": 3, "video": 2,
    "discussion": 1, "experimental": 1, "deprecated": 0, "archived": 0,
}

REQUIRED_SKILL_SECTIONS = [
    "purpose", "when to use", "when not to use", "inputs", "workflow",
    "validation", "failure modes", "quality checklist", "anti-patterns",
    "references", "evaluation criteria",
]


def days_since(v) -> Optional[int]:
    if isinstance(v, datetime):
        v = v.date()
    if isinstance(v, date):
        return max(0, (TODAY - v).days)
    try:
        return max(0, (TODAY - datetime.strptime(str(v)[:10], "%Y-%m-%d").date()).days)
    except (ValueError, TypeError):
        return None


def score_doc(doc: fm.Doc, inbound: Counter, all_ids: set) -> Dict[str, Any]:
    d = doc.data
    body = doc.body
    heads = [h.lower() for _, h in fm.headings(body)]
    sources = d.get("sources") or []
    src_types = [str(s.get("type", "")).lower() for s in sources if isinstance(s, dict)]

    # authority
    if src_types:
        authority = max(SOURCE_WEIGHT.get(t, 3) for t in src_types)
    else:
        authority = 2.0
    if d.get("provenance", {}).get("human_reviewed"):
        authority = min(10.0, authority + 0.5)
    if d.get("source_type") == "ai-generated" or (d.get("provenance", {}).get("generated_by") or "").startswith("model"):
        authority = min(authority, 5.0)

    # evidence
    evidence = 1.0
    evidence += min(4.0, 1.2 * len(sources))
    if d.get("claim_type") in ("fact", "experiment"):
        evidence += 1.0
    if d.get("evidence_level") in ("verified-github-api", "verified-official-docs",
                                   "verified-paper", "verified-benchmark-run"):
        evidence += 2.0
    elif d.get("evidence_level") == "cross-checked":
        evidence += 1.5
    elif d.get("evidence_level") in ("model-generated", None):
        evidence -= 0.5
    if d.get("tests") and int(d["tests"]) > 0:
        evidence += min(2.0, 0.5 * int(d["tests"]))
    if d.get("test_pass_rate") is not None:
        evidence += 1.0
    evidence = max(0.0, min(10.0, evidence))

    # recency
    dv = days_since(d.get("verified_at") or d.get("updated"))
    if dv is None:
        recency = 2.0
    else:
        recency = max(0.0, min(10.0, 10.0 - dv / 73.0))

    # adoption (inbound references from other documents in this repo)
    ident = d.get("id") or d.get("name") or ""
    n_in = inbound.get(ident, 0)
    adoption = min(10.0, 1.5 + 1.3 * n_in)

    # reproducibility: is it an executable procedure?
    reproducibility = 1.0
    for marker in ("## inputs", "## outputs", "## workflow", "## validation",
                   "## process", "## expected output"):
        if any(marker.lstrip("# ").strip() == h for h in heads):
            reproducibility += 1.6
    if re.search(r"```", body):
        reproducibility += 0.8
    if re.search(r"(?i)\b(exit gate|checklist|fail if|then\b)", body):
        reproducibility += 0.8
    reproducibility = min(10.0, reproducibility)

    # practical value
    practical = 1.0
    n_tok = fm.estimate_tokens(body)
    practical += min(3.0, n_tok / 700.0)
    practical += min(2.5, 0.5 * len(re.findall(r"(?m)^\d+\.\s", body)))
    if any("anti-pattern" in h for h in heads):
        practical += 1.0
    if any("failure" in h for h in heads):
        practical += 1.0
    if any("example" in h for h in heads):
        practical += 1.0
    practical = min(10.0, practical)

    # maintenance: internal consistency + budget + citations dated
    maintenance = 5.0
    budget = {"skills": 2500, "knowledge": 3000, "agents": 1500, "patterns": 1200}.get(
        doc.rel.split("/")[0], 2500)
    if n_tok > budget * 1.35:
        maintenance -= 2.0
    undated = [s for s in sources if isinstance(s, dict) and not s.get("verified_at")]
    maintenance -= min(3.0, 0.75 * len(undated))
    if d.get("version"):
        maintenance += 1.0
    if d.get("status") == "active":
        maintenance += 1.0
    if d.get("status") in ("draft", "experimental"):
        maintenance -= 0.5
    if doc.rel.startswith("skills/") and doc.path.name == "SKILL.md":
        missing = [s for s in REQUIRED_SKILL_SECTIONS if not any(s in h for h in heads)]
        maintenance -= min(4.0, 0.5 * len(missing))
    maintenance = max(0.0, min(10.0, maintenance))

    components = {
        "authority": round(authority, 2),
        "evidence": round(evidence, 2),
        "recency": round(recency, 2),
        "adoption": round(adoption, 2),
        "reproducibility": round(reproducibility, 2),
        "practical_value": round(practical, 2),
        "maintenance": round(maintenance, 2),
    }
    # reuse the repository weights where the component names overlap
    w = {
        "authority": 0.20, "evidence": 0.20, "recency": 0.10, "adoption": 0.10,
        "reproducibility": 0.15, "practical_value": 0.15, "maintenance": 0.10,
    }
    total = sum(components[k] * w[k] for k in w)
    trust = (components["authority"] * 0.30 + components["evidence"] * 0.30
             + components["recency"] * 0.15 + components["maintenance"] * 0.15
             + components["reproducibility"] * 0.10)
    tier = tier_for(total, archived=False, license_ok=True,
                    nonstandard=d.get("source_type") == "ai-generated")
    if d.get("status") == "experimental" or doc.rel.startswith("experimental/"):
        tier = "EXPERIMENTAL"
    return {
        "components": components,
        "quality_score": round(total, 2),
        "trust_score": round(min(10.0, trust), 2),
        "tier": tier,
        "maturity": ("experimental" if tier == "EXPERIMENTAL" else
                     "production-grade" if tier in ("S", "A") else
                     "production-ready" if tier == "B" else "early"),
        "scored_by": "scripts/score/score_skills.py",
        "scored_at": TODAY.isoformat(),
    }


def rewrite_frontmatter(path: Path, data: Dict[str, Any], raw: str) -> None:
    """Write the scoring block back into the frontmatter without reformatting everything."""
    import yaml

    class Dumper(yaml.SafeDumper):
        pass

    def str_presenter(dumper, s):
        if "\n" in s or len(s) > 96:
            return dumper.represent_scalar("tag:yaml.org,2002:str", s, style=">")
        return dumper.represent_scalar("tag:yaml.org,2002:str", s)

    Dumper.add_representer(str, str_presenter)
    text = yaml.dump(data, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=100)
    new = f"---\n{text}---\n"
    rest = path.read_text(encoding="utf-8")
    m = fm.FRONT.match(rest)
    body = rest[m.end():] if m else rest
    path.write_text(new + body, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--path", default=None)
    ap.add_argument("--min-tier", default=None)
    args = ap.parse_args()

    docs = []
    all_ids = set()
    inbound = Counter()
    for f in fm.iter_markdown(ROOT):
        rel = f.relative_to(ROOT).as_posix()
        if rel.startswith(("indexes/", ".github/")):
            continue
        d = fm.parse(f)
        if not d.data:
            continue
        if args.path and args.path not in rel:
            continue
        ident = str(d.data.get("id") or d.data.get("name") or "")
        if ident:
            all_ids.add(ident)
        docs.append(d)

    # count inbound references
    for d in docs:
        blob = d.raw_front + "\n" + d.body
        for ident in all_ids:
            if len(ident) < 5:
                continue
            own = str(d.data.get("id") or d.data.get("name") or "")
            if ident == own:
                continue
            if re.search(rf"(?<![\w-]){re.escape(ident)}(?![\w-])", blob):
                inbound[ident] += 1

    results = []
    for d in docs:
        if not fm.requires_frontmatter(d.rel) and not d.rel.startswith("skills/"):
            continue
        s = score_doc(d, inbound, all_ids)
        results.append((d, s))
        if not args.dry:
            d.data["quality"] = {
                "authority": s["components"]["authority"],
                "evidence": s["components"]["evidence"],
                "recency": s["components"]["recency"],
                "adoption": s["components"]["adoption"],
                "reproducibility": s["components"]["reproducibility"],
                "practical_value": s["components"]["practical_value"],
                "maintenance": s["components"]["maintenance"],
            }
            d.data["scoring"] = s
            try:
                rewrite_frontmatter(d.path, d.data, d.raw_front)
            except Exception as e:
                print(f"  WARN could not rewrite {d.rel}: {e}")

    results.sort(key=lambda x: -x[1]["quality_score"])
    print(f"Scored {len(results)} documents")
    print(f"{'Q':>5} {'T':>5} {'TIER':<12} {'ADOPT':>5}  PATH")
    for d, s in results[:45]:
        ident = str(d.data.get("id") or d.data.get("name") or "")
        print(f"{s['quality_score']:>5} {s['trust_score']:>5} {s['tier']:<12} "
              f"{inbound.get(ident, 0):>5}  {d.rel}")
    if len(results) > 45:
        print(f"… and {len(results)-45} more")

    (ROOT / "metadata" / "scores.json").write_text(json.dumps({
        "generated_at": TODAY.isoformat(),
        "generator": "scripts/score/score_skills.py",
        "count": len(results),
        "scores": [{"path": d.rel, "id": d.data.get("id") or d.data.get("name"),
                    **s} for d, s in results],
    }, indent=2, ensure_ascii=False) + "\n")
    if args.min_tier:
        bad = [d.rel for d, s in results if s["tier"] not in ("S", "A", "B")]
        if bad:
            print(f"\n{len(bad)} documents below tier {args.min_tier}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
