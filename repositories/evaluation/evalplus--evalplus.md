---
id: evalplus--evalplus
title: "evalplus/evalplus"
domain: evaluation
summary: >-
  evalplus/evalplus — STABLE, tier A,
  1,817 stars, license Apache-2.0, quality 7.17/10, trust 7.19/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["coding", "evaluation", "github-repository", "humaneval"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 3.5, "adoption": 10.0, "documentation": 7.27, "reproducibility": 9.5, "security": 4.5, "recency": 5.16, "evidence": 7.0}
  quality_score: 7.17
  trust_score: 7.19
  tier: A
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "evalplus/evalplus on GitHub"
    url: https://github.com/evalplus/evalplus
    type: github-repository
    organization: evalplus
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# evalplus/evalplus

🔵 STABLE · tier **A** · published-artifact · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Rigourous evaluation of LLM-synthesized code - NeurIPS 2023 & COLM 2024

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/evalplus/evalplus> |
| Owner | evalplus (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 1,817 (checked 2026-09-21) |
| Forks | 207 |
| Open issues | 76 |
| Contributors | 27 |
| Last push | 2025-10-02 (353 days before verification) |
| Latest release | v0.3.1 (2024-10-20) |
| Archived | no |
| Fork | no |
| Homepage | [https://evalplus.github.io](https://evalplus.github.io) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 3.5 |
| adoption | 10.0 |
| documentation | 7.27 |
| reproducibility | 9.5 |
| security | 4.5 |
| recency | 5.16 |
| evidence | 7.0 |
| **quality_score** (weighted) | **7.17** |
| **trust_score** | **7.19** |

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
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 15,259 bytes |

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

Reference implementation published with a benchmark. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug evalplus/evalplus
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
