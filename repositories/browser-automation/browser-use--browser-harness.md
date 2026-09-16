---
id: browser-use--browser-harness
title: "browser-use/browser-harness"
domain: browser-automation
summary: >-
  browser-use/browser-harness — ACTIVE, tier S,
  17,562 stars, license MIT, quality 8.52/10, trust 8.41/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "browser", "browser-automation", "github-repository", "self-healing"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.75, "reproducibility": 9.0, "security": 4.5, "recency": 9.96, "evidence": 7.0}
  quality_score: 8.52
  trust_score: 8.41
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "browser-use/browser-harness on GitHub"
    url: https://github.com/browser-use/browser-harness
    type: github-repository
    organization: browser-use
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# browser-use/browser-harness

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Browser Harness \| Self-healing harness that enables LLMs to complete any task.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/browser-use/browser-harness> |
| Owner | browser-use (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 17,562 (checked 2026-09-15) |
| Forks | 1,718 |
| Open issues | 344 |
| Contributors | 69 |
| Last push | 2026-09-12 (3 days before verification) |
| Latest release | v0.1.13 (2026-09-04) |
| Archived | no |
| Fork | no |
| Homepage | [https://browser-harness.com](https://browser-harness.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.75 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 9.96 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.52** |
| **trust_score** | **8.41** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 2,952 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug browser-use/browser-harness
python3 scripts/generate-index/generate_repository_cards.py --category browser-automation
```
