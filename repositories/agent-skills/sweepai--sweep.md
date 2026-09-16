---
id: sweepai--sweep
title: "sweepai/sweep"
domain: agent-skills
summary: >-
  sweepai/sweep — MAINTENANCE, tier B,
  7,713 stars, license NOASSERTION, quality 6.94/10, trust 7.03/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["abandoned-candidate", "agent-skills", "coding-agent", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 3.5, "adoption": 10.0, "documentation": 6.52, "reproducibility": 8.6, "security": 4.0, "recency": 5.04, "evidence": 7.0}
  quality_score: 6.94
  trust_score: 7.03
  tier: B
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "sweepai/sweep on GitHub"
    url: https://github.com/sweepai/sweep
    type: github-repository
    organization: sweepai
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

# sweepai/sweep

🟡 MAINTENANCE · tier **B** · maintenance-mode · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Sweep: AI coding assistant for JetBrains

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-15, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/sweepai/sweep> |
| Owner | sweepai (Organization) |
| Official upstream | yes |
| Language | Jupyter Notebook |
| License | `NOASSERTION` |
| Stars | 7,713 (checked 2026-09-15) |
| Forks | 465 |
| Open issues | 753 |
| Contributors | 33 |
| Last push | 2025-09-18 (362 days before verification) |
| Latest release | sweep-sandbox-v1 (2023-09-11) |
| Archived | no |
| Fork | no |
| Homepage | [https://sweep.dev](https://sweep.dev) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 3.5 |
| adoption | 10.0 |
| documentation | 6.52 |
| reproducibility | 8.6 |
| security | 4.0 |
| recency | 5.04 |
| evidence | 7.0 |
| **quality_score** (weighted) | **6.94** |
| **trust_score** | **7.03** |

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
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 245 bytes |

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

No push in 362 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting. Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug sweepai/sweep
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
