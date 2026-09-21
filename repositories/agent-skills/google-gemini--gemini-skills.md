---
id: google-gemini--gemini-skills
title: "google-gemini/gemini-skills"
domain: agent-skills
summary: >-
  google-gemini/gemini-skills — ACTIVE, tier B,
  4,188 stars, license Apache-2.0, quality 6.63/10, trust 5.35/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "github-repository", "google", "official", "skills"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 5.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 4.85, "reproducibility": 4.5, "security": 3.5, "recency": 9.96, "evidence": 2.5}
  quality_score: 6.63
  trust_score: 5.35
  tier: B
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "google-gemini/gemini-skills on GitHub"
    url: https://github.com/google-gemini/gemini-skills
    type: github-repository
    organization: google-gemini
    license: Apache-2.0
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# google-gemini/gemini-skills

🟢 ACTIVE · tier **B** · production-ready · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Skills for the Gemini API, SDK and model/agent interactions

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/google-gemini/gemini-skills> |
| Owner | google-gemini (Organization) |
| Official upstream | no |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 4,188 (checked 2026-09-21) |
| Forks | 439 |
| Open issues | 11 |
| Contributors | 15 |
| Last push | 2026-09-17 (3 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://ai.google.dev/gemini-api/docs](https://ai.google.dev/gemini-api/docs) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 4.85 |
| reproducibility | 4.5 |
| security | 3.5 |
| recency | 9.96 |
| evidence | 2.5 |
| **quality_score** (weighted) | **6.63** |
| **trust_score** | **5.35** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 4,208 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug google-gemini/gemini-skills
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
