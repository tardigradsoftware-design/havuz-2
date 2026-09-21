---
id: woodpecker-ci--woodpecker
title: "woodpecker-ci/woodpecker"
domain: developer-tools
summary: >-
  woodpecker-ci/woodpecker — ACTIVE, tier S,
  7,901 stars, license Apache-2.0, quality 8.18/10, trust 7.93/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["ci-cd", "developer-tools", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.84, "reproducibility": 7.5, "security": 4.5, "recency": 9.97, "evidence": 5.0}
  quality_score: 8.18
  trust_score: 7.93
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "woodpecker-ci/woodpecker on GitHub"
    url: https://github.com/woodpecker-ci/woodpecker
    type: github-repository
    organization: woodpecker-ci
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

# woodpecker-ci/woodpecker

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Woodpecker is a simple, yet powerful CI/CD engine with great extensibility.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/woodpecker-ci/woodpecker> |
| Owner | woodpecker-ci (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 7,901 (checked 2026-09-21) |
| Forks | 683 |
| Open issues | 383 |
| Contributors | 410 |
| Last push | 2026-09-19 (2 days before verification) |
| Latest release | v3.18.1 (2026-09-08) |
| Archived | no |
| Fork | no |
| Homepage | [https://woodpecker-ci.org](https://woodpecker-ci.org) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.84 |
| reproducibility | 7.5 |
| security | 4.5 |
| recency | 9.97 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.18** |
| **trust_score** | **7.93** |

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
| contributing | no |
| root entries | yes |
| README size | 4,086 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug woodpecker-ci/woodpecker
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
