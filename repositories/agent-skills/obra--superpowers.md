---
id: obra--superpowers
title: "obra/superpowers"
domain: agent-skills
summary: >-
  obra/superpowers — ACTIVE, tier S,
  287,007 stars, license MIT, quality 8.1/10, trust 7.73/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-skills", "claude-code", "github-repository", "methodology", "skills"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 7.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.01, "reproducibility": 9.0, "security": 4.5, "recency": 10.0, "evidence": 6.5}
  quality_score: 8.1
  trust_score: 7.73
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "obra/superpowers on GitHub"
    url: https://github.com/obra/superpowers
    type: github-repository
    organization: obra
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# obra/superpowers

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> An agentic skills framework & software development methodology that works.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/obra/superpowers> |
| Owner | obra (User) |
| Official upstream | yes |
| Language | Shell |
| License | `MIT` |
| Stars | 287,007 (checked 2026-09-15) |
| Forks | 25,665 |
| Open issues | 367 |
| Contributors | 37 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | v6.3.0 (2026-08-12) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 7.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.01 |
| reproducibility | 9.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 6.5 |
| **quality_score** (weighted) | **8.1** |
| **trust_score** | **7.73** |

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
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 12,137 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Studying skill authoring discipline and skill testing
- Subagent-driven development, brainstorming, planning and review workflows
- Adopting a proven agentic software-development methodology

**Not recommended for**

- Blindly copying every skill without evaluating fit
- Treating it as a library dependency rather than a methodology reference

**Strengths**

- Extraordinary adoption for a methodology repo (287k stars verified, created 2025-10-09)
- MIT license, versioned releases (v6.3.0)
- Explicit skill-testing methodology and writing-skills guidance
- Workflow patterns (brainstorm -> plan -> implement -> review) map cleanly onto this repository's workflow format

**Weaknesses**

- Opinionated; some workflow steps assume a specific harness
- Growth this fast usually means documentation lags the code

**Related projects**

- anthropics/skills
- VoltAgent/awesome-agent-skills
- addyosmani/agent-skills
- NousResearch/hermes-agent

## Verification notes

Verified 2026-09-15: ACTIVE, MIT, q=8.1, 37 contributors. Analysed as a methodology source in knowledge/ai-engineering/agentic-coding/superpowers-analysis.md, not merely catalogued.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug obra/superpowers
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
