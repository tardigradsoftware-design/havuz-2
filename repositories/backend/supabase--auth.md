---
id: supabase--auth
title: "supabase/auth"
domain: backend
summary: >-
  supabase/auth — ACTIVE, tier S,
  2,562 stars, license MIT, quality 8.55/10, trust 8.52/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["auth", "backend", "github-repository", "supabase"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 10.0, "reproducibility": 7.5, "security": 4.5, "recency": 10.0, "evidence": 5.5}
  quality_score: 8.55
  trust_score: 8.52
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "supabase/auth on GitHub"
    url: https://github.com/supabase/auth
    type: github-repository
    organization: supabase
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# supabase/auth

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A JWT based API for managing users and issuing JWT tokens

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/supabase/auth> |
| Owner | supabase (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `MIT` |
| Stars | 2,562 (checked 2026-09-15) |
| Forks | 759 |
| Open issues | 349 |
| Contributors | 135 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | v2.197.0 (2026-09-09) |
| Archived | no |
| Fork | no |
| Homepage | [https://supabase.com/docs/guides/auth](https://supabase.com/docs/guides/auth) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 10.0 |
| reproducibility | 7.5 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 5.5 |
| **quality_score** (weighted) | **8.55** |
| **trust_score** | **8.52** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 44,571 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug supabase/auth
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
