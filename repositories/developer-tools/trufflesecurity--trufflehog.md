---
id: trufflesecurity--trufflehog
title: "trufflesecurity/trufflehog"
domain: developer-tools
summary: >-
  trufflesecurity/trufflehog — ACTIVE, tier S,
  27,906 stars, license AGPL-3.0, quality 8.73/10, trust 8.85/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "secrets", "security"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.5, "reproducibility": 7.3, "security": 6.0, "recency": 10.0, "evidence": 6.5}
  quality_score: 8.73
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
  - title: "trufflesecurity/trufflehog on GitHub"
    url: https://github.com/trufflesecurity/trufflehog
    type: github-repository
    organization: trufflesecurity
    license: AGPL-3.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# trufflesecurity/trufflehog

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Find, verify, and analyze leaked credentials

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/trufflesecurity/trufflehog> |
| Owner | trufflesecurity (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `AGPL-3.0` |
| Stars | 27,906 (checked 2026-09-15) |
| Forks | 2,578 |
| Open issues | 552 |
| Contributors | 199 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v3.97.4 (2026-09-03) |
| Archived | no |
| Fork | no |
| Homepage | [https://trufflesecurity.com](https://trufflesecurity.com) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.5 |
| reproducibility | 7.3 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 6.5 |
| **quality_score** (weighted) | **8.73** |
| **trust_score** | **8.85** |

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
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 37,890 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug trufflesecurity/trufflehog
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
