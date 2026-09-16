---
id: langfuse--langfuse
title: "langfuse/langfuse"
domain: evaluation
summary: >-
  langfuse/langfuse — ACTIVE, tier A,
  34,637 stars, license NOASSERTION, quality 8.86/10, trust 8.92/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["evaluation", "github-repository", "observability", "tracing"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.0, "reproducibility": 8.6, "security": 6.5, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.86
  trust_score: 8.92
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "langfuse/langfuse on GitHub"
    url: https://github.com/langfuse/langfuse
    type: github-repository
    organization: langfuse
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# langfuse/langfuse

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> 🪢 Open source agent evals & observability: Trace, evaluate, and improve LLM applications with one open platform.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-15, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/langfuse/langfuse> |
| Owner | langfuse (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `NOASSERTION` |
| Stars | 34,637 (checked 2026-09-15) |
| Forks | 3,772 |
| Open issues | 954 |
| Contributors | 203 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v4.36.1 (2026-09-15) |
| Archived | no |
| Fork | no |
| Homepage | [https://langfuse.com](https://langfuse.com) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.0 |
| reproducibility | 8.6 |
| security | 6.5 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.86** |
| **trust_score** | **8.92** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | yes |
| examples | no |
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 52,651 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug langfuse/langfuse
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
