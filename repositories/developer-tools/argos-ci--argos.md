---
id: argos-ci--argos
title: "argos-ci/argos"
domain: developer-tools
summary: >-
  argos-ci/argos — ACTIVE, tier S,
  626 stars, license MIT, quality 8.43/10, trust 8.24/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "visual-regression"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 9.44, "documentation": 6.62, "reproducibility": 8.5, "security": 7.0, "recency": 10.0, "evidence": 6.0}
  quality_score: 8.43
  trust_score: 8.24
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "argos-ci/argos on GitHub"
    url: https://github.com/argos-ci/argos
    type: github-repository
    organization: argos-ci
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# argos-ci/argos

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> The open source visual testing platform for teams and AI agents. Review the product, not just the code.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/argos-ci/argos> |
| Owner | argos-ci (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 626 (checked 2026-09-15) |
| Forks | 64 |
| Open issues | 2 |
| Contributors | 15 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | https://argos-ci.com |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 9.44 |
| documentation | 6.62 |
| reproducibility | 8.5 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.43** |
| **trust_score** | **8.24** |

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
| README size | 1,387 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug argos-ci/argos
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
