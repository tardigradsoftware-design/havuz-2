---
id: upstash--context7
title: "upstash/context7"
domain: mcp-servers
summary: >-
  upstash/context7 — ACTIVE, tier S,
  62,051 stars, license MIT, quality 8.28/10, trust 8.02/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["context", "documentation", "github-repository", "mcp", "mcp-servers"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.8, "reproducibility": 7.0, "security": 7.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.28
  trust_score: 8.02
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "upstash/context7 on GitHub"
    url: https://github.com/upstash/context7
    type: github-repository
    organization: upstash
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# upstash/context7

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/upstash/context7> |
| Owner | upstash (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `MIT` |
| Stars | 62,051 (checked 2026-09-15) |
| Forks | 2,996 |
| Open issues | 66 |
| Contributors | 128 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | @upstash/context7-mcp@4.1.1 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | https://context7.com |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.8 |
| reproducibility | 7.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.28** |
| **trust_score** | **8.02** |

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
| contributing | no |
| root entries | yes |
| README size | 9,620 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Feeding current library documentation into an agent at request time
- Reducing reliance on stale training data for fast-moving frameworks

**Not recommended for**

- Offline or air-gapped environments
- Assuming fetched documentation is authoritative over the vendor's own site

**Strengths**

- Directly addresses the number one cause of agent coding errors: outdated API knowledge
- Very high adoption (62k stars verified)
- Remote-hosted, so setup is trivial

**Weaknesses**

- External service dependency and network egress
- Coverage varies by library

**Related projects**

- oraios/serena
- modelcontextprotocol/servers
- firecrawl/firecrawl-mcp-server

## Verification notes

Verified 2026-09-15.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug upstash/context7
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
