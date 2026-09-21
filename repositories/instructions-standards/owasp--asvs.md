---
id: owasp--asvs
title: "OWASP/ASVS"
domain: instructions-standards
summary: >-
  OWASP/ASVS — STABLE, tier A,
  3,610 stars, license CC-BY-SA-4.0, quality 7.9/10, trust 7.45/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "instructions-standards", "owasp", "security", "standard"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 4.83, "reproducibility": 6.9, "security": 7.0, "recency": 9.77, "evidence": 4.5}
  quality_score: 7.9
  trust_score: 7.45
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "OWASP/ASVS on GitHub"
    url: https://github.com/OWASP/ASVS
    type: github-repository
    organization: OWASP
    license: CC-BY-SA-4.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# OWASP/ASVS

🔵 STABLE · tier **A** · production-ready · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Application Security Verification Standard

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/OWASP/ASVS> |
| Owner | OWASP (Organization) |
| Official upstream | yes |
| Language | HTML |
| License | `CC-BY-SA-4.0` |
| Stars | 3,610 (checked 2026-09-21) |
| Forks | 832 |
| Open issues | 111 |
| Contributors | 113 |
| Last push | 2026-09-03 (17 days before verification) |
| Latest release | latest (2026-09-03) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `docs` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 4.83 |
| reproducibility | 6.9 |
| security | 7.0 |
| recency | 9.77 |
| evidence | 4.5 |
| **quality_score** (weighted) | **7.9** |
| **trust_score** | **7.45** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | yes |
| examples | no |
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 10,018 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug OWASP/ASVS
python3 scripts/generate-index/generate_repository_cards.py --category instructions-standards
```
