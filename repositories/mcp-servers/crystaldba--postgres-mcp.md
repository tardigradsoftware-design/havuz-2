---
id: crystaldba--postgres-mcp
title: "crystaldba/postgres-mcp"
domain: mcp-servers
summary: >-
  crystaldba/postgres-mcp — STABLE, tier S,
  3,327 stars, license MIT, quality 8.0/10, trust 7.73/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["dba", "github-repository", "mcp", "mcp-servers", "postgres"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 7.0, "adoption": 10.0, "documentation": 6.5, "reproducibility": 10.0, "security": 4.5, "recency": 9.52, "evidence": 8.0}
  quality_score: 8.0
  trust_score: 7.73
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "crystaldba/postgres-mcp on GitHub"
    url: https://github.com/crystaldba/postgres-mcp
    type: github-repository
    organization: crystaldba
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# crystaldba/postgres-mcp

🔵 STABLE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/crystaldba/postgres-mcp> |
| Owner | crystaldba (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 3,327 (checked 2026-09-21) |
| Forks | 380 |
| Open issues | 91 |
| Contributors | 10 |
| Last push | 2026-08-17 (35 days before verification) |
| Latest release | v0.3.0 (2025-05-16) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 7.0 |
| adoption | 10.0 |
| documentation | 6.5 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 9.52 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.0** |
| **trust_score** | **7.73** |

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
| README size | 37,523 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug crystaldba/postgres-mcp
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
