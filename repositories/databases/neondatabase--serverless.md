---
id: neondatabase--serverless
title: "neondatabase/serverless"
domain: databases
summary: >-
  neondatabase/serverless — ACTIVE, tier S,
  548 stars, license MIT, quality 8.13/10, trust 8.03/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["databases", "github-repository", "postgres", "serverless"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 9.34, "documentation": 5.89, "reproducibility": 8.0, "security": 4.5, "recency": 9.95, "evidence": 6.0}
  quality_score: 8.13
  trust_score: 8.03
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
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
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# neondatabase/serverless

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Connect to Neon PostgreSQL from serverless/worker/edge functions

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/neondatabase/serverless> |
| Owner | neondatabase (Organization) |
| Official upstream | yes |
| Language | JavaScript |
| License | `MIT` |
| Stars | 548 (checked 2026-09-21) |
| Forks | 81 |
| Open issues | 56 |
| Contributors | 15 |
| Last push | 2026-09-16 (4 days before verification) |
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
| adoption | 9.34 |
| documentation | 5.89 |
| reproducibility | 8.0 |
| security | 4.5 |
| recency | 9.95 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.13** |
| **trust_score** | **8.03** |

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
| README size | 10,690 bytes |

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
