---
id: deepseek-ai--deepseek-r1
title: "deepseek-ai/DeepSeek-R1"
domain: reasoning-research
summary: >-
  deepseek-ai/DeepSeek-R1 — STABLE, tier C,
  91,986 stars, license MIT, quality 5.66/10, trust 5.41/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "open-model", "reasoning", "reasoning-research", "rl"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 1.0, "adoption": 10.0, "documentation": 4.73, "reproducibility": 7.0, "security": 3.5, "recency": 3.9, "evidence": 5.0}
  quality_score: 5.66
  trust_score: 5.41
  tier: C
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "deepseek-ai/DeepSeek-R1 on GitHub"
    url: https://github.com/deepseek-ai/DeepSeek-R1
    type: github-repository
    organization: deepseek-ai
    license: MIT
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# deepseek-ai/DeepSeek-R1

🔵 STABLE · tier **C** · published-artifact · confidence **medium**

> _No description published._

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/deepseek-ai/DeepSeek-R1> |
| Owner | deepseek-ai (Organization) |
| Official upstream | yes |
| Language | — |
| License | `MIT` |
| Stars | 91,986 (checked 2026-09-15) |
| Forks | 11,681 |
| Open issues | 33 |
| Contributors | 12 |
| Last push | 2025-06-27 (445 days before verification) |
| Latest release | v1.0.0 (2025-06-27) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `model-release` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 1.0 |
| adoption | 10.0 |
| documentation | 4.73 |
| reproducibility | 7.0 |
| security | 3.5 |
| recency | 3.9 |
| evidence | 5.0 |
| **quality_score** (weighted) | **5.66** |
| **trust_score** | **5.41** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | yes |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 20,736 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Studying the published RL recipe for reasoning models
- Reading the technical report that accompanies the open checkpoints

**Not recommended for**

- Treating the repository as a maintained SDK
- Expecting bug fixes or security patches

**Strengths**

- MIT license on a frontier-class reasoning artifact
- Accompanied by a peer-reviewed paper (Nature 645:633-638, 2025)
- Very high adoption (92k stars verified)

**Weaknesses**

- No push in 445 days (verified 2026-09-15) - it is a publication, not a product
- Only 12 contributors

**Related projects**

- huggingface/open-r1
- volcengine/verl
- OpenRLHF/OpenRLHF
- QwenLM/Qwen3

## Verification notes

Reference implementation published with a model-release. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance. IMPORTANT CLASSIFICATION NOTE: a naive staleness rule labels this ABANDONED. It is not. It is a published research artifact whose value does not depend on commit activity. This repository carries repo_kind=model-release so the classifier reports STABLE. See knowledge/ai-engineering/repository-status.md. published research artifact

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug deepseek-ai/DeepSeek-R1
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
