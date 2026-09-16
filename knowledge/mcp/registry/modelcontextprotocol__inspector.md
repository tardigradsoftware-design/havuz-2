---
id: mcp-modelcontextprotocol-inspector
name: inspector
purpose: >-
  As stated by the repository itself: "Visual testing tool for MCP servers"
category: other
category_evidence: no-signal-matched
category_signals: []
registry_kind: tooling
registry_kind_evidence: >-
  description says "Visual testing"
distribution: source
official: true
maintainer: modelcontextprotocol
repository: modelcontextprotocol/inspector
url: https://github.com/modelcontextprotocol/inspector
npm_package: null
pypi_package: null
transport: []
tools: []
resources: []
prompts: []
permissions: {}
security:
  risk_level: high
  notes: >-
    SECURITY.md published.
local_or_remote: local
setup_complexity: medium
production_readiness: beta
status: ACTIVE
license: null
license_risk: no-license-do-not-redistribute
stars: 10885
stars_checked_at: 2026-09-16
tier: NO-LICENSE
quality_score: 7.92
confidence: high
recommended_for: []
not_recommended_for: []
capability_evidence: unverified
purpose_evidence: repository-description
days_since_push: 0
language: TypeScript
tags: ["cli", "debug", "debugging", "mcp", "tool", "tui", "web"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "modelcontextprotocol/inspector — GitHub repository metadata"
    url: https://github.com/modelcontextprotocol/inspector
    type: github-repository
    license: null
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-16
    note: >-
      Observed via the GitHub REST API on 2026-09-16. Star count, license, archival status,
      push date, language and repository structure are API facts. MCP transport, tool,
      resource and prompt lists are not exposed by the API and are deliberately left
      empty rather than inferred from the repository name.
---

# inspector

`modelcontextprotocol/inspector` — As stated by the repository itself: "Visual testing tool for MCP servers"

**Registry kind: `tooling`.** **This is not a server you can connect to.** It is a tool for testing or debugging servers. Recorded here because it is the right answer to the question “how do I check the server I just built”, not to the question “which server should I install”. Evidence: description says "Visual testing".

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`modelcontextprotocol/inspector`](https://github.com/modelcontextprotocol/inspector) |
| Stars | 10,885 (checked 2026-09-16) |
| License | `NONE` — **no SPDX-recognised license; do not redistribute** |
| Archived | no |
| Last push | 2026-09-15T06:16:59Z (0 days ago) |
| Language | TypeScript |
| Latest release | 2.6.0 |
| Contributors | 135 |
| SECURITY.md published | yes |
| Tests present | **no** |
| CI present | yes |
| Tier / quality score | NO-LICENSE / 7.92 |

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

As stated by the repository itself: "Visual testing tool for MCP servers"

## Adoption guidance

**Legally unsafe to redistribute.** The GitHub API reports the license as `NONE`. Absence of a license is not permission: without one, the default is all rights reserved, so vendoring, bundling or mirroring this code is a copyright risk regardless of how good the project is or how many stars it has. Using it as a running service under its own terms may be fine; copying it into this repository or into a product is not. Ask the maintainer for a license before depending on it.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
