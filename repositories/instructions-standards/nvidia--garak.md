---
id: nvidia--garak
title: "NVIDIA/garak"
domain: instructions-standards
summary: >-
  NVIDIA/garak — ACTIVE, tier S,
  9,252 stars, license Apache-2.0, quality 8.96/10, trust 9.0/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "instructions-standards", "llm-security", "red-team"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.18, "reproducibility": 9.0, "security": 7.0, "recency": 9.93, "evidence": 7.5}
  quality_score: 8.96
  trust_score: 9.0
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "NVIDIA/garak on GitHub"
    url: https://github.com/NVIDIA/garak
    type: github-repository
    organization: NVIDIA
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# NVIDIA/garak

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> the LLM vulnerability scanner

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/NVIDIA/garak> |
| Owner | NVIDIA (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 9,252 (checked 2026-09-15) |
| Forks | 1,278 |
| Open issues | 429 |
| Contributors | 129 |
| Last push | 2026-09-09 (5 days before verification) |
| Latest release | v0.17.0 (2026-09-09) |
| Archived | no |
| Fork | no |
| Homepage | [https://discord.gg/uVch4puUCs](https://discord.gg/uVch4puUCs) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.18 |
| reproducibility | 9.0 |
| security | 7.0 |
| recency | 9.93 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.96** |
| **trust_score** | **9.0** |

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
| README size | 20,123 bytes |

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

_No anomalies detected._

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug NVIDIA/garak
python3 scripts/generate-index/generate_repository_cards.py --category instructions-standards
```
