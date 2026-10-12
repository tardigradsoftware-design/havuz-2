---
id: exa-labs--exa-mcp-server
title: "exa-labs/exa-mcp-server"
domain: mcp-servers
summary: >-
  exa-labs/exa-mcp-server — ACTIVE, tier S,
  5,109 stars, license MIT, quality 8.21/10, trust 7.92/10.
  Verified against the GitHub API on 2026-10-12.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "search"]
version: 1.0.0
updated: 2026-10-12
verified_at: 2026-10-12
expires_at: 2026-11-26
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.14, "reproducibility": 8.5, "security": 4.5, "recency": 9.95, "evidence": 6.0}
  quality_score: 8.21
  trust_score: 7.92
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-12
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "exa-labs/exa-mcp-server on GitHub"
    url: https://github.com/exa-labs/exa-mcp-server
    type: github-repository
    organization: exa-labs
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-10-12
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-12)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# exa-labs/exa-mcp-server

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Exa MCP for web search and web crawling!

## Facts (verified 2026-10-12 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/exa-labs/exa-mcp-server> |
| Owner | exa-labs (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 5,109 (checked 2026-10-12) |
| Forks | 401 |
| Open issues | 16 |
| Contributors | 30 |
| Last push | 2026-10-07 (4 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://exa.ai/docs/reference/exa-mcp](https://exa.ai/docs/reference/exa-mcp) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.14 |
| reproducibility | 8.5 |
| security | 4.5 |
| recency | 9.95 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.21** |
| **trust_score** | **7.92** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | yes |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 7,653 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug exa-labs/exa-mcp-server
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
