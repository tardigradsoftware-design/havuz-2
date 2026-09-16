---
id: anomalyco--sst
title: "anomalyco/sst"
domain: developer-tools
summary: >-
  anomalyco/sst — STABLE, tier A,
  26,297 stars, license MIT, quality 7.01/10, trust 5.91/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["aws", "developer-tools", "github-repository", "iac", "serverless"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.5, "maintenance": 8.5, "adoption": 10.0, "documentation": 4.72, "reproducibility": 8.0, "security": 3.5, "recency": 9.12, "evidence": 6.0}
  quality_score: 7.01
  trust_score: 5.91
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "anomalyco/sst on GitHub"
    url: https://github.com/anomalyco/sst
    type: github-repository
    organization: anomalyco
    license: MIT
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# anomalyco/sst

🔵 STABLE · tier **A** · production-grade · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Build full-stack apps on your own infrastructure.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/anomalyco/sst> |
| Owner | anomalyco (Organization) |
| Official upstream | no |
| Language | TypeScript |
| License | `MIT` |
| Stars | 26,297 (checked 2026-09-15) |
| Forks | 2,118 |
| Open issues | 322 |
| Contributors | 290 |
| Last push | 2026-07-12 (64 days before verification) |
| Latest release | v4.17.1 (2026-07-12) |
| Archived | no |
| Fork | no |
| Homepage | [https://sst.dev](https://sst.dev) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 8.5 |
| adoption | 10.0 |
| documentation | 4.72 |
| reproducibility | 8.0 |
| security | 3.5 |
| recency | 9.12 |
| evidence | 6.0 |
| **quality_score** (weighted) | **7.01** |
| **trust_score** | **5.91** |

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
| examples | yes |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 2,644 bytes |

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

Repository moved: `sst/sst` -> `anomalyco/sst`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug anomalyco/sst
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
