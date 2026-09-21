---
id: anthropics--claude-cookbooks
title: "anthropics/claude-cookbooks"
domain: ai
summary: >-
  anthropics/claude-cookbooks — ACTIVE, tier A,
  52,861 stars, license MIT, quality 7.9/10, trust 7.4/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["ai", "anthropic", "examples", "github-repository", "prompting"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 4.51, "reproducibility": 8.5, "security": 4.5, "recency": 9.97, "evidence": 5.5}
  quality_score: 7.9
  trust_score: 7.4
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "anthropics/claude-cookbooks on GitHub"
    url: https://github.com/anthropics/claude-cookbooks
    type: github-repository
    organization: anthropics
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# anthropics/claude-cookbooks

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> A collection of notebooks/recipes showcasing some fun and effective ways of using Claude.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/anthropics/claude-cookbooks> |
| Owner | anthropics (Organization) |
| Official upstream | yes |
| Language | Jupyter Notebook |
| License | `MIT` |
| Stars | 52,861 (checked 2026-09-21) |
| Forks | 6,340 |
| Open issues | 339 |
| Contributors | 86 |
| Last push | 2026-09-18 (2 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 4.51 |
| reproducibility | 8.5 |
| security | 4.5 |
| recency | 9.97 |
| evidence | 5.5 |
| **quality_score** (weighted) | **7.9** |
| **trust_score** | **7.4** |

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
| contributing | yes |
| root entries | yes |
| README size | 6,083 bytes |

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

Repository moved: `anthropics/anthropic-cookbook` -> `anthropics/claude-cookbooks`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug anthropics/claude-cookbooks
python3 scripts/generate-index/generate_repository_cards.py --category ai
```
