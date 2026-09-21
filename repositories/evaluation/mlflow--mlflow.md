---
id: mlflow--mlflow
title: "mlflow/mlflow"
domain: evaluation
summary: >-
  mlflow/mlflow — ACTIVE, tier S,
  28,070 stars, license Apache-2.0, quality 8.63/10, trust 7.99/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["evaluation", "experiment-tracking", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.76, "reproducibility": 10.0, "security": 6.0, "recency": 10.0, "evidence": 8.5}
  quality_score: 8.63
  trust_score: 7.99
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "mlflow/mlflow on GitHub"
    url: https://github.com/mlflow/mlflow
    type: github-repository
    organization: mlflow
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

# mlflow/mlflow

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> The open source AI engineering platform for agents, LLMs, and ML models. MLflow enables teams of all sizes to debug, evaluate, monitor, and optimize production-quality AI applications while controlling costs and managing access to models and data.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/mlflow/mlflow> |
| Owner | mlflow (Organization) |
| Official upstream | no |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 28,070 (checked 2026-09-21) |
| Forks | 6,331 |
| Open issues | 2,116 |
| Contributors | 446 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v3.16.1 (2026-09-17) |
| Archived | no |
| Fork | no |
| Homepage | [https://mlflow.org](https://mlflow.org) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.76 |
| reproducibility | 10.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 8.5 |
| **quality_score** (weighted) | **8.63** |
| **trust_score** | **7.99** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 33,104 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug mlflow/mlflow
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
