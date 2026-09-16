---
id: aws--aws-cdk
title: "aws/aws-cdk"
domain: developer-tools
summary: >-
  aws/aws-cdk — ACTIVE, tier S,
  12,900 stars, license Apache-2.0, quality 8.24/10, trust 8.08/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["aws", "developer-tools", "github-repository", "iac"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.88, "reproducibility": 7.0, "security": 4.5, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.24
  trust_score: 8.08
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "aws/aws-cdk on GitHub"
    url: https://github.com/aws/aws-cdk
    type: github-repository
    organization: aws
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# aws/aws-cdk

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> The AWS Cloud Development Kit is a framework for defining cloud infrastructure in code

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/aws/aws-cdk> |
| Owner | aws (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 12,900 (checked 2026-09-15) |
| Forks | 4,632 |
| Open issues | 2,857 |
| Contributors | 390 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v2.269.0 (2026-09-10) |
| Archived | no |
| Fork | no |
| Homepage | https://aws.amazon.com/cdk |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.88 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.24** |
| **trust_score** | **8.08** |

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
| security md | no |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 10,559 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug aws/aws-cdk
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
