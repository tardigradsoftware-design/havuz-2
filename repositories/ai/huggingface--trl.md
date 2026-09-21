---
id: huggingface--trl
title: "huggingface/trl"
domain: ai
summary: >-
  huggingface/trl — ACTIVE, tier S,
  19,351 stars, license Apache-2.0, quality 8.92/10, trust 8.83/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["ai", "fine-tuning", "github-repository", "rl"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.22, "reproducibility": 10.0, "security": 7.0, "recency": 10.0, "evidence": 8.0}
  quality_score: 8.92
  trust_score: 8.83
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "huggingface/trl on GitHub"
    url: https://github.com/huggingface/trl
    type: github-repository
    organization: huggingface
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

# huggingface/trl

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Train transformer language models with reinforcement learning.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/huggingface/trl> |
| Owner | huggingface (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 19,351 (checked 2026-09-21) |
| Forks | 3,011 |
| Open issues | 281 |
| Contributors | 465 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v1.13.0 (2026-09-10) |
| Archived | no |
| Fork | no |
| Homepage | [http://hf.co/docs/trl](http://hf.co/docs/trl) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.22 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.92** |
| **trust_score** | **8.83** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 8,581 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug huggingface/trl
python3 scripts/generate-index/generate_repository_cards.py --category ai
```
