---
id: neondatabase--mcp-server-neon
title: "neondatabase/mcp-server-neon"
domain: mcp-servers
summary: >-
  neondatabase/mcp-server-neon — ACTIVE, tier A,
  642 stars, license MIT, quality 7.93/10, trust 7.81/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "neon", "postgres"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 9.58, "documentation": 7.92, "reproducibility": 6.0, "security": 4.5, "recency": 10.0, "evidence": 4.5}
  quality_score: 7.93
  trust_score: 7.81
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "neondatabase/mcp-server-neon on GitHub"
    url: https://github.com/neondatabase/mcp-server-neon
    type: github-repository
    organization: neondatabase
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# neondatabase/mcp-server-neon

🟢 ACTIVE · tier **A** · production-ready · confidence **very-high**

> MCP server for interacting with Neon Management API and databases

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/neondatabase/mcp-server-neon> |
| Owner | neondatabase (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 642 (checked 2026-09-15) |
| Forks | 124 |
| Open issues | 40 |
| Contributors | 21 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | https://mcp-server-neon-jet.vercel.app |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 9.58 |
| documentation | 7.92 |
| reproducibility | 6.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 4.5 |
| **quality_score** (weighted) | **7.93** |
| **trust_score** | **7.81** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | yes |
| examples | no |
| security md | no |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 29,029 bytes |

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

Repository moved: `neondatabase-labs/mcp-server-neon` -> `neondatabase/mcp-server-neon`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug neondatabase/mcp-server-neon
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
