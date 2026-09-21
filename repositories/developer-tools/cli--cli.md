---
id: cli--cli
title: "cli/cli"
domain: developer-tools
summary: >-
  cli/cli — ACTIVE, tier A,
  46,353 stars, license MIT, quality 7.75/10, trust 6.73/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["cli", "developer-tools", "github", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 5.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.52, "reproducibility": 9.5, "security": 3.5, "recency": 9.97, "evidence": 7.0}
  quality_score: 7.75
  trust_score: 6.73
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "cli/cli on GitHub"
    url: https://github.com/cli/cli
    type: github-repository
    organization: cli
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# cli/cli

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> GitHub’s official command line tool

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/cli/cli> |
| Owner | cli (Organization) |
| Official upstream | no |
| Language | Go |
| License | `MIT` |
| Stars | 46,353 (checked 2026-09-21) |
| Forks | 9,058 |
| Open issues | 1,088 |
| Contributors | 381 |
| Last push | 2026-09-19 (2 days before verification) |
| Latest release | v2.101.0 (2026-09-15) |
| Archived | no |
| Fork | no |
| Homepage | [https://cli.github.com](https://cli.github.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.52 |
| reproducibility | 9.5 |
| security | 3.5 |
| recency | 9.97 |
| evidence | 7.0 |
| **quality_score** (weighted) | **7.75** |
| **trust_score** | **6.73** |

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
| contributing | no |
| root entries | yes |
| README size | 6,262 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug cli/cli
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
