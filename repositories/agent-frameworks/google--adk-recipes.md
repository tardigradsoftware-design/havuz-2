---
id: google--adk-recipes
title: "google/adk-recipes"
domain: agent-frameworks
summary: >-
  google/adk-recipes — ACTIVE, tier A,
  10,355 stars, license Apache-2.0, quality 7.82/10, trust 7.51/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-frameworks", "github-repository", "google", "samples"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.71, "reproducibility": 6.0, "security": 4.5, "recency": 9.97, "evidence": 4.0}
  quality_score: 7.82
  trust_score: 7.51
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "google/adk-recipes on GitHub"
    url: https://github.com/google/adk-recipes
    type: github-repository
    organization: google
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

# google/adk-recipes

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A collection of sample agents built with Agent Development Kit (ADK)

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/google/adk-recipes> |
| Owner | google (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 10,355 (checked 2026-09-21) |
| Forks | 2,869 |
| Open issues | 54 |
| Contributors | 136 |
| Last push | 2026-09-19 (2 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://adk.dev](https://adk.dev) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `docs` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.71 |
| reproducibility | 6.0 |
| security | 4.5 |
| recency | 9.97 |
| evidence | 4.0 |
| **quality_score** (weighted) | **7.82** |
| **trust_score** | **7.51** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 2,537 bytes |

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

Repository moved: `google/adk-samples` -> `google/adk-recipes`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug google/adk-recipes
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
