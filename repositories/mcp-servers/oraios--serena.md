---
id: oraios--serena
title: "oraios/serena"
domain: mcp-servers
summary: >-
  oraios/serena — ACTIVE, tier A,
  29,662 stars, license NOASSERTION, quality 7.89/10, trust 7.09/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["coding", "github-repository", "mcp", "mcp-servers", "semantic-retrieval"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.26, "reproducibility": 8.6, "security": 3.0, "recency": 9.99, "evidence": 7.0}
  quality_score: 7.89
  trust_score: 7.09
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "oraios/serena on GitHub"
    url: https://github.com/oraios/serena
    type: github-repository
    organization: oraios
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# oraios/serena

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for your agent

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/oraios/serena> |
| Owner | oraios (Organization) |
| Official upstream | no |
| Language | Python |
| License | `NOASSERTION` |
| Stars | 29,662 (checked 2026-09-21) |
| Forks | 2,022 |
| Open issues | 206 |
| Contributors | 216 |
| Last push | 2026-09-19 (1 days before verification) |
| Latest release | v1.7.0 (2026-08-09) |
| Archived | no |
| Fork | no |
| Homepage | [https://oraios.github.io/serena](https://oraios.github.io/serena) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.26 |
| reproducibility | 8.6 |
| security | 3.0 |
| recency | 9.99 |
| evidence | 7.0 |
| **quality_score** (weighted) | **7.89** |
| **trust_score** | **7.09** |

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
| security md | no |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 15,097 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-21) and must be
re-checked against your own constraints._

**Recommended for**

- Semantic code retrieval and editing as an MCP toolkit
- Reducing token cost by giving agents symbol-level access instead of whole files

**Not recommended for**

- Repositories where an LSP server is unavailable for the language

**Strengths**

- Symbol-level retrieval maps directly onto the context-engineering goal of loading less and loading better
- High adoption for an MCP project (29k stars verified)

**Weaknesses**

- Depends on language-server infrastructure
- Filesystem plus code-edit permissions raise the risk level

**Related projects**

- DeusData/codebase-memory-mcp
- upstash/context7
- Graphify-Labs/graphify

## Verification notes

Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine. Discovered via topic:mcp-server search on 2026-09-15.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug oraios/serena
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
