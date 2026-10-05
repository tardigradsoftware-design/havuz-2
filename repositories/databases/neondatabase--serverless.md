---
id: neondatabase--serverless
title: "neondatabase/serverless"
domain: databases
summary: >-
  neondatabase/serverless — ACTIVE, tier S,
  549 stars, license MIT, quality 8.14/10, trust 8.04/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["databases", "github-repository", "postgres", "serverless"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 9.35, "documentation": 5.94, "reproducibility": 8.0, "security": 4.5, "recency": 9.96, "evidence": 6.0}
  quality_score: 8.14
  trust_score: 8.04
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "neondatabase/serverless on GitHub"
    url: https://github.com/neondatabase/serverless
    type: github-repository
    organization: neondatabase
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-10-05
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-05)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# neondatabase/serverless

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Connect to Neon PostgreSQL from serverless/worker/edge functions

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/neondatabase/serverless> |
| Owner | neondatabase (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 549 (checked 2026-10-05) |
| Forks | 83 |
| Open issues | 51 |
| Contributors | 15 |
| Last push | 2026-10-01 (3 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.npmjs.com/package/@neondatabase/serverless](https://www.npmjs.com/package/@neondatabase/serverless) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 9.35 |
| documentation | 5.94 |
| reproducibility | 8.0 |
| security | 4.5 |
| recency | 9.96 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.14** |
| **trust_score** | **8.04** |

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
| security md | no |
| changelog | yes |
| contributing | no |
| root entries | yes |
| README size | 11,291 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug neondatabase/serverless
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
