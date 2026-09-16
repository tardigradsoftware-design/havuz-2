---
id: suyoumo--clawprobench
title: "suyoumo/ClawProBench"
domain: evaluation
summary: >-
  suyoumo/ClawProBench — STABLE, tier A,
  823 stars, license Apache-2.0, quality 7.37/10, trust 6.21/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["benchmark", "evaluation", "github-repository", "live"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.0, "maintenance": 8.5, "adoption": 9.69, "documentation": 7.7, "reproducibility": 8.0, "security": 6.0, "recency": 9.71, "evidence": 5.0}
  quality_score: 7.37
  trust_score: 6.21
  tier: A
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "suyoumo/ClawProBench on GitHub"
    url: https://github.com/suyoumo/ClawProBench
    type: github-repository
    organization: suyoumo
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# suyoumo/ClawProBench

🔵 STABLE · tier **A** · published-artifact · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> ClawProBench is a live-first benchmark harness for evaluating LLM agents   in the OpenClaw runtime with deterministic grading and repeated-trial   reliability.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/suyoumo/ClawProBench> |
| Owner | suyoumo (User) |
| Official upstream | no |
| Language | Rust |
| License | `Apache-2.0` |
| Stars | 823 (checked 2026-09-15) |
| Forks | 54 |
| Open issues | 1 |
| Contributors | — |
| Last push | 2026-08-25 (21 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://suyoumo.github.io/bench/](https://suyoumo.github.io/bench/) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 8.5 |
| adoption | 9.69 |
| documentation | 7.7 |
| reproducibility | 8.0 |
| security | 6.0 |
| recency | 9.71 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.37** |
| **trust_score** | **6.21** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 14,379 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug suyoumo/ClawProBench
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
