---
id: arcboxlabs--arcbox
title: "arcboxlabs/arcbox"
domain: browser-automation
summary: >-
  arcboxlabs/arcbox — ACTIVE, tier S,
  4,225 stars, license Apache-2.0, quality 8.28/10, trust 7.4/10.
  Verified against the GitHub API on 2026-10-12.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-sandbox", "browser-automation", "github-repository", "isolation"]
version: 1.0.0
updated: 2026-10-12
verified_at: 2026-10-12
expires_at: 2026-11-26
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.31, "reproducibility": 9.5, "security": 6.0, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.28
  trust_score: 7.4
  tier: S
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-12
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "arcboxlabs/arcbox on GitHub"
    url: https://github.com/arcboxlabs/arcbox
    type: github-repository
    organization: arcboxlabs
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-10-12
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-12)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# arcboxlabs/arcbox

🟢 ACTIVE · tier **S** · production-ready · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Run AI agents on real and isolated machines — own kernel, filesystem, and network — with \<100ms boot. Local first, OCI compatible, pure Rust.

## Facts (verified 2026-10-12 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/arcboxlabs/arcbox> |
| Owner | arcboxlabs (Organization) |
| Official upstream | no |
| Language | Rust |
| License | `Apache-2.0` |
| Stars | 4,225 (checked 2026-10-12) |
| Forks | 187 |
| Open issues | 33 |
| Contributors | 12 |
| Last push | 2026-10-12 (0 days before verification) |
| Latest release | v0.9.0 (2026-10-07) |
| Archived | no |
| Fork | no |
| Homepage | [https://arcbox.dev](https://arcbox.dev) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.31 |
| reproducibility | 9.5 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.28** |
| **trust_score** | **7.4** |

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
| README size | 15,664 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug arcboxlabs/arcbox
python3 scripts/generate-index/generate_repository_cards.py --category browser-automation
```
