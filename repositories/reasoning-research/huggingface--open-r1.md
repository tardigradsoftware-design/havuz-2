---
id: huggingface--open-r1
title: "huggingface/open-r1"
domain: reasoning-research
summary: >-
  huggingface/open-r1 — STABLE, tier A,
  26,478 stars, license Apache-2.0, quality 7.23/10, trust 6.91/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "open-reproduction", "reasoning", "reasoning-research"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 5.5, "adoption": 10.0, "documentation": 6.42, "reproducibility": 8.5, "security": 4.5, "recency": 7.66, "evidence": 6.0}
  quality_score: 7.23
  trust_score: 6.91
  tier: A
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "huggingface/open-r1 on GitHub"
    url: https://github.com/huggingface/open-r1
    type: github-repository
    organization: huggingface
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# huggingface/open-r1

🔵 STABLE · tier **A** · published-artifact · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Fully open reproduction of DeepSeek-R1

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/huggingface/open-r1> |
| Owner | huggingface (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 26,478 (checked 2026-09-21) |
| Forks | 2,452 |
| Open issues | 340 |
| Contributors | 44 |
| Last push | 2026-04-02 (171 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `research-artifact` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 5.5 |
| adoption | 10.0 |
| documentation | 6.42 |
| reproducibility | 8.5 |
| security | 4.5 |
| recency | 7.66 |
| evidence | 6.0 |
| **quality_score** (weighted) | **7.23** |
| **trust_score** | **6.91** |

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
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 34,997 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug huggingface/open-r1
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
