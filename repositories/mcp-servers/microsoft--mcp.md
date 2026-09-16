---
id: microsoft--mcp
title: "microsoft/mcp"
domain: mcp-servers
summary: >-
  microsoft/mcp — ACTIVE, tier S,
  3,678 stars, license MIT, quality 8.4/10, trust 8.12/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["catalog", "github-repository", "mcp", "mcp-servers", "microsoft"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.5, "reproducibility": 7.5, "security": 7.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.4
  trust_score: 8.12
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "microsoft/mcp on GitHub"
    url: https://github.com/microsoft/mcp
    type: github-repository
    organization: microsoft
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

# microsoft/mcp

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/microsoft/mcp> |
| Owner | microsoft (Organization) |
| Official upstream | yes |
| Language | C# |
| License | `MIT` |
| Stars | 3,678 (checked 2026-09-15) |
| Forks | 621 |
| Open issues | 308 |
| Contributors | 164 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | Azure.Mcp.Server-3.0.0-beta.43 (2026-09-12) |
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
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.4** |
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
| README size | 44,274 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug microsoft/mcp
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
