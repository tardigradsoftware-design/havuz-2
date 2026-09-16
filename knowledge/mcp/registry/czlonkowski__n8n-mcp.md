---
id: mcp-czlonkowski-n8n-mcp
name: n8n-mcp
purpose: >-
  As stated by the repository itself: "A MCP for Claude Desktop / Claude Code / Windsurf / Cursor
  to build n8n workflows for you"
category: ci-cd
distribution: source
official: false
maintainer: czlonkowski
repository: czlonkowski/n8n-mcp
url: https://github.com/czlonkowski/n8n-mcp
transport: []
tools: []
security:
  risk_level: low
  notes: >-
    SECURITY.md published.
local_or_remote: local
setup_complexity: medium
production_readiness: production
status: ACTIVE
license: MIT
license_risk: none
stars: 22885
stars_checked_at: 2026-09-16
tier: S
quality_score: 8.25
confidence: high
capability_evidence: unverified
purpose_evidence: repository-description
tags: ["automation", "mcp", "mcp-server", "n8n", "workflows"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "czlonkowski/n8n-mcp — GitHub repository metadata"
    url: https://github.com/czlonkowski/n8n-mcp
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

# n8n-mcp

`czlonkowski/n8n-mcp` — As stated by the repository itself: "A MCP for Claude Desktop / Claude Code / Windsurf /
Cursor to build n8n workflows for you"

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`czlonkowski/n8n-mcp`](https://github.com/czlonkowski/n8n-mcp) |
| Stars | 22,885 (checked 2026-09-16) |
| License | `MIT` |
| Archived | no |
| Last push | 2026-09-14T10:13:47Z (1 days ago) |
| Language | TypeScript |
| Latest release | v2.85.0 |
| Contributors | 31 |
| SECURITY.md published | yes |
| Tests present | yes |
| CI present | yes |
| Tier / quality score | S / 8.25 |

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

As stated by the repository itself: "A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you"

## Adoption guidance

Actively maintained, license clear, security policy published. Adopt on the usual terms: pin a version, scope the credential to the minimum the integration needs, and confirm the capability checklist above before granting permissions. Re-verify after the expiry date on this entry — MCP servers move quickly and a tier earned in one quarter is not a tier earned in the next.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
