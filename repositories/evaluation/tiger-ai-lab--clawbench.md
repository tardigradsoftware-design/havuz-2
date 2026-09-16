---
id: tiger-ai-lab--clawbench
title: "TIGER-AI-Lab/ClawBench"
domain: evaluation
summary: >-
  TIGER-AI-Lab/ClawBench — STABLE, tier S,
  754 stars, license Apache-2.0, quality 8.14/10, trust 7.52/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["benchmark", "browser-agent", "evaluation", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 9.61, "documentation": 10.0, "reproducibility": 9.0, "security": 3.5, "recency": 9.99, "evidence": 7.5}
  quality_score: 8.14
  trust_score: 7.52
  tier: S
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "TIGER-AI-Lab/ClawBench on GitHub"
    url: https://github.com/TIGER-AI-Lab/ClawBench
    type: github-repository
    organization: TIGER-AI-Lab
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# TIGER-AI-Lab/ClawBench

🔵 STABLE · tier **S** · published-artifact · confidence **very-high**

> Open-source benchmark for browser AI agents on daily tasks.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/TIGER-AI-Lab/ClawBench> |
| Owner | TIGER-AI-Lab (Organization) |
| Official upstream | no |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 754 (checked 2026-09-15) |
| Forks | 57 |
| Open issues | 50 |
| Contributors | 12 |
| Last push | 2026-09-13 (1 days before verification) |
| Latest release | v0.10.0 (2026-08-30) |
| Archived | no |
| Fork | no |
| Homepage | https://claw-bench.com |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 9.61 |
| documentation | 10.0 |
| reproducibility | 9.0 |
| security | 3.5 |
| recency | 9.99 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.14** |
| **trust_score** | **7.52** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 72,273 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug TIGER-AI-Lab/ClawBench
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
