---
id: openrlhf--openrlhf
title: "OpenRLHF/OpenRLHF"
domain: reasoning-research
summary: >-
  OpenRLHF/OpenRLHF — ACTIVE, tier S,
  10,023 stars, license Apache-2.0, quality 9.04/10, trust 9.2/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "reasoning-research", "rl", "training"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.5, "reproducibility": 10.0, "security": 4.5, "recency": 9.95, "evidence": 8.5}
  quality_score: 9.04
  trust_score: 9.2
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "OpenRLHF/OpenRLHF on GitHub"
    url: https://github.com/OpenRLHF/OpenRLHF
    type: github-repository
    organization: OpenRLHF
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

# OpenRLHF/OpenRLHF

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> An Easy-to-use, Scalable and High-performance Agentic RL Framework based on Ray (PPO & DAPO & REINFORCE++ &  VLM & TIS & vLLM & Ray & Async  RL)

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/OpenRLHF/OpenRLHF> |
| Owner | OpenRLHF (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 10,023 (checked 2026-09-21) |
| Forks | 1,021 |
| Open issues | 384 |
| Contributors | 94 |
| Last push | 2026-09-17 (4 days before verification) |
| Latest release | v0.11.2 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | [https://openrlhf.readthedocs.io/](https://openrlhf.readthedocs.io/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.5 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 9.95 |
| evidence | 8.5 |
| **quality_score** (weighted) | **9.04** |
| **trust_score** | **9.2** |

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
| contributing | yes |
| root entries | yes |
| README size | 43,375 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug OpenRLHF/OpenRLHF
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
