---
id: modelcontextprotocol--servers
title: "modelcontextprotocol/servers"
domain: mcp-servers
summary: >-
  modelcontextprotocol/servers — ACTIVE, tier A,
  91,166 stars, license NOASSERTION, quality 8.18/10, trust 8.03/10.
  Verified against the GitHub API on 2026-10-12.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "reference-servers"]
version: 1.0.0
updated: 2026-10-12
verified_at: 2026-10-12
expires_at: 2026-11-26
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.23, "reproducibility": 6.1, "security": 6.5, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.18
  trust_score: 8.03
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-12
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
    verified_at: 2026-10-12
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-12)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# modelcontextprotocol/servers

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Model Context Protocol Servers

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-10-12, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-10-12 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/modelcontextprotocol/servers> |
| Owner | modelcontextprotocol (Organization) |
| Official upstream | yes |
| Language | JavaScript |
| License | `NOASSERTION` |
| Stars | 91,166 (checked 2026-10-12) |
| Forks | 11,780 |
| Open issues | 489 |
| Contributors | 428 |
| Last push | 2026-10-12 (0 days before verification) |
| Latest release | v1.0.0 (2026-10-11) |
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
| documentation | 7.23 |
| reproducibility | 6.1 |
| security | 6.5 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.18** |
| **trust_score** | **8.03** |

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
