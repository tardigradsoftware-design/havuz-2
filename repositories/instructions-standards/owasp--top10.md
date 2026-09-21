---
id: owasp--top10
title: "OWASP/Top10"
domain: instructions-standards
summary: >-
  OWASP/Top10 — ACTIVE, tier A,
  6,114 stars, license NOASSERTION, quality 7.63/10, trust 7.17/10.
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
  components: {"authority": 8.0, "maintenance": 9.5, "adoption": 10.0, "documentation": 5.61, "reproducibility": 5.6, "security": 6.5, "recency": 9.86, "evidence": 3.5}
  quality_score: 7.63
  trust_score: 7.17
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "OWASP/Top10 on GitHub"
    url: https://github.com/OWASP/Top10
    type: github-repository
    organization: OWASP
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# OWASP/Top10

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Official OWASP Top 10 Document Repository

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/OWASP/Top10> |
| Owner | OWASP (Organization) |
| Official upstream | yes |
| Language | HTML |
| License | `NOASSERTION` |
| Stars | 6,114 (checked 2026-09-21) |
| Forks | 1,146 |
| Open issues | 58 |
| Contributors | 169 |
| Last push | 2026-09-10 (10 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `docs` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 9.5 |
| adoption | 10.0 |
| documentation | 5.61 |
| reproducibility | 5.6 |
| security | 6.5 |
| recency | 9.86 |
| evidence | 3.5 |
| **quality_score** (weighted) | **7.63** |
| **trust_score** | **7.17** |

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
| README size | 1,293 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug OWASP/Top10
python3 scripts/generate-index/generate_repository_cards.py --category instructions-standards
```
