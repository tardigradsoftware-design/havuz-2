---
id: grafana--k6
title: "grafana/k6"
domain: developer-tools
summary: >-
  grafana/k6 — ACTIVE, tier S,
  31,537 stars, license AGPL-3.0, quality 8.19/10, trust 8.12/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "load-testing", "performance"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.11, "reproducibility": 7.3, "security": 3.5, "recency": 10.0, "evidence": 6.0}
  quality_score: 8.19
  trust_score: 8.12
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "grafana/k6 on GitHub"
    url: https://github.com/grafana/k6
    type: github-repository
    organization: grafana
    license: AGPL-3.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# grafana/k6

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A modern load testing tool, using Go and JavaScript

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/grafana/k6> |
| Owner | grafana (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `AGPL-3.0` |
| Stars | 31,537 (checked 2026-09-21) |
| Forks | 1,635 |
| Open issues | 851 |
| Contributors | 259 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v2.2.0 (2026-08-10) |
| Archived | no |
| Fork | no |
| Homepage | [https://grafana.com/oss/k6/](https://grafana.com/oss/k6/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.11 |
| reproducibility | 7.3 |
| security | 3.5 |
| recency | 10.0 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.19** |
| **trust_score** | **8.12** |

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
| examples | yes |
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 7,313 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug grafana/k6
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
