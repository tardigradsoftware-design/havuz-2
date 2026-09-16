---
id: prettier--prettier
title: "prettier/prettier"
domain: developer-tools
summary: >-
  prettier/prettier — ACTIVE, tier S,
  52,264 stars, license MIT, quality 8.58/10, trust 8.49/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "formatting", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.28, "reproducibility": 9.0, "security": 4.5, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.58
  trust_score: 8.49
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "prettier/prettier on GitHub"
    url: https://github.com/prettier/prettier
    type: github-repository
    organization: prettier
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# prettier/prettier

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> Prettier is an opinionated code formatter.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/prettier/prettier> |
| Owner | prettier (Organization) |
| Official upstream | yes |
| Language | JavaScript |
| License | `MIT` |
| Stars | 52,264 (checked 2026-09-15) |
| Forks | 4,999 |
| Open issues | 1,428 |
| Contributors | 432 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | 3.9.6 (2026-07-21) |
| Archived | no |
| Fork | no |
| Homepage | https://prettier.io |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.28 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.58** |
| **trust_score** | **8.49** |

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
| README size | 3,396 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug prettier/prettier
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
