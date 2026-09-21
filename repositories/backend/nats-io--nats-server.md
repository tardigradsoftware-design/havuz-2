---
id: nats-io--nats-server
title: "nats-io/nats-server"
domain: backend
summary: >-
  nats-io/nats-server — ACTIVE, tier S,
  20,756 stars, license Apache-2.0, quality 8.44/10, trust 8.28/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["backend", "github-repository", "messaging"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.88, "reproducibility": 9.0, "security": 4.5, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.44
  trust_score: 8.28
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
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
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# nats-io/nats-server

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> High-Performance server for NATS.io, the cloud and edge native messaging system.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/nats-io/nats-server> |
| Owner | nats-io (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 20,756 (checked 2026-09-21) |
| Forks | 1,964 |
| Open issues | 475 |
| Contributors | 205 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v2.15.0 (2026-09-17) |
| Archived | no |
| Fork | no |
| Homepage | [https://nats.io](https://nats.io) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.88 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.44** |
| **trust_score** | **8.28** |

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
