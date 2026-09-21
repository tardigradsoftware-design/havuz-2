---
id: berriai--litellm
title: "BerriAI/litellm"
domain: agent-frameworks
summary: >-
  BerriAI/litellm — ACTIVE, tier A,
  59,304 stars, license NOASSERTION, quality 9.21/10, trust 9.4/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-frameworks", "gateway", "github-repository", "multi-provider", "proxy"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.5, "reproducibility": 9.6, "security": 6.5, "recency": 10.0, "evidence": 8.5}
  quality_score: 9.21
  trust_score: 9.4
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "BerriAI/litellm on GitHub"
    url: https://github.com/BerriAI/litellm
    type: github-repository
    organization: BerriAI
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# BerriAI/litellm

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging \[Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM\]

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/BerriAI/litellm> |
| Owner | BerriAI (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `NOASSERTION` |
| Stars | 59,304 (checked 2026-09-21) |
| Forks | 11,630 |
| Open issues | 5,223 |
| Contributors | 375 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v1.101.0 (2026-09-15) |
| Archived | no |
| Fork | no |
| Homepage | [https://docs.litellm.ai/docs/](https://docs.litellm.ai/docs/) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.5 |
| reproducibility | 9.6 |
| security | 6.5 |
| recency | 10.0 |
| evidence | 8.5 |
| **quality_score** (weighted) | **9.21** |
| **trust_score** | **9.4** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 36,015 bytes |

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

Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug BerriAI/litellm
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
