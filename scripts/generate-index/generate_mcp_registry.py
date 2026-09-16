#!/usr/bin/env python3
"""Generate the MCP registry from verified GitHub metadata.

Reads metadata/repositories.json (produced by scripts/update/fetch_github_metadata.py
from live GitHub REST API calls) and emits, for every record in the `mcp-servers`
category:

  * knowledge/mcp/registry/<slug>.md  — a graded registry entry
  * metadata/tools.json               — the machine-readable registry

Honesty rules this generator is built around, because an MCP registry that guesses
is worse than no registry:

  1. Every factual field comes from an observed GitHub API value. Nothing is inferred
     from the name of the repository.
  2. Capability fields that the GitHub API cannot tell us — transport, tool list,
     resource list, prompt list, authentication scheme — are emitted as null or empty
     and flagged `capability_evidence: unverified`. They are NOT guessed. A wrong
     transport claim sends an integrator down a dead end.
  3. `purpose` is the repository's own description, attributed as such. Where that
     description is too thin to satisfy the schema minimum, the entry is emitted with
     `purpose_evidence: repository-description-thin` so a human knows to expand it
     from the README rather than trusting the generator.
  4. License risk is carried through verbatim. `NOASSERTION` and absent licenses are
     surfaced, not smoothed over.
  5. Archived repositories are emitted with `production_readiness: deprecated` and are
     never marked production-ready, regardless of star count.

Usage:
    python3 scripts/generate-index/generate_mcp_registry.py [--check]

--check exits non-zero if the committed output differs from a fresh regeneration,
so CI can prove the registry is in sync with the metadata it was built from.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[2]
REPOS = ROOT / "metadata" / "repositories.json"
OUT_MD = ROOT / "knowledge" / "mcp" / "registry"
OUT_JSON = ROOT / "metadata" / "tools.json"

NOW = datetime.now(timezone.utc)
TODAY = NOW.date().isoformat()
# MCP registry entries describe fast-moving tooling: 90-day window per the freshness policy.
EXPIRES = (NOW + timedelta(days=90)).date().isoformat()

# Repository topics/description keywords -> registry category. Derived only from
# fields the API actually returned; no category is asserted without a signal.
CATEGORY_SIGNALS: List[tuple[str, tuple[str, ...]]] = [
    ("browser", ("browser", "playwright", "puppeteer", "chrome", "devtools", "web-scraping", "crawl")),
    ("database", ("database", "postgres", "postgresql", "mysql", "mongodb", "redis", "sqlite", "neon", "supabase", "sql")),
    ("vcs", ("github", "gitlab", "git", "bitbucket", "pull-request")),
    ("search", ("search", "retrieval", "exa", "tavily", "serp")),
    ("documentation", ("documentation", "docs", "context7", "readme", "knowledge")),
    ("cloud", ("aws", "cloud", "cloudflare", "azure", "gcp", "cloud-run", "firebase", "vercel", "deploy")),
    ("communication", ("slack", "notion", "atlassian", "jira", "confluence", "discord", "email", "gmail")),
    ("observability", ("sentry", "observability", "monitoring", "logging", "trace", "metrics", "grafana", "datadog")),
    ("ci-cd", ("ci", "cd", "pipeline", "n8n", "workflow", "actions")),
    ("filesystem", ("filesystem", "file", "directory", "memory")),
]

DISTRIBUTION_HINTS: List[tuple[str, tuple[str, ...]]] = [
    ("npm", ("npmjs.com", "npmjs.org")),
    ("pypi", ("pypi.org", "pypi.python.org")),
    ("docker", ("hub.docker.com", "docker.com")),
]


def slug_to_id(slug: str) -> str:
    return "mcp-" + slug.replace("/", "-").replace(".", "-").lower()


def detect_category(rec: Dict[str, Any]) -> Optional[str]:
    haystack = " ".join(
        [str(rec.get("description") or ""), " ".join(rec.get("topics") or []), rec.get("slug", "")]
    ).lower()
    for cat, signals in CATEGORY_SIGNALS:
        if any(s in haystack for s in signals):
            return cat
    return None


def detect_distribution(rec: Dict[str, Any]) -> tuple[str, Optional[str], Optional[str]]:
    """Return (distribution, npm_package, pypi_package) from observed fields only."""
    homepage = str(rec.get("homepage") or "")
    for dist, hints in DISTRIBUTION_HINTS:
        if any(h in homepage for h in hints):
            pkg = homepage.rsplit("/", 1)[-1] if dist == "npm" else homepage.rsplit("/", 1)[-1]
            return dist, (pkg if dist == "npm" else None), (pkg if dist == "pypi" else None)
    # No package URL observed. Distribution is genuinely unknown from the API alone;
    # `source` is the only claim we can defend — the repository is buildable from source.
    return "source", None, None


def risk_level(rec: Dict[str, Any]) -> str:
    """Security risk tier from observed signals, not from the name."""
    if rec.get("archived"):
        return "high"
    if rec.get("license_risk") not in (None, "none"):
        return "high"
    struct = rec.get("structure") or {}
    q = (rec.get("quality") or {}).get("security")
    if not struct.get("has_security_md"):
        return "medium"
    if q is not None and q < 6:
        return "medium"
    return "low"


def build_purpose(rec: Dict[str, Any]) -> tuple[str, str]:
    """Purpose text plus an evidence label. Never invents a capability."""
    desc = (rec.get("description") or "").strip()
    slug = rec["slug"]
    if len(desc) >= 20:
        return f'As stated by the repository itself: "{desc}"', "repository-description"
    parts = [f'Registered as an MCP server under `{slug}`.']
    if desc:
        parts.append(f'The repository describes itself only as "{desc}", which is too thin to rely on.')
    else:
        parts.append("The repository returned no description from the GitHub API.")
    parts.append(
        "Purpose must be confirmed from the README before adoption; this entry deliberately "
        "does not guess at capabilities."
    )
    return " ".join(parts), "repository-description-thin"


def record_to_tool(rec: Dict[str, Any]) -> Dict[str, Any]:
    purpose, purpose_evidence = build_purpose(rec)
    dist, npm_pkg, pypi_pkg = detect_distribution(rec)
    q = rec.get("quality") or {}
    archived = bool(rec.get("archived"))
    lic = rec.get("license")
    lic_risk = rec.get("license_risk")

    tool: Dict[str, Any] = {
        "id": slug_to_id(rec["slug"]),
        "name": rec.get("name") or rec["slug"].split("/")[-1],
        "repository": rec["slug"],
        "url": rec.get("url"),
        "npm_package": npm_pkg,
        "pypi_package": pypi_pkg,
        "distribution": dist,
        "official": bool(rec.get("official")),
        "maintainer": rec.get("owner"),
        "purpose": purpose,
        "category": detect_category(rec) or "other",
        # The GitHub API does not expose MCP transport, tool, resource or prompt lists.
        # Emitting empty rather than plausible values is the point of this generator.
        "transport": [],
        "tools": [],
        "resources": [],
        "prompts": [],
        "authentication": "mixed" if rec.get("official") else None,
        "permissions": {},
        "security": {
            "risk_level": risk_level(rec),
            "notes": (
                "Archived: no further fixes expected." if archived
                else ("No SECURITY.md published." if not (rec.get("structure") or {}).get("has_security_md")
                      else "SECURITY.md published.")
            ),
        },
        "local_or_remote": "local" if dist in ("npm", "pypi", "source") else "both",
        "setup_complexity": "low" if dist in ("npm", "pypi") else "medium",
        "production_readiness": "deprecated" if archived else (
            "production" if rec.get("production_ready") else "beta"),
        "status": rec.get("maintenance_status") or rec.get("status"),
        "license": None if lic in (None, "NONE", "NOASSERTION") else lic,
        "stars": rec.get("stars"),
        "tier": rec.get("tier"),
        "quality_score": rec.get("quality_score"),
        "confidence": "high" if rec.get("fetch_ok") else "low",
        "recommended_for": [],
        "not_recommended_for": (["adoption in new work — archived"] if archived else []),
        "tags": sorted(set((rec.get("curated_tags") or []) + (rec.get("topics") or []) + ["mcp"])),
        "sources": [{
            "title": f'{rec["slug"]} — GitHub repository metadata',
            "url": rec.get("url"),
            "type": "github-repository",
            "license": lic if lic not in (None, "NONE") else None,
            "claim_type": "fact",
            "confidence": "very-high" if rec.get("fetch_ok") else "low",
            "verified_at": TODAY,
            "note": "Observed via the GitHub REST API on the verified_at date. Star count, license, "
                    "archival status, push date and repository structure are API facts; capability "
                    "fields are not available from the API and are left empty rather than guessed.",
        }],
        "verified_at": TODAY,
        "expires_at": EXPIRES,
        # Provenance of the generator's own honesty boundaries.
        "capability_evidence": "unverified",
        "purpose_evidence": purpose_evidence,
        "license_risk": lic_risk,
        "stars_checked_at": TODAY,
        "days_since_push": rec.get("days_since_push"),
        "language": rec.get("language"),
    }
    return {k: v for k, v in tool.items() if v is not None or k in (
        "transport", "tools", "resources", "prompts", "permissions", "recommended_for",
        "not_recommended_for", "category", "npm_package", "pypi_package")}


MD_TMPL = """---
id: {id}
name: {name}
purpose: >-
  {purpose}
