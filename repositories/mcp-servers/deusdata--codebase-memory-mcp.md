---
id: deusdata--codebase-memory-mcp
title: "DeusData/codebase-memory-mcp"
domain: mcp-servers
summary: >-
  DeusData/codebase-memory-mcp — ACTIVE, tier S,
  43,942 stars, license MIT, quality 8.2/10, trust 7.4/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["codebase", "github-repository", "indexing", "mcp", "mcp-servers"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 5.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.5, "reproducibility": 9.0, "security": 6.0, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.2
  trust_score: 7.4
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "DeusData/codebase-memory-mcp on GitHub"
    url: https://github.com/DeusData/codebase-memory-mcp
    type: github-repository
    organization: DeusData
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# DeusData/codebase-memory-mcp

🟢 ACTIVE · tier **S** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/DeusData/codebase-memory-mcp> |
| Owner | DeusData (User) |
| Official upstream | no |
| Language | C |
| License | `MIT` |
| Stars | 43,942 (checked 2026-09-21) |
| Forks | 3,583 |
| Open issues | 597 |
| Contributors | 153 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v0.11.0 (2026-09-15) |
| Archived | no |
| Fork | no |
| Homepage | [https://deusdata.github.io/codebase-memory-mcp/](https://deusdata.github.io/codebase-memory-mcp/) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.5 |
| reproducibility | 9.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.2** |
| **trust_score** | **7.4** |

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
| contributing | yes |
| root entries | yes |
| README size | 75,651 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug DeusData/codebase-memory-mcp
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
