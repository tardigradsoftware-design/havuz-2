---
id: arize-ai--phoenix
title: "Arize-ai/phoenix"
domain: evaluation
summary: >-
  Arize-ai/phoenix — ACTIVE, tier A,
  11,469 stars, license NOASSERTION, quality 9.26/10, trust 9.47/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["evaluation", "github-repository", "observability", "tracing"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 10.0, "reproducibility": 9.6, "security": 6.5, "recency": 10.0, "evidence": 8.5}
  quality_score: 9.26
  trust_score: 9.47
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "Arize-ai/phoenix on GitHub"
    url: https://github.com/Arize-ai/phoenix
    type: github-repository
    organization: Arize-ai
    license: NOASSERTION
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# Arize-ai/phoenix

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> AI Observability & Evaluation

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/Arize-ai/phoenix> |
| Owner | Arize-ai (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `NOASSERTION` |
| Stars | 11,469 (checked 2026-09-15) |
| Forks | 1,131 |
| Open issues | 997 |
| Contributors | 224 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | arize-phoenix-v20.12.0 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | https://arize.com/docs/phoenix |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 10.0 |
| reproducibility | 9.6 |
| security | 6.5 |
| recency | 10.0 |
| evidence | 8.5 |
| **quality_score** (weighted) | **9.26** |
| **trust_score** | **9.47** |

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
| README size | 55,436 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug Arize-ai/phoenix
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
