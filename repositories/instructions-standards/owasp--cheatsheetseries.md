---
id: owasp--cheatsheetseries
title: "OWASP/CheatSheetSeries"
domain: instructions-standards
summary: >-
  OWASP/CheatSheetSeries — ACTIVE, tier S,
  33,183 stars, license CC-BY-SA-4.0, quality 8.18/10, trust 7.93/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "instructions-standards", "owasp", "reference", "security"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.86, "reproducibility": 5.9, "security": 7.0, "recency": 10.0, "evidence": 4.0}
  quality_score: 8.18
  trust_score: 7.93
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "OWASP/CheatSheetSeries on GitHub"
    url: https://github.com/OWASP/CheatSheetSeries
    type: github-repository
    organization: OWASP
    license: CC-BY-SA-4.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# OWASP/CheatSheetSeries

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> The OWASP Cheat Sheet Series was created to provide a concise collection of high value information on specific application security topics.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/OWASP/CheatSheetSeries> |
| Owner | OWASP (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `CC-BY-SA-4.0` |
| Stars | 33,183 (checked 2026-09-15) |
| Forks | 4,623 |
| Open issues | 59 |
| Contributors | 457 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `docs` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.86 |
| reproducibility | 5.9 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 4.0 |
| **quality_score** (weighted) | **8.18** |
| **trust_score** | **7.93** |

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
| README size | 4,286 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug OWASP/CheatSheetSeries
python3 scripts/generate-index/generate_repository_cards.py --category instructions-standards
```
