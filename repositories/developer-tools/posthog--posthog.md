---
id: posthog--posthog
title: "PostHog/posthog"
domain: developer-tools
summary: >-
  PostHog/posthog — ACTIVE, tier A,
  39,881 stars, license NOASSERTION, quality 8.16/10, trust 8.04/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["analytics", "developer-tools", "github-repository", "product"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.95, "reproducibility": 6.6, "security": 4.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.16
  trust_score: 8.04
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "PostHog/posthog on GitHub"
    url: https://github.com/PostHog/posthog
    type: github-repository
    organization: PostHog
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

# PostHog/posthog

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> :hedgehog: PostHog is the leading platform for building self-driving products. Our developer tools – AI observability, analytics, session replay, flags, experiments, error tracking, logs, and more – capture all the context agents need to diagnose problems, uncover opportunities, and ship fixes. Steer it all from Slack, web, desktop, or the MCP.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/PostHog/posthog> |
| Owner | PostHog (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `NOASSERTION` |
| Stars | 39,881 (checked 2026-09-21) |
| Forks | 3,407 |
| Open issues | 5,586 |
| Contributors | 393 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | desktop-v0.61.469 (2026-09-19) |
| Archived | no |
| Fork | no |
| Homepage | [https://posthog.com](https://posthog.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.95 |
| reproducibility | 6.6 |
| security | 4.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.16** |
| **trust_score** | **8.04** |

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
| README size | 11,387 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug PostHog/posthog
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
