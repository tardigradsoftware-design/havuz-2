---
id: vercel--mcp-handler
title: "vercel/mcp-handler"
domain: mcp-servers
summary: >-
  vercel/mcp-handler — ACTIVE, tier UNVERIFIED,
  669 stars, license NONE, quality 8.02/10, trust 6.85/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["adapter", "github-repository", "mcp", "mcp-servers", "vercel"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 9.56, "documentation": 6.98, "reproducibility": 6.5, "security": 2.5, "recency": 9.9, "evidence": 8.0}
  quality_score: 8.02
  trust_score: 6.85
  tier: UNVERIFIED
  maturity: early
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "vercel/mcp-handler on GitHub"
    url: https://github.com/vercel/mcp-handler
    type: github-repository
    organization: vercel
    license: NONE
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# vercel/mcp-handler

🟢 ACTIVE · tier **UNVERIFIED** · early · confidence **high**

> Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/vercel/mcp-handler> |
| Owner | vercel (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `NONE` |
| Stars | 669 (checked 2026-09-15) |
| Forks | 88 |
| Open issues | 36 |
| Contributors | 25 |
| Last push | 2026-09-08 (7 days before verification) |
| Latest release | v2.1.1 (2026-08-13) |
| Archived | no |
| Fork | no |
| Homepage | https://www.npmjs.com/package/mcp-handler |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 9.56 |
| documentation | 6.98 |
| reproducibility | 6.5 |
| security | 2.5 |
| recency | 9.9 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.02** |
| **trust_score** | **6.85** |

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
| examples | yes |
| security md | no |
| changelog | yes |
| contributing | no |
| root entries | yes |
| README size | 5,706 bytes |

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

Repository moved: `vercel/mcp-adapter` -> `vercel/mcp-handler`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. NO LICENSE FILE DETECTED by GitHub. Copyright defaults to all-rights-reserved: do not vendor, copy or redistribute code from this repository. Reference and link only.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug vercel/mcp-handler
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
