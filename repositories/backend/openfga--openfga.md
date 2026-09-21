---
id: openfga--openfga
title: "openfga/openfga"
domain: backend
summary: >-
  openfga/openfga — ACTIVE, tier S,
  5,812 stars, license Apache-2.0, quality 8.69/10, trust 8.59/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["authorization", "backend", "github-repository", "rebac"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.93, "reproducibility": 9.5, "security": 4.5, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.69
  trust_score: 8.59
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "openfga/openfga on GitHub"
    url: https://github.com/openfga/openfga
    type: github-repository
    organization: openfga
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# openfga/openfga

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A high performance and flexible authorization/permission engine built for developers and inspired by Google Zanzibar

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/openfga/openfga> |
| Owner | openfga (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 5,812 (checked 2026-09-21) |
| Forks | 500 |
| Open issues | 217 |
| Contributors | 109 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v1.21.0 (2026-09-20) |
| Archived | no |
| Fork | no |
| Homepage | [https://openfga.dev](https://openfga.dev) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.93 |
| reproducibility | 9.5 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.69** |
| **trust_score** | **8.59** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 11,213 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug openfga/openfga
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
