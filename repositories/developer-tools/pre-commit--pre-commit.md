---
id: pre-commit--pre-commit
title: "pre-commit/pre-commit"
domain: developer-tools
summary: >-
  pre-commit/pre-commit — ACTIVE, tier S,
  15,607 stars, license MIT, quality 8.4/10, trust 8.23/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "git-hooks", "github-repository", "quality"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.54, "reproducibility": 9.0, "security": 4.5, "recency": 9.93, "evidence": 7.0}
  quality_score: 8.4
  trust_score: 8.23
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "pre-commit/pre-commit on GitHub"
    url: https://github.com/pre-commit/pre-commit
    type: github-repository
    organization: pre-commit
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-10-05
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-05)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# pre-commit/pre-commit

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A framework for managing and maintaining multi-language pre-commit hooks.

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/pre-commit/pre-commit> |
| Owner | pre-commit (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 15,607 (checked 2026-10-05) |
| Forks | 1,012 |
| Open issues | 25 |
| Contributors | 134 |
| Last push | 2026-09-29 (5 days before verification) |
| Latest release | v4.6.2 (2026-08-10) |
| Archived | no |
| Fork | no |
| Homepage | [https://pre-commit.com](https://pre-commit.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.54 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 9.93 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.4** |
| **trust_score** | **8.23** |

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
| contributing | yes |
| root entries | yes |
| README size | 480 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug pre-commit/pre-commit
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
