---
id: redis--mcp-redis
title: "redis/mcp-redis"
domain: mcp-servers
summary: >-
  redis/mcp-redis — ACTIVE, tier S,
  623 stars, license MIT, quality 8.62/10, trust 8.7/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["cache", "github-repository", "mcp", "mcp-servers", "redis"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 9.5, "adoption": 9.53, "documentation": 6.81, "reproducibility": 10.0, "security": 4.5, "recency": 9.82, "evidence": 8.5}
  quality_score: 8.62
  trust_score: 8.7
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "redis/mcp-redis on GitHub"
    url: https://github.com/redis/mcp-redis
    type: github-repository
    organization: redis
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# redis/mcp-redis

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/redis/mcp-redis> |
| Owner | redis (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 623 (checked 2026-09-15) |
| Forks | 113 |
| Open issues | 18 |
| Contributors | 25 |
| Last push | 2026-09-02 (13 days before verification) |
| Latest release | 0.5.1 (2026-08-05) |
| Archived | no |
| Fork | no |
| Homepage | https://redis.io/docs/latest/integrate/redis-mcp/ |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 9.5 |
| adoption | 9.53 |
| documentation | 6.81 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 9.82 |
| evidence | 8.5 |
| **quality_score** (weighted) | **8.62** |
| **trust_score** | **8.7** |

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
| examples | yes |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 27,768 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug redis/mcp-redis
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
