---
id: gitleaks--gitleaks
title: "gitleaks/gitleaks"
domain: developer-tools
summary: >-
  gitleaks/gitleaks — ACTIVE, tier S,
  29,320 stars, license MIT, quality 8.69/10, trust 8.62/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "secrets", "security"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.94, "reproducibility": 7.5, "security": 7.0, "recency": 9.92, "evidence": 5.5}
  quality_score: 8.69
  trust_score: 8.62
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "gitleaks/gitleaks on GitHub"
    url: https://github.com/gitleaks/gitleaks
    type: github-repository
    organization: gitleaks
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# gitleaks/gitleaks

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> Find secrets with Gitleaks 🔑

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/gitleaks/gitleaks> |
| Owner | gitleaks (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `MIT` |
| Stars | 29,320 (checked 2026-09-15) |
| Forks | 2,236 |
| Open issues | 480 |
| Contributors | 211 |
| Last push | 2026-09-09 (6 days before verification) |
| Latest release | v8.30.1 (2026-03-21) |
| Archived | no |
| Fork | no |
| Homepage | https://gitleaks.io |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.94 |
| reproducibility | 7.5 |
| security | 7.0 |
| recency | 9.92 |
| evidence | 5.5 |
| **quality_score** (weighted) | **8.69** |
| **trust_score** | **8.62** |

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
| examples | no |
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 29,328 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug gitleaks/gitleaks
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
