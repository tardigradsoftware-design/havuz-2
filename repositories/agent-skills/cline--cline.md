---
id: cline--cline
title: "cline/cline"
domain: agent-skills
summary: >-
  cline/cline — ACTIVE, tier S,
  68,097 stars, license Apache-2.0, quality 8.38/10, trust 8.17/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "coding-agent", "github-repository", "vscode"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.77, "reproducibility": 7.0, "security": 7.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.38
  trust_score: 8.17
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "cline/cline on GitHub"
    url: https://github.com/cline/cline
    type: github-repository
    organization: cline
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# cline/cline

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> Autonomous coding agent as an SDK, IDE extension, or CLI assistant.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/cline/cline> |
| Owner | cline (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 68,097 (checked 2026-09-15) |
| Forks | 7,355 |
| Open issues | 1,320 |
| Contributors | 319 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | desktop-v0.0.28 (2026-09-15) |
| Archived | no |
| Fork | no |
| Homepage | https://cline.bot |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.77 |
| reproducibility | 7.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.38** |
| **trust_score** | **8.17** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 9,239 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug cline/cline
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
