---
id: mlcommons--croissant
title: "mlcommons/croissant"
domain: evaluation
summary: >-
  mlcommons/croissant — STABLE, tier S,
  906 stars, license Apache-2.0, quality 8.1/10, trust 7.88/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["dataset", "evaluation", "github-repository", "metadata", "standard"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 9.94, "documentation": 7.55, "reproducibility": 7.0, "security": 4.5, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.1
  trust_score: 7.88
  tier: S
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
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
    confidence: very-high
    claim_type: fact
    verified_at: 2026-10-05
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-05)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# mlcommons/croissant

🔵 STABLE · tier **S** · published-artifact · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Croissant is a high-level format for machine learning datasets that brings together four rich layers.

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/mlcommons/croissant> |
| Owner | mlcommons (Organization) |
| Official upstream | yes |
| Language | Jupyter Notebook |
| License | `Apache-2.0` |
| Stars | 906 (checked 2026-10-05) |
| Forks | 125 |
| Open issues | 225 |
| Contributors | 40 |
| Last push | 2026-10-05 (0 days before verification) |
| Latest release | v1.1.1 (2026-10-05) |
| Archived | no |
| Fork | no |
| Homepage | [https://mlcommons.org/croissant](https://mlcommons.org/croissant) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `dataset` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 9.94 |
| documentation | 7.55 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.1** |
| **trust_score** | **7.88** |

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
