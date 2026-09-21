---
id: tatsu-lab--alpaca_eval
title: "tatsu-lab/alpaca_eval"
domain: evaluation
summary: >-
  tatsu-lab/alpaca_eval — STABLE, tier A,
  2,015 stars, license Apache-2.0, quality 7.07/10, trust 7.32/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["evaluation", "github-repository", "instruction-following"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 1.5, "adoption": 10.0, "documentation": 9.0, "reproducibility": 10.0, "security": 3.5, "recency": 4.41, "evidence": 8.5}
  quality_score: 7.07
  trust_score: 7.32
  tier: A
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "tatsu-lab/alpaca_eval on GitHub"
    url: https://github.com/tatsu-lab/alpaca_eval
    type: github-repository
    organization: tatsu-lab
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

# tatsu-lab/alpaca_eval

🔵 STABLE · tier **A** · published-artifact · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> An automatic evaluator for instruction-following language models. Human-validated, high-quality, cheap, and fast.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/tatsu-lab/alpaca_eval> |
| Owner | tatsu-lab (Organization) |
| Official upstream | yes |
| Language | Jupyter Notebook |
| License | `Apache-2.0` |
| Stars | 2,015 (checked 2026-09-21) |
| Forks | 315 |
| Open issues | 35 |
| Contributors | 80 |
| Last push | 2025-08-09 (408 days before verification) |
| Latest release | v0.6.6 (2024-12-27) |
| Archived | no |
| Fork | no |
| Homepage | [https://tatsu-lab.github.io/alpaca_eval/](https://tatsu-lab.github.io/alpaca_eval/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 1.5 |
| adoption | 10.0 |
| documentation | 9.0 |
| reproducibility | 10.0 |
| security | 3.5 |
| recency | 4.41 |
| evidence | 8.5 |
| **quality_score** (weighted) | **7.07** |
| **trust_score** | **7.32** |

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
| README size | 84,471 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug tatsu-lab/alpaca_eval
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
