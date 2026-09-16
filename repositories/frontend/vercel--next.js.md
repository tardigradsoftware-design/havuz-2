---
id: vercel--next.js
title: "vercel/next.js"
domain: frontend
summary: >-
  vercel/next.js — ACTIVE, tier S,
  142,318 stars, license MIT, quality 8.7/10, trust 8.62/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["framework", "frontend", "github-repository", "nextjs", "react"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.5, "reproducibility": 10.0, "security": 4.5, "recency": 10.0, "evidence": 8.0}
  quality_score: 8.7
  trust_score: 8.62
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "vercel/next.js on GitHub"
    url: https://github.com/vercel/next.js
    type: github-repository
    organization: vercel
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# vercel/next.js

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> The React Framework

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/vercel/next.js> |
| Owner | vercel (Organization) |
| Official upstream | yes |
| Language | JavaScript |
| License | `MIT` |
| Stars | 142,318 (checked 2026-09-15) |
| Forks | 31,907 |
| Open issues | 3,364 |
| Contributors | 422 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v16.3.5 (2026-09-11) |
| Archived | no |
| Fork | no |
| Homepage | https://nextjs.org |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.5 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.7** |
| **trust_score** | **8.62** |

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
| examples | yes |
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 23 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Production React applications needing SSR, SSG, ISR and API routes
- The default choice for AI-built SaaS dashboards and marketing sites in this knowledge base's target stack

**Not recommended for**

- Purely static single-page apps where Vite + React is simpler
- Teams that cannot accept a fast major-version cadence

**Strengths**

- 142k stars, MIT, pushed on the verification date
- App Router + Server Components + Server Actions cover most full-stack needs
- Deepest integration with the shadcn/ui and Tailwind ecosystem

**Weaknesses**

- Rapid change: App Router guidance from 2023-2024 is frequently wrong for current versions
- Caching semantics are the single most common source of AI-generated Next.js bugs

**Related projects**

- react/react
- shadcn-ui/ui
- tailwindlabs/tailwindcss
- vercel/ai
- vercel/turborepo

## Verification notes

Verified 2026-09-15. Because caching and Server Component rules change often, every Next.js claim in this knowledge base must carry a verified_at date.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug vercel/next.js
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
