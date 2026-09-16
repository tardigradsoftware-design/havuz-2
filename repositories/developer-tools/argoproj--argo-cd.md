---
id: argoproj--argo-cd
title: "argoproj/argo-cd"
domain: developer-tools
summary: >-
  argoproj/argo-cd — ACTIVE, tier S,
  24,164 stars, license Apache-2.0, quality 9.06/10, trust 9.04/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["ci-cd", "developer-tools", "github-repository", "gitops"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.63, "reproducibility": 10.0, "security": 7.0, "recency": 10.0, "evidence": 8.0}
  quality_score: 9.06
  trust_score: 9.04
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "argoproj/argo-cd on GitHub"
    url: https://github.com/argoproj/argo-cd
    type: github-repository
    organization: argoproj
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# argoproj/argo-cd

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Declarative Continuous Deployment for Kubernetes

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/argoproj/argo-cd> |
| Owner | argoproj (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 24,164 (checked 2026-09-15) |
| Forks | 7,843 |
| Open issues | 4,361 |
| Contributors | 425 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v3.5.3 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | [https://argo-cd.readthedocs.io](https://argo-cd.readthedocs.io) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.63 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **9.06** |
| **trust_score** | **9.04** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 7,517 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug argoproj/argo-cd
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
