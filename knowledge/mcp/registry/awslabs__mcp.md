---
id: mcp-awslabs-mcp
name: mcp
purpose: >-
  As stated by the repository itself: "Open source MCP Servers for AWS"
category: cloud
distribution: source
official: true
maintainer: awslabs
repository: awslabs/mcp
url: https://github.com/awslabs/mcp
transport: []
tools: []
security:
  risk_level: medium
  notes: >-
    No SECURITY.md published.
local_or_remote: local
setup_complexity: medium
production_readiness: production
status: ACTIVE
license: Apache-2.0
license_risk: none
stars: 9695
stars_checked_at: 2026-09-16
tier: S
quality_score: 8.65
confidence: high
capability_evidence: unverified
purpose_evidence: repository-description
tags: ["aws", "catalog", "mcp", "mcp-client", "mcp-clients", "mcp-host", "mcp-server", "mcp-servers", "mcp-tools", "modelcontextprotocol"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "awslabs/mcp — GitHub repository metadata"
    url: https://github.com/awslabs/mcp
    type: github-repository
    license: Apache-2.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-16
    note: >-
      Observed via the GitHub REST API on 2026-09-16. Star count, license, archival status,
      push date, language and repository structure are API facts. MCP transport, tool,
      resource and prompt lists are not exposed by the API and are deliberately left
      empty rather than inferred from the repository name.
---

# mcp

`awslabs/mcp` — As stated by the repository itself: "Open source MCP Servers for AWS"

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`awslabs/mcp`](https://github.com/awslabs/mcp) |
| Stars | 9,695 (checked 2026-09-16) |
| License | `Apache-2.0` |
| Archived | no |
| Last push | 2026-09-15T14:36:14Z (0 days ago) |
| Language | Python |
| Latest release | 2026.09.20260908143235 |
| Contributors | 328 |
| SECURITY.md published | **no** |
| Tests present | **no** |
| CI present | yes |
| Tier / quality score | S / 8.65 |

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

As stated by the repository itself: "Open source MCP Servers for AWS"

## Adoption guidance

Usable, with a caveat: **no SECURITY.md is published**, so there is no stated disclosure channel and no published security posture. For a server that will hold a credential or reach a private system, that is a real gap — raise it with the maintainer, pin a version, and scope the credential as narrowly as the integration allows.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
