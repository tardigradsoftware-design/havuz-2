---
id: prisma--orm
title: "prisma/orm"
domain: databases
summary: >-
  prisma/orm — ACTIVE, tier S,
  47,647 stars, license Apache-2.0, quality 9.06/10, trust 9.04/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["databases", "github-repository", "orm", "typescript"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.63, "reproducibility": 10.0, "security": 7.0, "recency": 10.0, "evidence": 8.0}
  quality_score: 9.06
  trust_score: 9.04
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "prisma/orm on GitHub"
    url: https://github.com/prisma/orm
    type: github-repository
    organization: prisma
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# prisma/orm

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Next-generation ORM for Node.js & TypeScript \| PostgreSQL, MySQL, MariaDB, SQL Server, SQLite, MongoDB and CockroachDB

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/prisma/orm> |
| Owner | prisma (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 47,647 (checked 2026-09-21) |
| Forks | 2,541 |
| Open issues | 2,651 |
| Contributors | 23 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v0.17.0 (2026-08-04) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.prisma.io](https://www.prisma.io) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.63 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **9.06** |
| **trust_score** | **9.04** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | yes |
| ci | yes |
| examples | yes |
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 7,556 bytes |

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

Repository moved: `prisma/prisma` -> `prisma/orm`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug prisma/orm
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
