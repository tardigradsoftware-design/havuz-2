---
id: helicone--helicone
title: "Helicone/helicone"
domain: evaluation
summary: >-
  Helicone/helicone — ACTIVE, tier S,
  6,158 stars, license Apache-2.0, quality 8.08/10, trust 7.24/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["evaluation", "github-repository", "observability", "proxy"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.29, "reproducibility": 10.0, "security": 3.5, "recency": 9.99, "evidence": 8.0}
  quality_score: 8.08
  trust_score: 7.24
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "Helicone/helicone on GitHub"
    url: https://github.com/Helicone/helicone
    type: github-repository
    organization: Helicone
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# Helicone/helicone

🟢 ACTIVE · tier **S** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> 🧊 Open source LLM observability platform. One line of code to monitor, evaluate, and experiment. YC W23 🍓

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/Helicone/helicone> |
| Owner | Helicone (Organization) |
| Official upstream | no |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 6,158 (checked 2026-09-15) |
| Forks | 670 |
| Open issues | 157 |
| Contributors | 96 |
| Last push | 2026-09-13 (1 days before verification) |
| Latest release | v2025.08.21-1 (2025-08-21) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.helicone.ai](https://www.helicone.ai) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.29 |
| reproducibility | 10.0 |
| security | 3.5 |
| recency | 9.99 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.08** |
| **trust_score** | **7.24** |

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
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 15,453 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug Helicone/helicone
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
