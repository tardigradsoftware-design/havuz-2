---
id: mcp-neondatabase-mcp-server-neon
name: mcp-server-neon
purpose: >-
  As stated by the repository itself: "MCP server for interacting with Neon Management API and
  databases"
category: database
category_evidence: topics-or-slug
category_signals: ["neon"]
registry_kind: server
registry_kind_evidence: >-
  description says "MCP server"
distribution: source
official: true
maintainer: neondatabase
repository: neondatabase/mcp-server-neon
url: https://github.com/neondatabase/mcp-server-neon
npm_package: null
pypi_package: null
transport: []
tools: []
resources: []
prompts: []
permissions: {}
security:
  risk_level: medium
  notes: >-
    No SECURITY.md published.
local_or_remote: local
setup_complexity: medium
production_readiness: production
status: ACTIVE
license: MIT
license_risk: none
stars: 642
stars_checked_at: 2026-09-16
tier: A
quality_score: 7.93
confidence: high
recommended_for: []
not_recommended_for: []
capability_evidence: unverified
purpose_evidence: repository-description
days_since_push: 0
language: TypeScript
tags: ["mcp", "neon", "postgres"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "neondatabase/mcp-server-neon — GitHub repository metadata"
    url: https://github.com/neondatabase/mcp-server-neon
    type: github-repository
    license: MIT
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-16
    note: >-
      Observed via the GitHub REST API on 2026-09-16. Star count, license, archival status,
      push date, language and repository structure are API facts. MCP transport, tool,
      resource and prompt lists are not exposed by the API and are deliberately left
      empty rather than inferred from the repository name.
---

# mcp-server-neon

`neondatabase/mcp-server-neon` — As stated by the repository itself: "MCP server for interacting with Neon Management API
and databases"

**Registry kind: `server`.** Counted as an MCP server in `indexes/mcp.md` and in the README statistics. This is what the registry's consumers — `skills/mcp-integration` and `skills/dont-reinvent-the-wheel` — mean when they say consult the registry before installing a server. Evidence: description says "MCP server".

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`neondatabase/mcp-server-neon`](https://github.com/neondatabase/mcp-server-neon) |
| Stars | 642 (checked 2026-09-16) |
| License | `MIT` |
| Archived | no |
| Last push | 2026-09-15T04:32:49Z (0 days ago) |
| Language | TypeScript |
| Latest release | none published |
| Contributors | 21 |
| SECURITY.md published | **no** |
| Tests present | **no** |
| CI present | yes |
| Tier / quality score | A / 7.93 |

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

As stated by the repository itself: "MCP server for interacting with Neon Management API and databases"

## Adoption guidance

Usable, with a caveat: **no SECURITY.md is published**, so there is no stated disclosure channel and no published security posture. For a server that will hold a credential or reach a private system, that is a real gap — raise it with the maintainer, pin a version, and scope the credential as narrowly as the integration allows.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
