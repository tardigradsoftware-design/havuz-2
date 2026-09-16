---
id: typicode--husky
title: "typicode/husky"
domain: developer-tools
summary: >-
  typicode/husky — MAINTENANCE, tier A,
  35,314 stars, license MIT, quality 7.31/10, trust 7.05/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "git-hooks", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 7.5, "maintenance": 6.0, "adoption": 10.0, "documentation": 6.0, "reproducibility": 9.0, "security": 4.5, "recency": 7.55, "evidence": 7.0}
  quality_score: 7.31
  trust_score: 7.05
  tier: A
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "typicode/husky on GitHub"
    url: https://github.com/typicode/husky
    type: github-repository
    organization: typicode
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

# typicode/husky

🟡 MAINTENANCE · tier **A** · maintenance-mode · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Git hooks made easy 🐶 woof!

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/typicode/husky> |
| Owner | typicode (User) |
| Official upstream | yes |
| Language | JavaScript |
| License | `MIT` |
| Stars | 35,314 (checked 2026-09-15) |
| Forks | 1,098 |
| Open issues | 108 |
| Contributors | 124 |
| Last push | 2026-03-19 (179 days before verification) |
| Latest release | v9.1.7 (2024-11-18) |
| Archived | no |
| Fork | no |
| Homepage | [https://typicode.github.io/husky](https://typicode.github.io/husky) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 7.5 |
| maintenance | 6.0 |
| adoption | 10.0 |
| documentation | 6.0 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 7.55 |
| evidence | 7.0 |
| **quality_score** (weighted) | **7.31** |
| **trust_score** | **7.05** |

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
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 33 bytes |

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

No push in 179 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug typicode/husky
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
