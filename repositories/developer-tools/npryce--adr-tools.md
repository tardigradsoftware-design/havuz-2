---
id: npryce--adr-tools
title: "npryce/adr-tools"
domain: developer-tools
summary: >-
  npryce/adr-tools — ABANDONED, tier C,
  5,687 stars, license NOASSERTION, quality 4.92/10, trust 4.9/10.
  Verified against the GitHub API on 2026-09-15.
status: deprecated
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["architecture", "decision-records", "developer-tools", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 7.0, "maintenance": 1.0, "adoption": 10.0, "documentation": 3.65, "reproducibility": 7.1, "security": 3.0, "recency": 0.0, "evidence": 5.0}
  quality_score: 4.92
  trust_score: 4.9
  tier: C
  maturity: end-of-life
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "npryce/adr-tools on GitHub"
    url: https://github.com/npryce/adr-tools
    type: github-repository
    organization: npryce
    license: NOASSERTION
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# npryce/adr-tools

🔴 ABANDONED · tier **C** · end-of-life · confidence **medium**

> Command-line tools for working with Architecture Decision Records

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/npryce/adr-tools> |
| Owner | npryce (User) |
| Official upstream | yes |
| Language | Shell |
| License | `NOASSERTION` |
| Stars | 5,687 (checked 2026-09-15) |
| Forks | 634 |
| Open issues | 69 |
| Contributors | 13 |
| Last push | 2024-04-25 (872 days before verification) |
| Latest release | 3.0.0 (2018-07-25) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 7.0 |
| maintenance | 1.0 |
| adoption | 10.0 |
| documentation | 3.65 |
| reproducibility | 7.1 |
| security | 3.0 |
| recency | 0.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **4.92** |
| **trust_score** | **4.9** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 1,832 bytes |

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

No push in 872 days (>365d). Likely abandoned; prefer an actively maintained alternative. Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug npryce/adr-tools
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
