---
id: upsonic--upsonic
title: "Upsonic/Upsonic"
domain: agent-frameworks
summary: >-
  Upsonic/Upsonic — STABLE, tier A,
  7,958 stars, license MIT, quality 7.25/10, trust 6.15/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-frameworks", "github-repository", "python"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 6.0, "maintenance": 5.5, "adoption": 10.0, "documentation": 5.99, "reproducibility": 9.5, "security": 6.0, "recency": 8.71, "evidence": 7.0}
  quality_score: 7.25
  trust_score: 6.15
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "Upsonic/Upsonic on GitHub"
    url: https://github.com/Upsonic/Upsonic
    type: github-repository
    organization: Upsonic
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

# Upsonic/Upsonic

🔵 STABLE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Build autonomous AI agents in Python.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/Upsonic/Upsonic> |
| Owner | Upsonic (Organization) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 7,958 (checked 2026-09-21) |
| Forks | 745 |
| Open issues | 33 |
| Contributors | 38 |
| Last push | 2026-06-18 (94 days before verification) |
| Latest release | v0.77.3 (2026-05-19) |
| Archived | no |
| Fork | no |
| Homepage | [https://docs.upsonic.ai](https://docs.upsonic.ai) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 5.5 |
| adoption | 10.0 |
| documentation | 5.99 |
| reproducibility | 9.5 |
| security | 6.0 |
| recency | 8.71 |
| evidence | 7.0 |
| **quality_score** (weighted) | **7.25** |
| **trust_score** | **6.15** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 5,938 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug Upsonic/Upsonic
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
