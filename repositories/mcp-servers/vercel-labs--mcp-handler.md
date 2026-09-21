---
id: vercel-labs--mcp-handler
title: "vercel-labs/mcp-handler"
domain: mcp-servers
summary: >-
  vercel-labs/mcp-handler — ACTIVE, tier NO-LICENSE,
  670 stars, license NONE, quality 7.34/10, trust 5.36/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["adapter", "github-repository", "mcp", "mcp-servers", "vercel"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 5.5, "maintenance": 10.0, "adoption": 9.57, "documentation": 7.05, "reproducibility": 6.5, "security": 1.5, "recency": 9.97, "evidence": 8.0}
  quality_score: 7.34
  trust_score: 5.36
  tier: NO-LICENSE
  maturity: early
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "vercel-labs/mcp-handler on GitHub"
    url: https://github.com/vercel-labs/mcp-handler
    type: github-repository
    organization: vercel-labs
    license: NONE
    license_risk: no-license-do-not-redistribute
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# vercel-labs/mcp-handler

🟢 ACTIVE · tier **NO-LICENSE** · early · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

> ⚠️ **LICENSE RISK — `no-license-do-not-redistribute`.** GitHub detected **no license file**
> on 2026-09-21. Default copyright applies, so all rights are reserved: **reference and link only**.
> Do not vendor, copy, quote at length, or redistribute any file from this repository, however
> useful it looks. A high star count does not create a license.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/vercel-labs/mcp-handler> |
| Owner | vercel-labs (Organization) |
| Official upstream | no |
| Language | TypeScript |
| License | `NONE` |
| Stars | 670 (checked 2026-09-21) |
| Forks | 89 |
| Open issues | 35 |
| Contributors | 26 |
| Last push | 2026-09-18 (2 days before verification) |
| Latest release | v2.2.0 (2026-09-18) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.npmjs.com/package/mcp-handler](https://www.npmjs.com/package/mcp-handler) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 10.0 |
| adoption | 9.57 |
| documentation | 7.05 |
| reproducibility | 6.5 |
| security | 1.5 |
| recency | 9.97 |
| evidence | 8.0 |
| **quality_score** (weighted) | **7.34** |
| **trust_score** | **5.36** |

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
| README size | 6,659 bytes |

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

Repository moved: `vercel/mcp-adapter` -> `vercel-labs/mcp-handler`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. NO LICENSE FILE DETECTED by GitHub. Copyright defaults to all-rights-reserved: do not vendor, copy or redistribute code from this repository. Reference and link only.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug vercel-labs/mcp-handler
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
