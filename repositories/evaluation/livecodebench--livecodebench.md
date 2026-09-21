---
id: livecodebench--livecodebench
title: "LiveCodeBench/LiveCodeBench"
domain: evaluation
summary: >-
  LiveCodeBench/LiveCodeBench — STABLE, tier C,
  950 stars, license MIT, quality 5.47/10, trust 5.21/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["coding", "contamination-free", "evaluation", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 1.0, "adoption": 10.0, "documentation": 5.57, "reproducibility": 4.5, "security": 3.5, "recency": 4.08, "evidence": 2.5}
  quality_score: 5.47
  trust_score: 5.21
  tier: C
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "LiveCodeBench/LiveCodeBench on GitHub"
    url: https://github.com/LiveCodeBench/LiveCodeBench
    type: github-repository
    organization: LiveCodeBench
    license: MIT
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# LiveCodeBench/LiveCodeBench

🔵 STABLE · tier **C** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Official repository for the paper "LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code"

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/LiveCodeBench/LiveCodeBench> |
| Owner | LiveCodeBench (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 950 (checked 2026-09-21) |
| Forks | 203 |
| Open issues | 46 |
| Contributors | 16 |
| Last push | 2025-07-16 (432 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://livecodebench.github.io/](https://livecodebench.github.io/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 1.0 |
| adoption | 10.0 |
| documentation | 5.57 |
| reproducibility | 4.5 |
| security | 3.5 |
| recency | 4.08 |
| evidence | 2.5 |
| **quality_score** (weighted) | **5.47** |
| **trust_score** | **5.21** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 12,825 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug LiveCodeBench/LiveCodeBench
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
