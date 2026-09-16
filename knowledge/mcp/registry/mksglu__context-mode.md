---
id: mcp-mksglu-context-mode
name: context-mode
purpose: >-
  As stated by the repository itself: "Context window optimization for AI coding agents. Sandboxes
  tool output (98% reduction), persists session memory, and   enforces routing across 17 platforms
  via MCP + hooks."
category: filesystem
distribution: source
official: false
maintainer: mksglu
repository: mksglu/context-mode
url: https://github.com/mksglu/context-mode
transport: []
tools: []
security:
  risk_level: high
  notes: >-
    No SECURITY.md published.
local_or_remote: local
setup_complexity: medium
production_readiness: production
status: ACTIVE
license: null
license_risk: custom-license-review-before-vendoring
stars: 23009
stars_checked_at: 2026-09-16
tier: A
quality_score: 7.81
confidence: high
capability_evidence: unverified
purpose_evidence: repository-description
tags: ["antigravity", "claude", "claude-code", "claude-code-hooks", "claude-code-plugins", "claude-code-skill", "codex", "codex-cli", "context", "context-mode", "copilot", "cursor-plugin", "kiro", "mcp", "mcp-server", "mcp-tools", "openclaw", "opencode", "pi-agent", "skills", "tokens", "zed-extension"]
verified_at: 2026-09-16
expires_at: 2026-12-15
sources:
  - title: "mksglu/context-mode — GitHub repository metadata"
    url: https://github.com/mksglu/context-mode
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

# context-mode

`mksglu/context-mode` — As stated by the repository itself: "Context window optimization for AI coding agents.
Sandboxes tool output (98% reduction), persists session memory, and   enforces routing
across 17 platforms via MCP + hooks."

## What is verified

These fields were read from the GitHub REST API on **2026-09-16** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`mksglu/context-mode`](https://github.com/mksglu/context-mode) |
| Stars | 23,009 (checked 2026-09-16) |
| License | `NOASSERTION` — **no SPDX-recognised license; do not redistribute** |
| Archived | no |
| Last push | 2026-09-15T12:06:28Z (0 days ago) |
| Language | TypeScript |
| Latest release | v1.0.169 |
| Contributors | 110 |
| SECURITY.md published | **no** |
| Tests present | yes |
| CI present | yes |
| Tier / quality score | A / 7.81 |

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

As stated by the repository itself: "Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and   enforces routing across 17 platforms via MCP + hooks."

## Adoption guidance

**Legally unsafe to redistribute.** The GitHub API reports the license as `NOASSERTION`. Absence of a license is not permission: without one, the default is all rights reserved, so vendoring, bundling or mirroring this code is a copyright risk regardless of how good the project is or how many stars it has. Using it as a running service under its own terms may be fine; copying it into this repository or into a product is not. Ask the maintainer for a license before depending on it.

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
