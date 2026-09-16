---
id: mcp-upstash-context7
name: context7
purpose: >-
  As stated by the repository itself: "Context7 Platform -- Up-to-date code documentation for LLMs
  and AI code editors"
category: documentation
distribution: source
official: true
maintainer: upstash
repository: upstash/context7
url: https://github.com/upstash/context7
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
status: ACTIVE
license: MIT
license_risk: none
stars: 62051
stars_checked_at: 2026-09-16
tier: S
quality_score: 8.28
confidence: high
capability_evidence: unverified
purpose_evidence: repository-description
tags: ["context", "documentation", "llm", "mcp", "mcp-server", "vibe-coding"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "upstash/context7 — GitHub repository metadata"
    url: https://github.com/upstash/context7
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

# context7

`upstash/context7` — As stated by the repository itself: "Context7 Platform -- Up-to-date code documentation
for LLMs and AI code editors"

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`upstash/context7`](https://github.com/upstash/context7) |
| Stars | 62,051 (checked 2026-09-16) |
| License | `MIT` |
| Archived | no |
| Last push | 2026-09-15T13:11:04Z (0 days ago) |
| Language | TypeScript |
| Latest release | @upstash/context7-mcp@4.1.1 |
| Contributors | 128 |
| SECURITY.md published | yes |
| Tests present | **no** |
| CI present | yes |
| Tier / quality score | S / 8.28 |

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

As stated by the repository itself: "Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors"

## Adoption guidance

Actively maintained, license clear, security policy published. Adopt on the usual terms: pin a version, scope the credential to the minimum the integration needs, and confirm the capability checklist above before granting permissions. Re-verify after the expiry date on this entry — MCP servers move quickly and a tier earned in one quarter is not a tier earned in the next.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
