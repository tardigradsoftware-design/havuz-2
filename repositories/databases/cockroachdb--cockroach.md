---
id: cockroachdb--cockroach
title: "cockroachdb/cockroach"
domain: databases
summary: >-
  cockroachdb/cockroach — ACTIVE, tier A,
  32,481 stars, license NOASSERTION, quality 7.82/10, trust 7.67/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["databases", "distributed", "github-repository", "sql"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.12, "reproducibility": 5.1, "security": 4.0, "recency": 9.95, "evidence": 4.0}
  quality_score: 7.82
  trust_score: 7.67
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "cockroachdb/cockroach on GitHub"
    url: https://github.com/cockroachdb/cockroach
    type: github-repository
    organization: cockroachdb
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

# cockroachdb/cockroach

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> CockroachDB — the cloud native, distributed SQL database designed for high availability, effortless scale, and control over data placement.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/cockroachdb/cockroach> |
| Owner | cockroachdb (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `NOASSERTION` |
| Stars | 32,481 (checked 2026-09-21) |
| Forks | 4,111 |
| Open issues | 8,466 |
| Contributors | 306 |
| Last push | 2026-09-16 (4 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.cockroachlabs.com](https://www.cockroachlabs.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.12 |
| reproducibility | 5.1 |
| security | 4.0 |
| recency | 9.95 |
| evidence | 4.0 |
| **quality_score** (weighted) | **7.82** |
| **trust_score** | **7.67** |

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
| contributing | yes |
| root entries | yes |
| README size | 7,431 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug cockroachdb/cockroach
python3 scripts/generate-index/generate_repository_cards.py --category databases
```
