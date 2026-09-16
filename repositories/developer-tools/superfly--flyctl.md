---
id: superfly--flyctl
title: "superfly/flyctl"
domain: developer-tools
summary: >-
  superfly/flyctl — ACTIVE, tier S,
  1,702 stars, license Apache-2.0, quality 8.32/10, trust 8.03/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["cli", "deployment", "developer-tools", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.18, "reproducibility": 9.5, "security": 4.5, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.32
  trust_score: 8.03
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "superfly/flyctl on GitHub"
    url: https://github.com/superfly/flyctl
    type: github-repository
    organization: superfly
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# superfly/flyctl

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> Command line tools for fly.io services

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/superfly/flyctl> |
| Owner | superfly (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 1,702 (checked 2026-09-15) |
| Forks | 310 |
| Open issues | 217 |
| Contributors | 223 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | v0.4.103 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | https://fly.io |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.18 |
| reproducibility | 9.5 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.32** |
| **trust_score** | **8.03** |

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
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 2,176 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug superfly/flyctl
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
