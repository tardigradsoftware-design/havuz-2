---
id: apache--echarts
title: "apache/echarts"
domain: frontend
summary: >-
  apache/echarts — ACTIVE, tier S,
  67,363 stars, license Apache-2.0, quality 8.38/10, trust 8.2/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["charts", "frontend", "github-repository", "visualization"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.35, "reproducibility": 9.0, "security": 4.5, "recency": 9.93, "evidence": 7.0}
  quality_score: 8.38
  trust_score: 8.2
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "apache/echarts on GitHub"
    url: https://github.com/apache/echarts
    type: github-repository
    organization: apache
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

# apache/echarts

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Apache ECharts is a powerful, interactive charting and data visualization library for browser

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/apache/echarts> |
| Owner | apache (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 67,363 (checked 2026-09-21) |
| Forks | 19,819 |
| Open issues | 1,494 |
| Contributors | 274 |
| Last push | 2026-09-16 (5 days before verification) |
| Latest release | 6.1.0 (2026-05-19) |
| Archived | no |
| Fork | no |
| Homepage | [https://echarts.apache.org](https://echarts.apache.org) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.35 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 9.93 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.38** |
| **trust_score** | **8.2** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | yes |
| examples | no |
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 4,194 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug apache/echarts
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
