---
id: openai--simple-evals
title: "openai/simple-evals"
domain: evaluation
summary: >-
  openai/simple-evals — MAINTENANCE, tier B,
  4,631 stars, license MIT, quality 6.16/10, trust 5.46/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["evaluation", "github-repository", "minimal"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 5.0, "adoption": 10.0, "documentation": 4.1, "reproducibility": 4.5, "security": 4.5, "recency": 8.01, "evidence": 2.0}
  quality_score: 6.16
  trust_score: 5.46
  tier: B
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "openai/simple-evals on GitHub"
    url: https://github.com/openai/simple-evals
    type: github-repository
    organization: openai
    license: MIT
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# openai/simple-evals

🟡 MAINTENANCE · tier **B** · maintenance-mode · confidence **medium**

> _No description published._

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/openai/simple-evals> |
| Owner | openai (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 4,631 (checked 2026-09-15) |
| Forks | 509 |
| Open issues | 62 |
| Contributors | 12 |
| Last push | 2026-04-22 (145 days before verification) |
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
| maintenance | 5.0 |
| adoption | 10.0 |
| documentation | 4.1 |
| reproducibility | 4.5 |
| security | 4.5 |
| recency | 8.01 |
| evidence | 2.0 |
| **quality_score** (weighted) | **6.16** |
| **trust_score** | **5.46** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 13,160 bytes |

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

No push in 145 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug openai/simple-evals
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
