---
id: meta-llama--llama-models
title: "meta-llama/llama-models"
domain: reasoning-research
summary: >-
  meta-llama/llama-models — STABLE, tier B,
  7,694 stars, license NOASSERTION, quality 6.67/10, trust 6.33/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "open-model", "reasoning-research"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 3.5, "adoption": 10.0, "documentation": 6.34, "reproducibility": 6.1, "security": 6.5, "recency": 6.97, "evidence": 4.5}
  quality_score: 6.67
  trust_score: 6.33
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "meta-llama/llama-models on GitHub"
    url: https://github.com/meta-llama/llama-models
    type: github-repository
    organization: meta-llama
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# meta-llama/llama-models

🔵 STABLE · tier **B** · published-artifact · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Utilities intended for use with Llama models.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/meta-llama/llama-models> |
| Owner | meta-llama (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `NOASSERTION` |
| Stars | 7,694 (checked 2026-09-21) |
| Forks | 1,407 |
| Open issues | 220 |
| Contributors | 40 |
| Last push | 2026-02-11 (221 days before verification) |
| Latest release | v0.2.0 (2025-04-05) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `model-release` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 3.5 |
| adoption | 10.0 |
| documentation | 6.34 |
| reproducibility | 6.1 |
| security | 6.5 |
| recency | 6.97 |
| evidence | 4.5 |
| **quality_score** (weighted) | **6.67** |
| **trust_score** | **6.33** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 10,065 bytes |

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

Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine. Reference implementation published with a model-release. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug meta-llama/llama-models
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
