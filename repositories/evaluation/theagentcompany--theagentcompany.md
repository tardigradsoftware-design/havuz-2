---
id: theagentcompany--theagentcompany
title: "TheAgentCompany/TheAgentCompany"
domain: evaluation
summary: >-
  TheAgentCompany/TheAgentCompany — STABLE, tier B,
  780 stars, license MIT, quality 5.93/10, trust 5.01/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "benchmark", "evaluation", "github-repository", "simulated-company"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 6.0, "maintenance": 3.0, "adoption": 9.78, "documentation": 6.71, "reproducibility": 7.0, "security": 3.5, "recency": 5.88, "evidence": 5.0}
  quality_score: 5.93
  trust_score: 5.01
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "TheAgentCompany/TheAgentCompany on GitHub"
    url: https://github.com/TheAgentCompany/TheAgentCompany
    type: github-repository
    organization: TheAgentCompany
    license: MIT
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# TheAgentCompany/TheAgentCompany

🔵 STABLE · tier **B** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> An agent benchmark with tasks in a simulated software company.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/TheAgentCompany/TheAgentCompany> |
| Owner | TheAgentCompany (Organization) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 780 (checked 2026-09-15) |
| Forks | 124 |
| Open issues | 25 |
| Contributors | 24 |
| Last push | 2025-11-17 (301 days before verification) |
| Latest release | 1.0.0 (2024-12-20) |
| Archived | no |
| Fork | no |
| Homepage | [https://the-agent-company.com](https://the-agent-company.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 3.0 |
| adoption | 9.78 |
| documentation | 6.71 |
| reproducibility | 7.0 |
| security | 3.5 |
| recency | 5.88 |
| evidence | 5.0 |
| **quality_score** (weighted) | **5.93** |
| **trust_score** | **5.01** |

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
| contributing | no |
| root entries | yes |
| README size | 8,545 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug TheAgentCompany/TheAgentCompany
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
