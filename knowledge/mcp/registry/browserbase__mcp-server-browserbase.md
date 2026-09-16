---
id: mcp-browserbase-mcp-server-browserbase
name: mcp-server-browserbase
purpose: >-
  As stated by the repository itself: "Allow LLMs to control a browser with Browserbase and
  Stagehand"
category: browser
distribution: source
official: true
maintainer: browserbase
repository: browserbase/mcp-server-browserbase
url: https://github.com/browserbase/mcp-server-browserbase
transport: []
tools: []
security:
  risk_level: high
  notes: >-
    Archived: no further fixes expected.
local_or_remote: local
setup_complexity: medium
production_readiness: deprecated
status: ARCHIVED
license: Apache-2.0
license_risk: none
stars: 3409
stars_checked_at: 2026-09-16
tier: ARCHIVED
quality_score: 6.77
confidence: high
capability_evidence: unverified
purpose_evidence: repository-description
tags: ["ai", "browser", "chrome", "chromium", "cloud", "mcp", "playwright", "puppeteer"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "browserbase/mcp-server-browserbase — GitHub repository metadata"
    url: https://github.com/browserbase/mcp-server-browserbase
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

# mcp-server-browserbase

`browserbase/mcp-server-browserbase` — As stated by the repository itself: "Allow LLMs to control a browser with Browserbase
and Stagehand"

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`browserbase/mcp-server-browserbase`](https://github.com/browserbase/mcp-server-browserbase) |
| Stars | 3,409 (checked 2026-09-16) |
| License | `Apache-2.0` |
| Archived | yes |
| Last push | 2026-07-20T21:48:14Z (56 days ago) |
| Language | TypeScript |
| Latest release | v3.0.0 |
| Contributors | 16 |
| SECURITY.md published | **no** |
| Tests present | yes |
| CI present | yes |
| Tier / quality score | ARCHIVED / 6.77 |

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

As stated by the repository itself: "Allow LLMs to control a browser with Browserbase and Stagehand"

## Adoption guidance

**Do not adopt for new work.** This repository is archived: no further fixes, no further dependency updates and no security patches should be expected. It remains in the registry because an archived server can still be the correct answer for a frozen integration, and because hiding it would send the next reader to rediscover it without the warning. If you are already running it, treat it as a pinned dependency with a known end of life and plan the migration.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
