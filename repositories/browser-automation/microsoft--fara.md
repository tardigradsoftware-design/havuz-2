---
id: microsoft--fara
title: "microsoft/fara"
domain: browser-automation
summary: >-
  microsoft/fara — STABLE, tier A,
  6,178 stars, license MIT, quality 7.74/10, trust 7.31/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["browser-automation", "computer-use", "github-repository", "model", "official"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 7.0, "adoption": 10.0, "documentation": 7.6, "reproducibility": 6.5, "security": 7.0, "recency": 9.26, "evidence": 3.5}
  quality_score: 7.74
  trust_score: 7.31
  tier: A
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "microsoft/fara on GitHub"
    url: https://github.com/microsoft/fara
    type: github-repository
    organization: microsoft
    license: MIT
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# microsoft/fara

🔵 STABLE · tier **A** · published-artifact · confidence **high**

> Fara1.5 – A family of frontier computer use agent models

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/microsoft/fara> |
| Owner | microsoft (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 6,178 (checked 2026-09-15) |
| Forks | 604 |
| Open issues | 41 |
| Contributors | 7 |
| Last push | 2026-07-22 (54 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | https://www.microsoft.com/en-us/research/articles/fara1-5-computer-use-agent/ |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `model-release` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 7.0 |
| adoption | 10.0 |
| documentation | 7.6 |
| reproducibility | 6.5 |
| security | 7.0 |
| recency | 9.26 |
| evidence | 3.5 |
| **quality_score** (weighted) | **7.74** |
| **trust_score** | **7.31** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | yes |
| ci | no |
| examples | no |
| security md | yes |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 19,152 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Studying frontier computer-use agent models from a major lab
- Comparing vision-grounded computer use against DOM-based automation

**Not recommended for**

- Assuming the weights are freely redistributable without reading the license

**Strengths**

- Official Microsoft release of a computer-use agent model family
- Directly relevant to the computer-use section of this knowledge base

**Weaknesses**

- Newer and less battle-tested than DOM-based automation
- Computer-use agents operate at the pixel level, so they are slower and less reliable than accessibility-tree approaches

**Related projects**

- microsoft/OmniParser
- bytedance/UI-TARS-desktop
- trycua/cua
- xlang-ai/OSWorld

## Verification notes

Reference implementation published with a model-release. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance. Discovered via topic:computer-use search on 2026-09-15.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug microsoft/fara
python3 scripts/generate-index/generate_repository_cards.py --category browser-automation
```
