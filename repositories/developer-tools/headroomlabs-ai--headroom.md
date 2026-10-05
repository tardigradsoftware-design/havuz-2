---
id: headroomlabs-ai--headroom
title: "headroomlabs-ai/headroom"
domain: developer-tools
summary: >-
  headroomlabs-ai/headroom — ACTIVE, tier S,
  74,438 stars, license Apache-2.0, quality 8.63/10, trust 7.99/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["context-compression", "developer-tools", "github-repository", "rag"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.78, "reproducibility": 10.0, "security": 6.0, "recency": 10.0, "evidence": 8.5}
  quality_score: 8.63
  trust_score: 7.99
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "headroomlabs-ai/headroom on GitHub"
    url: https://github.com/headroomlabs-ai/headroom
    type: github-repository
    organization: headroomlabs-ai
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-10-05
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-05)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# headroomlabs-ai/headroom

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/headroomlabs-ai/headroom> |
| Owner | headroomlabs-ai (Organization) |
| Official upstream | no |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 74,438 (checked 2026-10-05) |
| Forks | 5,762 |
| Open issues | 447 |
| Contributors | 311 |
| Last push | 2026-10-05 (0 days before verification) |
| Latest release | v0.39.1 (2026-09-26) |
| Archived | no |
| Fork | no |
| Homepage | [https://docs.headroomlabs.ai/docs](https://docs.headroomlabs.ai/docs) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.78 |
| reproducibility | 10.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 8.5 |
| **quality_score** (weighted) | **8.63** |
| **trust_score** | **7.99** |

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
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 33,394 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug headroomlabs-ai/headroom
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
