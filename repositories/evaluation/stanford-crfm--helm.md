---
id: stanford-crfm--helm
title: "stanford-crfm/helm"
domain: evaluation
summary: >-
  stanford-crfm/helm — ACTIVE, tier A,
  2,909 stars, license Apache-2.0, quality 7.97/10, trust 7.72/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["benchmark", "evaluation", "github-repository", "methodology"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 9.5, "adoption": 10.0, "documentation": 7.1, "reproducibility": 7.0, "security": 4.5, "recency": 9.81, "evidence": 5.0}
  quality_score: 7.97
  trust_score: 7.72
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "stanford-crfm/helm on GitHub"
    url: https://github.com/stanford-crfm/helm
    type: github-repository
    organization: stanford-crfm
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# stanford-crfm/helm

🟢 ACTIVE · tier **A** · production-ready · confidence **very-high**

> Holistic Evaluation of Language Models (HELM) is an open source Python framework created by the Center for Research on Foundation Models (CRFM) at Stanford for holistic, reproducible and transparent evaluation of foundation models, including large language models (LLMs) and multimodal models.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/stanford-crfm/helm> |
| Owner | stanford-crfm (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 2,909 (checked 2026-09-15) |
| Forks | 414 |
| Open issues | 105 |
| Contributors | 130 |
| Last push | 2026-09-01 (14 days before verification) |
| Latest release | v0.5.16 (2026-04-30) |
| Archived | no |
| Fork | no |
| Homepage | https://crfm.stanford.edu/helm |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 9.5 |
| adoption | 10.0 |
| documentation | 7.1 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 9.81 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.97** |
| **trust_score** | **7.72** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | no |
| ci | yes |
| examples | no |
| security md | no |
| changelog | yes |
| contributing | no |
| root entries | yes |
| README size | 7,194 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Studying holistic evaluation methodology: multiple metrics across multiple scenarios
- Taxonomy of what to measure beyond accuracy (bias, toxicity, robustness, efficiency)
- Archival reference for benchmark design

**Not recommended for**

- Assuming the leaderboard reflects the current model landscape without checking the run date
- As a lightweight dependency - it is a large framework

**Strengths**

- Apache-2.0, from Stanford CRFM
- The methodology (scenario x metric x adaptation) is the most influential evaluation framing in the field
- Still receiving pushes (14 days before verification) with release v0.5.16

**Weaknesses**

- Only 2.9k stars relative to its influence - adoption as a *tool* is lower than as a *reference*
- Heavy to run end-to-end

**Related projects**

- EleutherAI/lm-evaluation-harness
- huggingface/lighteval
- crfm/...

## Verification notes

The brief expected HELM to be in maintenance mode by 2026. Verified 2026-09-15: the repository is NOT archived and was pushed 14 days before verification, so it is still active - but its role in this knowledge base is primarily methodological reference rather than day-to-day tooling. Recorded as a CONFLICT between the brief's expectation and the observed data; the observation wins.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug stanford-crfm/helm
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
