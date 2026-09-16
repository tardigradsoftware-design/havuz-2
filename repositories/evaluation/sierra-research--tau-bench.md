---
id: sierra-research--tau-bench
title: "sierra-research/tau-bench"
domain: evaluation
summary: >-
  sierra-research/tau-bench — STABLE, tier B,
  1,435 stars, license MIT, quality 6.12/10, trust 5.48/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "evaluation", "github-repository", "tool-use"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 5.0, "adoption": 10.0, "documentation": 4.2, "reproducibility": 4.5, "security": 4.5, "recency": 7.53, "evidence": 2.0}
  quality_score: 6.12
  trust_score: 5.48
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "sierra-research/tau-bench on GitHub"
    url: https://github.com/sierra-research/tau-bench
    type: github-repository
    organization: sierra-research
    license: MIT
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# sierra-research/tau-bench

🔵 STABLE · tier **B** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Code and Data for Tau-Bench

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/sierra-research/tau-bench> |
| Owner | sierra-research (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 1,435 (checked 2026-09-15) |
| Forks | 217 |
| Open issues | 53 |
| Contributors | 15 |
| Last push | 2026-03-18 (180 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 5.0 |
| adoption | 10.0 |
| documentation | 4.2 |
| reproducibility | 4.5 |
| security | 4.5 |
| recency | 7.53 |
| evidence | 2.0 |
| **quality_score** (weighted) | **6.12** |
| **trust_score** | **5.48** |

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
| README size | 8,447 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug sierra-research/tau-bench
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
