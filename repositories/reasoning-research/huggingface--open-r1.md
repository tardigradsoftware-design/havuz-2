---
id: huggingface--open-r1
title: "huggingface/open-r1"
domain: reasoning-research
summary: >-
  huggingface/open-r1 — STABLE, tier S,
  26,478 stars, license Apache-2.0, quality 8.14/10, trust 7.81/10.
  Verified against the GitHub API on 2026-09-28.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "open-reproduction", "reasoning", "reasoning-research"]
version: 1.0.0
updated: 2026-09-28
verified_at: 2026-09-28
expires_at: 2026-11-12
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.42, "reproducibility": 8.5, "security": 4.5, "recency": 9.96, "evidence": 6.0}
  quality_score: 8.14
  trust_score: 7.81
  tier: S
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-28
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
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-28
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-28)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# huggingface/open-r1

🔵 STABLE · tier **S** · published-artifact · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Fully open reproduction of DeepSeek-R1

## Facts (verified 2026-09-28 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/huggingface/open-r1> |
| Owner | huggingface (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 26,478 (checked 2026-09-28) |
| Forks | 2,453 |
| Open issues | 343 |
| Contributors | 44 |
| Last push | 2026-09-24 (3 days before verification) |
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
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.42 |
| reproducibility | 8.5 |
| security | 4.5 |
| recency | 9.96 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.14** |
| **trust_score** | **7.81** |

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
