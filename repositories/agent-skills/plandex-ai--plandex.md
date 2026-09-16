---
id: plandex-ai--plandex
title: "plandex-ai/plandex"
domain: agent-skills
summary: >-
  plandex-ai/plandex — MAINTENANCE, tier A,
  15,637 stars, license MIT, quality 7.02/10, trust 7.03/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "coding-agent", "github-repository", "terminal"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 3.0, "adoption": 10.0, "documentation": 6.9, "reproducibility": 9.0, "security": 4.5, "recency": 5.26, "evidence": 7.0}
  quality_score: 7.02
  trust_score: 7.03
  tier: A
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "plandex-ai/plandex on GitHub"
    url: https://github.com/plandex-ai/plandex
    type: github-repository
    organization: plandex-ai
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

# plandex-ai/plandex

🟡 MAINTENANCE · tier **A** · maintenance-mode · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Open source AI coding agent. Designed for large projects and real world tasks.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/plandex-ai/plandex> |
| Owner | plandex-ai (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `MIT` |
| Stars | 15,637 (checked 2026-09-15) |
| Forks | 1,175 |
| Open issues | 62 |
| Contributors | 22 |
| Last push | 2025-10-03 (346 days before verification) |
| Latest release | cli/v2.2.1 (2025-07-16) |
| Archived | no |
| Fork | no |
| Homepage | [https://plandex.ai](https://plandex.ai) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 3.0 |
| adoption | 10.0 |
| documentation | 6.9 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 5.26 |
| evidence | 7.0 |
| **quality_score** (weighted) | **7.02** |
| **trust_score** | **7.03** |

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
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 10,851 bytes |

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

No push in 346 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug plandex-ai/plandex
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
