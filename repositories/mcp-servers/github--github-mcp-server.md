---
id: github--github-mcp-server
title: "github/github-mcp-server"
domain: mcp-servers
summary: >-
  github/github-mcp-server — ACTIVE, tier S,
  33,096 stars, license MIT, quality 8.39/10, trust 8.12/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github", "github-repository", "mcp", "mcp-servers"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.5, "reproducibility": 7.5, "security": 7.0, "recency": 9.95, "evidence": 5.0}
  quality_score: 8.39
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
  - title: "github/github-mcp-server on GitHub"
    url: https://github.com/github/github-mcp-server
    type: github-repository
    organization: github
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# github/github-mcp-server

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> GitHub's official MCP Server

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/github/github-mcp-server> |
| Owner | github (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `MIT` |
| Stars | 33,096 (checked 2026-09-21) |
| Forks | 5,023 |
| Open issues | 335 |
| Contributors | 164 |
| Last push | 2026-09-16 (4 days before verification) |
| Latest release | v1.12.2 (2026-09-16) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.5 |
| reproducibility | 7.5 |
| security | 7.0 |
| recency | 9.95 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.39** |
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
| examples | no |
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 113,197 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug github/github-mcp-server
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
