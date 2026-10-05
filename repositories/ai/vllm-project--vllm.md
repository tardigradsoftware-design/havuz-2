---
id: vllm-project--vllm
title: "vllm-project/vllm"
domain: ai
summary: >-
  vllm-project/vllm — ACTIVE, tier S,
  93,203 stars, license Apache-2.0, quality 8.95/10, trust 8.87/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["ai", "github-repository", "inference", "performance", "serving"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.48, "reproducibility": 10.0, "security": 7.0, "recency": 10.0, "evidence": 8.0}
  quality_score: 8.95
  trust_score: 8.87
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "vllm-project/vllm on GitHub"
    url: https://github.com/vllm-project/vllm
    type: github-repository
    organization: vllm-project
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

# vllm-project/vllm

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A high-throughput and memory-efficient inference and serving engine for LLMs

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/vllm-project/vllm> |
| Owner | vllm-project (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 93,203 (checked 2026-10-05) |
| Forks | 23,010 |
| Open issues | 8,465 |
| Contributors | 453 |
| Last push | 2026-10-05 (0 days before verification) |
| Latest release | v0.31.0 (2026-10-05) |
| Archived | no |
| Fork | no |
| Homepage | [https://vllm.ai](https://vllm.ai) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.48 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.95** |
| **trust_score** | **8.87** |

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
| contributing | no |
| root entries | yes |
| README size | 5,708 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug vllm-project/vllm
python3 scripts/generate-index/generate_repository_cards.py --category ai
```
