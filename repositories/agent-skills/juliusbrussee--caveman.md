---
id: juliusbrussee--caveman
title: "JuliusBrussee/caveman"
domain: agent-skills
summary: >-
  JuliusBrussee/caveman — ACTIVE, tier A,
  105,720 stars, license NOASSERTION, quality 8.09/10, trust 7.33/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "context-compression", "github-repository", "skills", "tokens"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.34, "reproducibility": 8.6, "security": 5.5, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.09
  trust_score: 7.33
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "JuliusBrussee/caveman on GitHub"
    url: https://github.com/JuliusBrussee/caveman
    type: github-repository
    organization: JuliusBrussee
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# JuliusBrussee/caveman

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> 🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-15, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/JuliusBrussee/caveman> |
| Owner | JuliusBrussee (User) |
| Official upstream | no |
| Language | Go |
| License | `NOASSERTION` |
| Stars | 105,720 (checked 2026-09-15) |
| Forks | 6,116 |
| Open issues | 114 |
| Contributors | 51 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v2.7.0 (2026-09-15) |
| Archived | no |
| Fork | no |
| Homepage | [https://docs.caveman.so/docs/quickstart](https://docs.caveman.so/docs/quickstart) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.34 |
| reproducibility | 8.6 |
| security | 5.5 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.09** |
| **trust_score** | **7.33** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 34,120 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug JuliusBrussee/caveman
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
