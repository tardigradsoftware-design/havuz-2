---
id: sooperset--mcp-atlassian
title: "sooperset/mcp-atlassian"
domain: mcp-servers
summary: >-
  sooperset/mcp-atlassian — ACTIVE, tier S,
  5,901 stars, license MIT, quality 8.54/10, trust 8.24/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["confluence", "github-repository", "jira", "mcp", "mcp-servers"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 7.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.93, "reproducibility": 9.5, "security": 7.0, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.54
  trust_score: 8.24
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "sooperset/mcp-atlassian on GitHub"
    url: https://github.com/sooperset/mcp-atlassian
    type: github-repository
    organization: sooperset
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# sooperset/mcp-atlassian

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> MCP server for Atlassian tools (Confluence, Jira)

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/sooperset/mcp-atlassian> |
| Owner | sooperset (User) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 5,901 (checked 2026-09-15) |
| Forks | 1,358 |
| Open issues | 227 |
| Contributors | 181 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v0.23.1 (2026-08-19) |
| Archived | no |
| Fork | no |
| Homepage | https://mcp-atlassian.soomiles.com |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 7.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.93 |
| reproducibility | 9.5 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.54** |
| **trust_score** | **8.24** |

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
| README size | 5,134 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug sooperset/mcp-atlassian
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
