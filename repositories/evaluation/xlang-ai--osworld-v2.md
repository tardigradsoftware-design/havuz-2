---
id: xlang-ai--osworld-v2
title: "xlang-ai/OSWorld-V2"
domain: evaluation
summary: >-
  xlang-ai/OSWorld-V2 — STABLE, tier S,
  324 stars, license Apache-2.0, quality 8.19/10, trust 8.33/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["benchmark", "computer-use", "evaluation", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 8.71, "documentation": 7.84, "reproducibility": 7.5, "security": 4.5, "recency": 9.95, "evidence": 6.0}
  quality_score: 8.19
  trust_score: 8.33
  tier: S
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "xlang-ai/OSWorld-V2 on GitHub"
    url: https://github.com/xlang-ai/OSWorld-V2
    type: github-repository
    organization: xlang-ai
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

# xlang-ai/OSWorld-V2

🔵 STABLE · tier **S** · published-artifact · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/xlang-ai/OSWorld-V2> |
| Owner | xlang-ai (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 324 (checked 2026-09-21) |
| Forks | 50 |
| Open issues | 22 |
| Contributors | 27 |
| Last push | 2026-09-16 (4 days before verification) |
| Latest release | osworld-v2.1 (2026-09-16) |
| Archived | no |
| Fork | no |
| Homepage | [https://osworld-v2.xlang.ai](https://osworld-v2.xlang.ai) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 8.71 |
| documentation | 7.84 |
| reproducibility | 7.5 |
| security | 4.5 |
| recency | 9.95 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.19** |
| **trust_score** | **8.33** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | yes |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 22,045 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug xlang-ai/OSWorld-V2
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
