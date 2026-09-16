---
id: giskard-ai--giskard-oss
title: "Giskard-AI/giskard-oss"
domain: instructions-standards
summary: >-
  Giskard-AI/giskard-oss — ACTIVE, tier S,
  5,815 stars, license Apache-2.0, quality 8.6/10, trust 8.37/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "instructions-standards", "llm-security", "testing"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.47, "reproducibility": 8.5, "security": 7.0, "recency": 9.99, "evidence": 6.0}
  quality_score: 8.6
  trust_score: 8.37
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "Giskard-AI/giskard-oss on GitHub"
    url: https://github.com/Giskard-AI/giskard-oss
    type: github-repository
    organization: Giskard-AI
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# Giskard-AI/giskard-oss

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> 🐢 Open-Source Evaluation & Testing library for LLM Agents

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/Giskard-AI/giskard-oss> |
| Owner | Giskard-AI (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 5,815 (checked 2026-09-15) |
| Forks | 537 |
| Open issues | 65 |
| Contributors | 74 |
| Last push | 2026-09-14 (1 days before verification) |
| Latest release | giskard-checks/v1.0.4 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | https://docs.giskard.ai |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.47 |
| reproducibility | 8.5 |
| security | 7.0 |
| recency | 9.99 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.6** |
| **trust_score** | **8.37** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | yes |
| examples | yes |
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 11,620 bytes |

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

Repository moved: `giskard-ai/giskard` -> `Giskard-AI/giskard-oss`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug Giskard-AI/giskard-oss
python3 scripts/generate-index/generate_repository_cards.py --category instructions-standards
```
