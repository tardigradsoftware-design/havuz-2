---
id: modelcontextprotocol--servers
title: "modelcontextprotocol/servers"
domain: mcp-servers
summary: >-
  modelcontextprotocol/servers — ACTIVE, tier A,
  90,358 stars, license NOASSERTION, quality 8.02/10, trust 7.81/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "reference-servers"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.73, "reproducibility": 6.1, "security": 6.5, "recency": 9.84, "evidence": 5.0}
  quality_score: 8.02
  trust_score: 7.81
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "modelcontextprotocol/servers on GitHub"
    url: https://github.com/modelcontextprotocol/servers
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

# modelcontextprotocol/servers

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Model Context Protocol Servers

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-15, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/modelcontextprotocol/servers> |
| Owner | modelcontextprotocol (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `NOASSERTION` |
| Stars | 90,358 (checked 2026-09-15) |
| Forks | 11,638 |
| Open issues | 534 |
| Contributors | 427 |
| Last push | 2026-09-03 (12 days before verification) |
| Latest release | 2026.8.31 (2026-08-31) |
| Archived | no |
| Fork | no |
| Homepage | [https://modelcontextprotocol.io](https://modelcontextprotocol.io) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.73 |
| reproducibility | 6.1 |
| security | 6.5 |
| recency | 9.84 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.02** |
| **trust_score** | **7.81** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 8,707 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug modelcontextprotocol/servers
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
