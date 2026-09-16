---
id: mongodb--mongo
title: "mongodb/mongo"
domain: databases
summary: >-
  mongodb/mongo — ACTIVE, tier A,
  28,556 stars, license NOASSERTION, quality 7.76/10, trust 7.57/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["database", "databases", "document", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.47, "reproducibility": 5.1, "security": 4.0, "recency": 10.0, "evidence": 4.0}
  quality_score: 7.76
  trust_score: 7.57
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "mongodb/mongo on GitHub"
    url: https://github.com/mongodb/mongo
    type: github-repository
    organization: mongodb
    license: NOASSERTION
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# mongodb/mongo

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> The MongoDB Database

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/mongodb/mongo> |
| Owner | mongodb (Organization) |
| Official upstream | yes |
| Language | C++ |
| License | `NOASSERTION` |
| Stars | 28,556 (checked 2026-09-15) |
| Forks | 5,806 |
| Open issues | 34 |
| Contributors | 334 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | https://www.mongodb.com/ |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.47 |
| reproducibility | 5.1 |
| security | 4.0 |
| recency | 10.0 |
| evidence | 4.0 |
| **quality_score** (weighted) | **7.76** |
| **trust_score** | **7.57** |

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
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 17,692 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug mongodb/mongo
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
