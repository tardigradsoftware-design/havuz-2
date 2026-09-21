---
id: fastapi--fastapi
title: "fastapi/fastapi"
domain: backend
summary: >-
  fastapi/fastapi — ACTIVE, tier S,
  102,496 stars, license MIT, quality 8.69/10, trust 8.71/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["api", "async", "backend", "github-repository", "python"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.9, "reproducibility": 9.0, "security": 4.5, "recency": 9.97, "evidence": 7.5}
  quality_score: 8.69
  trust_score: 8.71
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "fastapi/fastapi on GitHub"
    url: https://github.com/fastapi/fastapi
    type: github-repository
    organization: fastapi
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

# fastapi/fastapi

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> FastAPI framework, high performance, easy to learn, fast to code, ready for production

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/fastapi/fastapi> |
| Owner | fastapi (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 102,496 (checked 2026-09-21) |
| Forks | 9,921 |
| Open issues | 82 |
| Contributors | 457 |
| Last push | 2026-09-18 (2 days before verification) |
| Latest release | 0.141.1 (2026-07-29) |
| Archived | no |
| Fork | no |
| Homepage | [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.9 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 9.97 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.69** |
| **trust_score** | **8.71** |

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
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 22,780 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug fastapi/fastapi
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
