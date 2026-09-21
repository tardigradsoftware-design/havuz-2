---
id: vectifyai--pageindex
title: "VectifyAI/PageIndex"
domain: ai
summary: >-
  VectifyAI/PageIndex — ACTIVE, tier S,
  35,785 stars, license MIT, quality 8.06/10, trust 7.21/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["ai", "github-repository", "rag", "reasoning-based-retrieval"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.08, "reproducibility": 10.0, "security": 3.5, "recency": 10.0, "evidence": 8.0}
  quality_score: 8.06
  trust_score: 7.21
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "VectifyAI/PageIndex on GitHub"
    url: https://github.com/VectifyAI/PageIndex
    type: github-repository
    organization: VectifyAI
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# VectifyAI/PageIndex

🟢 ACTIVE · tier **S** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/VectifyAI/PageIndex> |
| Owner | VectifyAI (Organization) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 35,785 (checked 2026-09-21) |
| Forks | 3,153 |
| Open issues | 107 |
| Contributors | 16 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v0.2.19 (2026-09-21) |
| Archived | no |
| Fork | no |
| Homepage | [https://pageindex.ai](https://pageindex.ai) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.08 |
| reproducibility | 10.0 |
| security | 3.5 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.06** |
| **trust_score** | **7.21** |

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
| README size | 12,965 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug VectifyAI/PageIndex
python3 scripts/generate-index/generate_repository_cards.py --category ai
```
