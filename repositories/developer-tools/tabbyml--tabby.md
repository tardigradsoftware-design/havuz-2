---
id: tabbyml--tabby
title: "TabbyML/tabby"
domain: developer-tools
summary: >-
  TabbyML/tabby — STABLE, tier A,
  33,883 stars, license NOASSERTION, quality 7.05/10, trust 6.14/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["code-completion", "developer-tools", "github-repository", "self-hosted"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 6.0, "maintenance": 8.0, "adoption": 10.0, "documentation": 7.9, "reproducibility": 6.6, "security": 3.0, "recency": 8.96, "evidence": 5.0}
  quality_score: 7.05
  trust_score: 6.14
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "TabbyML/tabby on GitHub"
    url: https://github.com/TabbyML/tabby
    type: github-repository
    organization: TabbyML
    license: NOASSERTION
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# TabbyML/tabby

🔵 STABLE · tier **A** · production-grade · confidence **high**

> Self-hosted AI coding assistant

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/TabbyML/tabby> |
| Owner | TabbyML (Organization) |
| Official upstream | no |
| Language | Rust |
| License | `NOASSERTION` |
| Stars | 33,883 (checked 2026-09-15) |
| Forks | 1,785 |
| Open issues | 336 |
| Contributors | 117 |
| Last push | 2026-06-30 (76 days before verification) |
| Latest release | v0.32.0 (2026-01-25) |
| Archived | no |
| Fork | no |
| Homepage | https://tabbyml.com |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 8.0 |
| adoption | 10.0 |
| documentation | 7.9 |
| reproducibility | 6.6 |
| security | 3.0 |
| recency | 8.96 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.05** |
| **trust_score** | **6.14** |

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
| README size | 10,814 bytes |

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

Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug TabbyML/tabby
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
