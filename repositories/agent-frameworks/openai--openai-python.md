---
id: openai--openai-python
title: "openai/openai-python"
domain: agent-frameworks
summary: >-
  openai/openai-python — ACTIVE, tier S,
  31,623 stars, license Apache-2.0, quality 9.25/10, trust 9.38/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-frameworks", "github-repository", "openai", "sdk"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 10.0, "reproducibility": 10.0, "security": 7.0, "recency": 10.0, "evidence": 8.5}
  quality_score: 9.25
  trust_score: 9.38
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "openai/openai-python on GitHub"
    url: https://github.com/openai/openai-python
    type: github-repository
    organization: openai
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# openai/openai-python

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> The official Python library for the OpenAI API

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/openai/openai-python> |
| Owner | openai (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 31,623 (checked 2026-09-15) |
| Forks | 5,191 |
| Open issues | 306 |
| Contributors | 176 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v3.14.0 (2026-09-14) |
| Archived | no |
| Fork | no |
| Homepage | https://pypi.org/project/openai/ |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 10.0 |
| reproducibility | 10.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 8.5 |
| **quality_score** (weighted) | **9.25** |
| **trust_score** | **9.38** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 40,091 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug openai/openai-python
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
