---
id: seleniumhq--selenium
title: "SeleniumHQ/selenium"
domain: browser-automation
summary: >-
  SeleniumHQ/selenium — ACTIVE, tier S,
  34,491 stars, license Apache-2.0, quality 8.25/10, trust 8.11/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["browser", "browser-automation", "github-repository", "testing"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.04, "reproducibility": 7.0, "security": 4.5, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.25
  trust_score: 8.11
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "SeleniumHQ/selenium on GitHub"
    url: https://github.com/SeleniumHQ/selenium
    type: github-repository
    organization: SeleniumHQ
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# SeleniumHQ/selenium

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A browser automation framework and ecosystem.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/SeleniumHQ/selenium> |
| Owner | SeleniumHQ (Organization) |
| Official upstream | yes |
| Language | Java |
| License | `Apache-2.0` |
| Stars | 34,491 (checked 2026-09-15) |
| Forks | 8,718 |
| Open issues | 190 |
| Contributors | 404 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | selenium-4.49.0 (2026-09-09) |
| Archived | no |
| Fork | no |
| Homepage | [https://selenium.dev](https://selenium.dev) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.04 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.25** |
| **trust_score** | **8.11** |

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
| README size | 18,510 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug SeleniumHQ/selenium
python3 scripts/generate-index/generate_repository_cards.py --category browser-automation
```
