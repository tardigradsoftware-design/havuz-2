---
id: getsentry--toolkit
title: "getsentry/toolkit"
domain: mcp-servers
summary: >-
  getsentry/toolkit — ACTIVE, tier A,
  912 stars, license NOASSERTION, quality 7.95/10, trust 7.73/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "observability", "sentry"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.89, "reproducibility": 6.6, "security": 4.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 7.95
  trust_score: 7.73
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "getsentry/toolkit on GitHub"
    url: https://github.com/getsentry/toolkit
    type: github-repository
    organization: getsentry
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: very-high
    claim_type: fact
    verified_at: 2026-10-05
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-05)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# getsentry/toolkit

🟢 ACTIVE · tier **A** · production-ready · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Agentic tooling for Sentry

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-10-05, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/getsentry/toolkit> |
| Owner | getsentry (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `NOASSERTION` |
| Stars | 912 (checked 2026-10-05) |
| Forks | 159 |
| Open issues | 128 |
| Contributors | 82 |
| Last push | 2026-10-05 (0 days before verification) |
| Latest release | cli@0.46.0 (2026-10-01) |
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
| documentation | 6.89 |
| reproducibility | 6.6 |
| security | 4.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.95** |
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
| README size | 10,677 bytes |

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

Repository moved: `getsentry/sentry-mcp` -> `getsentry/toolkit`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug getsentry/toolkit
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
