---
id: changesets--changesets
title: "changesets/changesets"
domain: developer-tools
summary: >-
  changesets/changesets — ACTIVE, tier A,
  12,393 stars, license MIT, quality 7.96/10, trust 7.67/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "release", "versioning"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.13, "reproducibility": 7.0, "security": 4.5, "recency": 9.99, "evidence": 5.0}
  quality_score: 7.96
  trust_score: 7.67
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "changesets/changesets on GitHub"
    url: https://github.com/changesets/changesets
    type: github-repository
    organization: changesets
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

# changesets/changesets

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> 🦋 A tool to manage versioning and changelogs with a focus on monorepos

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/changesets/changesets> |
| Owner | changesets (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 12,393 (checked 2026-09-15) |
| Forks | 831 |
| Open issues | 256 |
| Contributors | 198 |
| Last push | 2026-09-14 (1 days before verification) |
| Latest release | @changesets/cli@3.0.3 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | [https://changesets.dev](https://changesets.dev) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.13 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 9.99 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.96** |
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
| contributing | no |
| root entries | yes |
| README size | 1,591 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug changesets/changesets
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
