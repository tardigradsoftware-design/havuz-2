---
id: trpc--trpc
title: "trpc/trpc"
domain: backend
summary: >-
  trpc/trpc — ACTIVE, tier S,
  40,631 stars, license MIT, quality 8.51/10, trust 8.32/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["api", "backend", "end-to-end-types", "github-repository", "typescript"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.15, "reproducibility": 8.0, "security": 7.0, "recency": 9.95, "evidence": 6.0}
  quality_score: 8.51
  trust_score: 8.32
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "trpc/trpc on GitHub"
    url: https://github.com/trpc/trpc
    type: github-repository
    organization: trpc
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

# trpc/trpc

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> 🧙‍♀️  Move Fast and Break Nothing. End-to-end typesafe APIs made easy.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/trpc/trpc> |
| Owner | trpc (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 40,631 (checked 2026-09-21) |
| Forks | 1,680 |
| Open issues | 201 |
| Contributors | 460 |
| Last push | 2026-09-17 (4 days before verification) |
| Latest release | v11.19.0 (2026-09-16) |
| Archived | no |
| Fork | no |
| Homepage | [https://tRPC.io](https://tRPC.io) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.15 |
| reproducibility | 8.0 |
| security | 7.0 |
| recency | 9.95 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.51** |
| **trust_score** | **8.32** |

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
| examples | yes |
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 13,786 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug trpc/trpc
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
