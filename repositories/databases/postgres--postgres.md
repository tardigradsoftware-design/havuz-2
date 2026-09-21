---
id: postgres--postgres
title: "postgres/postgres"
domain: databases
summary: >-
  postgres/postgres — ACTIVE, tier A,
  22,173 stars, license NOASSERTION, quality 7.52/10, trust 7.14/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["database", "databases", "github-repository", "postgres"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 4.58, "reproducibility": 5.6, "security": 4.0, "recency": 9.99, "evidence": 4.0}
  quality_score: 7.52
  trust_score: 7.14
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "postgres/postgres on GitHub"
    url: https://github.com/postgres/postgres
    type: github-repository
    organization: postgres
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# postgres/postgres

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Mirror of the official PostgreSQL GIT repository. Note that this is just a \*mirror\* - we don't work with pull requests on github. To contribute, please see `https://wiki.postgresql.org/wiki/Submitting_a_Patch`

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/postgres/postgres> |
| Owner | postgres (Organization) |
| Official upstream | yes |
| Language | C |
| License | `NOASSERTION` |
| Stars | 22,173 (checked 2026-09-21) |
| Forks | 5,922 |
| Open issues | 0 |
| Contributors | 42 |
| Last push | 2026-09-20 (1 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.postgresql.org/](https://www.postgresql.org/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 4.58 |
| reproducibility | 5.6 |
| security | 4.0 |
| recency | 9.99 |
| evidence | 4.0 |
| **quality_score** (weighted) | **7.52** |
| **trust_score** | **7.14** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | yes |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 989 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug postgres/postgres
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
