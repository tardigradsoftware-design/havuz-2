---
id: openhands--openhands
title: "OpenHands/OpenHands"
domain: agent-skills
summary: >-
  OpenHands/OpenHands — ACTIVE, tier S,
  87,990 stars, license MIT, quality 8.08/10, trust 7.25/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "autonomous", "coding-agent", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.34, "reproducibility": 10.0, "security": 3.5, "recency": 10.0, "evidence": 8.0}
  quality_score: 8.08
  trust_score: 7.25
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "OpenHands/OpenHands on GitHub"
    url: https://github.com/OpenHands/OpenHands
    type: github-repository
    organization: OpenHands
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

# OpenHands/OpenHands

🟢 ACTIVE · tier **S** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> 🙌 OpenHands: AI-Driven Development

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/OpenHands/OpenHands> |
| Owner | OpenHands (Organization) |
| Official upstream | no |
| Language | TypeScript |
| License | `MIT` |
| Stars | 87,990 (checked 2026-09-15) |
| Forks | 11,536 |
| Open issues | 789 |
| Contributors | 460 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v1.18.0 (2026-09-11) |
| Archived | no |
| Fork | no |
| Homepage | [https://openhands.dev](https://openhands.dev) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.34 |
| reproducibility | 10.0 |
| security | 3.5 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.08** |
| **trust_score** | **7.25** |

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
| changelog | yes |
| contributing | no |
| root entries | yes |
| README size | 10,126 bytes |

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

Repository moved: `All-Hands-AI/OpenHands` -> `OpenHands/OpenHands`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug OpenHands/OpenHands
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
