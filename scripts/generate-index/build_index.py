#!/usr/bin/env python3
"""Build the retrieval index and every human-readable index.

Outputs
    metadata/index.json     flat, normalised, embedding-ready (schemas/index.schema.json)
    indexes/skills.md       indexes/tools.md      indexes/mcp.md
    indexes/repositories.md indexes/frameworks.md indexes/research.md
    indexes/prompts.md      indexes/evaluations.md indexes/agents.md
    indexes/workflows.md    indexes/topics.md     indexes/best-of.md
    indexes/stale.md

Design: an agent should be able to answer "what do I need?" from an index alone,
without opening a single content file (progressive disclosure, brief §72).

Usage:
    python3 scripts/generate-index/build_index.py
    python3 scripts/generate-index/build_index.py --no-markdown   # only index.json
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402
from lib.sanitize import untrusted, untrusted_list  # noqa: E402

# Entry kinds whose title, summary and tags originate outside this repository — a repository
# `description`, its `topics`, or an MCP `purpose` built from that description. Everything else
# in the index is authored here, and escaping authored text would change content that is
# already correct: 11 workflow summaries differ under `untrusted()` and none of them is a
# security problem. `metadata/repositories.json` keeps the raw upstream string; the index is a
# retrieval artifact rendered into indexes/*.md, so it carries the safe form.
UPSTREAM_KINDS = frozenset({"repository", "mcp"})

NOW = datetime.now(timezone.utc).isoformat(timespec="seconds")
TODAY = date.today()
GEN = "scripts/generate-index/build_index.py"
HEADER = ("<!-- GENERATED FILE — DO NOT EDIT BY HAND.\n"
          f"     Regenerate: python3 {GEN}\n"
          f"     Generated: {NOW} -->\n")


def load(name: str) -> List[Dict[str, Any]]:
    p = ROOT / "metadata" / name
    if not p.exists():
        return []
    try:
        blob = json.loads(p.read_text())
    except json.JSONDecodeError:
        return []
    for k in ("skills", "tools", "evaluations", "sources", "repositories", "agents",
              "workflows", "models", "datasets", "prompts"):
        if k in blob:
            return blob[k]
    return []


def entry(**kw) -> Dict[str, Any]:
    base = {"id": None, "title": None, "path": None, "kind": None, "summary": "", "tags": []}
    base.update({k: v for k, v in kw.items() if v is not None})
    return base


def build_entries() -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []

    for s in load("skills.json"):
        out.append(entry(
            id=s.get("name"), title=s.get("description"), path=s.get("_path"), kind="skill",
            domain=s.get("category"), category=s.get("category"),
            summary=(s.get("description") or "")[:600], tags=s.get("tags") or [],
            status=s.get("status"), tier=(s.get("scoring") or {}).get("tier"),
            confidence=s.get("confidence"), claim_type=s.get("claim_type"),
            quality_score=(s.get("scoring") or {}).get("quality_score"),
            trust_score=(s.get("scoring") or {}).get("trust_score"),
            version=s.get("version"), updated_at=s.get("updated"), verified_at=s.get("verified_at"),
            expires_at=s.get("expires_at"), estimated_tokens=s.get("_tokens"),
            relations=[{"type": "requires", "target": r} for r in (s.get("requires") or [])] +
                      [{"type": "conflicts_with", "target": r} for r in (s.get("conflicts_with") or [])]))

    for a in load("agents.json"):
        out.append(entry(id=a.get("name"), title=a.get("role"), path=a.get("_path"), kind="agent",
                         domain=a.get("category"), category=a.get("category"),
                         summary=(a.get("mandate") or "")[:600], tags=a.get("tags") or [],
                         status=a.get("status"), confidence=a.get("confidence"),
                         version=a.get("version"), updated_at=a.get("updated"),
                         estimated_tokens=a.get("_tokens")))

    for w in load("workflows.json"):
        stages = [st.get("name") for st in (w.get("stages") or []) if isinstance(st, dict)]
        out.append(entry(id=w.get("name"), title=w.get("description"), path=w.get("_path"), kind="workflow",
                         summary=(w.get("trigger") or "")[:400] + (" | stages: " + " → ".join(stages) if stages else ""),
                         tags=w.get("tags") or [], status=w.get("status"),
                         confidence=w.get("confidence"), version=w.get("version"),
                         updated_at=w.get("updated"), estimated_tokens=w.get("_tokens")))

    for t in load("tools.json"):
        sec = t.get("security") or {}
        out.append(entry(id=t.get("id"), title=t.get("name"), path=t.get("_path"), kind="mcp",
                         category=t.get("category"), summary=untrusted(t.get("purpose"))[:600],
                         tags=untrusted_list(t.get("tags")), status=t.get("status"), tier=t.get("tier"),
                         confidence=t.get("confidence"), updated_at=t.get("verified_at"),
                         verified_at=t.get("verified_at"), expires_at=t.get("expires_at"),
                         license=t.get("license"),
                         relations=([{"type": "uses", "target": t["repository"],
                                      "note": f"risk={sec.get('risk_level')}"}] if t.get("repository") else [])))

    for r in load("repositories.json"):
        if not r.get("fetch_ok", True):
            continue
        out.append(entry(id=r.get("slug"), title=untrusted(r.get("name")),
                         path=f"repositories/{r.get('category')}/{r['slug'].replace('/', '--').lower()}.md",
                         kind="repository", domain=r.get("category"), category=r.get("category"),
                         summary=untrusted(r.get("description"))[:500],
                         # curated_tags are chosen here; topics are set by the repository owner
                         tags=sorted(set((r.get("curated_tags") or [])
                                         + untrusted_list((r.get("topics") or [])[:6]))),
                         status=r.get("status"), tier=r.get("tier"), confidence=r.get("confidence"),
                         quality_score=r.get("quality_score"), trust_score=r.get("trust_score"),
                         stars=r.get("stars"), license=r.get("license"),
                         source=r.get("url"), updated_at=str(r.get("pushed_at") or "")[:10] or None,
                         verified_at=r.get("verified_at"), expires_at=r.get("expires_at")))

    for s in load("sources.json"):
        out.append(entry(id=s.get("id"), title=s.get("title"), path=s.get("_path") or "metadata/sources.json",
                         kind="source", domain=s.get("category"), category=s.get("category"),
                         summary=(s.get("summary") or "")[:600], tags=s.get("tags") or [],
                         confidence=s.get("confidence"), claim_type=s.get("claim_type"),
                         source=s.get("url"), updated_at=s.get("updated"),
                         verified_at=s.get("verified_at"), expires_at=s.get("expires_at")))

    for e in load("evaluations.json"):
        out.append(entry(id=e.get("id"), title=e.get("name"), path=e.get("_path"), kind="evaluation",
                         domain=e.get("domain"), category=e.get("domain"),
                         summary=(e.get("purpose") or e.get("task") or "")[:600], tags=e.get("tags") or [],
                         status=e.get("status"), confidence=e.get("confidence"),
                         source=e.get("url"), updated_at=e.get("updated"),
                         verified_at=e.get("verified_at")))

    for m in load("models.json"):
        out.append(entry(id=m.get("id"), title=f"{m.get('provider')} {m.get('model')}", path=m.get("_path"),
                         kind="model", category=m.get("provider"),
                         summary=" · ".join(x for x in [
                             f"context {m.get('context_window')}" if m.get("context_window") else None,
                             "open-weights" if m.get("open_weights") else "closed-weights",
                             m.get("license") or "",
                         ] if x)[:600],
                         tags=m.get("tags") or [], confidence=m.get("confidence"),
                         verified_at=m.get("verified_at"), expires_at=m.get("expires_at")))

    for d in load("datasets.json"):
        out.append(entry(id=d.get("id"), title=d.get("name"), path=d.get("_path"), kind="dataset",
                         domain=d.get("category"), category=d.get("category"),
                         summary=(d.get("purpose") or "")[:600], tags=d.get("tags") or [],
                         status=d.get("status"), confidence=d.get("confidence"),
                         license=d.get("license"), source=d.get("url"),
                         verified_at=d.get("verified_at"), expires_at=d.get("expires_at")))

    for p in load("prompts.json"):
        out.append(entry(id=p.get("id"), title=p.get("task"), path=p.get("_path"), kind="prompt",
                         category=p.get("category"), summary=(p.get("use_case") or "")[:600],
                         tags=p.get("tags") or [], status=p.get("status"),
                         confidence=p.get("confidence"), updated_at=p.get("updated"),
                         estimated_tokens=p.get("_tokens")))

    # authored knowledge / patterns / failure knowledge
    kindmap = [("knowledge/", "knowledge"), ("patterns/", "pattern"),
               ("anti-patterns/", "anti-pattern"), ("failure-modes/", "failure-mode"),
               ("gotchas/", "gotcha"), ("decision-records/", "decision-record"),
               ("research-archive/", "knowledge"), ("experimental/", "knowledge")]
    for f in fm.iter_markdown(ROOT):
        rel = f.relative_to(ROOT).as_posix()
        kind = next((k for pre, k in kindmap if rel.startswith(pre)), None)
        if not kind:
            continue
        if Path(rel).name in ("README.md", "AGENTS.md"):
            continue
        d = fm.parse(f)
        if not d.data:
            continue
        out.append(entry(id=d.data.get("id") or rel, title=d.data.get("title") or rel, path=rel,
                         kind=kind, domain=d.data.get("domain"), category=d.data.get("domain"),
                         summary=(d.data.get("summary") or "")[:600], tags=d.data.get("tags") or [],
                         status=d.data.get("status"), confidence=d.data.get("confidence"),
                         claim_type=d.data.get("claim_type"),
                         quality_score=(d.data.get("scoring") or {}).get("quality_score"),
                         trust_score=(d.data.get("scoring") or {}).get("trust_score"),
                         version=d.data.get("version"), updated_at=str(d.data.get("updated") or "")[:10] or None,
                         verified_at=str(d.data.get("verified_at") or "")[:10] or None,
                         expires_at=str(d.data.get("expires_at") or "")[:10] or None,
                         estimated_tokens=d.data.get("estimated_tokens") or fm.estimate_tokens(d.body)))

    # drop quarantined / non-authoritative material from the retrieval index
    out = [e for e in out if e.get("path") and "experimental/" not in str(e["path"])]
    return out


def md_table(rows: List[List[str]], headers: List[str]) -> str:
    lines = ["| " + " | ".join(headers) + " |",
             "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        lines.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(lines)


def link(text: str, path: Optional[str]) -> str:
    if not path:
        return str(text)
    return f"[{text}](../{path})"


def stars_fmt(n) -> str:
    if n is None:
        return "—"
    if n >= 1000:
        return f"{n/1000:.1f}k"
    return str(n)


def write(rel: str, title: str, intro: str, body: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(HEADER + f"\n# {title}\n\n{intro}\n\n{body}\n")
    print(f"  {rel}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-markdown", action="store_true")
    args = ap.parse_args()

    entries = build_entries()
    (ROOT / "metadata" / "index.json").write_text(json.dumps({
        "$schema": "../schemas/index.schema.json",
        "generated_at": NOW, "generator": GEN, "schema_version": "1.0.0",
        "entry_count": len(entries),
        "normalisation": "id, title, summary, path, kind, domain, tags, status, confidence, "
                         "claim_type, quality_score, trust_score, version, updated_at, verified_at, "
                         "expires_at, estimated_tokens — stable field names for embedding ingestion.",
        "excluded": ["experimental/", "metadata/pending-paper-candidates.json",
                     "metadata/unresolved-seeds.json", ".cache/"],
        "entries": entries,
    }, indent=2, ensure_ascii=False, default=str) + "\n")
    print(f"  metadata/index.json             {len(entries)} entries")
    if args.no_markdown:
        return 0

    by_kind = defaultdict(list)
    for e in entries:
        by_kind[e["kind"]].append(e)

    # ---------------- skills ----------------
    rows = []
    for s in sorted(by_kind["skill"], key=lambda x: (x.get("domain") or "", str(x.get("id")))):
        rows.append([link(s["id"], s["path"]), s.get("domain") or "—", s.get("status") or "—",
                     s.get("confidence") or "—", s.get("tier") or "—",
                     s.get("quality_score") if s.get("quality_score") is not None else "—",
                     ", ".join((s.get("tags") or [])[:4])])
    write("indexes/skills.md", "Skill index",
          f"{len(rows)} skills. Load `SKILL.md` frontmatter first; open `references/` only when needed.",
          md_table(rows, ["Skill", "Category", "Status", "Confidence", "Tier", "Q", "Tags"]))

    # ---------------- repositories ----------------
    repos = by_kind["repository"]
    body = [f"{len(repos)} repositories, all verified against the GitHub API on their `verified_at` date.\n"]
    for cat in sorted({r.get("category") for r in repos}):
        sub = sorted([r for r in repos if r.get("category") == cat], key=lambda x: -(x.get("trust_score") or 0))
        body.append(f"\n## {cat} ({len(sub)})\n")
        rows = [[link(r["id"], r["path"]), stars_fmt(r.get("stars")), r.get("tier") or "—",
                 r.get("status") or "—", r.get("license") or "—",
                 r.get("trust_score") if r.get("trust_score") is not None else "—",
                 r.get("verified_at") or "—"] for r in sub[:60]]
        body.append(md_table(rows, ["Repository", "Stars", "Tier", "Status", "License", "Trust", "Verified"]))
        if len(sub) > 60:
            body.append(f"\n_…and {len(sub)-60} more in `metadata/repositories.json`._")
    write("indexes/repositories.md", "Repository index",
          "Sort by `trust_score` when choosing a tool; check `status` before adopting.",
          "\n".join(body))

    # ---------------- frameworks ----------------
    fw = [r for r in repos if r.get("category") in ("agent-frameworks", "ai")]
    rows = [[link(r["id"], r["path"]), stars_fmt(r.get("stars")), r.get("tier") or "—",
             r.get("status") or "—", r.get("quality_score") or "—", r.get("license") or "—"]
            for r in sorted(fw, key=lambda x: -(x.get("quality_score") or 0))]
    write("indexes/frameworks.md", "Framework & model-tooling index",
          f"{len(rows)} agent frameworks, SDKs and model tooling projects. See "
          "`knowledge/agent-engineering/framework-comparison.md` for the capability matrix.",
          md_table(rows, ["Project", "Stars", "Tier", "Status", "Quality", "License"]))

    # ---------------- mcp / tools ----------------
    # The registry was seeded from the seed-list category `mcp-servers`, which is not a
    # verified property of a repository, so not every entry is a server. Splitting on
    # `registry_kind` is what stops the index from telling an agent to install an SDK, a
    # testing tool or a curated catalog when it asked for a server. Non-servers stay
    # listed — an SDK and an inspector are genuinely useful to record, they are just not
    # servers, and hiding them would send the next reader to rediscover them.
    mcp = by_kind["mcp"]
    tools_meta = {t.get("id"): t for t in load("tools.json")}

    def mcp_row(t) -> List[str]:
        meta = tools_meta.get(t["id"], {})
        perm = meta.get("permissions") or {}
        sec = meta.get("security") or {}
        return [link(t["id"], t["path"]), t.get("category") or "—",
                "official" if meta.get("official") else "community",
                sec.get("risk_level") or "—",
                perm.get("filesystem") or "—", perm.get("network") or "—",
                perm.get("code_execution") or "—", t.get("status") or "—"]

    ordered = sorted(mcp, key=lambda x: (x.get("category") or "", str(x.get("id"))))
    servers = [t for t in ordered if tools_meta.get(t["id"], {}).get("registry_kind") == "server"]
    KIND_HEADINGS = [
        ("sdk", "SDKs — for building a server, not for connecting to one"),
        ("tooling", "Testing and debugging tools"),
        ("registry", "Registry services — a peer of this registry, not an entry in it"),
        ("catalog", "Catalogs — curated lists of other servers"),
        ("unproven", "Not established as servers — nothing observed says what they are"),
    ]
    blocks = [md_table([mcp_row(t) for t in servers],
                       ["Server", "Category", "Provenance", "Risk", "FS", "Network", "Exec", "Status"])]
    for kind, heading in KIND_HEADINGS:
        group = [t for t in ordered if tools_meta.get(t["id"], {}).get("registry_kind") == kind]
        if not group:
            continue
        blocks.append(f"\n## {heading}\n")
        blocks.append(md_table(
            [[mcp_row(t)[0], mcp_row(t)[1], mcp_row(t)[2],
              (tools_meta.get(t["id"], {}).get("registry_kind_evidence") or "—")]
             for t in group],
            ["Repository", "Category", "Provenance", "Why it is not counted as a server"]))

    others = len(ordered) - len(servers)
    write("indexes/mcp.md", "MCP server index",
          f"**{len(servers)} MCP servers**, with their permission surface and risk level. "
          f"The registry holds {len(ordered)} entries in total: the other {others} are SDKs, "
          "testing tools, a registry service, catalogs and one repository whose own published "
          "text does not establish that it is a server. They are listed separately below "
          "rather than excluded, and rather than counted as servers. "
          "Read `knowledge/security/mcp-security/mcp-threat-model.md` before enabling any of them.",
          "\n".join(blocks))
    write("indexes/tools.md", "Tool index (MCP + CLI + services)",
          "MCP servers live in `indexes/mcp.md`; CLI and developer tooling is indexed below by category.",
          md_table([[link(r["id"], r["path"]), stars_fmt(r.get("stars")), r.get("tier") or "—",
                     r.get("status") or "—", ", ".join((r.get("tags") or [])[:4])]
                    for r in sorted([x for x in repos if x.get("category") == "developer-tools"],
                                    key=lambda x: -(x.get("trust_score") or 0))],
                   ["Tool", "Stars", "Tier", "Status", "Tags"]))

    # ---------------- research ----------------
    src = by_kind["source"]
    rows = [[link((s.get("title") or s["id"])[:78], s["path"]), s.get("category") or "—",
             s.get("confidence") or "—", s.get("verified_at") or "—", (s.get("source") or "")[:60]]
            for s in sorted(src, key=lambda x: (x.get("category") or "", str(x.get("title"))))]
    pend = ROOT / "metadata" / "pending-paper-candidates.json"
    pend_n = json.loads(pend.read_text()).get("count", 0) if pend.exists() else 0
    write("indexes/research.md", "Research source index",
          f"{len(rows)} verified sources. **{pend_n} additional candidate papers are quarantined** in "
          "`metadata/pending-paper-candidates.json` and must not be cited until "
          "`scripts/crawl/verify_arxiv_papers.py` confirms them against arXiv.",
          md_table(rows, ["Source", "Category", "Confidence", "Verified", "URL"]))

    # ---------------- evaluations ----------------
    ev = by_kind["evaluation"]
    rows = [[link(e.get("id"), e["path"]), e.get("domain") or "—", e.get("status") or "—",
             e.get("confidence") or "—", ", ".join((e.get("tags") or [])[:4])]
            for e in sorted(ev, key=lambda x: (x.get("domain") or "", str(x.get("id"))))]
    write("indexes/evaluations.md", "Evaluation index",
          f"{len(ev)} evaluation records: external benchmarks plus the internal WITHOUT_KB / WITH_KB task suite.",
          md_table(rows, ["Evaluation", "Domain", "Status", "Confidence", "Tags"]))

    # ---------------- agents / workflows / prompts ----------------
    ag = by_kind["agent"]
    write("indexes/agents.md", "Agent role index",
          f"{len(ag)} agent roles with bounded mandates and explicit output contracts.",
          md_table([[link(a.get("id"), a["path"]), a.get("domain") or "—", (a.get("title") or "")[:60],
                     a.get("status") or "—"] for a in sorted(ag, key=lambda x: str(x.get("id")))],
                   ["Agent", "Category", "Role", "Status"]))
    wf = by_kind["workflow"]
    write("indexes/workflows.md", "Workflow index",
          f"{len(wf)} gated workflows.",
          md_table([[link(w.get("id"), w["path"]), (w.get("summary") or "")[:110], w.get("status") or "—"]
                    for w in sorted(wf, key=lambda x: str(x.get("id")))],
                   ["Workflow", "Trigger", "Status"]))
    pr = by_kind["prompt"]
    write("indexes/prompts.md", "Prompt template index",
          f"{len(pr)} evaluated prompt templates.",
          md_table([[link(p.get("id"), p["path"]), p.get("category") or "—", (p.get("title") or "")[:60],
                     p.get("status") or "—", p.get("confidence") or "—"]
                    for p in sorted(pr, key=lambda x: (x.get("category") or "", str(x.get("id"))))],
                   ["Prompt", "Category", "Task", "Status", "Confidence"]))

    # ---------------- topics ----------------
    tag_map = defaultdict(list)
    for e in entries:
        for t in (e.get("tags") or []):
            tag_map[t].append(e)
    dom_map = defaultdict(list)
    for e in entries:
        if e.get("domain"):
            dom_map[e["domain"]].append(e)
    body = ["Start here. Pick a domain, then a tag, then open the specific entry.\n",
            "## By domain\n"]
    for d in sorted(dom_map, key=lambda x: -len(dom_map[x])):
        items = dom_map[d]
        kinds = defaultdict(int)
        for i in items:
            kinds[i["kind"]] += 1
        body.append(f"- **{d}** ({len(items)}) — " + ", ".join(f"{k}:{v}" for k, v in sorted(kinds.items())))
    body.append("\n## By tag (top 80)\n")
    rows = [[f"`{t}`", len(v), ", ".join(sorted({i['kind'] for i in v}))[:60],
             ", ".join(str(i.get("id"))[:28] for i in sorted(v, key=lambda z: -(z.get("trust_score") or z.get("quality_score") or 0))[:3])]
            for t, v in sorted(tag_map.items(), key=lambda kv: -len(kv[1]))[:80]]
    body.append(md_table(rows, ["Tag", "Entries", "Kinds", "Top entries"]))
    write("indexes/topics.md", "Topic index",
          f"{len(dom_map)} domains, {len(tag_map)} tags, {len(entries)} entries.",
          "\n".join(body))

    # ---------------- best-of ----------------
    def best(cat: str, n: int = 12, key="trust_score"):
        sub = [r for r in repos if r.get("category") == cat and r.get("status") not in ("ARCHIVED", "ABANDONED")]
        return sorted(sub, key=lambda x: -(x.get(key) or 0))[:n]

    body = []
    sections = [
        ("BEST AGENT FRAMEWORKS", best("agent-frameworks")),
        ("BEST AGENT SKILL SOURCES", best("agent-skills")),
        ("BEST MCP SERVERS", best("mcp-servers")),
        ("BEST CODING AGENTS", [r for r in best("agent-skills", 25) if any(t in (r.get("tags") or []) for t in ("coding-agent",))]),
        ("BEST BROWSER / COMPUTER-USE AGENTS", best("browser-automation")),
        ("BEST EVALUATION FRAMEWORKS", best("evaluation")),
        ("BEST REASONING RESEARCH (public)", best("reasoning-research")),
        ("BEST FRONTEND REFERENCES", best("frontend")),
        ("BEST BACKEND REFERENCES", best("backend")),
        ("BEST DATABASE REFERENCES", best("databases")),
        ("BEST AI DEV TOOLS", best("developer-tools")),
        ("BEST INSTRUCTION / STANDARDS SOURCES", best("instructions-standards")),
    ]
    for title, items in sections:
        if not items:
            continue
        body.append(f"\n## {title}\n")
        rows = []
        for r in items:
            rows.append([link(r["id"], r["path"]), stars_fmt(r.get("stars")), r.get("tier") or "—",
                         r.get("status") or "—", r.get("verified_at") or "—"])
        body.append(md_table(rows, ["Project", "Stars", "Tier", "Status", "Last verified"]))
        body.append("\n_Tradeoffs and alternatives are recorded per project in "
                    "`repositories/<category>/` and in the relevant `decision-records/` file._")
    write("indexes/best-of.md", "Best-of collections",
          "Ranked by **trust score**, filtered to exclude ARCHIVED and ABANDONED projects. "
          "This is a shortlist to investigate, not a verdict — every entry still needs a "
          "fit check against your constraints.",
          "\n".join(body))

    # ---------------- stale ----------------
    stale = []
    for e in entries:
        exp = e.get("expires_at")
        if not exp:
            continue
        try:
            d = datetime.strptime(str(exp)[:10], "%Y-%m-%d").date()
        except ValueError:
            continue
        if d < TODAY:
            stale.append((d, e))
    stale.sort(key=lambda x: x[0])
    rows = [[d.isoformat(), (TODAY - d).days, e["kind"], link(str(e.get("id"))[:44], e["path"])]
            for d, e in stale[:400]]
    write("indexes/stale.md", "Staleness report",
          f"{len(stale)} entries are past `expires_at`. Expired does not mean wrong — it means "
          "**re-verify before acting**. Run `make refresh-github` and `make refresh-papers`.",
          md_table(rows, ["Expired", "Days overdue", "Kind", "Entry"]) if rows else "_Nothing is expired._")

    print(f"\n{len(entries)} index entries written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
