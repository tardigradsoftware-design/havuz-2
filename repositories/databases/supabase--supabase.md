---
id: supabase--supabase
title: "supabase/supabase"
domain: databases
summary: >-
  supabase/supabase — ACTIVE, tier S,
  109,289 stars, license Apache-2.0, quality 8.49/10, trust 8.34/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["auth", "baas", "databases", "github-repository", "postgres", "storage"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.9, "reproducibility": 8.5, "security": 4.5, "recency": 10.0, "evidence": 6.0}
  quality_score: 8.49
  trust_score: 8.34
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "supabase/supabase on GitHub"
    url: https://github.com/supabase/supabase
    type: github-repository
    organization: supabase
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# supabase/supabase

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/supabase/supabase> |
| Owner | supabase (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 109,289 (checked 2026-09-15) |
| Forks | 13,780 |
| Open issues | 1,141 |
| Contributors | 396 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v1.26.08 (2026-08-07) |
| Archived | no |
| Fork | no |
| Homepage | https://supabase.com |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.9 |
| reproducibility | 8.5 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.49** |
| **trust_score** | **8.34** |

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
| examples | yes |
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 16,831 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug supabase/supabase
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
