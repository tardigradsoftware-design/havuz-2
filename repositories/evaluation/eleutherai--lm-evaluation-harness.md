---
id: eleutherai--lm-evaluation-harness
title: "EleutherAI/lm-evaluation-harness"
domain: evaluation
summary: >-
  EleutherAI/lm-evaluation-harness — ACTIVE, tier S,
  13,988 stars, license MIT, quality 8.9/10, trust 8.97/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["benchmark", "evaluation", "github-repository", "reproducible"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.0, "reproducibility": 10.0, "security": 4.5, "recency": 9.99, "evidence": 8.5}
  quality_score: 8.9
  trust_score: 8.97
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "EleutherAI/lm-evaluation-harness on GitHub"
    url: https://github.com/EleutherAI/lm-evaluation-harness
    type: github-repository
    organization: EleutherAI
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# EleutherAI/lm-evaluation-harness

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> A framework for few-shot evaluation of language models.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/EleutherAI/lm-evaluation-harness> |
| Owner | EleutherAI (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 13,988 (checked 2026-09-15) |
| Forks | 3,565 |
| Open issues | 976 |
| Contributors | 435 |
| Last push | 2026-09-14 (1 days before verification) |
| Latest release | v0.4.13 (2026-08-31) |
| Archived | no |
| Fork | no |
| Homepage | https://www.eleuther.ai |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.0 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 9.99 |
| evidence | 8.5 |
| **quality_score** (weighted) | **8.9** |
| **trust_score** | **8.97** |

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
| contributing | no |
| root entries | yes |
| README size | 60,912 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Reproducible few-shot evaluation across a large catalogue of benchmarks
- Comparing models on a common harness instead of vendor-reported numbers
- CI gates for model or prompt changes

**Not recommended for**

- Evaluating agent behaviour end-to-end (use an agent benchmark)
- Assuming a high score transfers to your task distribution

**Strengths**

- The de-facto standard open evaluation harness
- MIT, 435 contributors, release v0.4.13, pushed 1 day before verification
- Task definitions are declarative and inspectable

**Weaknesses**

- Benchmark contamination is a standing risk for older tasks
- Few-shot prompting results are sensitive to formatting

**Related projects**

- stanford-crfm/helm
- huggingface/lighteval
- open-compass/opencompass
- openai/simple-evals

## Verification notes

Verified 2026-09-15: ACTIVE, MIT, q=8.9.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug EleutherAI/lm-evaluation-harness
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
