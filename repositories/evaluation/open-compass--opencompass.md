---
id: open-compass--opencompass
title: "open-compass/opencompass"
domain: evaluation
summary: >-
  open-compass/opencompass — STABLE, tier S,
  7,463 stars, license Apache-2.0, quality 8.9/10, trust 8.97/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["benchmark", "evaluation", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.96, "reproducibility": 10.0, "security": 4.5, "recency": 10.0, "evidence": 8.5}
  quality_score: 8.9
  trust_score: 8.97
  tier: S
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "open-compass/opencompass on GitHub"
    url: https://github.com/open-compass/opencompass
    type: github-repository
    organization: open-compass
    license: Apache-2.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# open-compass/opencompass

🔵 STABLE · tier **S** · published-artifact · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> OpenCompass is an LLM evaluation platform, supporting a wide range of models from OpenAI, Anthropic, Gemini, Qwen, GLM, DeepSeek, etc, across 100+ datasets covering knowledge, reasoning, coding, science, language, long-context, and safety.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/open-compass/opencompass> |
| Owner | open-compass (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 7,463 (checked 2026-09-21) |
| Forks | 869 |
| Open issues | 404 |
| Contributors | 183 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | 0.5.4 (2026-08-26) |
| Archived | no |
| Fork | no |
| Homepage | [https://opencompass.org.cn/](https://opencompass.org.cn/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.96 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 8.5 |
| **quality_score** (weighted) | **8.9** |
| **trust_score** | **8.97** |

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
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 23,546 bytes |

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

Reference implementation published with a benchmark. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug open-compass/opencompass
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
