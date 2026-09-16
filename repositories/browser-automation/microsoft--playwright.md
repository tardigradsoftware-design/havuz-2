---
id: microsoft--playwright
title: "microsoft/playwright"
domain: browser-automation
summary: >-
  microsoft/playwright — ACTIVE, tier S,
  96,163 stars, license Apache-2.0, quality 9.04/10, trust 9.02/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["automation", "browser", "browser-automation", "github-repository", "testing"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.44, "reproducibility": 10.0, "security": 7.0, "recency": 10.0, "evidence": 8.0}
  quality_score: 9.04
  trust_score: 9.02
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "microsoft/playwright on GitHub"
    url: https://github.com/microsoft/playwright
    type: github-repository
    organization: microsoft
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

# microsoft/playwright

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/microsoft/playwright> |
| Owner | microsoft (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 96,163 (checked 2026-09-15) |
| Forks | 6,437 |
| Open issues | 186 |
| Contributors | 472 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | v1.63.0 (2026-09-04) |
| Archived | no |
| Fork | no |
| Homepage | [https://playwright.dev](https://playwright.dev) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.44 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **9.04** |
| **trust_score** | **9.02** |

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
| README size | 11,280 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug microsoft/playwright
python3 scripts/generate-index/generate_repository_cards.py --category browser-automation
```
