---
id: apache--casbin
title: "apache/casbin"
domain: backend
summary: >-
  apache/casbin — ACTIVE, tier S,
  20,390 stars, license Apache-2.0, quality 8.49/10, trust 8.34/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["authorization", "backend", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.92, "reproducibility": 8.5, "security": 4.5, "recency": 9.95, "evidence": 6.0}
  quality_score: 8.49
  trust_score: 8.34
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "apache/casbin on GitHub"
    url: https://github.com/apache/casbin
    type: github-repository
    organization: apache
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

# apache/casbin

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Apache Casbin: an authorization library that supports access control models like ACL, RBAC, ABAC.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/apache/casbin> |
| Owner | apache (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 20,390 (checked 2026-09-15) |
| Forks | 1,755 |
| Open issues | 38 |
| Contributors | 155 |
| Last push | 2026-09-11 (4 days before verification) |
| Latest release | v3.11.0 (2026-08-20) |
| Archived | no |
| Fork | no |
| Homepage | [https://casbin.apache.org/](https://casbin.apache.org/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.92 |
| reproducibility | 8.5 |
| security | 4.5 |
| recency | 9.95 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.49** |
| **trust_score** | **8.34** |

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
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 17,031 bytes |

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

Repository moved: `casbin/casbin` -> `apache/casbin`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug apache/casbin
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
