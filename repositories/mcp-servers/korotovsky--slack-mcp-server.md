---
id: korotovsky--slack-mcp-server
title: "korotovsky/slack-mcp-server"
domain: mcp-servers
summary: >-
  korotovsky/slack-mcp-server — STABLE, tier A,
  1,829 stars, license MIT, quality 7.06/10, trust 5.85/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "mcp", "mcp-servers", "slack"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 4.5, "maintenance": 7.5, "adoption": 10.0, "documentation": 7.66, "reproducibility": 7.5, "security": 6.0, "recency": 9.18, "evidence": 5.0}
  quality_score: 7.06
  trust_score: 5.85
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "korotovsky/slack-mcp-server on GitHub"
    url: https://github.com/korotovsky/slack-mcp-server
    type: github-repository
    organization: korotovsky
    license: MIT
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# korotovsky/slack-mcp-server

🔵 STABLE · tier **A** · production-ready · confidence **medium**

> The most powerful MCP Slack Server with no permission requirements, Apps support, GovSlack, DMs, Group DMs and smart history fetch logic.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/korotovsky/slack-mcp-server> |
| Owner | korotovsky (User) |
| Official upstream | no |
| Language | Go |
| License | `MIT` |
| Stars | 1,829 (checked 2026-09-15) |
| Forks | 367 |
| Open issues | 73 |
| Contributors | 52 |
| Last push | 2026-07-16 (60 days before verification) |
| Latest release | v1.3.0 (2026-05-14) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 4.5 |
| maintenance | 7.5 |
| adoption | 10.0 |
| documentation | 7.66 |
| reproducibility | 7.5 |
| security | 6.0 |
| recency | 9.18 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.06** |
| **trust_score** | **5.85** |

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
| contributing | no |
| root entries | yes |
| README size | 31,951 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug korotovsky/slack-mcp-server
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
