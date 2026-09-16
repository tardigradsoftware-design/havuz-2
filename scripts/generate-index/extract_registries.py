#!/usr/bin/env python3
"""Extract machine-readable registries from authored Markdown frontmatter.

Direction of truth:
    repositories : GitHub API -> metadata/repositories.json -> generated cards
    everything else : authored Markdown -> metadata/*.json

Outputs:
    metadata/skills.json        from skills/*/SKILL.md
    metadata/tools.json         from knowledge/mcp/registry/*.md
    metadata/evaluations.json   from evaluations/**/*.md
    metadata/sources.json       from sources/**/*.md + metadata/sources-papers.json
    metadata/agents.json        from agents/*/AGENT.md
    metadata/workflows.json     from workflows/*/WORKFLOW.md
    metadata/graph.json         relationship edges harvested from all of the above

Usage:
    python3 scripts/generate-index/extract_registries.py
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402

NOW = datetime.now(timezone.utc).isoformat(timespec="seconds")


def collect(matcher, root: Path = ROOT) -> List[Dict[str, Any]]:
    out = []
    for f in fm.iter_markdown(root):
        rel = f.relative_to(ROOT).as_posix()
        if not matcher(rel):
            continue
        d = fm.parse(f)
        if not d.data:
            continue
        rec = dict(d.data)
        rec["_path"] = rel
        rec["_tokens"] = fm.estimate_tokens(d.body)
        rec["_headings"] = [h for _, h in fm.headings(d.body)]
        out.append(rec)
    return out


def dump(name: str, listkey: str, records: List[Dict[str, Any]], extra: Dict[str, Any] | None = None,
         schema: str | None = None) -> None:
    blob = {
        "generated_at": NOW,
        "generator": "scripts/generate-index/extract_registries.py",
        "records": len(records),
    }
    if schema:
        blob["$schema"] = f"../schemas/{schema}"
    if extra:
        blob.update(extra)
    blob[listkey] = records
    p = ROOT / "metadata" / name
    p.write_text(json.dumps(blob, indent=2, ensure_ascii=False, default=str) + "\n")
    print(f"  metadata/{name:26} {len(records):>4} records")


def edges_from(rec: Dict[str, Any], src: str, kind: str) -> List[Dict[str, str]]:
    e = []

    def add(t, target, note=None):
        if target:
            e.append({"source": src, "source_kind": kind, "type": t, "target": str(target),
                      **({"note": note} if note else {})})

    for r in rec.get("requires") or []:
        add("requires", r)
    for r in rec.get("conflicts_with") or []:
        add("conflicts_with", r)
    for r in rec.get("related_skills") or []:
        add("related", r)
    for r in rec.get("related_repositories") or []:
        add("uses", r)
    for r in rec.get("related") or []:
        if isinstance(r, dict):
            add(r.get("type", "related"), r.get("target"), r.get("note"))
    for r in rec.get("skills") or []:
        add("uses", r)
    for r in rec.get("mcp") or []:
        add("uses", r)
    for r in rec.get("knowledge") or []:
        add("uses", r)
    for r in rec.get("delegates_to") or []:
        add("requires", r)
    for s in rec.get("sources") or []:
        if isinstance(s, dict) and s.get("url"):
            add("documented_by", s["url"], s.get("title"))
        if isinstance(s, dict) and s.get("repository"):
            add("documented_by", s["repository"], s.get("title"))
    if rec.get("repository"):
        add("implements", rec["repository"])
    for k in ("supersedes",):
        for r in rec.get(k) or []:
            add("supersedes", r)
    return e


def main() -> int:
    skills = collect(lambda r: r.startswith("skills/") and Path(r).name == "SKILL.md")
    agents = collect(lambda r: r.startswith("agents/") and Path(r).name == "AGENT.md")
    workflows = collect(lambda r: r.startswith("workflows/") and Path(r).name == "WORKFLOW.md")
    tools = collect(lambda r: r.startswith("knowledge/mcp/registry/") and r.endswith(".md"))
    evals_ = collect(lambda r: r.startswith("evaluations/") and Path(r).name not in ("README.md", "AGENTS.md"))
    sources_md = collect(lambda r: r.startswith("sources/") and Path(r).name != "README.md")
    knowledge = collect(lambda r: r.startswith(("knowledge/", "patterns/", "anti-patterns/",
                                               "failure-modes/", "gotchas/", "decision-records/")))
    models = collect(lambda r: r.startswith("models/") and Path(r).name != "README.md")
    datasets = collect(lambda r: r.startswith("datasets/") and Path(r).name != "README.md")
    prompts = collect(lambda r: r.startswith("prompts/") and Path(r).name != "README.md")

    dump("skills.json", "skills", skills, schema="skill.schema.json")
    dump("tools.json", "tools", tools, schema="mcp.schema.json")
    dump("evaluations.json", "evaluations", evals_, schema="evaluation.schema.json")
    dump("agents.json", "agents", agents, schema="agent.schema.json")
    dump("workflows.json", "workflows", workflows, schema="workflow.schema.json")
    dump("models.json", "models", models, schema="model.schema.json")
    dump("datasets.json", "datasets", datasets, schema="dataset.schema.json")
    dump("prompts.json", "prompts", prompts, schema="prompt.schema.json")

    # merge authored sources with the verified arXiv records
    papers = []
    pp = ROOT / "metadata" / "sources-papers.json"
    if pp.exists():
        papers = json.loads(pp.read_text()).get("sources", [])
    seen = {s.get("id") for s in papers}
    merged = list(papers)
    for s in sources_md:
        sid = s.get("id") or s.get("_path")
        if sid in seen:
            continue
        seen.add(sid)
        merged.append(s)
    dump("sources.json", "sources", merged, schema="source.schema.json",
         extra={"verification_note": "arXiv records come from metadata/sources-papers.json; "
                                     "unverified candidates stay in metadata/pending-paper-candidates.json"})

    # knowledge graph
    edges: List[Dict[str, str]] = []
    for kind, recs in [("skill", skills), ("agent", agents), ("workflow", workflows), ("mcp", tools),
                       ("evaluation", evals_), ("source", merged), ("knowledge", knowledge),
                       ("model", models), ("dataset", datasets), ("prompt", prompts)]:
        for r in recs:
            ident = r.get("name") or r.get("id") or r.get("_path")
            edges += edges_from(r, str(ident), kind)
    repos = []
    rp = ROOT / "metadata" / "repositories.json"
    if rp.exists():
        repos = json.loads(rp.read_text()).get("repositories", [])
    for r in repos:
        for rel in r.get("related_projects") or []:
            edges.append({"source": r["slug"], "source_kind": "repository", "type": "related", "target": rel})
        if r.get("homepage"):
            edges.append({"source": r["slug"], "source_kind": "repository", "type": "documented_by",
                          "target": r["homepage"]})

    # dedupe edges
    uniq, seen_e = [], set()
    for e in edges:
        k = (e["source"], e["type"], e["target"])
        if k in seen_e:
            continue
        seen_e.add(k)
        uniq.append(e)

    nodes = defaultdict(set)
    for e in uniq:
        nodes[e["source"]].add(e["source_kind"])
        nodes[e["target"]].add("referenced")
    (ROOT / "metadata" / "graph.json").write_text(json.dumps({
        "generated_at": NOW,
        "generator": "scripts/generate-index/extract_registries.py",
        "description": "Knowledge graph. Traverse from a task's domain to the skills, frameworks, "
                       "MCP servers, repositories and papers that support it.",
        "node_count": len(nodes),
        "edge_count": len(uniq),
        "nodes": [{"id": k, "kinds": sorted(v)} for k, v in sorted(nodes.items())],
        "edges": uniq,
    }, indent=2, ensure_ascii=False, default=str) + "\n")
    print(f"  metadata/graph.json             {len(uniq):>4} edges, {len(nodes)} nodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
