---
id: inclusionai--aenvironment
title: "inclusionAI/AEnvironment"
domain: evaluation
summary: >-
  inclusionAI/AEnvironment — STABLE, tier B,
  316 stars, license Apache-2.0, quality 6.65/10, trust 5.68/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "benchmark", "environment", "evaluation", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 6.0, "maintenance": 7.0, "adoption": 8.63, "documentation": 7.54, "reproducibility": 7.0, "security": 3.5, "recency": 9.0, "evidence": 4.0}
  quality_score: 6.65
  trust_score: 5.68
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "inclusionAI/AEnvironment on GitHub"
    url: https://github.com/inclusionAI/AEnvironment
    type: github-repository
    organization: inclusionAI
    license: Apache-2.0
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# inclusionAI/AEnvironment

🔵 STABLE · tier **B** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Standardized environment infrastructure for Agentic AI development.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/inclusionAI/AEnvironment> |
| Owner | inclusionAI (Organization) |
| Official upstream | no |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 316 (checked 2026-09-21) |
| Forks | 37 |
| Open issues | 14 |
| Contributors | 6 |
| Last push | 2026-07-10 (73 days before verification) |
| Latest release | v0.1.7 (2026-05-21) |
| Archived | no |
| Fork | no |
| Homepage | [https://inclusionai.github.io/AEnvironment/](https://inclusionai.github.io/AEnvironment/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 7.0 |
| adoption | 8.63 |
| documentation | 7.54 |
| reproducibility | 7.0 |
| security | 3.5 |
| recency | 9.0 |
| evidence | 4.0 |
| **quality_score** (weighted) | **6.65** |
| **trust_score** | **5.68** |

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
| README size | 12,444 bytes |

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

Reference implementation published with a benchmark. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug inclusionAI/AEnvironment
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
