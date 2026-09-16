---
id: q00--ouroboros
title: "Q00/ouroboros"
domain: agent-frameworks
summary: >-
  Q00/ouroboros — ACTIVE, tier S,
  5,908 stars, license MIT, quality 8.45/10, trust 7.72/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-frameworks", "agent-os", "github-repository", "self-improving"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 10.0, "reproducibility": 10.0, "security": 6.0, "recency": 10.0, "evidence": 8.5}
  quality_score: 8.45
  trust_score: 7.72
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "Q00/ouroboros on GitHub"
    url: https://github.com/Q00/ouroboros
    type: github-repository
    organization: Q00
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# Q00/ouroboros

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> Agent OS: the agent gets smarter on its own. We just hold the line: Interview-gated, staged evaluation, budgeted evolution loop. MCP server, 14 runtimes: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot, Kiro and more.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/Q00/ouroboros> |
| Owner | Q00 (User) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 5,908 (checked 2026-09-15) |
| Forks | 599 |
| Open issues | 105 |
| Contributors | 81 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | v0.54.4 (2026-09-13) |
| Archived | no |
| Fork | no |
| Homepage | https://ouroboros.page/ |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 10.0 |
| reproducibility | 10.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 8.5 |
| **quality_score** (weighted) | **8.45** |
| **trust_score** | **7.72** |

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
| README size | 39,012 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug Q00/ouroboros
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
