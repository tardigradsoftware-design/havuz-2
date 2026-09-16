---
id: stripe--ai
title: "stripe/ai"
domain: mcp-servers
summary: >-
  stripe/ai — ACTIVE, tier S,
  1,816 stars, license MIT, quality 8.42/10, trust 8.18/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "payments", "stripe"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.2, "reproducibility": 8.0, "security": 7.0, "recency": 10.0, "evidence": 6.0}
  quality_score: 8.42
  trust_score: 8.18
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "stripe/ai on GitHub"
    url: https://github.com/stripe/ai
    type: github-repository
    organization: stripe
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

# stripe/ai

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> One-stop shop for building AI-powered products and businesses with Stripe.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/stripe/ai> |
| Owner | stripe (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 1,816 (checked 2026-09-15) |
| Forks | 339 |
| Open issues | 87 |
| Contributors | 40 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://docs.stripe.com/agents](https://docs.stripe.com/agents) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.2 |
| reproducibility | 8.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.42** |
| **trust_score** | **8.18** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 2,402 bytes |

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

Repository moved: `stripe/agent-toolkit` -> `stripe/ai`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug stripe/ai
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
