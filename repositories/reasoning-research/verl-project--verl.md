---
id: verl-project--verl
title: "verl-project/verl"
domain: reasoning-research
summary: >-
  verl-project/verl — ACTIVE, tier S,
  23,513 stars, license Apache-2.0, quality 8.25/10, trust 7.55/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "reasoning", "reasoning-research", "rl", "training"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 5.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.5, "reproducibility": 10.0, "security": 3.5, "recency": 10.0, "evidence": 8.5}
  quality_score: 8.25
  trust_score: 7.55
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "verl-project/verl on GitHub"
    url: https://github.com/verl-project/verl
    type: github-repository
    organization: verl-project
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# verl-project/verl

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/verl-project/verl> |
| Owner | verl-project (Organization) |
| Official upstream | no |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 23,513 (checked 2026-09-21) |
| Forks | 4,567 |
| Open issues | 1,250 |
| Contributors | 445 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v0.9.1 (2026-09-20) |
| Archived | no |
| Fork | no |
| Homepage | [https://verl-project.github.io](https://verl-project.github.io) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.5 |
| reproducibility | 10.0 |
| security | 3.5 |
| recency | 10.0 |
| evidence | 8.5 |
| **quality_score** (weighted) | **8.25** |
| **trust_score** | **7.55** |

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
| contributing | yes |
| root entries | yes |
| README size | 39,437 bytes |

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

Repository moved: `volcengine/verl` -> `verl-project/verl`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug verl-project/verl
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
