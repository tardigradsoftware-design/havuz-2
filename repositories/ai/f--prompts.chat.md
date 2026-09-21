---
id: f--prompts.chat
title: "f/prompts.chat"
domain: ai
summary: >-
  f/prompts.chat — ACTIVE, tier A,
  170,869 stars, license NOASSERTION, quality 7.52/10, trust 6.57/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["ai", "catalog", "github-repository", "prompting"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 5.0, "maintenance": 9.5, "adoption": 10.0, "documentation": 7.45, "reproducibility": 7.1, "security": 5.5, "recency": 9.85, "evidence": 6.0}
  quality_score: 7.52
  trust_score: 6.57
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "f/prompts.chat on GitHub"
    url: https://github.com/f/prompts.chat
    type: github-repository
    organization: f
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

# f/prompts.chat

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/f/prompts.chat> |
| Owner | f (User) |
| Official upstream | no |
| Language | HTML |
| License | `NOASSERTION` |
| Stars | 170,869 (checked 2026-09-21) |
| Forks | 21,958 |
| Open issues | 78 |
| Contributors | 280 |
| Last push | 2026-09-09 (11 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://prompts.chat](https://prompts.chat) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `catalog` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 9.5 |
| adoption | 10.0 |
| documentation | 7.45 |
| reproducibility | 7.1 |
| security | 5.5 |
| recency | 9.85 |
| evidence | 6.0 |
| **quality_score** (weighted) | **7.52** |
| **trust_score** | **6.57** |

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
| README size | 11,382 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug f/prompts.chat
python3 scripts/generate-index/generate_repository_cards.py --category ai
```
