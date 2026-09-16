---
id: httpie--cli
title: "httpie/cli"
domain: developer-tools
summary: >-
  httpie/cli — ABANDONED, tier B,
  38,515 stars, license BSD-3-Clause, quality 6.7/10, trust 7.06/10.
  Verified against the GitHub API on 2026-09-15.
status: deprecated
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["api-client", "cli", "developer-tools", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 2.0, "adoption": 10.0, "documentation": 7.41, "reproducibility": 9.35, "security": 6.0, "recency": 1.29, "evidence": 7.0}
  quality_score: 6.7
  trust_score: 7.06
  tier: B
  maturity: end-of-life
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "httpie/cli on GitHub"
    url: https://github.com/httpie/cli
    type: github-repository
    organization: httpie
    license: BSD-3-Clause
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# httpie/cli

🔴 ABANDONED · tier **B** · end-of-life · confidence **high**

> 🥧 HTTPie CLI  — modern, user-friendly command-line HTTP client for the API era. JSON support, colors, sessions, downloads, plugins & more.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/httpie/cli> |
| Owner | httpie (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `BSD-3-Clause` |
| Stars | 38,515 (checked 2026-09-15) |
| Forks | 4,002 |
| Open issues | 338 |
| Contributors | 147 |
| Last push | 2024-12-17 (636 days before verification) |
| Latest release | 3.2.4 (2024-11-01) |
| Archived | no |
| Fork | no |
| Homepage | https://httpie.io |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 2.0 |
| adoption | 10.0 |
| documentation | 7.41 |
| reproducibility | 9.35 |
| security | 6.0 |
| recency | 1.29 |
| evidence | 7.0 |
| **quality_score** (weighted) | **6.7** |
| **trust_score** | **7.06** |

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
| examples | no |
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 4,893 bytes |

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

No push in 636 days (>365d). Likely abandoned; prefer an actively maintained alternative.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug httpie/cli
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
