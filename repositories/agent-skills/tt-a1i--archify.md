---
id: tt-a1i--archify
title: "tt-a1i/archify"
domain: agent-skills
summary: >-
  tt-a1i/archify — ACTIVE, tier A,
  63,151 stars, license MIT, quality 7.92/10, trust 7.03/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "architecture", "diagrams", "github-repository", "skills"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.71, "reproducibility": 8.0, "security": 6.0, "recency": 10.0, "evidence": 6.5}
  quality_score: 7.92
  trust_score: 7.03
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "tt-a1i/archify on GitHub"
    url: https://github.com/tt-a1i/archify
    type: github-repository
    organization: tt-a1i
    license: MIT
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# tt-a1i/archify

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/tt-a1i/archify> |
| Owner | tt-a1i (User) |
| Official upstream | no |
| Language | JavaScript |
| License | `MIT` |
| Stars | 63,151 (checked 2026-09-15) |
| Forks | 4,194 |
| Open issues | 171 |
| Contributors | 29 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v2.16.0 (2026-08-30) |
| Archived | no |
| Fork | no |
| Homepage | https://tt-a1i.github.io/archify/ |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.71 |
| reproducibility | 8.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 6.5 |
| **quality_score** (weighted) | **7.92** |
| **trust_score** | **7.03** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | no |
| ci | yes |
| examples | yes |
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 20,534 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug tt-a1i/archify
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
