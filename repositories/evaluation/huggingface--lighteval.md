---
id: huggingface--lighteval
title: "huggingface/lighteval"
domain: evaluation
summary: >-
  huggingface/lighteval — ACTIVE, tier S,
  2,541 stars, license MIT, quality 8.61/10, trust 8.51/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["benchmark", "evaluation", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.72, "reproducibility": 10.0, "security": 4.5, "recency": 9.92, "evidence": 8.0}
  quality_score: 8.61
  trust_score: 8.51
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "huggingface/lighteval on GitHub"
    url: https://github.com/huggingface/lighteval
    type: github-repository
    organization: huggingface
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# huggingface/lighteval

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Lighteval is your all-in-one toolkit for evaluating LLMs across multiple backends

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/huggingface/lighteval> |
| Owner | huggingface (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 2,541 (checked 2026-09-15) |
| Forks | 554 |
| Open issues | 409 |
| Contributors | 121 |
| Last push | 2026-09-09 (6 days before verification) |
| Latest release | v0.13.0 (2025-11-24) |
| Archived | no |
| Fork | no |
| Homepage | [https://huggingface.co/docs/lighteval/en/index](https://huggingface.co/docs/lighteval/en/index) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.72 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 9.92 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.61** |
| **trust_score** | **8.51** |

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
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 8,623 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug huggingface/lighteval
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
