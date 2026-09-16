---
id: moby--moby
title: "moby/moby"
domain: developer-tools
summary: >-
  moby/moby — ACTIVE, tier S,
  72,106 stars, license Apache-2.0, quality 8.35/10, trust 8.04/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["containers", "developer-tools", "docker", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.96, "reproducibility": 7.5, "security": 7.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.35
  trust_score: 8.04
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "moby/moby on GitHub"
    url: https://github.com/moby/moby
    type: github-repository
    organization: moby
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# moby/moby

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> The Moby Project - a collaborative project for the container ecosystem to assemble container-based systems

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/moby/moby> |
| Owner | moby (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `Apache-2.0` |
| Stars | 72,106 (checked 2026-09-15) |
| Forks | 19,233 |
| Open issues | 3,907 |
| Contributors | 394 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | docker-v29.8.0 (2026-09-03) |
| Archived | no |
| Fork | no |
| Homepage | https://mobyproject.org/ |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.96 |
| reproducibility | 7.5 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.35** |
| **trust_score** | **8.04** |

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
| README size | 5,487 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug moby/moby
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
