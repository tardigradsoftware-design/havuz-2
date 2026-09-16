---
id: prime-rl--prime
title: "PRIME-RL/PRIME"
domain: reasoning-research
summary: >-
  PRIME-RL/PRIME — STABLE, tier EXPERIMENTAL,
  1,873 stars, license Apache-2.0, quality 4.16/10, trust 2.89/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: low
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "reasoning", "reasoning-research", "rl", "training"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.0, "maintenance": 1.0, "adoption": 10.0, "documentation": 4.62, "reproducibility": 4.5, "security": 2.5, "recency": 2.52, "evidence": 1.0}
  quality_score: 4.16
  trust_score: 2.89
  tier: EXPERIMENTAL
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "PRIME-RL/PRIME on GitHub"
    url: https://github.com/PRIME-RL/PRIME
    type: github-repository
    organization: PRIME-RL
    license: Apache-2.0
    license_risk: none
    confidence: low
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# PRIME-RL/PRIME

🔵 STABLE · tier **EXPERIMENTAL** · published-artifact · confidence **low**

> _Upstream description, quoted as published and not verified here:_
>
> Scalable RL solution for advanced reasoning of language models

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/PRIME-RL/PRIME> |
| Owner | PRIME-RL (Organization) |
| Official upstream | no |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 1,873 (checked 2026-09-15) |
| Forks | 115 |
| Open issues | 10 |
| Contributors | 8 |
| Last push | 2025-03-18 (546 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `research-artifact` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 1.0 |
| adoption | 10.0 |
| documentation | 4.62 |
| reproducibility | 4.5 |
| security | 2.5 |
| recency | 2.52 |
| evidence | 1.0 |
| **quality_score** (weighted) | **4.16** |
| **trust_score** | **2.89** |

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
| README size | 13,449 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug PRIME-RL/PRIME
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
