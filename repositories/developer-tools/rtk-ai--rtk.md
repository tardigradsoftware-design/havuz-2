---
id: rtk-ai--rtk
title: "rtk-ai/rtk"
domain: developer-tools
summary: >-
  rtk-ai/rtk — ACTIVE, tier S,
  81,218 stars, license Apache-2.0, quality 8.38/10, trust 7.66/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["context-compression", "developer-tools", "github-repository", "proxy", "tokens"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.25, "reproducibility": 9.0, "security": 6.0, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.38
  trust_score: 7.66
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "rtk-ai/rtk on GitHub"
    url: https://github.com/rtk-ai/rtk
    type: github-repository
    organization: rtk-ai
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

# rtk-ai/rtk

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/rtk-ai/rtk> |
| Owner | rtk-ai (Organization) |
| Official upstream | no |
| Language | Rust |
| License | `Apache-2.0` |
| Stars | 81,218 (checked 2026-09-21) |
| Forks | 5,147 |
| Open issues | 1,542 |
| Contributors | 149 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v0.49.0 (2026-09-11) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.rtk-ai.app](https://www.rtk-ai.app) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.25 |
| reproducibility | 9.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.38** |
| **trust_score** | **7.66** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 26,993 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug rtk-ai/rtk
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
