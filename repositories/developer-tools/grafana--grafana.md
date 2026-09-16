---
id: grafana--grafana
title: "grafana/grafana"
domain: developer-tools
summary: >-
  grafana/grafana — ACTIVE, tier S,
  76,761 stars, license AGPL-3.0, quality 8.01/10, trust 7.89/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["dashboards", "developer-tools", "github-repository", "observability"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.26, "reproducibility": 6.3, "security": 3.5, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.01
  trust_score: 7.89
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "grafana/grafana on GitHub"
    url: https://github.com/grafana/grafana
    type: github-repository
    organization: grafana
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

# grafana/grafana

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> The open and composable observability and data visualization platform. Visualize metrics, logs, and traces from multiple sources like Prometheus, Loki, Elasticsearch, InfluxDB, Postgres and many more.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/grafana/grafana> |
| Owner | grafana (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `AGPL-3.0` |
| Stars | 76,761 (checked 2026-09-15) |
| Forks | 14,744 |
| Open issues | 3,291 |
| Contributors | 373 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v13.2.2 (2026-09-15) |
| Archived | no |
| Fork | no |
| Homepage | [https://grafana.com](https://grafana.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.26 |
| reproducibility | 6.3 |
| security | 3.5 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.01** |
| **trust_score** | **7.89** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 3,114 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug grafana/grafana
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
