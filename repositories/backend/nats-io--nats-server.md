---
id: nats-io--nats-server
title: "nats-io/nats-server"
domain: backend
summary: >-
  nats-io/nats-server — ACTIVE, tier S,
  20,863 stars, license Apache-2.0, quality 8.69/10, trust 8.53/10.
  Verified against the GitHub API on 2026-10-12.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["backend", "github-repository", "messaging"]
version: 1.0.0
updated: 2026-10-12
verified_at: 2026-10-12
expires_at: 2026-11-26
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.88, "reproducibility": 9.0, "security": 7.0, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.69
  trust_score: 8.53
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-12
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "nats-io/nats-server on GitHub"
    url: https://github.com/nats-io/nats-server
    type: github-repository
    organization: nats-io
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-10-12
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-12)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# nats-io/nats-server

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> High-Performance server for NATS.io, the cloud and edge native messaging system.

## Facts (verified 2026-10-12 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/nats-io/nats-server> |
| Owner | nats-io (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 20,863 (checked 2026-10-12) |
| Forks | 1,997 |
| Open issues | 477 |
| Contributors | 217 |
| Last push | 2026-10-12 (0 days before verification) |
| Latest release | v2.15.1 (2026-10-09) |
| Archived | no |
| Fork | no |
| Homepage | [https://nats.io](https://nats.io) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.88 |
| reproducibility | 9.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.69** |
| **trust_score** | **8.53** |

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
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 4,576 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug nats-io/nats-server
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
