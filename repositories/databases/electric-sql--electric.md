---
id: electric-sql--electric
title: "electric-sql/electric"
domain: databases
summary: >-
  electric-sql/electric — ACTIVE, tier S,
  10,367 stars, license Apache-2.0, quality 8.52/10, trust 8.37/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["databases", "github-repository", "local-first", "postgres", "sync"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 9.5, "adoption": 10.0, "documentation": 7.11, "reproducibility": 8.0, "security": 7.0, "recency": 9.85, "evidence": 6.0}
  quality_score: 8.52
  trust_score: 8.37
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "electric-sql/electric on GitHub"
    url: https://github.com/electric-sql/electric
    type: github-repository
    organization: electric-sql
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

# electric-sql/electric

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> The agent platform built on sync.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/electric-sql/electric> |
| Owner | electric-sql (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 10,367 (checked 2026-09-21) |
| Forks | 375 |
| Open issues | 257 |
| Contributors | 75 |
| Last push | 2026-09-09 (11 days before verification) |
| Latest release | @electric-sql/y-electric@0.1.54 (2026-09-09) |
| Archived | no |
| Fork | no |
| Homepage | [https://electric.ax](https://electric.ax) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 9.5 |
| adoption | 10.0 |
| documentation | 7.11 |
| reproducibility | 8.0 |
| security | 7.0 |
| recency | 9.85 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.52** |
| **trust_score** | **8.37** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 7,343 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug electric-sql/electric
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
