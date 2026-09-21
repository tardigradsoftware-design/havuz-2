---
id: rolldown--rolldown
title: "rolldown/rolldown"
domain: frontend
summary: >-
  rolldown/rolldown — ACTIVE, tier S,
  13,951 stars, license MIT, quality 8.34/10, trust 8.11/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["build", "bundler", "frontend", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.42, "reproducibility": 8.5, "security": 4.5, "recency": 10.0, "evidence": 6.0}
  quality_score: 8.34
  trust_score: 8.11
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "rolldown/rolldown on GitHub"
    url: https://github.com/rolldown/rolldown
    type: github-repository
    organization: rolldown
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

# rolldown/rolldown

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Fast Rust bundler for JavaScript/TypeScript with Rollup-compatible API.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/rolldown/rolldown> |
| Owner | rolldown (Organization) |
| Official upstream | yes |
| Language | Rust |
| License | `MIT` |
| Stars | 13,951 (checked 2026-09-21) |
| Forks | 1,030 |
| Open issues | 420 |
| Contributors | 211 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v1.2.9 (2026-09-16) |
| Archived | no |
| Fork | no |
| Homepage | [https://rolldown.rs](https://rolldown.rs) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.42 |
| reproducibility | 8.5 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.34** |
| **trust_score** | **8.11** |

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
| examples | yes |
| security md | no |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 4,995 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug rolldown/rolldown
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
