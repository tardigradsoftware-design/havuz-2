---
id: getsentry--sentry-mcp
title: "getsentry/sentry-mcp"
domain: mcp-servers
summary: >-
  getsentry/sentry-mcp — ACTIVE, tier A,
  853 stars, license NOASSERTION, quality 7.94/10, trust 7.73/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "observability", "sentry"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.84, "reproducibility": 6.6, "security": 4.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 7.94
  trust_score: 7.73
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "getsentry/sentry-mcp on GitHub"
    url: https://github.com/getsentry/sentry-mcp
    type: github-repository
    organization: getsentry
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# getsentry/sentry-mcp

🟢 ACTIVE · tier **A** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> An MCP server for interacting with Sentry via LLMs.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-15, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/getsentry/sentry-mcp> |
| Owner | getsentry (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `NOASSERTION` |
| Stars | 853 (checked 2026-09-15) |
| Forks | 144 |
| Open issues | 112 |
| Contributors | 68 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | 0.39.0 (2026-08-27) |
| Archived | no |
| Fork | no |
| Homepage | [https://mcp.sentry.dev](https://mcp.sentry.dev) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.84 |
| reproducibility | 6.6 |
| security | 4.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.94** |
| **trust_score** | **7.73** |

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
| contributing | no |
| root entries | yes |
| README size | 10,052 bytes |

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

Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug getsentry/sentry-mcp
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
