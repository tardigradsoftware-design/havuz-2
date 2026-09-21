---
id: supabase--mcp
title: "supabase/mcp"
domain: mcp-servers
summary: >-
  supabase/mcp — ACTIVE, tier S,
  2,917 stars, license Apache-2.0, quality 8.07/10, trust 7.83/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["database", "github-repository", "mcp", "mcp-servers", "supabase"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.17, "reproducibility": 7.0, "security": 4.5, "recency": 9.99, "evidence": 5.0}
  quality_score: 8.07
  trust_score: 7.83
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "supabase/mcp on GitHub"
    url: https://github.com/supabase/mcp
    type: github-repository
    organization: supabase
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# supabase/mcp

🟢 ACTIVE · tier **S** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Connect Supabase to your AI assistants

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/supabase/mcp> |
| Owner | supabase (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 2,917 (checked 2026-09-21) |
| Forks | 407 |
| Open issues | 125 |
| Contributors | 24 |
| Last push | 2026-09-19 (1 days before verification) |
| Latest release | mcp-server-supabase-v0.13.0 (2026-09-17) |
| Archived | no |
| Fork | no |
| Homepage | [https://supabase.com/mcp](https://supabase.com/mcp) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.17 |
| reproducibility | 7.0 |
| security | 4.5 |
| recency | 9.99 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.07** |
| **trust_score** | **7.83** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 8,088 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-21) and must be
re-checked against your own constraints._

**Recommended for**

- Agents managing Supabase projects: database, auth, storage, edge functions
- Schema inspection and migration drafting

**Not recommended for**

- Granting write/admin scope in production without a human approval gate
- Assuming row-level security is configured correctly because the MCP succeeded

**Strengths**

- Official Supabase project, Apache-2.0
- Release-tagged server (mcp-server-supabase-v0.12.0 verified)
- Read-only mode available as a safe default

**Weaknesses**

- Only 24 contributors - concentrated maintenance
- Database admin scope plus network egress is a high-risk permission set
- The brief's seed slug supabase-community/supabase-mcp now redirects here

**Related projects**

- supabase/supabase
- neondatabase/mcp-server-neon
- crystaldba/postgres-mcp
- drizzle-team/drizzle-orm

## Verification notes

Repository moved: `supabase-community/supabase-mcp` -> `supabase/mcp`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. Verified 2026-09-15: ACTIVE, Apache-2.0, q=8.07. Seed slug supabase-community/supabase-mcp resolved to supabase/mcp.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug supabase/mcp
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
