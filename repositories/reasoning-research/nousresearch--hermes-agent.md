---
id: nousresearch--hermes-agent
title: "NousResearch/hermes-agent"
domain: reasoning-research
summary: >-
  NousResearch/hermes-agent — ACTIVE, tier S,
  247,608 stars, license MIT, quality 9.05/10, trust 9.05/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "github-repository", "reasoning-research", "self-improving"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.51, "reproducibility": 9.5, "security": 7.0, "recency": 10.0, "evidence": 7.5}
  quality_score: 9.05
  trust_score: 9.05
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "NousResearch/hermes-agent on GitHub"
    url: https://github.com/NousResearch/hermes-agent
    type: github-repository
    organization: NousResearch
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# NousResearch/hermes-agent

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> The agent that grows with you

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/NousResearch/hermes-agent> |
| Owner | NousResearch (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 247,608 (checked 2026-09-21) |
| Forks | 52,096 |
| Open issues | 43,122 |
| Contributors | 397 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v2026.9.14 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | [https://hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.51 |
| reproducibility | 9.5 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **9.05** |
| **trust_score** | **9.05** |

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
| README size | 24,070 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-21) and must be
re-checked against your own constraints._

**Recommended for**

- Studying self-improving agent architecture
- Agents that synthesise skills from their own successful trajectories
- Open, MIT-licensed reference for procedural memory

**Not recommended for**

- Assuming it is a drop-in replacement for a coding harness without reading its docs
- Environments that cannot tolerate an agent writing to its own skill store

**Strengths**

- Highest quality score in this registry (9.05 verified 2026-09-15)
- MIT license, 401 contributors, dated releases (v2026.9.14)
- Explicit self-improvement loop: experience -> skill candidate -> validated skill
- Very high adoption for an agent project (245k+ stars verified)

**Weaknesses**

- Self-modifying skill stores are a security surface: a bad trajectory can poison future runs
- Fast-moving; APIs and skill formats change between dated releases

**Related projects**

- obra/superpowers
- anthropics/skills
- VoltAgent/awesome-agent-skills
- thedotmack/claude-mem

## Verification notes

Verified 2026-09-15: ACTIVE, MIT, release v2026.9.14. The initial seed slug 404'd on the first run and was confirmed via GitHub search before being re-fetched - see metadata/fetch-report.json.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug NousResearch/hermes-agent
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
