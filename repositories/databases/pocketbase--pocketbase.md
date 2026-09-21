---
id: pocketbase--pocketbase
title: "pocketbase/pocketbase"
domain: databases
summary: >-
  pocketbase/pocketbase — ACTIVE, tier S,
  61,120 stars, license MIT, quality 8.56/10, trust 8.41/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["baas", "databases", "github-repository", "go", "sqlite"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.08, "reproducibility": 10.0, "security": 4.5, "recency": 10.0, "evidence": 8.0}
  quality_score: 8.56
  trust_score: 8.41
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "pocketbase/pocketbase on GitHub"
    url: https://github.com/pocketbase/pocketbase
    type: github-repository
    organization: pocketbase
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

# pocketbase/pocketbase

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Open Source realtime backend in 1 file

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/pocketbase/pocketbase> |
| Owner | pocketbase (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `MIT` |
| Stars | 61,120 (checked 2026-09-21) |
| Forks | 3,693 |
| Open issues | 19 |
| Contributors | 44 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v0.40.4 (2026-09-12) |
| Archived | no |
| Fork | no |
| Homepage | [https://pocketbase.io](https://pocketbase.io) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.08 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.56** |
| **trust_score** | **8.41** |

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
| examples | yes |
| security md | no |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 6,992 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug pocketbase/pocketbase
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