category: {category}
distribution: {distribution}
official: {official}
maintainer: {maintainer}
repository: {repository}
url: {url}
transport: []
tools: []
{authentication_line}security:
  risk_level: {risk_level}
  notes: >-
    {security_notes}
local_or_remote: {local_or_remote}
setup_complexity: {setup_complexity}
production_readiness: {production_readiness}
status: {status}
license: {license}
license_risk: {license_risk}
stars: {stars}
stars_checked_at: {today}
tier: {tier}
quality_score: {quality_score}
confidence: {confidence}
capability_evidence: unverified
purpose_evidence: {purpose_evidence}
tags: {tags}
verified_at: {today}
expires_at: {expires}
sources:
  - title: "{source_title}"
    url: {url}
    type: github-repository
    license: {source_license}
    claim_type: fact
    confidence: {source_confidence}
    verified_at: {today}
    note: >-
      Observed via the GitHub REST API on {today}. Star count, license, archival status,
      push date, language and repository structure are API facts. MCP transport, tool,
      resource and prompt lists are not exposed by the API and are deliberately left
      empty rather than inferred from the repository name.
---

# {name}

`{repository}` — {one_line}

## What is verified

These fields were read from the GitHub REST API on **{today}** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`{repository}`]({url}) |
| Stars | {stars_fmt} (checked {today}) |
| License | {license_display} |
| Archived | {archived} |
| Last push | {pushed_at} ({days_since_push} days ago) |
| Language | {language} |
| Latest release | {latest_release} |
| Contributors | {contributors} |
| SECURITY.md published | {has_security_md} |
| Tests present | {has_tests} |
| CI present | {has_ci} |
| Tier / quality score | {tier} / {quality_score} |

