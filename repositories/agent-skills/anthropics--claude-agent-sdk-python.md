---
id: anthropics--claude-agent-sdk-python
title: "anthropics/claude-agent-sdk-python"
domain: agent-skills
summary: >-
  anthropics/claude-agent-sdk-python — ACTIVE, tier S,
  8,100 stars, license MIT, quality 8.25/10, trust 7.9/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "anthropic", "github-repository", "sdk"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 4.52, "reproducibility": 10.0, "security": 4.5, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.25
  trust_score: 7.9
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "anthropics/claude-agent-sdk-python on GitHub"
    url: https://github.com/anthropics/claude-agent-sdk-python
    type: github-repository
    organization: anthropics
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# anthropics/claude-agent-sdk-python

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _No description published._

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/anthropics/claude-agent-sdk-python> |
| Owner | anthropics (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 8,100 (checked 2026-09-15) |
| Forks | 1,277 |
| Open issues | 457 |
| Contributors | 71 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v0.2.152 (2026-09-02) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 4.52 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.25** |
| **trust_score** | **7.9** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | yes |
| examples | yes |
| security md | no |
| changelog | yes |
| contributing | no |
| root entries | yes |
| README size | 12,277 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug anthropics/claude-agent-sdk-python
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
