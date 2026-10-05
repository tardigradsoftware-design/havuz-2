---
id: adr--madr
title: "adr/madr"
domain: developer-tools
summary: >-
  adr/madr — STABLE, tier A,
  2,534 stars, license NOASSERTION, quality 7.63/10, trust 7.48/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["architecture", "decision-records", "developer-tools", "github-repository"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 9.0, "maintenance": 7.5, "adoption": 10.0, "documentation": 7.51, "reproducibility": 6.1, "security": 4.0, "recency": 9.48, "evidence": 5.0}
  quality_score: 7.63
  trust_score: 7.48
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "adr/madr on GitHub"
    url: https://github.com/adr/madr
    type: github-repository
    organization: adr
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: high
    claim_type: fact
    verified_at: 2026-10-05
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-05)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# adr/madr

🔵 STABLE · tier **A** · production-ready · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Markdown Architectural Decision Records

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-10-05, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/adr/madr> |
| Owner | adr (Organization) |
| Official upstream | yes |
| Language | Markdown |
| License | `NOASSERTION` |
| Stars | 2,534 (checked 2026-10-05) |
| Forks | 470 |
| Open issues | 28 |
| Contributors | 30 |
| Last push | 2026-08-28 (38 days before verification) |
| Latest release | 4.0.0 (2024-09-17) |
| Archived | no |
| Fork | no |
| Homepage | [https://adr.github.io/madr/](https://adr.github.io/madr/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 7.5 |
| adoption | 10.0 |
| documentation | 7.51 |
| reproducibility | 6.1 |
| security | 4.0 |
| recency | 9.48 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.63** |
| **trust_score** | **7.48** |

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
| security md | no |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 6,102 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug adr/madr
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
