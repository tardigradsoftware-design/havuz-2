---
id: qwenlm--qwen3
title: "QwenLM/Qwen3"
domain: reasoning-research
summary: >-
  QwenLM/Qwen3 — STABLE, tier NO-LICENSE,
  27,624 stars, license NONE, quality 6.09/10, trust 4.66/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "open-model", "reasoning", "reasoning-research"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 3.5, "adoption": 10.0, "documentation": 7.06, "reproducibility": 3.5, "security": 2.5, "recency": 6.59, "evidence": 5.0}
  quality_score: 6.09
  trust_score: 4.66
  tier: NO-LICENSE
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "QwenLM/Qwen3 on GitHub"
    url: https://github.com/QwenLM/Qwen3
    type: github-repository
    organization: QwenLM
    license: NONE
    license_risk: no-license-do-not-redistribute
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# QwenLM/Qwen3

🔵 STABLE · tier **NO-LICENSE** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud.

> ⚠️ **LICENSE RISK — `no-license-do-not-redistribute`.** GitHub detected **no license file**
> on 2026-09-15. Default copyright applies, so all rights are reserved: **reference and link only**.
> Do not vendor, copy, quote at length, or redistribute any file from this repository, however
> useful it looks. A high star count does not create a license.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/QwenLM/Qwen3> |
| Owner | QwenLM (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `NONE` |
| Stars | 27,624 (checked 2026-09-15) |
| Forks | 2,058 |
| Open issues | 67 |
| Contributors | 46 |
| Last push | 2026-01-09 (249 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `model-release` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 3.5 |
| adoption | 10.0 |
| documentation | 7.06 |
| reproducibility | 3.5 |
| security | 2.5 |
| recency | 6.59 |
| evidence | 5.0 |
| **quality_score** (weighted) | **6.09** |
| **trust_score** | **4.66** |

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
| examples | yes |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 24,732 bytes |

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

NO LICENSE FILE DETECTED by GitHub. Copyright defaults to all-rights-reserved: do not vendor, copy or redistribute code from this repository. Reference and link only. Reference implementation published with a model-release. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug QwenLM/Qwen3
python3 scripts/generate-index/generate_repository_cards.py --category reasoning-research
```
