---
id: huggingface--datasets
title: "huggingface/datasets"
domain: ai
summary: >-
  huggingface/datasets — STABLE, tier S,
  21,974 stars, license Apache-2.0, quality 8.92/10, trust 8.81/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["ai", "datasets", "github-repository", "library"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.71, "reproducibility": 9.5, "security": 7.0, "recency": 9.95, "evidence": 7.0}
  quality_score: 8.92
  trust_score: 8.81
  tier: S
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "huggingface/datasets on GitHub"
    url: https://github.com/huggingface/datasets
    type: github-repository
    organization: huggingface
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

# huggingface/datasets

🔵 STABLE · tier **S** · published-artifact · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/huggingface/datasets> |
| Owner | huggingface (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 21,974 (checked 2026-09-15) |
| Forks | 3,429 |
| Open issues | 1,374 |
| Contributors | 443 |
| Last push | 2026-09-11 (4 days before verification) |
| Latest release | 5.0.1 (2026-07-28) |
| Archived | no |
| Fork | no |
| Homepage | [https://huggingface.co/docs/datasets](https://huggingface.co/docs/datasets) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `dataset` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.71 |
| reproducibility | 9.5 |
| security | 7.0 |
| recency | 9.95 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.92** |
| **trust_score** | **8.81** |

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
| README size | 14,466 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug huggingface/datasets
python3 scripts/generate-index/generate_repository_cards.py --category ai
```
