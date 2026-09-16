---
id: google--adk-go
title: "google/adk-go"
domain: agent-frameworks
summary: >-
  google/adk-go — ACTIVE, tier S,
  8,793 stars, license Apache-2.0, quality 8.18/10, trust 7.95/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-frameworks", "github-repository", "go", "google"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.32, "reproducibility": 8.0, "security": 4.5, "recency": 10.0, "evidence": 6.0}
  quality_score: 8.18
  trust_score: 7.95
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "google/adk-go on GitHub"
    url: https://github.com/google/adk-go
    type: github-repository
    organization: google
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# google/adk-go

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/google/adk-go> |
| Owner | google (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 8,793 (checked 2026-09-15) |
| Forks | 1,007 |
| Open issues | 239 |
| Contributors | 102 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v2.4.0 (2026-09-11) |
| Archived | no |
| Fork | no |
| Homepage | https://google.github.io/adk-docs/ |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.32 |
| reproducibility | 8.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.18** |
| **trust_score** | **7.95** |

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
| examples | yes |
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 3,837 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug google/adk-go
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
