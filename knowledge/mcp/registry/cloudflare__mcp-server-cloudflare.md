---
id: mcp-cloudflare-mcp-server-cloudflare
name: mcp-server-cloudflare
purpose: >-
  Registered as an MCP server under `cloudflare/mcp-server-cloudflare`. The repository returned no
  description from the GitHub API. Purpose must be confirmed from the README before adoption; this
  entry deliberately does not guess at capabilities.
category: cloud
category_evidence: topics-or-slug
category_signals: ["cloudflare"]
registry_kind: server
registry_kind_evidence: >-
  slug "cloudflare/mcp-server-cloudflare" names the repository as MCP
distribution: source
official: true
maintainer: cloudflare
repository: cloudflare/mcp-server-cloudflare
url: https://github.com/cloudflare/mcp-server-cloudflare
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
license: Apache-2.0
license_risk: none
stars: 4195
stars_checked_at: 2026-09-16
tier: A
quality_score: 7.53
confidence: high
recommended_for: []
not_recommended_for: []
capability_evidence: unverified
purpose_evidence: repository-description-thin
days_since_push: 14
language: TypeScript
tags: ["cloudflare", "edge", "mcp"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "cloudflare/mcp-server-cloudflare — GitHub repository metadata"
    url: https://github.com/cloudflare/mcp-server-cloudflare
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

# mcp-server-cloudflare

`cloudflare/mcp-server-cloudflare` — Registered as an MCP server under \`cloudflare/mcp-server-cloudflare\`. The repository
returned no description from the GitHub API. Purpose must be confirmed from the README
before adoption; this entry deliberately does not guess at capabilities.

**Registry kind: `server`.** Counted as an MCP server in `indexes/mcp.md` and in the README statistics. This is what the registry's consumers — `skills/mcp-integration` and `skills/dont-reinvent-the-wheel` — mean when they say consult the registry before installing a server. Evidence: slug "cloudflare/mcp-server-cloudflare" names the repository as MCP.

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`cloudflare/mcp-server-cloudflare`](https://github.com/cloudflare/mcp-server-cloudflare) |
| Stars | 4,195 (checked 2026-09-16) |
| License | `Apache-2.0` |
| Archived | no |
| Last push | 2026-09-01T14:26:32Z (14 days ago) |
| Language | TypeScript |
| Latest release | containers-mcp@0.2.19 |
| Contributors | 41 |
| SECURITY.md published | **no** |
| Tests present | **no** |
| CI present | yes |
| Tier / quality score | A / 7.53 |

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

Registered as an MCP server under \`cloudflare/mcp-server-cloudflare\`. The repository returned no description from the GitHub API. Purpose must be confirmed from the README before adoption; this entry deliberately does not guess at capabilities.

> The repository's own description was too thin to serve as a purpose statement. Expand this section from the README, then change `purpose_evidence` to `readme-reviewed` and date it.

## Adoption guidance

Usable, with a caveat: **no SECURITY.md is published**, so there is no stated disclosure channel and no published security posture. For a server that will hold a credential or reach a private system, that is a real gap — raise it with the maintainer, pin a version, and scope the credential as narrowly as the integration allows.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
