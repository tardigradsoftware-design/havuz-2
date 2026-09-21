---
id: truera--trulens
title: "truera/trulens"
domain: evaluation
summary: >-
  truera/trulens — ACTIVE, tier S,
  3,568 stars, license MIT, quality 8.82/10, trust 8.8/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["evaluation", "github-repository", "observability"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.7, "reproducibility": 10.0, "security": 4.5, "recency": 10.0, "evidence": 8.0}
  quality_score: 8.82
  trust_score: 8.8
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "truera/trulens on GitHub"
    url: https://github.com/truera/trulens
    type: github-repository
    organization: truera
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

# truera/trulens

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Evaluation and Tracking for LLM Experiments and AI Agents

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/truera/trulens> |
| Owner | truera (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 3,568 (checked 2026-09-21) |
| Forks | 345 |
| Open issues | 72 |
| Contributors | 110 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | trulens-2.14.0 (2026-09-03) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.trulens.org/](https://www.trulens.org/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.7 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.82** |
| **trust_score** | **8.8** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 8,410 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug truera/trulens
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
