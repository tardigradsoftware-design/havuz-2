---
id: react--react
title: "react/react"
domain: frontend
summary: >-
  react/react — ACTIVE, tier A,
  250,456 stars, license MIT, quality 7.74/10, trust 6.77/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["frontend", "github-repository", "react", "ui"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.44, "reproducibility": 7.0, "security": 6.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 7.74
  trust_score: 6.77
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "react/react on GitHub"
    url: https://github.com/react/react
    type: github-repository
    organization: react
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# react/react

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> The library for web and native user interfaces.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/react/react> |
| Owner | react (Organization) |
| Official upstream | no |
| Language | JavaScript |
| License | `MIT` |
| Stars | 250,456 (checked 2026-09-15) |
| Forks | 51,345 |
| Open issues | 1,370 |
| Contributors | 411 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v19.3.0 (2026-09-09) |
| Archived | no |
| Fork | no |
| Homepage | [https://react.dev](https://react.dev) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.44 |
| reproducibility | 7.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.74** |
| **trust_score** | **6.77** |

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
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 5,317 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- All React work
- Checking current behaviour against the canonical implementation

**Not recommended for**

- Citing the old facebook/react URL in new documentation - it redirects today but will not forever

**Strengths**

- 250k stars, MIT, the canonical implementation
- Pushed on the verification date

**Weaknesses**

- The repository moved from facebook/react to react/react; hard-coded URLs in older content are now stale

**Related projects**

- vercel/next.js
- vitejs/vite
- TanStack/query

## Verification notes

Repository moved: `facebook/react` -> `react/react`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. Verified 2026-09-15: the seed slug facebook/react returned HTTP 301 and resolved to react/react. This is exactly the kind of move that silently breaks agent knowledge bases.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug react/react
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
