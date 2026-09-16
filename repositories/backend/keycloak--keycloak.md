---
id: keycloak--keycloak
title: "keycloak/keycloak"
domain: backend
summary: >-
  keycloak/keycloak — ACTIVE, tier S,
  36,783 stars, license Apache-2.0, quality 8.69/10, trust 8.53/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["auth", "backend", "enterprise", "github-repository", "identity"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.87, "reproducibility": 9.0, "security": 7.0, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.69
  trust_score: 8.53
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "keycloak/keycloak on GitHub"
    url: https://github.com/keycloak/keycloak
    type: github-repository
    organization: keycloak
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# keycloak/keycloak

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Open Source Identity and Access Management For Modern Applications and Services

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/keycloak/keycloak> |
| Owner | keycloak (Organization) |
| Official upstream | yes |
| Language | Java |
| License | `Apache-2.0` |
| Stars | 36,783 (checked 2026-09-15) |
| Forks | 8,931 |
| Open issues | 3,287 |
| Contributors | 319 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | 26.7.3 (2026-08-31) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.keycloak.org](https://www.keycloak.org) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.87 |
| reproducibility | 9.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.69** |
| **trust_score** | **8.53** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 4,414 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug keycloak/keycloak
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
