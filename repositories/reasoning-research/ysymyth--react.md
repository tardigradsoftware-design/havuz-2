---
id: ysymyth--react
title: "ysymyth/ReAct"
domain: reasoning-research
summary: >-
  ysymyth/ReAct — STABLE, tier C,
  4,183 stars, license MIT, quality 4.41/10, trust 4.1/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "paper-code", "reasoning", "reasoning-research", "tool-use"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 7.5, "maintenance": 1.0, "adoption": 10.0, "documentation": 3.65, "reproducibility": 4.5, "security": 3.5, "recency": 0.0, "evidence": 1.0}
  quality_score: 4.41
  trust_score: 4.1
  tier: C
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "ysymyth/ReAct on GitHub"
    url: https://github.com/ysymyth/ReAct
    type: github-repository
    organization: ysymyth
    license: MIT
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# ysymyth/ReAct

🔵 STABLE · tier **C** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> \[ICLR 2023\] ReAct: Synergizing Reasoning and Acting in Language Models

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/ysymyth/ReAct> |
| Owner | ysymyth (User) |
| Official upstream | yes |
| Language | Jupyter Notebook |
| License | `MIT` |
| Stars | 4,183 (checked 2026-09-21) |
| Forks | 401 |
| Open issues | 5 |
| Contributors | 2 |
| Last push | 2024-02-06 (958 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `research-artifact` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 7.5 |
| maintenance | 1.0 |
| adoption | 10.0 |
| documentation | 3.65 |
| reproducibility | 4.5 |
| security | 3.5 |
| recency | 0.0 |
| evidence | 1.0 |
| **quality_score** (weighted) | **4.41** |
| **trust_score** | **4.1** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 1,808 bytes |

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

Reference implementation published with a research-artifact. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug ysymyth/ReAct
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
