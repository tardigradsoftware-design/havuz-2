---
id: skyworkai--skywork-r1v
title: "SkyworkAI/Skywork-R1V"
domain: reasoning-research
summary: >-
  SkyworkAI/Skywork-R1V — STABLE, tier B,
  3,170 stars, license MIT, quality 6.25/10, trust 4.95/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "multimodal", "open-model", "reasoning", "reasoning-research"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 6.0, "maintenance": 7.0, "adoption": 10.0, "documentation": 5.17, "reproducibility": 4.5, "security": 3.5, "recency": 9.34, "evidence": 2.5}
  quality_score: 6.25
  trust_score: 4.95
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "SkyworkAI/Skywork-R1V on GitHub"
    url: https://github.com/SkyworkAI/Skywork-R1V
    type: github-repository
    organization: SkyworkAI
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

# SkyworkAI/Skywork-R1V

🔵 STABLE · tier **B** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Skywork-R1V is an advanced multimodal AI model series developed by Skywork AI, specializing in vision-language reasoning.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/SkyworkAI/Skywork-R1V> |
| Owner | SkyworkAI (Organization) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 3,170 (checked 2026-09-15) |
| Forks | 282 |
| Open issues | 36 |
| Contributors | 11 |
| Last push | 2026-07-29 (48 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://arxiv.org/abs/2504.05599](https://arxiv.org/abs/2504.05599) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `model-release` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 7.0 |
| adoption | 10.0 |
| documentation | 5.17 |
| reproducibility | 4.5 |
| security | 3.5 |
| recency | 9.34 |
| evidence | 2.5 |
| **quality_score** (weighted) | **6.25** |
| **trust_score** | **4.95** |

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
| README size | 8,046 bytes |

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

Reference implementation published with a model-release. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug SkyworkAI/Skywork-R1V
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
