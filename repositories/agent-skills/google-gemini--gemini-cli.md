---
id: google-gemini--gemini-cli
title: "google-gemini/gemini-cli"
domain: agent-skills
summary: >-
  google-gemini/gemini-cli — ACTIVE, tier A,
  107,004 stars, license Apache-2.0, quality 7.81/10, trust 6.79/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "coding-agent", "github-repository", "google"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.62, "reproducibility": 7.5, "security": 6.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 7.81
  trust_score: 6.79
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "google-gemini/gemini-cli on GitHub"
    url: https://github.com/google-gemini/gemini-cli
    type: github-repository
    organization: google-gemini
    license: Apache-2.0
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# google-gemini/gemini-cli

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> An open-source AI agent that brings the power of Gemini directly into your terminal.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/google-gemini/gemini-cli> |
| Owner | google-gemini (Organization) |
| Official upstream | no |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 107,004 (checked 2026-09-15) |
| Forks | 14,584 |
| Open issues | 841 |
| Contributors | 442 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v0.59.0 (2026-09-08) |
| Archived | no |
| Fork | no |
| Homepage | https://geminicli.com |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.62 |
| reproducibility | 7.5 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.81** |
| **trust_score** | **6.79** |

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
| README size | 13,489 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug google-gemini/gemini-cli
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
