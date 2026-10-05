---
id: graphql--graphql-spec
title: "graphql/graphql-spec"
domain: backend
summary: >-
  graphql/graphql-spec — ACTIVE, tier A,
  14,593 stars, license NOASSERTION, quality 8.54/10, trust 8.66/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["api", "backend", "github-repository", "specification"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.92, "reproducibility": 8.1, "security": 4.0, "recency": 9.92, "evidence": 7.5}
  quality_score: 8.54
  trust_score: 8.66
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "graphql/graphql-spec on GitHub"
    url: https://github.com/graphql/graphql-spec
    type: github-repository
    organization: graphql
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: very-high
    claim_type: fact
    verified_at: 2026-10-05
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-05)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# graphql/graphql-spec

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> GraphQL is a query language and execution engine tied to any backend service.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-10-05, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/graphql/graphql-spec> |
| Owner | graphql (Organization) |
| Official upstream | yes |
| Language | HTML |
| License | `NOASSERTION` |
| Stars | 14,593 (checked 2026-10-05) |
| Forks | 1,157 |
| Open issues | 193 |
| Contributors | 130 |
| Last push | 2026-09-28 (6 days before verification) |
| Latest release | September2025 (2025-09-04) |
| Archived | no |
| Fork | no |
| Homepage | [https://spec.graphql.org](https://spec.graphql.org) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `docs` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.92 |
| reproducibility | 8.1 |
| security | 4.0 |
| recency | 9.92 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.54** |
| **trust_score** | **8.66** |

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
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 29,093 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug graphql/graphql-spec
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
