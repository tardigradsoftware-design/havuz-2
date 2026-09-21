---
id: ossf--package-analysis
title: "ossf/package-analysis"
domain: developer-tools
summary: >-
  ossf/package-analysis — ACTIVE, tier S,
  912 stars, license Apache-2.0, quality 8.63/10, trust 8.38/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "security", "supply-chain"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 9.86, "documentation": 6.06, "reproducibility": 10.0, "security": 7.0, "recency": 9.96, "evidence": 7.5}
  quality_score: 8.63
  trust_score: 8.38
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
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
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# ossf/package-analysis

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Open Source Package Analysis

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/ossf/package-analysis> |
| Owner | ossf (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 912 (checked 2026-09-21) |
| Forks | 74 |
| Open issues | 86 |
| Contributors | 23 |
| Last push | 2026-09-17 (3 days before verification) |
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
| maintenance | 10.0 |
| adoption | 9.86 |
| documentation | 6.06 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 9.96 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.63** |
| **trust_score** | **8.38** |

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
