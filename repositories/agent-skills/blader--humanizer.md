---
id: blader--humanizer
title: "blader/humanizer"
domain: agent-skills
summary: >-
  blader/humanizer — ACTIVE, tier B,
  56,008 stars, license MIT, quality 6.99/10, trust 5.81/10.
  Verified against the GitHub API on 2026-10-12.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "ai-slop", "github-repository", "skills", "writing"]
version: 1.0.0
updated: 2026-10-12
verified_at: 2026-10-12
expires_at: 2026-11-26
scoring:
  components: {"authority": 5.0, "maintenance": 9.0, "adoption": 10.0, "documentation": 6.07, "reproducibility": 7.0, "security": 3.5, "recency": 9.81, "evidence": 5.0}
  quality_score: 6.99
  trust_score: 5.81
  tier: B
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-12
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "blader/humanizer on GitHub"
    url: https://github.com/blader/humanizer
    type: github-repository
    organization: blader
    license: MIT
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-10-12
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-12)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# blader/humanizer

🟢 ACTIVE · tier **B** · production-ready · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Agent skill that removes signs of AI-generated writing from text

## Facts (verified 2026-10-12 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/blader/humanizer> |
| Owner | blader (User) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 56,008 (checked 2026-10-12) |
| Forks | 4,427 |
| Open issues | 3 |
| Contributors | 21 |
| Last push | 2026-09-28 (14 days before verification) |
| Latest release | v3.1.0 (2026-09-28) |
| Archived | no |
| Fork | no |
| Homepage | [https://skills.sh/blader/humanizer](https://skills.sh/blader/humanizer) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 9.0 |
| adoption | 10.0 |
| documentation | 6.07 |
| reproducibility | 7.0 |
| security | 3.5 |
| recency | 9.81 |
| evidence | 5.0 |
| **quality_score** (weighted) | **6.99** |
| **trust_score** | **5.81** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | yes |
| examples | no |
| security md | no |
| changelog | yes |
| contributing | no |
| root entries | yes |
| README size | 12,884 bytes |

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

_No anomalies detected._

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug blader/humanizer
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
