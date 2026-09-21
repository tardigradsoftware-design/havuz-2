---
id: web-arena-x--webarena
title: "web-arena-x/webarena"
domain: evaluation
summary: >-
  web-arena-x/webarena — STABLE, tier B,
  1,611 stars, license Apache-2.0, quality 6.82/10, trust 6.65/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["benchmark", "browser", "evaluation", "github-repository", "web-agent"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 3.0, "adoption": 10.0, "documentation": 5.31, "reproducibility": 9.0, "security": 4.5, "recency": 5.92, "evidence": 7.0}
  quality_score: 6.82
  trust_score: 6.65
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "web-arena-x/webarena on GitHub"
    url: https://github.com/web-arena-x/webarena
    type: github-repository
    organization: web-arena-x
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# web-arena-x/webarena

🔵 STABLE · tier **B** · published-artifact · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Code repo for "WebArena: A Realistic Web Environment for Building Autonomous Agents"

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/web-arena-x/webarena> |
| Owner | web-arena-x (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 1,611 (checked 2026-09-21) |
| Forks | 248 |
| Open issues | 103 |
| Contributors | 14 |
| Last push | 2025-11-26 (298 days before verification) |
| Latest release | v0.2.0 (2023-10-21) |
| Archived | no |
| Fork | no |
| Homepage | [https://webarena.dev](https://webarena.dev) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 3.0 |
| adoption | 10.0 |
| documentation | 5.31 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 5.92 |
| evidence | 7.0 |
| **quality_score** (weighted) | **6.82** |
| **trust_score** | **6.65** |

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
| README size | 9,717 bytes |

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

Reference implementation published with a benchmark. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug web-arena-x/webarena
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
