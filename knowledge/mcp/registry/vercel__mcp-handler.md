---
id: mcp-vercel-mcp-handler
name: mcp-handler
purpose: >-
  As stated by the repository itself: "Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and
  more"
category: cloud
distribution: npm
official: true
maintainer: vercel
repository: vercel/mcp-handler
url: https://github.com/vercel/mcp-handler
transport: []
tools: []
security:
  risk_level: high
  notes: >-
    No SECURITY.md published.
local_or_remote: local
setup_complexity: low
production_readiness: beta
status: ACTIVE
license: null
license_risk: no-license-do-not-redistribute
stars: 669
stars_checked_at: 2026-09-16
tier: UNVERIFIED
quality_score: 8.02
confidence: high
capability_evidence: unverified
purpose_evidence: repository-description
tags: ["adapter", "mcp", "vercel"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "vercel/mcp-handler — GitHub repository metadata"
    url: https://github.com/vercel/mcp-handler
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

# mcp-handler

`vercel/mcp-handler` — As stated by the repository itself: "Easily spin up an MCP Server on Next.js, Nuxt,
Svelte, and more"

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`vercel/mcp-handler`](https://github.com/vercel/mcp-handler) |
| Stars | 669 (checked 2026-09-16) |
| License | `NONE` — **no SPDX-recognised license; do not redistribute** |
| Archived | no |
| Last push | 2026-09-08T14:35:46Z (7 days ago) |
| Language | TypeScript |
| Latest release | v2.1.1 |
| Contributors | 25 |
| SECURITY.md published | **no** |
| Tests present | yes |
| CI present | yes |
| Tier / quality score | UNVERIFIED / 8.02 |

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

As stated by the repository itself: "Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more"

## Adoption guidance

**Legally unsafe to redistribute.** The GitHub API reports the license as `NONE`. Absence of a license is not permission: without one, the default is all rights reserved, so vendoring, bundling or mirroring this code is a copyright risk regardless of how good the project is or how many stars it has. Using it as a running service under its own terms may be fine; copying it into this repository or into a product is not. Ask the maintainer for a license before depending on it.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
