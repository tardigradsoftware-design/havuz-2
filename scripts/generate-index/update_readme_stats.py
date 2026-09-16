#!/usr/bin/env python3
"""Refresh the statistics block in README.md between the KB:STATS markers.

Numbers in prose rot. This keeps the front page honest by regenerating it from
the artifacts that were actually produced.

Usage:
    python3 scripts/generate-index/update_readme_stats.py
    python3 scripts/generate-index/update_readme_stats.py --check   # CI: fail if stale
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402

BEGIN = "<!-- KB:STATS:BEGIN -->"
END = "<!-- KB:STATS:END -->"


def load_meta(name: str, key: str) -> List[Dict[str, Any]]:
    p = ROOT / "metadata" / name
    if not p.exists():
        return []
    try:
        return json.loads(p.read_text()).get(key, [])
    except json.JSONDecodeError:
        return []


def count_md(pred) -> int:
    n = 0
    for f in fm.iter_markdown(ROOT):
        rel = f.relative_to(ROOT).as_posix()
        if pred(rel, f):
            n += 1
    return n


def build() -> str:
    repos = load_meta("repositories.json", "repositories")
    tools = load_meta("tools.json", "tools")
    skills = load_meta("skills.json", "skills")
    agents = load_meta("agents.json", "agents")
    workflows = load_meta("workflows.json", "workflows")
    evals_ = load_meta("evaluations.json", "evaluations")
    sources = load_meta("sources.json", "sources")
    models = load_meta("models.json", "models")
    datasets = load_meta("datasets.json", "datasets")
    prompts = load_meta("prompts.json", "prompts")
    index = []
    ip = ROOT / "metadata" / "index.json"
    if ip.exists():
        index = json.loads(ip.read_text()).get("entries", [])

    pend = ROOT / "metadata" / "pending-paper-candidates.json"
    pend_n = json.loads(pend.read_text()).get("count", 0) if pend.exists() else 0

    status = Counter(r["status"] for r in repos)
    tiers = Counter(r["tier"] for r in repos)
    cats = Counter(r["category"] for r in repos)
    renamed = [r for r in repos if r.get("renamed_to")]
    nolic = [r for r in repos if r["license"] == "NONE"]
    archived = [r for r in repos if r["archived"]]
    papers = [s for s in sources if s.get("type") == "research-paper"]

    knowledge_docs = count_md(lambda rel, f: rel.startswith("knowledge/") and f.name != "README.md")
    patterns = count_md(lambda rel, f: rel.startswith("patterns/") and f.name != "README.md")
    anti = count_md(lambda rel, f: rel.startswith(("anti-patterns/", "failure-modes/", "gotchas/"))
                    and f.name != "README.md")
    decisions = count_md(lambda rel, f: rel.startswith("decision-records/") and f.name != "README.md")
    tests = count_md(lambda rel, f: "/tests/" in rel and rel.startswith("skills/") and f.suffix == ".md")
    experimental = count_md(lambda rel, f: rel.startswith("experimental/") and f.name != "README.md")

    stars = sum(r.get("stars") or 0 for r in repos)
    top = sorted(repos, key=lambda r: -(r.get("trust_score") or 0))[:10]

    def li(items, fmt):
        return "\n".join(fmt(i) for i in items)

    lines = [
        f"_Generated {datetime.now(timezone.utc).date().isoformat()} by "
        f"`scripts/generate-index/update_readme_stats.py`. Do not edit by hand._",
        "",
        "### Corpus",
        "",
        "| Layer | Count | Where |",
        "|---|---|---|",
        f"| Skills | **{len(skills)}** | [`skills/`](skills/) |",
        f"| Agent roles | **{len(agents)}** | [`agents/`](agents/) |",
        f"| Workflows | **{len(workflows)}** | [`workflows/`](workflows/) |",
        f"| Knowledge articles | **{knowledge_docs}** | [`knowledge/`](knowledge/) |",
        f"| Patterns | **{patterns}** | [`patterns/`](patterns/) |",
        f"| Failure knowledge (anti-patterns, failure modes, gotchas) | **{anti}** | [`anti-patterns/`](anti-patterns/) · [`failure-modes/`](failure-modes/) · [`gotchas/`](gotchas/) |",
        f"| Decision records | **{decisions}** | [`decision-records/`](decision-records/) |",
        f"| Verified GitHub repositories | **{len(repos)}** | [`indexes/repositories.md`](indexes/repositories.md) |",
        f"| MCP servers | **{len(tools)}** | [`indexes/mcp.md`](indexes/mcp.md) |",
        f"| Research sources (incl. {len(papers)} verified papers) | **{len(sources)}** | [`indexes/research.md`](indexes/research.md) |",
        f"| Evaluations & benchmarks | **{len(evals_)}** | [`indexes/evaluations.md`](indexes/evaluations.md) |",
        f"| Model cards | **{len(models)}** | [`models/`](models/) |",
        f"| Datasets | **{len(datasets)}** | [`datasets/`](datasets/) |",
        f"| Prompt templates | **{len(prompts)}** | [`indexes/prompts.md`](indexes/prompts.md) |",
        f"| Skill test cases | **{tests}** | `skills/*/tests/` |",
        f"| Quarantined / experimental | **{experimental + pend_n}** | [`experimental/`](experimental/) · `metadata/pending-paper-candidates.json` |",
        f"| Retrieval index entries | **{len(index)}** | [`metadata/index.json`](metadata/index.json) |",
        "",
        "### Verification status of the repository database",
        "",
        f"All **{len(repos)}** repositories were verified against the GitHub REST API. "
        f"Aggregate adoption tracked: **{stars:,} stars** across {len(cats)} categories.",
        "",
        "| Maintenance status | Count | | Tier | Count |",
        "|---|---|---|---|---|",
    ]
    s_keys = ["ACTIVE", "STABLE", "MAINTENANCE", "EXPERIMENTAL", "ARCHIVED", "ABANDONED", "UNKNOWN"]
    t_keys = ["S", "A", "B", "C", "EXPERIMENTAL", "ARCHIVED", "UNVERIFIED"]
    for i in range(max(len(s_keys), len(t_keys))):
        a = s_keys[i] if i < len(s_keys) else ""
        b = status.get(a, "") if a else ""
        c = t_keys[i] if i < len(t_keys) else ""
        d = tiers.get(c, "") if c else ""
        lines.append(f"| {a} | {b} | | {c} | {d} |")

    lines += [
        "",
        "### Findings the verification run produced",
        "",
        f"- **{len(renamed)} repositories have moved.** Every one was recorded with its new slug; "
        f"hard-coded URLs to the old paths silently break agents.",
        f"- **{len(archived)} are archived** — read-only, no security patches, successor required.",
        f"- **{len(nolic)} have no detectable license** — flagged "
        f"`license_risk: no-license-do-not-redistribute`; they are referenced, never vendored.",
        f"- **{status.get('MAINTENANCE', 0)} are in maintenance mode** (>120 days without a push) "
        f"and **{status.get('ABANDONED', 0)} are abandoned** (>365 days), excluding published "
        f"research artifacts, which are classified `STABLE` on purpose.",
        f"- **{pend_n} candidate research papers are quarantined** because no primary source could "
        f"confirm them from the build environment. They are excluded from the retrieval index.",
        "",
        "### Top 10 by trust score",
        "",
        "| Repository | Stars | Tier | Status | Trust |",
        "|---|---|---|---|---|",
    ]
    for r in top:
        lines.append(f"| [`{r['slug']}`]({r['url']}) | {r['stars']:,} | {r['tier']} | {r['status']} | {r['trust_score']} |")

    lines += [
        "",
        "### Categories",
        "",
        "| Category | Repositories |",
        "|---|---|",
    ]
    for k, v in cats.most_common():
        lines.append(f"| `{k}` | {v} |")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if the README block is out of date")
    args = ap.parse_args()

    readme = ROOT / "README.md"
    text = readme.read_text()
    block = build()
    if BEGIN not in text or END not in text:
        print(f"ERROR: README.md is missing the {BEGIN} / {END} markers")
        return 1
    new = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), BEGIN + "\n" + block + "\n" + END,
                 text, flags=re.DOTALL)
    if args.check:
        if new != text:
            print("README statistics block is stale. Run: python3 scripts/generate-index/update_readme_stats.py")
            return 1
        print("README statistics block is current.")
        return 0
    if new != text:
        readme.write_text(new)
        print("README.md statistics block updated.")
    else:
        print("README.md statistics block already current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
