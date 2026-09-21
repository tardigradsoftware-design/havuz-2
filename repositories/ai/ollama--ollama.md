---
id: ollama--ollama
title: "ollama/ollama"
domain: ai
summary: >-
  ollama/ollama — ACTIVE, tier S,
  181,355 stars, license MIT, quality 8.56/10, trust 8.36/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["ai", "github-repository", "inference", "local"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.1, "reproducibility": 7.5, "security": 7.0, "recency": 9.99, "evidence": 5.0}
  quality_score: 8.56
  trust_score: 8.36
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "ollama/ollama on GitHub"
    url: https://github.com/ollama/ollama
    type: github-repository
    organization: ollama
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# ollama/ollama

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/ollama/ollama> |
| Owner | ollama (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `MIT` |
| Stars | 181,355 (checked 2026-09-21) |
| Forks | 17,952 |
| Open issues | 4,045 |
| Contributors | 451 |
| Last push | 2026-09-19 (1 days before verification) |
| Latest release | v0.34.2 (2026-09-15) |
| Archived | no |
| Fork | no |
| Homepage | [https://ollama.com](https://ollama.com) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.1 |
| reproducibility | 7.5 |
| security | 7.0 |
| recency | 9.99 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.56** |
| **trust_score** | **8.36** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 19,225 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug ollama/ollama
python3 scripts/generate-index/generate_repository_cards.py --category ai
```
