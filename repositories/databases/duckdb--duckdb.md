---
id: duckdb--duckdb
title: "duckdb/duckdb"
domain: databases
summary: >-
  duckdb/duckdb — ACTIVE, tier S,
  41,264 stars, license MIT, quality 8.83/10, trust 8.69/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["analytics", "databases", "embedded", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.29, "reproducibility": 10.0, "security": 7.0, "recency": 10.0, "evidence": 8.0}
  quality_score: 8.83
  trust_score: 8.69
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "duckdb/duckdb on GitHub"
    url: https://github.com/duckdb/duckdb
    type: github-repository
    organization: duckdb
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# duckdb/duckdb

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> DuckDB is an analytical in-process SQL database management system

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/duckdb/duckdb> |
| Owner | duckdb (Organization) |
| Official upstream | yes |
| Language | C++ |
| License | `MIT` |
| Stars | 41,264 (checked 2026-09-15) |
| Forks | 3,770 |
| Open issues | 864 |
| Contributors | 344 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v1.5.5 (2026-07-22) |
| Archived | no |
| Fork | no |
| Homepage | http://www.duckdb.org |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.29 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.83** |
| **trust_score** | **8.69** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 3,480 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug duckdb/duckdb
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
