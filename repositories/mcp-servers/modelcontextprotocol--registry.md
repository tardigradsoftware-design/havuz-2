---
id: modelcontextprotocol--registry
title: "modelcontextprotocol/registry"
domain: mcp-servers
summary: >-
  modelcontextprotocol/registry — ACTIVE, tier A,
  7,250 stars, license NOASSERTION, quality 8.62/10, trust 8.53/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "registry"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.18, "reproducibility": 8.6, "security": 6.5, "recency": 9.93, "evidence": 7.0}
  quality_score: 8.62
  trust_score: 8.53
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "modelcontextprotocol/registry on GitHub"
    url: https://github.com/modelcontextprotocol/registry
    type: github-repository
    organization: modelcontextprotocol
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

# modelcontextprotocol/registry

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A community driven registry service for Model Context Protocol (MCP) servers.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-15, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/modelcontextprotocol/registry> |
| Owner | modelcontextprotocol (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `NOASSERTION` |
| Stars | 7,250 (checked 2026-09-15) |
| Forks | 988 |
| Open issues | 167 |
| Contributors | 72 |
| Last push | 2026-09-09 (5 days before verification) |
| Latest release | v1.8.1 (2026-08-06) |
| Archived | no |
| Fork | no |
| Homepage | [https://github.com/modelcontextprotocol/registry/tree/main/docs](https://github.com/modelcontextprotocol/registry/tree/main/docs) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.18 |
| reproducibility | 8.6 |
| security | 6.5 |
| recency | 9.93 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.62** |
| **trust_score** | **8.53** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 8,193 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug modelcontextprotocol/registry
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
