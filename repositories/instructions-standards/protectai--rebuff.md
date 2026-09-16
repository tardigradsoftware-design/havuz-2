---
id: protectai--rebuff
title: "protectai/rebuff"
domain: instructions-standards
summary: >-
  protectai/rebuff — ARCHIVED, tier ARCHIVED,
  1,522 stars, license Apache-2.0, quality 5.32/10, trust 3.42/10.
  Verified against the GitHub API on 2026-09-15.
status: deprecated
confidence: low
claim_type: fact
evidence_level: verified-github-api
tags: ["abandoned-candidate", "github-repository", "instructions-standards", "prompt-injection"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 0.5, "adoption": 10.0, "documentation": 6.48, "reproducibility": 7.5, "security": 1.5, "recency": 0.0, "evidence": 4.0}
  quality_score: 5.32
  trust_score: 3.42
  tier: ARCHIVED
  maturity: end-of-life
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "protectai/rebuff on GitHub"
    url: https://github.com/protectai/rebuff
    type: github-repository
    organization: protectai
    license: Apache-2.0
    license_risk: none
    confidence: low
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# protectai/rebuff

⛔ ARCHIVED · tier **ARCHIVED** · end-of-life · confidence **low**

> _Upstream description, quoted as published and not verified here:_
>
> LLM Prompt Injection Detector

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/protectai/rebuff> |
| Owner | protectai (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 1,522 (checked 2026-09-15) |
| Forks | 146 |
| Open issues | 33 |
| Contributors | 9 |
| Last push | 2024-08-07 (768 days before verification) |
| Latest release | v0.1.1 (2024-01-20) |
| Archived | **YES** |
| Fork | no |
| Homepage | [https://playground.rebuff.ai](https://playground.rebuff.ai) |
| SECURITY.md | no → `archived-no-patches` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 0.5 |
| adoption | 10.0 |
| documentation | 6.48 |
| reproducibility | 7.5 |
| security | 1.5 |
| recency | 0.0 |
| evidence | 4.0 |
| **quality_score** (weighted) | **5.32** |
| **trust_score** | **3.42** |

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
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 5,775 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Reading about early prompt-injection detection approaches

**Not recommended for**

- Production prompt-injection defence - the project is ARCHIVED (last push 768 days before verification)

**Strengths**

- Apache-2.0
- One of the first dedicated prompt-injection detectors

**Weaknesses**

- ARCHIVED and unmaintained for over two years
- Detection-only; no mitigation path

**Related projects**

- NVIDIA/garak
- protectai/llm-guard
- promptfoo/promptfoo

## Verification notes

ARCHIVED by owner: read-only, receives no fixes or security patches. Do not start new work on it; look for the successor project. Verified 2026-09-15: archived. protectai/llm-guard is also archived. Both are recorded so that agents do not recommend dead defences.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug protectai/rebuff
python3 scripts/generate-index/generate_repository_cards.py --category instructions-standards
```
