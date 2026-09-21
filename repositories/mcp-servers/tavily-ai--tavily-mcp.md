---
id: tavily-ai--tavily-mcp
title: "tavily-ai/tavily-mcp"
domain: mcp-servers
summary: >-
  tavily-ai/tavily-mcp — ACTIVE, tier A,
  2,396 stars, license MIT, quality 7.57/10, trust 6.98/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "search"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 4.23, "reproducibility": 7.0, "security": 4.5, "recency": 9.95, "evidence": 4.0}
  quality_score: 7.57
  trust_score: 6.98
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "tavily-ai/tavily-mcp on GitHub"
    url: https://github.com/tavily-ai/tavily-mcp
    type: github-repository
    organization: tavily-ai
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# tavily-ai/tavily-mcp

🟢 ACTIVE · tier **A** · production-ready · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Production ready MCP server with real-time search, extract, map & crawl.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/tavily-ai/tavily-mcp> |
| Owner | tavily-ai (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 2,396 (checked 2026-09-21) |
| Forks | 302 |
| Open issues | 57 |
| Contributors | 16 |
| Last push | 2026-09-16 (4 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 4.23 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 9.95 |
| evidence | 4.0 |
| **quality_score** (weighted) | **7.57** |
| **trust_score** | **6.98** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 8,727 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(not yet curated) and must be
re-checked against your own constraints._

**Recommended for**

- _not curated yet_

**Not recommended for**

- _not curated yet_

**Strengths**

- _not curated yet_

**Weaknesses**

- _not curated yet_

**Related projects**

- _not curated yet_

## Verification notes

_No anomalies detected._

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug tavily-ai/tavily-mcp
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
