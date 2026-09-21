---
id: madaan--self-refine
title: "madaan/self-refine"
domain: reasoning-research
summary: >-
  madaan/self-refine — STABLE, tier C,
  822 stars, license Apache-2.0, quality 5.14/10, trust 5.19/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["critique", "github-repository", "paper-code", "reasoning", "reasoning-research"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 1.0, "adoption": 9.74, "documentation": 6.6, "reproducibility": 6.0, "security": 3.5, "recency": 0.19, "evidence": 3.0}
  quality_score: 5.14
  trust_score: 5.19
  tier: C
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "madaan/self-refine on GitHub"
    url: https://github.com/madaan/self-refine
    type: github-repository
    organization: madaan
    license: Apache-2.0
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# madaan/self-refine

🔵 STABLE · tier **C** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> LLMs can generate feedback on their work, use it to improve the output, and repeat this process iteratively.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/madaan/self-refine> |
| Owner | madaan (User) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 822 (checked 2026-09-21) |
| Forks | 70 |
| Open issues | 10 |
| Contributors | 5 |
| Last push | 2024-10-04 (716 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://selfrefine.info](https://selfrefine.info) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `research-artifact` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 1.0 |
| adoption | 9.74 |
| documentation | 6.6 |
| reproducibility | 6.0 |
| security | 3.5 |
| recency | 0.19 |
| evidence | 3.0 |
| **quality_score** (weighted) | **5.14** |
| **trust_score** | **5.19** |

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
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 7,178 bytes |

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

Reference implementation published with a research-artifact. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug madaan/self-refine
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
