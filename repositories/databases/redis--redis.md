---
id: redis--redis
title: "redis/redis"
domain: databases
summary: >-
  redis/redis — ACTIVE, tier A,
  76,370 stars, license NOASSERTION, quality 8.82/10, trust 8.86/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["cache", "databases", "github-repository", "kv"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.57, "reproducibility": 8.6, "security": 6.5, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.82
  trust_score: 8.86
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "redis/redis on GitHub"
    url: https://github.com/redis/redis
    type: github-repository
    organization: redis
    license: NOASSERTION
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# redis/redis

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> For developers, who are building real-time data-driven applications, Redis is the preferred, fastest, and most feature-rich cache, data structure server, and document and vector query engine.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/redis/redis> |
| Owner | redis (Organization) |
| Official upstream | yes |
| Language | C |
| License | `NOASSERTION` |
| Stars | 76,370 (checked 2026-09-15) |
| Forks | 24,807 |
| Open issues | 2,946 |
| Contributors | 382 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | 8.10.1 (2026-08-17) |
| Archived | no |
| Fork | no |
| Homepage | http://redis.io |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.57 |
| reproducibility | 8.6 |
| security | 6.5 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.82** |
| **trust_score** | **8.86** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 30,856 bytes |

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

Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug redis/redis
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
