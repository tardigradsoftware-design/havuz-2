---
id: calcom--cal.diy
title: "calcom/cal.diy"
domain: frontend
summary: >-
  calcom/cal.diy — ACTIVE, tier S,
  48,481 stars, license MIT, quality 9.15/10, trust 9.2/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["example", "frontend", "github-repository", "nextjs", "saas"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.5, "reproducibility": 9.5, "security": 7.0, "recency": 9.99, "evidence": 7.5}
  quality_score: 9.15
  trust_score: 9.2
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "calcom/cal.diy on GitHub"
    url: https://github.com/calcom/cal.diy
    type: github-repository
    organization: calcom
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

# calcom/cal.diy

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Scheduling infrastructure for absolutely everyone.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/calcom/cal.diy> |
| Owner | calcom (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 48,481 (checked 2026-09-15) |
| Forks | 15,132 |
| Open issues | 1,412 |
| Contributors | 436 |
| Last push | 2026-09-14 (1 days before verification) |
| Latest release | v6.2.0 (2026-03-01) |
| Archived | no |
| Fork | no |
| Homepage | [https://cal.diy](https://cal.diy) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.5 |
| reproducibility | 9.5 |
| security | 7.0 |
| recency | 9.99 |
| evidence | 7.5 |
| **quality_score** (weighted) | **9.15** |
| **trust_score** | **9.2** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 36,824 bytes |

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

Repository moved: `calcom/cal.com` -> `calcom/cal.diy`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug calcom/cal.diy
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
