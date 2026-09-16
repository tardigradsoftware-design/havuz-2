---
id: t3-oss--create-t3-app
title: "t3-oss/create-t3-app"
domain: frontend
summary: >-
  t3-oss/create-t3-app — MAINTENANCE, tier B,
  29,117 stars, license MIT, quality 6.67/10, trust 6.45/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["frontend", "github-repository", "scaffold", "typescript"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 4.0, "adoption": 10.0, "documentation": 5.0, "reproducibility": 7.0, "security": 4.5, "recency": 6.22, "evidence": 5.0}
  quality_score: 6.67
  trust_score: 6.45
  tier: B
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "t3-oss/create-t3-app on GitHub"
    url: https://github.com/t3-oss/create-t3-app
    type: github-repository
    organization: t3-oss
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# t3-oss/create-t3-app

🟡 MAINTENANCE · tier **B** · maintenance-mode · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> The best way to start a full-stack, typesafe Next.js app

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/t3-oss/create-t3-app> |
| Owner | t3-oss (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 29,117 (checked 2026-09-15) |
| Forks | 1,535 |
| Open issues | 133 |
| Contributors | 347 |
| Last push | 2025-12-13 (276 days before verification) |
| Latest release | create-t3-app@7.40.0 (2025-11-05) |
| Archived | no |
| Fork | no |
| Homepage | [https://create.t3.gg](https://create.t3.gg) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 4.0 |
| adoption | 10.0 |
| documentation | 5.0 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 6.22 |
| evidence | 5.0 |
| **quality_score** (weighted) | **6.67** |
| **trust_score** | **6.45** |

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
| README size | 15 bytes |

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

No push in 276 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug t3-oss/create-t3-app
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
