---
id: vibrantlabsai--ragas
title: "vibrantlabsai/ragas"
domain: evaluation
summary: >-
  vibrantlabsai/ragas — MAINTENANCE, tier A,
  15,803 stars, license Apache-2.0, quality 7.02/10, trust 6.11/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["evaluation", "github-repository", "rag"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 5.5, "maintenance": 4.0, "adoption": 10.0, "documentation": 7.08, "reproducibility": 10.0, "security": 6.0, "recency": 7.14, "evidence": 8.0}
  quality_score: 7.02
  trust_score: 6.11
  tier: A
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "vibrantlabsai/ragas on GitHub"
    url: https://github.com/vibrantlabsai/ragas
    type: github-repository
    organization: vibrantlabsai
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# vibrantlabsai/ragas

🟡 MAINTENANCE · tier **A** · maintenance-mode · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Supercharge Your LLM Application Evaluations 🚀

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/vibrantlabsai/ragas> |
| Owner | vibrantlabsai (Organization) |
| Official upstream | no |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 15,803 (checked 2026-09-21) |
| Forks | 1,716 |
| Open issues | 603 |
| Contributors | 240 |
| Last push | 2026-02-24 (209 days before verification) |
| Latest release | v0.4.3 (2026-01-13) |
| Archived | no |
| Fork | no |
| Homepage | [https://docs.ragas.io](https://docs.ragas.io) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 4.0 |
| adoption | 10.0 |
| documentation | 7.08 |
| reproducibility | 10.0 |
| security | 6.0 |
| recency | 7.14 |
| evidence | 8.0 |
| **quality_score** (weighted) | **7.02** |
| **trust_score** | **6.11** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 6,996 bytes |

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

Repository moved: `explodinggradients/ragas` -> `vibrantlabsai/ragas`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. No push in 209 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug vibrantlabsai/ragas
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
