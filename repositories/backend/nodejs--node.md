---
id: nodejs--node
title: "nodejs/node"
domain: backend
summary: >-
  nodejs/node — ACTIVE, tier A,
  121,952 stars, license NOASSERTION, quality 8.91/10, trust 9.0/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["backend", "github-repository", "javascript", "runtime"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.5, "reproducibility": 8.6, "security": 6.5, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.91
  trust_score: 9.0
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "nodejs/node on GitHub"
    url: https://github.com/nodejs/node
    type: github-repository
    organization: nodejs
    license: NOASSERTION
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# nodejs/node

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> Node.js JavaScript runtime ✨🐢🚀✨

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/nodejs/node> |
| Owner | nodejs (Organization) |
| Official upstream | yes |
| Language | JavaScript |
| License | `NOASSERTION` |
| Stars | 121,952 (checked 2026-09-15) |
| Forks | 36,750 |
| Open issues | 1,182 |
| Contributors | 421 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v26.8.2 (2026-09-09) |
| Archived | no |
| Fork | no |
| Homepage | https://nodejs.org |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.5 |
| reproducibility | 8.6 |
| security | 6.5 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.91** |
| **trust_score** | **9.0** |

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
| README size | 41,778 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug nodejs/node
python3 scripts/generate-index/generate_repository_cards.py --category backend
```
