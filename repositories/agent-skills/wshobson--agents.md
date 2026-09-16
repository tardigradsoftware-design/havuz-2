---
id: wshobson--agents
title: "wshobson/agents"
domain: agent-skills
summary: >-
  wshobson/agents — ACTIVE, tier A,
  39,683 stars, license MIT, quality 7.14/10, trust 5.96/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "github-repository", "marketplace", "multi-harness", "skills"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.37, "reproducibility": 6.5, "security": 3.5, "recency": 9.99, "evidence": 4.0}
  quality_score: 7.14
  trust_score: 5.96
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "wshobson/agents on GitHub"
    url: https://github.com/wshobson/agents
    type: github-repository
    organization: wshobson
    license: MIT
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# wshobson/agents

🟢 ACTIVE · tier **A** · production-grade · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Multi-harness agentic plugin marketplace for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Google Antigravity, and Pi

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/wshobson/agents> |
| Owner | wshobson (User) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 39,683 (checked 2026-09-15) |
| Forks | 4,226 |
| Open issues | 7 |
| Contributors | 79 |
| Last push | 2026-09-14 (1 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://sethhobson.com](https://sethhobson.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.37 |
| reproducibility | 6.5 |
| security | 3.5 |
| recency | 9.99 |
| evidence | 4.0 |
| **quality_score** (weighted) | **7.14** |
| **trust_score** | **5.96** |

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
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 10,444 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug wshobson/agents
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
