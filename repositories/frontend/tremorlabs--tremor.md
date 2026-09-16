---
id: tremorlabs--tremor
title: "tremorlabs/tremor"
domain: frontend
summary: >-
  tremorlabs/tremor — MAINTENANCE, tier B,
  3,615 stars, license Apache-2.0, quality 6.1/10, trust 5.7/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["components", "dashboards", "frontend", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 3.0, "adoption": 10.0, "documentation": 4.69, "reproducibility": 6.0, "security": 4.5, "recency": 5.34, "evidence": 3.0}
  quality_score: 6.1
  trust_score: 5.7
  tier: B
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "tremorlabs/tremor on GitHub"
    url: https://github.com/tremorlabs/tremor
    type: github-repository
    organization: tremorlabs
    license: Apache-2.0
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# tremorlabs/tremor

🟡 MAINTENANCE · tier **B** · maintenance-mode · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Copy & Paste React components to build modern web applications.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/tremorlabs/tremor> |
| Owner | tremorlabs (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 3,615 (checked 2026-09-15) |
| Forks | 186 |
| Open issues | 26 |
| Contributors | 4 |
| Last push | 2025-10-10 (340 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://tremor.so](https://tremor.so) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 3.0 |
| adoption | 10.0 |
| documentation | 4.69 |
| reproducibility | 6.0 |
| security | 4.5 |
| recency | 5.34 |
| evidence | 3.0 |
| **quality_score** (weighted) | **6.1** |
| **trust_score** | **5.7** |

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
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 2,224 bytes |

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

No push in 340 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug tremorlabs/tremor
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
