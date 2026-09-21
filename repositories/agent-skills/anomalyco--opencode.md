---
id: anomalyco--opencode
title: "anomalyco/opencode"
domain: agent-skills
summary: >-
  anomalyco/opencode — ACTIVE, tier A,
  209,005 stars, license MIT, quality 7.87/10, trust 6.85/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "coding-agent", "github-repository", "terminal"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 5.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.67, "reproducibility": 9.0, "security": 6.0, "recency": 10.0, "evidence": 7.0}
  quality_score: 7.87
  trust_score: 6.85
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "anomalyco/opencode on GitHub"
    url: https://github.com/anomalyco/opencode
    type: github-repository
    organization: anomalyco
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# anomalyco/opencode

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> The open source coding agent.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/anomalyco/opencode> |
| Owner | anomalyco (Organization) |
| Official upstream | no |
| Language | TypeScript |
| License | `MIT` |
| Stars | 209,005 (checked 2026-09-21) |
| Forks | 27,526 |
| Open issues | 6,004 |
| Contributors | 456 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v1.18.31 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | [https://opencode.ai](https://opencode.ai) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.67 |
| reproducibility | 9.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **7.87** |
| **trust_score** | **6.85** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 8,083 bytes |

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

Repository moved: `sst/opencode` -> `anomalyco/opencode`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug anomalyco/opencode
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
