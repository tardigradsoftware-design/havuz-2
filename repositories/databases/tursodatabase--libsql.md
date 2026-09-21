---
id: tursodatabase--libsql
title: "tursodatabase/libsql"
domain: databases
summary: >-
  tursodatabase/libsql — ACTIVE, tier A,
  17,225 stars, license MIT, quality 7.53/10, trust 6.5/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["databases", "github-repository", "serverless", "sqlite"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.36, "reproducibility": 7.5, "security": 3.5, "recency": 9.93, "evidence": 5.0}
  quality_score: 7.53
  trust_score: 6.5
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "tursodatabase/libsql on GitHub"
    url: https://github.com/tursodatabase/libsql
    type: github-repository
    organization: tursodatabase
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

# tursodatabase/libsql

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> libSQL is a fork of SQLite that is both Open Source, and Open Contributions.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/tursodatabase/libsql> |
| Owner | tursodatabase (Organization) |
| Official upstream | no |
| Language | C |
| License | `MIT` |
| Stars | 17,225 (checked 2026-09-21) |
| Forks | 532 |
| Open issues | 455 |
| Contributors | 108 |
| Last push | 2026-09-16 (5 days before verification) |
| Latest release | libsql-server-v0.24.32 (2025-02-14) |
| Archived | no |
| Fork | no |
| Homepage | [https://turso.tech/libsql](https://turso.tech/libsql) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.36 |
| reproducibility | 7.5 |
| security | 3.5 |
| recency | 9.93 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.53** |
| **trust_score** | **6.5** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | no |
| ci | yes |
| examples | no |
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 10,292 bytes |

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

Repository moved: `libsql/libsql` -> `tursodatabase/libsql`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug tursodatabase/libsql
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
