---
id: actions--runner
title: "actions/runner"
domain: developer-tools
summary: >-
  actions/runner — ACTIVE, tier A,
  6,261 stars, license MIT, quality 7.97/10, trust 7.68/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["ci-cd", "developer-tools", "github-actions", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.22, "reproducibility": 7.0, "security": 4.5, "recency": 10.0, "evidence": 5.0}
  quality_score: 7.97
  trust_score: 7.68
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "actions/runner on GitHub"
    url: https://github.com/actions/runner
    type: github-repository
    organization: actions
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# actions/runner

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> The Runner for GitHub Actions :rocket:

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/actions/runner> |
| Owner | actions (Organization) |
| Official upstream | yes |
| Language | C# |
| License | `MIT` |
| Stars | 6,261 (checked 2026-09-15) |
| Forks | 1,426 |
| Open issues | 535 |
| Contributors | 168 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | v2.337.0 (2026-08-26) |
| Archived | no |
| Fork | no |
| Homepage | [https://github.com/features/actions](https://github.com/features/actions) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.22 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.97** |
| **trust_score** | **7.68** |

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
| README size | 2,621 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug actions/runner
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
