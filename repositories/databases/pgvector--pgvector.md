---
id: pgvector--pgvector
title: "pgvector/pgvector"
domain: databases
summary: >-
  pgvector/pgvector — ACTIVE, tier A,
  23,113 stars, license NOASSERTION, quality 7.82/10, trust 7.55/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["databases", "github-repository", "postgres", "rag", "vector"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 8.5, "adoption": 10.0, "documentation": 7.0, "reproducibility": 7.6, "security": 4.0, "recency": 9.86, "evidence": 6.0}
  quality_score: 7.82
  trust_score: 7.55
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "pgvector/pgvector on GitHub"
    url: https://github.com/pgvector/pgvector
    type: github-repository
    organization: pgvector
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# pgvector/pgvector

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Open-source vector similarity search for Postgres

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/pgvector/pgvector> |
| Owner | pgvector (Organization) |
| Official upstream | yes |
| Language | C |
| License | `NOASSERTION` |
| Stars | 23,113 (checked 2026-09-21) |
| Forks | 1,329 |
| Open issues | 16 |
| Contributors | 23 |
| Last push | 2026-09-10 (10 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 8.5 |
| adoption | 10.0 |
| documentation | 7.0 |
| reproducibility | 7.6 |
| security | 4.0 |
| recency | 9.86 |
| evidence | 6.0 |
| **quality_score** (weighted) | **7.82** |
| **trust_score** | **7.55** |

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
| README size | 42,305 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug pgvector/pgvector
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
