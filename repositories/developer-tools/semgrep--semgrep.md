---
id: semgrep--semgrep
title: "semgrep/semgrep"
domain: developer-tools
summary: >-
  semgrep/semgrep — ACTIVE, tier S,
  16,652 stars, license LGPL-2.1, quality 8.84/10, trust 8.85/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "sast", "security"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.19, "reproducibility": 8.75, "security": 7.0, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.84
  trust_score: 8.85
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "semgrep/semgrep on GitHub"
    url: https://github.com/semgrep/semgrep
    type: github-repository
    organization: semgrep
    license: LGPL-2.1
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# semgrep/semgrep

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Lightweight static analysis for many languages. Find bug variants with patterns that look like source code.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/semgrep/semgrep> |
| Owner | semgrep (Organization) |
| Official upstream | yes |
| Language | C |
| License | `LGPL-2.1` |
| Stars | 16,652 (checked 2026-09-15) |
| Forks | 1,055 |
| Open issues | 920 |
| Contributors | 205 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v1.177.0 (2026-09-10) |
| Archived | no |
| Fork | no |
| Homepage | [https://semgrep.dev](https://semgrep.dev) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.19 |
| reproducibility | 8.75 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.84** |
| **trust_score** | **8.85** |

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
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 20,250 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug semgrep/semgrep
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
