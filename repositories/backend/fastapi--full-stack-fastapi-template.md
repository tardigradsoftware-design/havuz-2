---
id: fastapi--full-stack-fastapi-template
title: "fastapi/full-stack-fastapi-template"
domain: backend
summary: >-
  fastapi/full-stack-fastapi-template — ACTIVE, tier A,
  45,568 stars, license MIT, quality 7.64/10, trust 7.17/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["backend", "fullstack", "github-repository", "template"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 9.5, "adoption": 10.0, "documentation": 4.27, "reproducibility": 7.0, "security": 4.5, "recency": 9.84, "evidence": 4.5}
  quality_score: 7.64
  trust_score: 7.17
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "fastapi/full-stack-fastapi-template on GitHub"
    url: https://github.com/fastapi/full-stack-fastapi-template
    type: github-repository
    organization: fastapi
    license: MIT
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# fastapi/full-stack-fastapi-template

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> Full-stack web application template with FastAPI, React, SQLModel, PostgreSQL, Vite, Tailwind CSS, shadcn/ui, FastAPI Cloud, and Docker Compose.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/fastapi/full-stack-fastapi-template> |
| Owner | fastapi (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 45,568 (checked 2026-09-15) |
| Forks | 9,061 |
| Open issues | 11 |
| Contributors | 82 |
| Last push | 2026-09-03 (12 days before verification) |
| Latest release | 0.12.0 (2026-08-12) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 9.5 |
| adoption | 10.0 |
| documentation | 4.27 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 9.84 |
| evidence | 4.5 |
| **quality_score** (weighted) | **7.64** |
| **trust_score** | **7.17** |

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
| README size | 3,193 bytes |

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

Repository moved: `tiangolo/full-stack-fastapi-template` -> `fastapi/full-stack-fastapi-template`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug fastapi/full-stack-fastapi-template
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
