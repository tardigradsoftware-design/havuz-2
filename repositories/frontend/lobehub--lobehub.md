---
id: lobehub--lobehub
title: "lobehub/lobehub"
domain: frontend
summary: >-
  lobehub/lobehub — ACTIVE, tier A,
  82,714 stars, license NOASSERTION, quality 9.06/10, trust 9.22/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["ai-chat", "example", "frontend", "github-repository"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 10.0, "reproducibility": 8.6, "security": 6.5, "recency": 10.0, "evidence": 7.5}
  quality_score: 9.06
  trust_score: 9.22
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "lobehub/lobehub on GitHub"
    url: https://github.com/lobehub/lobehub
    type: github-repository
    organization: lobehub
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# lobehub/lobehub

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/lobehub/lobehub> |
| Owner | lobehub (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `NOASSERTION` |
| Stars | 82,714 (checked 2026-09-21) |
| Forks | 15,908 |
| Open issues | 942 |
| Contributors | 348 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v2.2.18 (2026-09-20) |
| Archived | no |
| Fork | no |
| Homepage | [https://lobehub.com](https://lobehub.com) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 10.0 |
| reproducibility | 8.6 |
| security | 6.5 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **9.06** |
| **trust_score** | **9.22** |

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
| examples | no |
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 39,136 bytes |

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

Repository moved: `lobehub/lobe-chat` -> `lobehub/lobehub`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug lobehub/lobehub
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
