---
id: prime-rl--ttrl
title: "PRIME-RL/TTRL"
domain: reasoning-research
summary: >-
  PRIME-RL/TTRL — STABLE, tier C,
  1,123 stars, license MIT, quality 5.79/10, trust 4.38/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "reasoning", "reasoning-research", "test-time-rl"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.5, "maintenance": 5.0, "adoption": 10.0, "documentation": 5.03, "reproducibility": 5.5, "security": 3.5, "recency": 7.9, "evidence": 2.5}
  quality_score: 5.79
  trust_score: 4.38
  tier: C
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "PRIME-RL/TTRL on GitHub"
    url: https://github.com/PRIME-RL/TTRL
    type: github-repository
    organization: PRIME-RL
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

# PRIME-RL/TTRL

🔵 STABLE · tier **C** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> \[NeurIPS 2025\] TTRL: Test-Time Reinforcement Learning

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/PRIME-RL/TTRL> |
| Owner | PRIME-RL (Organization) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 1,123 (checked 2026-09-15) |
| Forks | 81 |
| Open issues | 17 |
| Contributors | 5 |
| Last push | 2026-04-15 (153 days before verification) |
| Latest release | verl (2025-07-11) |
| Archived | no |
| Fork | no |
| Homepage | [https://arxiv.org/abs/2504.16084](https://arxiv.org/abs/2504.16084) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `research-artifact` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 5.0 |
| adoption | 10.0 |
| documentation | 5.03 |
| reproducibility | 5.5 |
| security | 3.5 |
| recency | 7.9 |
| evidence | 2.5 |
| **quality_score** (weighted) | **5.79** |
| **trust_score** | **4.38** |

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
| README size | 6,402 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug PRIME-RL/TTRL
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
