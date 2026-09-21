---
id: 12factor--12factor-br
title: "12factor/12factor-br"
domain: instructions-standards
summary: >-
  12factor/12factor-br — ABANDONED, tier EXPERIMENTAL,
  3 stars, license MIT, quality 3.18/10, trust 3.94/10.
  Verified against the GitHub API on 2026-09-21.
status: deprecated
confidence: low
claim_type: fact
evidence_level: verified-github-api
tags: ["architecture", "github-repository", "instructions-standards", "standard"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 6.0, "maintenance": 1.5, "adoption": 2.64, "documentation": 4.1, "reproducibility": 4.5, "security": 3.5, "recency": 0.0, "evidence": 1.5}
  quality_score: 3.18
  trust_score: 3.94
  tier: EXPERIMENTAL
  maturity: end-of-life
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "12factor/12factor-br on GitHub"
    url: https://github.com/12factor/12factor-br
    type: github-repository
    organization: 12factor
    license: MIT
    license_risk: none
    confidence: low
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# 12factor/12factor-br

🔴 ABANDONED · tier **EXPERIMENTAL** · end-of-life · confidence **low**

> _No description published._

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/12factor/12factor-br> |
| Owner | 12factor (Organization) |
| Official upstream | yes |
| Language | CSS |
| License | `MIT` |
| Stars | 3 (checked 2026-09-21) |
| Forks | 2 |
| Open issues | 0 |
| Contributors | 32 |
| Last push | 2016-02-16 (3869 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | yes |
| Homepage | [http://www.12factor.net/](http://www.12factor.net/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 1.5 |
| adoption | 2.64 |
| documentation | 4.1 |
| reproducibility | 4.5 |
| security | 3.5 |
| recency | 0.0 |
| evidence | 1.5 |
| **quality_score** (weighted) | **3.18** |
| **trust_score** | **3.94** |

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
| README size | 1,152 bytes |

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

Repository moved: `12factor/12factor` -> `12factor/12factor-br`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. No push in 3869 days (>365d). Likely abandoned; prefer an actively maintained alternative. This is a fork. Check the upstream parent before trusting provenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug 12factor/12factor-br
python3 scripts/generate-index/generate_repository_cards.py --category instructions-standards
```
