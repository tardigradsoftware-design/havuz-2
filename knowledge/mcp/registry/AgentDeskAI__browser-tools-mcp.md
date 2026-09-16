---
id: mcp-agentdeskai-browser-tools-mcp
name: browser-tools-mcp
purpose: >-
  As stated by the repository itself: "Monitor browser logs directly from Cursor and other MCP
  compatible IDEs."
category: browser
distribution: source
official: true
maintainer: AgentDeskAI
repository: AgentDeskAI/browser-tools-mcp
url: https://github.com/AgentDeskAI/browser-tools-mcp
transport: []
tools: []
authentication: mixed
security:
  risk_level: low
  notes: >-
    SECURITY.md published.
local_or_remote: local
setup_complexity: medium
production_readiness: production
status: STABLE
license: MIT
license_risk: none
stars: 7319
stars_checked_at: 2026-09-16
tier: A
quality_score: 7.92
confidence: high
capability_evidence: unverified
purpose_evidence: repository-description
tags: ["ai", "anthropic", "browser", "cursor", "devtools", "mcp", "mcp-server"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "AgentDeskAI/browser-tools-mcp — GitHub repository metadata"
    url: https://github.com/AgentDeskAI/browser-tools-mcp
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

# browser-tools-mcp

`AgentDeskAI/browser-tools-mcp` — As stated by the repository itself: "Monitor browser logs directly from Cursor and other
MCP compatible IDEs."

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`AgentDeskAI/browser-tools-mcp`](https://github.com/AgentDeskAI/browser-tools-mcp) |
| Stars | 7,319 (checked 2026-09-16) |
| License | `MIT` |
| Archived | no |
| Last push | 2026-08-12T16:48:04Z (33 days ago) |
| Language | TypeScript |
| Latest release | v2.0.2 |
| Contributors | 7 |
| SECURITY.md published | yes |
| Tests present | **no** |
| CI present | yes |
| Tier / quality score | A / 7.92 |

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

As stated by the repository itself: "Monitor browser logs directly from Cursor and other MCP compatible IDEs."

## Adoption guidance

Actively maintained, license clear, security policy published. Adopt on the usual terms: pin a version, scope the credential to the minimum the integration needs, and confirm the capability checklist above before granting permissions. Re-verify after the expiry date on this entry — MCP servers move quickly and a tier earned in one quarter is not a tier earned in the next.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
