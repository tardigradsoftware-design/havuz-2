---
id: adr--madr
title: "adr/madr"
domain: developer-tools
summary: >-
  adr/madr — STABLE, tier A,
  2,485 stars, license NOASSERTION, quality 7.89/10, trust 7.78/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["architecture", "decision-records", "developer-tools", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 9.0, "adoption": 10.0, "documentation": 7.51, "reproducibility": 6.1, "security": 4.0, "recency": 9.75, "evidence": 5.0}
  quality_score: 7.89
  trust_score: 7.78
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
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
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# adr/madr

🔵 STABLE · tier **A** · production-ready · confidence **very-high**

> Markdown Architectural Decision Records

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/adr/madr> |
| Owner | adr (Organization) |
| Official upstream | yes |
| Language | Markdown |
| License | `NOASSERTION` |
| Stars | 2,485 (checked 2026-09-15) |
| Forks | 469 |
| Open issues | 28 |
| Contributors | 30 |
| Last push | 2026-08-28 (18 days before verification) |
| Latest release | 4.0.0 (2024-09-17) |
| Archived | no |
| Fork | no |
| Homepage | https://adr.github.io/madr/ |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 9.0 |
| adoption | 10.0 |
| documentation | 7.51 |
| reproducibility | 6.1 |
| security | 4.0 |
| recency | 9.75 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.89** |
| **trust_score** | **7.78** |

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
