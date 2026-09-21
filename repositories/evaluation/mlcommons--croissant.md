---
id: mlcommons--croissant
title: "mlcommons/croissant"
domain: evaluation
summary: >-
  mlcommons/croissant — STABLE, tier A,
  901 stars, license Apache-2.0, quality 7.55/10, trust 7.28/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["dataset", "evaluation", "github-repository", "metadata", "standard"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 7.0, "adoption": 9.93, "documentation": 7.55, "reproducibility": 7.0, "security": 4.5, "recency": 9.07, "evidence": 5.0}
  quality_score: 7.55
  trust_score: 7.28
  tier: A
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "mlcommons/croissant on GitHub"
    url: https://github.com/mlcommons/croissant
    type: github-repository
    organization: mlcommons
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# mlcommons/croissant

🔵 STABLE · tier **A** · published-artifact · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Croissant is a high-level format for machine learning datasets that brings together four rich layers.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/mlcommons/croissant> |
| Owner | mlcommons (Organization) |
| Official upstream | yes |
| Language | Jupyter Notebook |
| License | `Apache-2.0` |
| Stars | 901 (checked 2026-09-21) |
| Forks | 125 |
| Open issues | 222 |
| Contributors | 40 |
| Last push | 2026-07-15 (68 days before verification) |
| Latest release | v1.1.0 (2026-04-16) |
| Archived | no |
| Fork | no |
| Homepage | [https://mlcommons.org/croissant](https://mlcommons.org/croissant) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `dataset` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 7.0 |
| adoption | 9.93 |
| documentation | 7.55 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 9.07 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.55** |
| **trust_score** | **7.28** |

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
| contributing | yes |
| root entries | yes |
| README size | 12,651 bytes |

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

Reference implementation published with a dataset. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug mlcommons/croissant
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
