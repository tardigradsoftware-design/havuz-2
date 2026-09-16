---
id: run-llama--llama_index
title: "run-llama/llama_index"
domain: agent-frameworks
summary: >-
  run-llama/llama_index — ACTIVE, tier S,
  52,168 stars, license MIT, quality 8.55/10, trust 8.34/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-frameworks", "data", "framework", "github-repository", "rag"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.96, "reproducibility": 7.5, "security": 7.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.55
  trust_score: 8.34
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "run-llama/llama_index on GitHub"
    url: https://github.com/run-llama/llama_index
    type: github-repository
    organization: run-llama
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# run-llama/llama_index

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> LlamaIndex is the document processing platform for AI

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/run-llama/llama_index> |
| Owner | run-llama (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 52,168 (checked 2026-09-15) |
| Forks | 8,146 |
| Open issues | 774 |
| Contributors | 476 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v0.14.24 (2026-08-19) |
| Archived | no |
| Fork | no |
| Homepage | https://developers.llamaindex.ai |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.96 |
| reproducibility | 7.5 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.55** |
| **trust_score** | **8.34** |

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
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 11,489 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug run-llama/llama_index
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
