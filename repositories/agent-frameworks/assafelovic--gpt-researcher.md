---
id: assafelovic--gpt-researcher
title: "assafelovic/gpt-researcher"
domain: agent-frameworks
summary: >-
  assafelovic/gpt-researcher — ACTIVE, tier S,
  29,918 stars, license Apache-2.0, quality 8.14/10, trust 7.23/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-frameworks", "deep-research", "github-repository"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 5.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.39, "reproducibility": 9.5, "security": 6.0, "recency": 9.96, "evidence": 7.5}
  quality_score: 8.14
  trust_score: 7.23
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "assafelovic/gpt-researcher on GitHub"
    url: https://github.com/assafelovic/gpt-researcher
    type: github-repository
    organization: assafelovic
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-10-05
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-05)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# assafelovic/gpt-researcher

🟢 ACTIVE · tier **S** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> An autonomous agent that conducts deep research on any data using any LLM providers

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/assafelovic/gpt-researcher> |
| Owner | assafelovic (User) |
| Official upstream | no |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 29,918 (checked 2026-10-05) |
| Forks | 4,084 |
| Open issues | 25 |
| Contributors | 252 |
| Last push | 2026-10-01 (3 days before verification) |
| Latest release | v3.7.0 (2026-09-26) |
| Archived | no |
| Fork | no |
| Homepage | [https://gptr.dev](https://gptr.dev) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.39 |
| reproducibility | 9.5 |
| security | 6.0 |
| recency | 9.96 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.14** |
| **trust_score** | **7.23** |

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
| README size | 22,628 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-10-05) and must be
re-checked against your own constraints._

**Recommended for**

- Deep multi-source research agents
- Reference architecture for plan -> search -> read -> synthesise -> cite loops

**Not recommended for**

- Assuming its output is fact-checked; it still needs an evidence-validation pass

**Strengths**

- Well-known reference implementation of an autonomous research agent
- High adoption (29k stars verified)

**Weaknesses**

- Research output quality depends entirely on the sources it retrieves
- Cost and latency grow with research depth

**Related projects**

- Ayanami0730/deep_research_bench
- exa-labs/exa-mcp-server
- firecrawl/firecrawl-mcp-server

## Verification notes

Discovered via topic:mcp-server search on 2026-09-15.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug assafelovic/gpt-researcher
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
