---
id: timescale--timescaledb
title: "timescale/timescaledb"
domain: databases
summary: >-
  timescale/timescaledb — ACTIVE, tier A,
  23,553 stars, license NOASSERTION, quality 8.82/10, trust 8.9/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["databases", "github-repository", "postgres", "timeseries"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.64, "reproducibility": 8.1, "security": 6.5, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.82
  trust_score: 8.9
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "timescale/timescaledb on GitHub"
    url: https://github.com/timescale/timescaledb
    type: github-repository
    organization: timescale
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

# timescale/timescaledb

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A time-series database for high-performance real-time analytics packaged as a Postgres extension

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/timescale/timescaledb> |
| Owner | timescale (Organization) |
| Official upstream | yes |
| Language | C |
| License | `NOASSERTION` |
| Stars | 23,553 (checked 2026-09-21) |
| Forks | 1,154 |
| Open issues | 393 |
| Contributors | 119 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | 2.30.1 (2026-09-17) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.tigerdata.com/](https://www.tigerdata.com/) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.64 |
| reproducibility | 8.1 |
| security | 6.5 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.82** |
| **trust_score** | **8.9** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 19,688 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug timescale/timescaledb
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
