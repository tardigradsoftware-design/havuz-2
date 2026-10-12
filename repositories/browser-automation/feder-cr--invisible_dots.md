---
id: feder-cr--invisible_dots
title: "feder-cr/invisible_dots"
domain: browser-automation
summary: >-
  feder-cr/invisible_dots — ACTIVE, tier A,
  31,980 stars, license MIT, quality 7.8/10, trust 6.65/10.
  Verified against the GitHub API on 2026-10-12.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["anti-detect", "browser", "browser-automation", "github-repository", "mcp"]
version: 1.0.0
updated: 2026-10-12
verified_at: 2026-10-12
expires_at: 2026-11-26
scoring:
  components: {"authority": 5.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.02, "reproducibility": 9.0, "security": 6.0, "recency": 10.0, "evidence": 6.0}
  quality_score: 7.8
  trust_score: 6.65
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-12
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "feder-cr/invisible_dots on GitHub"
    url: https://github.com/feder-cr/invisible_dots
    type: github-repository
    organization: feder-cr
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-10-12
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-12)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# feder-cr/invisible_dots

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Open-source, self-hosted alternative to OpenAI Dots, Grok Bot. Built to be undetectable by anti-bot systems.

## Facts (verified 2026-10-12 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/feder-cr/invisible_dots> |
| Owner | feder-cr (User) |
| Official upstream | no |
| Language | TypeScript |
| License | `MIT` |
| Stars | 31,980 (checked 2026-10-12) |
| Forks | 4,712 |
| Open issues | 0 |
| Contributors | — |
| Last push | 2026-10-12 (0 days before verification) |
| Latest release | golden-e0c6bb5c740a (2026-10-12) |
| Archived | no |
| Fork | no |
| Homepage | [https://github.com/feder-cr/invisible_dots/blob/main/docs/guide.md](https://github.com/feder-cr/invisible_dots/blob/main/docs/guide.md) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.02 |
| reproducibility | 9.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 6.0 |
| **quality_score** (weighted) | **7.8** |
| **trust_score** | **6.65** |

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
| README size | 6,280 bytes |

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

Repository moved: `feder-cr/AIHawk` -> `feder-cr/invisible_dots`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug feder-cr/invisible_dots
python3 scripts/generate-index/generate_repository_cards.py --category browser-automation
```
