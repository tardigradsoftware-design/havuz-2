---
id: lucia-auth--lucia
title: "lucia-auth/lucia"
domain: backend
summary: >-
  lucia-auth/lucia — STABLE, tier A,
  10,450 stars, license MIT, quality 7.39/10, trust 7.0/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["auth", "backend", "deprecated-candidate", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 8.0, "adoption": 10.0, "documentation": 6.03, "reproducibility": 6.0, "security": 4.5, "recency": 9.41, "evidence": 4.0}
  quality_score: 7.39
  trust_score: 7.0
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "lucia-auth/lucia on GitHub"
    url: https://github.com/lucia-auth/lucia
    type: github-repository
    organization: lucia-auth
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

# lucia-auth/lucia

🔵 STABLE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Authentication, simple and clean

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/lucia-auth/lucia> |
| Owner | lucia-auth (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 10,450 (checked 2026-09-21) |
| Forks | 519 |
| Open issues | 24 |
| Contributors | 215 |
| Last push | 2026-08-08 (43 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://lucia-auth.com](https://lucia-auth.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 8.0 |
| adoption | 10.0 |
| documentation | 6.03 |
| reproducibility | 6.0 |
| security | 4.5 |
| recency | 9.41 |
| evidence | 4.0 |
| **quality_score** (weighted) | **7.39** |
| **trust_score** | **7.0** |

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
| contributing | no |
| root entries | yes |
| README size | 410 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-21) and must be
re-checked against your own constraints._

**Recommended for**

- Reading its authentication learning material
- Understanding why session-based auth guidance changed

**Not recommended for**

- New projects: Lucia v3 was retired as an installable library and repositioned as a learning resource

**Strengths**

- Its documentation and teaching material on sessions, tokens and CSRF remain valuable
- Influenced a generation of TypeScript auth implementations

**Weaknesses**

- Not a maintained library dependency any more
- Migrating to it now means adopting a retired package

**Related projects**

- better-auth/better-auth
- ory/kratos
- supabase/auth
- keycloak/keycloak

## Verification notes

A textbook example of why maintenance status must be verified rather than remembered. Confirm the current position on the project's own site before citing.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug lucia-auth/lucia
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
