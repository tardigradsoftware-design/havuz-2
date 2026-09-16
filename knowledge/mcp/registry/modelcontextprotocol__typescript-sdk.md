---
id: mcp-modelcontextprotocol-typescript-sdk
name: typescript-sdk
purpose: >-
  As stated by the repository itself: "The official TypeScript SDK for Model Context Protocol
  servers and clients"
category: other
category_evidence: no-signal-matched
category_signals: []
registry_kind: sdk
registry_kind_evidence: >-
  description says "SDK"
distribution: source
official: true
maintainer: modelcontextprotocol
repository: modelcontextprotocol/typescript-sdk
url: https://github.com/modelcontextprotocol/typescript-sdk
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
production_readiness: production
status: ACTIVE
license: null
license_risk: custom-license-review-before-vendoring
stars: 13402
stars_checked_at: 2026-09-16
tier: A
quality_score: 8.78
confidence: high
recommended_for: []
not_recommended_for: []
capability_evidence: unverified
purpose_evidence: repository-description
days_since_push: 0
language: TypeScript
tags: ["mcp", "mcp-client", "mcp-server", "sdk", "typescript"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "modelcontextprotocol/typescript-sdk — GitHub repository metadata"
    url: https://github.com/modelcontextprotocol/typescript-sdk
    type: github-repository
    license: NOASSERTION
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-16
    note: >-
      Observed via the GitHub REST API on 2026-09-16. Star count, license, archival status,
      push date, language and repository structure are API facts. MCP transport, tool,
      resource and prompt lists are not exposed by the API and are deliberately left
      empty rather than inferred from the repository name.
---

# typescript-sdk

`modelcontextprotocol/typescript-sdk` — As stated by the repository itself: "The official TypeScript SDK for Model Context
Protocol servers and clients"

**Registry kind: `sdk`.** **This is not a server you can connect to.** It is a library for *building* one. Installing it as an MCP server will not work; it is recorded here so that somebody about to write a server finds it instead of writing their own. Evidence: description says "SDK".

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`modelcontextprotocol/typescript-sdk`](https://github.com/modelcontextprotocol/typescript-sdk) |
| Stars | 13,402 (checked 2026-09-16) |
| License | `NOASSERTION` — **no SPDX-recognised license; do not redistribute** |
| Archived | no |
| Last push | 2026-09-15T04:08:11Z (0 days ago) |
| Language | TypeScript |
| Latest release | @modelcontextprotocol/fastify@2.0.0 |
| Contributors | 169 |
| SECURITY.md published | yes |
| Tests present | yes |
| CI present | yes |
| Tier / quality score | A / 8.78 |

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

As stated by the repository itself: "The official TypeScript SDK for Model Context Protocol servers and clients"

## Adoption guidance

**Legally unsafe to redistribute.** The GitHub API reports the license as `NOASSERTION`. Absence of a license is not permission: without one, the default is all rights reserved, so vendoring, bundling or mirroring this code is a copyright risk regardless of how good the project is or how many stars it has. Using it as a running service under its own terms may be fine; copying it into this repository or into a product is not. Ask the maintainer for a license before depending on it.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
