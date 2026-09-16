---
id: renovatebot--renovate
title: "renovatebot/renovate"
domain: developer-tools
summary: >-
  renovatebot/renovate — ACTIVE, tier S,
  22,503 stars, license AGPL-3.0, quality 8.54/10, trust 8.54/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["automation", "dependencies", "developer-tools", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.61, "reproducibility": 7.8, "security": 6.0, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.54
  trust_score: 8.54
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "renovatebot/renovate on GitHub"
    url: https://github.com/renovatebot/renovate
    type: github-repository
    organization: renovatebot
    license: AGPL-3.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# renovatebot/renovate

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Home of the Renovate CLI: Cross-platform Dependency Automation by Mend.io

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/renovatebot/renovate> |
| Owner | renovatebot (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `AGPL-3.0` |
| Stars | 22,503 (checked 2026-09-15) |
| Forks | 3,314 |
| Open issues | 1,489 |
| Contributors | 435 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | 44.93.1 (2026-09-15) |
| Archived | no |
| Fork | no |
| Homepage | [https://mend.io/renovate](https://mend.io/renovate) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.61 |
| reproducibility | 7.8 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.54** |
| **trust_score** | **8.54** |

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
| security md | yes |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 7,281 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug renovatebot/renovate
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
