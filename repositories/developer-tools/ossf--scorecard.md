---
id: ossf--scorecard
title: "ossf/scorecard"
domain: developer-tools
summary: >-
  ossf/scorecard — ACTIVE, tier S,
  5,698 stars, license Apache-2.0, quality 8.65/10, trust 8.55/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "scoring", "security", "supply-chain"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.5, "reproducibility": 7.5, "security": 7.0, "recency": 10.0, "evidence": 5.5}
  quality_score: 8.65
  trust_score: 8.55
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "ossf/scorecard on GitHub"
    url: https://github.com/ossf/scorecard
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

# ossf/scorecard

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> OpenSSF Scorecard - Security health metrics for Open Source

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/ossf/scorecard> |
| Owner | ossf (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 5,698 (checked 2026-09-21) |
| Forks | 722 |
| Open issues | 456 |
| Contributors | 183 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v5.5.0 (2026-04-23) |
| Archived | no |
| Fork | no |
| Homepage | [https://scorecard.dev](https://scorecard.dev) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.5 |
| reproducibility | 7.5 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 5.5 |
| **quality_score** (weighted) | **8.65** |
| **trust_score** | **8.55** |

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
| README size | 45,402 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug ossf/scorecard
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
