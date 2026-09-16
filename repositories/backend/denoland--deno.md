---
id: denoland--deno
title: "denoland/deno"
domain: backend
summary: >-
  denoland/deno — ACTIVE, tier S,
  108,446 stars, license MIT, quality 8.28/10, trust 8.05/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["backend", "github-repository", "javascript", "runtime"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.32, "reproducibility": 9.0, "security": 4.5, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.28
  trust_score: 8.05
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "denoland/deno on GitHub"
    url: https://github.com/denoland/deno
    type: github-repository
    organization: denoland
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# denoland/deno

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> A modern runtime for JavaScript and TypeScript.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/denoland/deno> |
| Owner | denoland (Organization) |
| Official upstream | yes |
| Language | Rust |
| License | `MIT` |
| Stars | 108,446 (checked 2026-09-15) |
| Forks | 6,372 |
| Open issues | 1,586 |
| Contributors | 432 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v2.9.6 (2026-08-27) |
| Archived | no |
| Fork | no |
| Homepage | https://deno.com |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.32 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.28** |
| **trust_score** | **8.05** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | yes |
| examples | no |
| security md | no |
| changelog | yes |
| contributing | no |
| root entries | yes |
| README size | 3,807 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug denoland/deno
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
