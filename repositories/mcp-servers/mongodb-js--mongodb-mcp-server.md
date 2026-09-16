---
id: mongodb-js--mongodb-mcp-server
title: "mongodb-js/mongodb-mcp-server"
domain: mcp-servers
summary: >-
  mongodb-js/mongodb-mcp-server — ACTIVE, tier S,
  1,129 stars, license Apache-2.0, quality 8.05/10, trust 7.8/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "mongodb"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.0, "reproducibility": 7.0, "security": 4.5, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.05
  trust_score: 7.8
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "mongodb-js/mongodb-mcp-server on GitHub"
    url: https://github.com/mongodb-js/mongodb-mcp-server
    type: github-repository
    organization: mongodb-js
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# mongodb-js/mongodb-mcp-server

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/mongodb-js/mongodb-mcp-server> |
| Owner | mongodb-js (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 1,129 (checked 2026-09-15) |
| Forks | 290 |
| Open issues | 20 |
| Contributors | 50 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v2.1.1 (2026-09-03) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.0 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.05** |
| **trust_score** | **7.8** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | yes |
| examples | no |
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 103,549 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug mongodb-js/mongodb-mcp-server
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
