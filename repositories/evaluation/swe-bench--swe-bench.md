---
id: swe-bench--swe-bench
title: "SWE-bench/SWE-bench"
domain: evaluation
summary: >-
  SWE-bench/SWE-bench — STABLE, tier S,
  5,884 stars, license MIT, quality 8.31/10, trust 8.14/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "benchmark", "coding", "evaluation", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.61, "reproducibility": 8.0, "security": 4.5, "recency": 9.96, "evidence": 6.0}
  quality_score: 8.31
  trust_score: 8.14
  tier: S
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "SWE-bench/SWE-bench on GitHub"
    url: https://github.com/SWE-bench/SWE-bench
    type: github-repository
    organization: SWE-bench
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# SWE-bench/SWE-bench

🔵 STABLE · tier **S** · published-artifact · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> SWE-bench: Can Language Models Resolve Real-world Github Issues?

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/SWE-bench/SWE-bench> |
| Owner | SWE-bench (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 5,884 (checked 2026-09-21) |
| Forks | 975 |
| Open issues | 16 |
| Contributors | 68 |
| Last push | 2026-09-18 (3 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.swebench.com](https://www.swebench.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.61 |
| reproducibility | 8.0 |
| security | 4.5 |
| recency | 9.96 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.31** |
| **trust_score** | **8.14** |

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
| contributing | no |
| root entries | yes |
| README size | 13,302 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug SWE-bench/SWE-bench
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
