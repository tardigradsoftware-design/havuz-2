---
id: microsoft--playwright-mcp
title: "microsoft/playwright-mcp"
domain: mcp-servers
summary: >-
  microsoft/playwright-mcp — ACTIVE, tier S,
  37,137 stars, license Apache-2.0, quality 8.9/10, trust 8.82/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["automation", "browser", "github-repository", "mcp", "mcp-servers"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.0, "reproducibility": 9.5, "security": 7.0, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.9
  trust_score: 8.82
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "microsoft/playwright-mcp on GitHub"
    url: https://github.com/microsoft/playwright-mcp
    type: github-repository
    organization: microsoft
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# microsoft/playwright-mcp

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> Playwright MCP server

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/microsoft/playwright-mcp> |
| Owner | microsoft (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 37,137 (checked 2026-09-15) |
| Forks | 3,151 |
| Open issues | 2 |
| Contributors | 70 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | v0.0.81 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | https://www.npmjs.com/package/@playwright/mcp |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.0 |
| reproducibility | 9.5 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.9** |
| **trust_score** | **8.82** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | yes |
| examples | no |
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 65,725 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Giving a coding agent browser control through MCP
- Accessibility-tree-based automation rather than pixel clicking
- Reproducible browser testing from an agent

**Not recommended for**

- Unattended agents with write access to authenticated sessions
- Assuming it replaces visual/computer-use agents when the task needs screenshots

**Strengths**

- Official Microsoft project, Apache-2.0
- Frequent releases (v0.0.81 verified), 70 contributors
- Ships agent-oriented integration examples including .claude/skills
- Accessibility-tree driven, which is more stable and cheaper than vision-based clicking

**Weaknesses**

- Version 0.x: expect interface churn
- Browser control plus network egress is a high-risk permission combination

**Related projects**

- microsoft/playwright
- ChromeDevTools/chrome-devtools-mcp
- browser-use/browser-use
- browserbase/mcp-server-browserbase

## Verification notes

Verified 2026-09-15: ACTIVE, Apache-2.0, q=8.9 - the strongest MCP entry in the registry.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug microsoft/playwright-mcp
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
