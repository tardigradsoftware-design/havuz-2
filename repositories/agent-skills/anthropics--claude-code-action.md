---
id: anthropics--claude-code-action
title: "anthropics/claude-code-action"
domain: agent-skills
summary: >-
  anthropics/claude-code-action — ACTIVE, tier S,
  8,876 stars, license MIT, quality 8.59/10, trust 8.29/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "ci", "coding-agent", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.41, "reproducibility": 10.0, "security": 7.0, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.59
  trust_score: 8.29
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "anthropics/claude-code-action on GitHub"
    url: https://github.com/anthropics/claude-code-action
    type: github-repository
    organization: anthropics
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

# anthropics/claude-code-action

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _No description published._

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/anthropics/claude-code-action> |
| Owner | anthropics (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 8,876 (checked 2026-09-15) |
| Forks | 2,141 |
| Open issues | 785 |
| Contributors | 136 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v1 (2025-08-26) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.41 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.59** |
| **trust_score** | **8.29** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 4,896 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug anthropics/claude-code-action
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
