---
id: vercel--chatbot
title: "vercel/chatbot"
domain: frontend
summary: >-
  vercel/chatbot — STABLE, tier A,
  20,995 stars, license NOASSERTION, quality 7.19/10, trust 6.92/10.
  Verified against the GitHub API on 2026-10-12.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["ai", "example", "frontend", "github-repository", "streaming"]
version: 1.0.0
updated: 2026-10-12
verified_at: 2026-10-12
expires_at: 2026-11-26
scoring:
  components: {"authority": 9.0, "maintenance": 5.5, "adoption": 10.0, "documentation": 4.8, "reproducibility": 7.1, "security": 4.0, "recency": 8.7, "evidence": 6.0}
  quality_score: 7.19
  trust_score: 6.92
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-12
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "vercel/chatbot on GitHub"
    url: https://github.com/vercel/chatbot
    type: github-repository
    organization: vercel
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: high
    claim_type: fact
    verified_at: 2026-10-12
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-12)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# vercel/chatbot

🔵 STABLE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> A full-featured, hackable Next.js AI chatbot built by Vercel

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-10-12, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-10-12 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/vercel/chatbot> |
| Owner | vercel (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `NOASSERTION` |
| Stars | 20,995 (checked 2026-10-12) |
| Forks | 6,755 |
| Open issues | 29 |
| Contributors | 75 |
| Last push | 2026-07-08 (95 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://chatbot.ai-sdk.dev](https://chatbot.ai-sdk.dev) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 5.5 |
| adoption | 10.0 |
| documentation | 4.8 |
| reproducibility | 7.1 |
| security | 4.0 |
| recency | 8.7 |
| evidence | 6.0 |
| **quality_score** (weighted) | **7.19** |
| **trust_score** | **6.92** |

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
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 3,575 bytes |

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

Repository moved: `vercel/ai-chatbot` -> `vercel/chatbot`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug vercel/chatbot
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
