---
id: nektos--act
title: "nektos/act"
domain: developer-tools
summary: >-
  nektos/act — STABLE, tier A,
  72,007 stars, license MIT, quality 7.58/10, trust 7.14/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["ci-cd", "developer-tools", "github-actions", "github-repository", "local"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 8.0, "adoption": 10.0, "documentation": 5.28, "reproducibility": 7.5, "security": 4.5, "recency": 9.51, "evidence": 5.0}
  quality_score: 7.58
  trust_score: 7.14
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "nektos/act on GitHub"
    url: https://github.com/nektos/act
    type: github-repository
    organization: nektos
    license: MIT
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# nektos/act

🔵 STABLE · tier **A** · production-grade · confidence **high**

> Run your GitHub Actions locally 🚀

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/nektos/act> |
| Owner | nektos (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `MIT` |
| Stars | 72,007 (checked 2026-09-15) |
| Forks | 2,033 |
| Open issues | 380 |
| Contributors | 202 |
| Last push | 2026-08-09 (36 days before verification) |
| Latest release | v0.2.89 (2026-06-01) |
| Archived | no |
| Fork | no |
| Homepage | https://nektosact.com |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 8.0 |
| adoption | 10.0 |
| documentation | 5.28 |
| reproducibility | 7.5 |
| security | 4.5 |
| recency | 9.51 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.58** |
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
| contributing | yes |
| root entries | yes |
| README size | 3,315 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug nektos/act
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