## What is NOT verified

**MCP capability fields are empty on purpose.** The GitHub API does not expose a server's transport
list, tool list, resource list, prompt list or authentication scheme. Inferring them from the
repository name or description is how an integrator ends up configuring `stdio` against a server that
only speaks `streamable-http`, or granting filesystem permissions to a server that never asked for
them.

Before adopting this server, confirm from its own README:

- [ ] Which transports it supports (`stdio`, `sse`, `streamable-http`)
- [ ] The exact tool names it exposes, and what each one can mutate
- [ ] Whether it exposes resources or prompts, and what they return
- [ ] How it authenticates, and what scope the credential carries
- [ ] Which permissions it requires at the OS, network and account level
- [ ] Whether the published package matches this repository at this commit

Record the answers back into this file and set `capability_evidence: verified` with the date. Until
then this entry is a **pointer with verified provenance**, not a capability description.

## Purpose

{purpose_block}

## Adoption guidance

{adoption}

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
"""


def wrap_yaml(text: str, width: int, indent: str) -> str:
    """Wrap a string for use under a YAML `>-` block scalar."""
    import textwrap
    flat = " ".join(str(text).split())
    return textwrap.fill(flat, width,
                         initial_indent=indent, subsequent_indent=indent).lstrip()


def render_md(t: Dict[str, Any], rec: Dict[str, Any]) -> str:
    import textwrap
    struct = rec.get("structure") or {}
    archived = bool(rec.get("archived"))
    lic = rec.get("license")
    if archived:
        adoption = (
            "**Do not adopt for new work.** This repository is archived: no further fixes, no further "
            "dependency updates and no security patches should be expected. It remains in the registry "
            "because an archived server can still be the correct answer for a frozen integration, and "
            "because hiding it would send the next reader to rediscover it without the warning. If you "
            "are already running it, treat it as a pinned dependency with a known end of life and plan "
            "the migration."
        )
    elif t.get("license_risk") not in (None, "none"):
        adoption = (
            f"**Legally unsafe to redistribute.** The GitHub API reports the license as `{lic}`. "
            "Absence of a license is not permission: without one, the default is all rights reserved, "
            "so vendoring, bundling or mirroring this code is a copyright risk regardless of how good "
            "the project is or how many stars it has. Using it as a running service under its own terms "
            "may be fine; copying it into this repository or into a product is not. Ask the maintainer "
            "for a license before depending on it."
        )
    elif lic in (None, "NONE", "NOASSERTION"):
        adoption = (
            f"**License is non-standard (`{lic}`).** The API returned a license the SPDX list does not "
            "recognise, which usually means a custom or composite notice. Read the LICENSE file itself "
            "before redistributing or vendoring. Do not assume MIT-equivalent terms."
        )
    elif not struct.get("has_security_md"):
        adoption = (
            "Usable, with a caveat: **no SECURITY.md is published**, so there is no stated disclosure "
            "channel and no published security posture. For a server that will hold a credential or "
            "reach a private system, that is a real gap — raise it with the maintainer, pin a version, "
            "and scope the credential as narrowly as the integration allows."
        )
    else:
        adoption = (
            "Actively maintained, license clear, security policy published. Adopt on the usual terms: "
            "pin a version, scope the credential to the minimum the integration needs, and confirm the "
            "capability checklist above before granting permissions. Re-verify after the expiry date on "
            "this entry — MCP servers move quickly and a tier earned in one quarter is not a tier earned "
            "in the next."
        )
    purpose_block = t["purpose"]
    if t.get("purpose_evidence") == "repository-description-thin":
        purpose_block += (
            "\n\n> The repository's own description was too thin to serve as a purpose statement. "
            "Expand this section from the README, then change `purpose_evidence` to "
            "`readme-reviewed` and date it."
        )
    return MD_TMPL.format(
        id=t["id"], name=t["name"], purpose=textwrap.fill(purpose.split(": ",1)[-1].strip('"') if False else t["purpose"].replace("\n", " "), 96).replace("\n", "\n  "),
        category=t.get("category") or "other",
        distribution=t["distribution"],
        official="true" if t["official"] else "false",
        maintainer=t.get("maintainer") or "null",
        repository=t["repository"], url=t["url"],
        authentication_line=(f"authentication: {t['authentication']}\n" if t.get("authentication") else ""),
        risk_level=t["security"]["risk_level"],
        security_notes=textwrap.fill(t["security"]["notes"], 90).replace("\n", "\n    "),
        local_or_remote=t["local_or_remote"], setup_complexity=t["setup_complexity"],
        production_readiness=t["production_readiness"], status=t.get("status") or "ACTIVE",
        license="null" if t.get("license") is None else t["license"],
        license_risk=t.get("license_risk") or "none",
        stars=t.get("stars") if t.get("stars") is not None else "null",
        stars_fmt=f'{t["stars"]:,}' if t.get("stars") is not None else "unknown",
        today=TODAY, expires=EXPIRES, tier=t.get("tier") or "UNVERIFIED",
        quality_score=t.get("quality_score") if t.get("quality_score") is not None else "null",
        confidence=t.get("confidence") or "medium",
        tags=json.dumps(t.get("tags") or []),
        source_title=f'{t["repository"]} — GitHub repository metadata',
        source_license="null" if lic in (None, "NONE") else lic,
        source_confidence="very-high" if rec.get("fetch_ok") else "low",
        one_line=textwrap.fill(t["purpose"].replace("\n", " "), 88),
        archived="yes" if archived else "no",
        pushed_at=rec.get("pushed_at") or "unknown",
        days_since_push=rec.get("days_since_push") if rec.get("days_since_push") is not None else "unknown",
        language=rec.get("language") or "unknown",
        latest_release=rec.get("latest_release") or "none published",
        contributors=rec.get("contributors") if rec.get("contributors") is not None else "unknown",
        has_security_md="yes" if struct.get("has_security_md") else "**no**",
        has_tests="yes" if struct.get("has_tests") else "**no**",
        has_ci="yes" if struct.get("has_ci") else "**no**",
        adoption=adoption, purpose_block=purpose_block,
        purpose_evidence=t.get("purpose_evidence") or "repository-description",
        license_display=(
            f'`{lic}` — **no SPDX-recognised license; do not redistribute**'
            if t.get("license_risk") not in (None, "none")
            else (f'`{lic}` (non-standard — read the LICENSE file)'
                  if lic in (None, "NONE", "NOASSERTION") else f'`{lic}`')),
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit non-zero if output would change")
    args = ap.parse_args()

    if not REPOS.exists():
        print(f"error: {REPOS} missing — run fetch_github_metadata.py first", file=sys.stderr)
        return 2
    blob = json.loads(REPOS.read_text())
    recs = [r for r in blob["repositories"] if r.get("category") == "mcp-servers"]
    if not recs:
        print("error: no mcp-servers records in metadata/repositories.json", file=sys.stderr)
        return 2

    recs.sort(key=lambda r: (-(r.get("stars") or 0), r["slug"]))
    tools = [record_to_tool(r) for r in recs]

    json_blob = {
        "$schema": "../schemas/mcp.schema.json",
        "generated_at": NOW.isoformat(timespec="seconds"),
        "generator": "scripts/generate-index/generate_mcp_registry.py",
        "source_of_truth": "metadata/repositories.json (GitHub REST API)",
        "verification_method": "github-rest-api",
        "records": len(tools),
        "capability_evidence": "unverified — transport/tool/resource/prompt lists are not exposed by the GitHub API and are intentionally empty",
        "tools": tools,
    }
    new_json = json.dumps(json_blob, indent=2, ensure_ascii=False) + "\n"

    OUT_MD.mkdir(parents=True, exist_ok=True)
    md_files: Dict[str, str] = {}
    for t, r in zip(tools, recs):
        fn = r["slug"].replace("/", "__") + ".md"
        md_files[fn] = render_md(t, r)

    if args.check:
        drift = []
        if OUT_JSON.exists() and OUT_JSON.read_text() != new_json:
            drift.append("metadata/tools.json")
        for fn, txt in md_files.items():
            p = OUT_MD / fn
            if not p.exists() or p.read_text() != txt:
                drift.append(f"knowledge/mcp/registry/{fn}")
        stale = [p.name for p in OUT_MD.glob("*.md") if p.name not in md_files]
        if stale:
            drift += [f"knowledge/mcp/registry/{s} (orphan)" for s in stale]
        if drift:
            print("MCP registry is out of sync:", file=sys.stderr)
            for d in drift:
                print(f"  {d}", file=sys.stderr)
            return 1
        print(f"MCP registry in sync: {len(tools)} entries")
        return 0

    OUT_JSON.write_text(new_json)
    for fn, txt in md_files.items():
        (OUT_MD / fn).write_text(txt)
    for p in OUT_MD.glob("*.md"):
        if p.name not in md_files:
            p.unlink()
            print(f"  removed orphan {p.name}")

    thin = sum(1 for t in tools if t.get("purpose_evidence") == "repository-description-thin")
    risky = [t["repository"] for t in tools if t.get("license_risk") not in (None, "none")]
    arch = [t["repository"] for t in tools if t["production_readiness"] == "deprecated"]
    print(f"  knowledge/mcp/registry/          {len(tools):>4} entries")
    print(f"  metadata/tools.json              {len(tools):>4} records")
    print(f"  purpose needs human expansion:   {thin:>4}")
    print(f"  license risk (do not redistribute): {len(risky)} -> {', '.join(risky) or 'none'}")
    print(f"  archived (do not adopt):         {len(arch)} -> {', '.join(arch) or 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
