---
id: bigcode-project--bigcode-evaluation-harness
title: "bigcode-project/bigcode-evaluation-harness"
domain: evaluation
summary: >-
  bigcode-project/bigcode-evaluation-harness — STABLE, tier B,
  1,062 stars, license Apache-2.0, quality 6.36/10, trust 6.18/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["benchmark", "coding", "evaluation", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 1.5, "adoption": 10.0, "documentation": 6.71, "reproducibility": 9.5, "security": 3.5, "recency": 4.18, "evidence": 6.5}
  quality_score: 6.36
  trust_score: 6.18
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "bigcode-project/bigcode-evaluation-harness on GitHub"
    url: https://github.com/bigcode-project/bigcode-evaluation-harness
    type: github-repository
    organization: bigcode-project
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

# bigcode-project/bigcode-evaluation-harness

🔵 STABLE · tier **B** · published-artifact · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> A framework for the evaluation of autoregressive code generation language models.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/bigcode-project/bigcode-evaluation-harness> |
| Owner | bigcode-project (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 1,062 (checked 2026-09-21) |
| Forks | 260 |
| Open issues | 97 |
| Contributors | 32 |
| Last push | 2025-07-22 (425 days before verification) |
| Latest release | v0.1.0 (2023-05-25) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 1.5 |
| adoption | 10.0 |
| documentation | 6.71 |
| reproducibility | 9.5 |
| security | 3.5 |
| recency | 4.18 |
| evidence | 6.5 |
| **quality_score** (weighted) | **6.36** |
| **trust_score** | **6.18** |

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
| contributing | yes |
| root entries | yes |
| README size | 14,543 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug bigcode-project/bigcode-evaluation-harness
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
