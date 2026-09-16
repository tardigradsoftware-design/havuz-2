---
id: aider-ai--aider
title: "Aider-AI/aider"
domain: agent-skills
summary: >-
  Aider-AI/aider — STABLE, tier A,
  48,966 stars, license Apache-2.0, quality 7.89/10, trust 7.8/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "coding-agent", "git", "github-repository", "terminal"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 6.0, "adoption": 10.0, "documentation": 8.03, "reproducibility": 9.0, "security": 4.5, "recency": 8.41, "evidence": 7.0}
  quality_score: 7.89
  trust_score: 7.8
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "Aider-AI/aider on GitHub"
    url: https://github.com/Aider-AI/aider
    type: github-repository
    organization: Aider-AI
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# Aider-AI/aider

🔵 STABLE · tier **A** · production-grade · confidence **very-high**

> aider is AI pair programming in your terminal

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/Aider-AI/aider> |
| Owner | Aider-AI (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 48,966 (checked 2026-09-15) |
| Forks | 4,949 |
| Open issues | 1,868 |
| Contributors | 172 |
| Last push | 2026-05-22 (116 days before verification) |
| Latest release | v0.86.0 (2025-08-09) |
| Archived | no |
| Fork | no |
| Homepage | https://aider.chat/ |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 6.0 |
| adoption | 10.0 |
| documentation | 8.03 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 8.41 |
| evidence | 7.0 |
| **quality_score** (weighted) | **7.89** |
| **trust_score** | **7.8** |

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
| examples | no |
| security md | no |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 12,406 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug Aider-AI/aider
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
