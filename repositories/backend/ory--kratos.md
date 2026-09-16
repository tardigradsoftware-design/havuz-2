---
id: ory--kratos
title: "ory/kratos"
domain: backend
summary: >-
  ory/kratos — STABLE, tier S,
  13,877 stars, license Apache-2.0, quality 8.93/10, trust 9.04/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["auth", "backend", "github-repository", "identity"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 8.0, "adoption": 10.0, "documentation": 9.46, "reproducibility": 10.0, "security": 7.0, "recency": 9.34, "evidence": 8.5}
  quality_score: 8.93
  trust_score: 9.04
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "ory/kratos on GitHub"
    url: https://github.com/ory/kratos
    type: github-repository
    organization: ory
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# ory/kratos

🔵 STABLE · tier **S** · production-grade · confidence **very-high**

> Headless cloud-native authentication and identity management written in Go. Scales to a billion+ users. Replace Homegrown, Auth0, Okta, Firebase with better UX and DX. Passkeys, Social Sign In, OIDC, Magic Link, Multi-Factor Auth, SMS, SAML, TOTP, and more. Runs everywhere, runs best on Ory Network.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/ory/kratos> |
| Owner | ory (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 13,877 (checked 2026-09-15) |
| Forks | 1,185 |
| Open issues | 224 |
| Contributors | 236 |
| Last push | 2026-07-29 (48 days before verification) |
| Latest release | v26.2.0 (2026-03-20) |
| Archived | no |
| Fork | no |
| Homepage | https://www.ory.com/?utm_source=github&utm_medium=banner&utm_campaign=kratos |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 8.0 |
| adoption | 10.0 |
| documentation | 9.46 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 9.34 |
| evidence | 8.5 |
| **quality_score** (weighted) | **8.93** |
| **trust_score** | **9.04** |

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
| examples | yes |
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 29,571 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug ory/kratos
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
