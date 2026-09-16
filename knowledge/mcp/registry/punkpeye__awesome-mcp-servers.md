---
id: mcp-punkpeye-awesome-mcp-servers
name: awesome-mcp-servers
purpose: >-
  As stated by the repository itself: "A collection of MCP servers."
category: other
category_evidence: no-signal-matched
category_signals: []
registry_kind: catalog
registry_kind_evidence: >-
  description says "collection of"
distribution: source
official: true
maintainer: punkpeye
repository: punkpeye/awesome-mcp-servers
url: https://github.com/punkpeye/awesome-mcp-servers
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
production_readiness: beta
status: ACTIVE
license: MIT
license_risk: none
stars: 95034
stars_checked_at: 2026-09-16
tier: A
quality_score: 7.8
confidence: high
recommended_for: []
not_recommended_for: []
capability_evidence: unverified
purpose_evidence: repository-description
days_since_push: 2
language: null
tags: ["ai", "catalog", "discovery", "mcp"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "punkpeye/awesome-mcp-servers — GitHub repository metadata"
    url: https://github.com/punkpeye/awesome-mcp-servers
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

# awesome-mcp-servers

`punkpeye/awesome-mcp-servers` — As stated by the repository itself: "A collection of MCP servers."

**Registry kind: `catalog`.** **This is a curated list of other servers, not a server.** Consult it to find candidates; do not install it. Recorded here because a catalog with a high star count looks exactly like a popular server in a filtered list. Evidence: description says "collection of".

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`punkpeye/awesome-mcp-servers`](https://github.com/punkpeye/awesome-mcp-servers) |
| Stars | 95,034 (checked 2026-09-16) |
| License | `MIT` |
| Archived | no |
| Last push | 2026-09-13T07:49:46Z (2 days ago) |
| Language | unknown |
| Latest release | none published |
| Contributors | 443 |
| SECURITY.md published | **no** |
| Tests present | **no** |
| CI present | yes |
| Tier / quality score | A / 7.8 |

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

As stated by the repository itself: "A collection of MCP servers."

## Adoption guidance

Usable, with a caveat: **no SECURITY.md is published**, so there is no stated disclosure channel and no published security posture. For a server that will hold a credential or reach a private system, that is a real gap — raise it with the maintainer, pin a version, and scope the credential as narrowly as the integration allows.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
