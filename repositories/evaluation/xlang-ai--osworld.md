---
id: xlang-ai--osworld
title: "xlang-ai/OSWorld"
domain: evaluation
summary: >-
  xlang-ai/OSWorld — STABLE, tier S,
  3,143 stars, license Apache-2.0, quality 8.15/10, trust 7.92/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["benchmark", "computer-use", "evaluation", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.97, "reproducibility": 7.5, "security": 4.5, "recency": 10.0, "evidence": 5.5}
  quality_score: 8.15
  trust_score: 7.92
  tier: S
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "xlang-ai/OSWorld on GitHub"
    url: https://github.com/xlang-ai/OSWorld
    type: github-repository
    organization: xlang-ai
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# xlang-ai/OSWorld

🔵 STABLE · tier **S** · published-artifact · confidence **very-high**

> [NeurIPS 2024] OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/xlang-ai/OSWorld> |
| Owner | xlang-ai (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 3,143 (checked 2026-09-15) |
| Forks | 532 |
| Open issues | 201 |
| Contributors | 97 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | v0.1.16 (2024-06-26) |
| Archived | no |
| Fork | no |
| Homepage | https://os-world.github.io |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.97 |
| reproducibility | 7.5 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 5.5 |
| **quality_score** (weighted) | **8.15** |
| **trust_score** | **7.92** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 17,595 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug xlang-ai/OSWorld
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
