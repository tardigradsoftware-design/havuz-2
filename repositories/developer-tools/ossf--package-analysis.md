---
id: ossf--package-analysis
title: "ossf/package-analysis"
domain: developer-tools
summary: >-
  ossf/package-analysis — ACTIVE, tier S,
  913 stars, license Apache-2.0, quality 8.4/10, trust 8.08/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "security", "supply-chain"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 8.5, "adoption": 9.86, "documentation": 6.06, "reproducibility": 10.0, "security": 7.0, "recency": 9.86, "evidence": 7.5}
  quality_score: 8.4
  trust_score: 8.08
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "ossf/package-analysis on GitHub"
    url: https://github.com/ossf/package-analysis
    type: github-repository
    organization: ossf
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# ossf/package-analysis

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> Open Source Package Analysis

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/ossf/package-analysis> |
| Owner | ossf (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 913 (checked 2026-09-15) |
| Forks | 74 |
| Open issues | 85 |
| Contributors | 23 |
| Last push | 2026-09-04 (10 days before verification) |
| Latest release | rel-38 (2026-05-20) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 8.5 |
| adoption | 9.86 |
| documentation | 6.06 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 9.86 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.4** |
| **trust_score** | **8.08** |

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
| README size | 6,753 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug ossf/package-analysis
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
