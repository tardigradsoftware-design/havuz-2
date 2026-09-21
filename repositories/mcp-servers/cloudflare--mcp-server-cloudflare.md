---
id: cloudflare--mcp-server-cloudflare
title: "cloudflare/mcp-server-cloudflare"
domain: mcp-servers
summary: >-
  cloudflare/mcp-server-cloudflare — STABLE, tier A,
  4,262 stars, license Apache-2.0, quality 7.53/10, trust 7.01/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["cloudflare", "edge", "github-repository", "mcp", "mcp-servers"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 9.5, "adoption": 10.0, "documentation": 4.26, "reproducibility": 7.0, "security": 4.5, "recency": 9.74, "evidence": 4.5}
  quality_score: 7.53
  trust_score: 7.01
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "cloudflare/mcp-server-cloudflare on GitHub"
    url: https://github.com/cloudflare/mcp-server-cloudflare
    type: github-repository
    organization: cloudflare
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# cloudflare/mcp-server-cloudflare

🔵 STABLE · tier **A** · production-ready · confidence **high**

> _No description published._

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/cloudflare/mcp-server-cloudflare> |
| Owner | cloudflare (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 4,262 (checked 2026-09-21) |
| Forks | 529 |
| Open issues | 77 |
| Contributors | 41 |
| Last push | 2026-09-01 (19 days before verification) |
| Latest release | containers-mcp@0.2.19 (2026-08-11) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 9.5 |
| adoption | 10.0 |
| documentation | 4.26 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 9.74 |
| evidence | 4.5 |
| **quality_score** (weighted) | **7.53** |
| **trust_score** | **7.01** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 9,138 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug cloudflare/mcp-server-cloudflare
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
