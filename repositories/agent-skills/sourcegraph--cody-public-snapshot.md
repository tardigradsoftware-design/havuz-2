---
id: sourcegraph--cody-public-snapshot
title: "sourcegraph/cody-public-snapshot"
domain: agent-skills
summary: >-
  sourcegraph/cody-public-snapshot — ARCHIVED, tier ARCHIVED,
  3,807 stars, license Apache-2.0, quality 5.76/10, trust 3.5/10.
  Verified against the GitHub API on 2026-09-15.
status: deprecated
confidence: low
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "coding-agent", "deprecated-candidate", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 1.5, "adoption": 10.0, "documentation": 4.98, "reproducibility": 7.5, "security": 1.5, "recency": 4.38, "evidence": 5.0}
  quality_score: 5.76
  trust_score: 3.5
  tier: ARCHIVED
  maturity: end-of-life
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "sourcegraph/cody-public-snapshot on GitHub"
    url: https://github.com/sourcegraph/cody-public-snapshot
    type: github-repository
    organization: sourcegraph
    license: Apache-2.0
    license_risk: none
    confidence: low
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# sourcegraph/cody-public-snapshot

⛔ ARCHIVED · tier **ARCHIVED** · end-of-life · confidence **low**

> _Upstream description, quoted as published and not verified here:_
>
> Type less, code more: Cody is an AI code assistant that uses advanced search and codebase context to help you write and fix code.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/sourcegraph/cody-public-snapshot> |
| Owner | sourcegraph (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 3,807 (checked 2026-09-15) |
| Forks | 486 |
| Open issues | 43 |
| Contributors | 120 |
| Last push | 2025-08-01 (410 days before verification) |
| Latest release | vscode-v1.116.0 (2025-07-30) |
| Archived | **YES** |
| Fork | no |
| Homepage | [https://cody.dev](https://cody.dev) |
| SECURITY.md | no → `archived-no-patches` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 1.5 |
| adoption | 10.0 |
| documentation | 4.98 |
| reproducibility | 7.5 |
| security | 1.5 |
| recency | 4.38 |
| evidence | 5.0 |
| **quality_score** (weighted) | **5.76** |
| **trust_score** | **3.5** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | yes |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 5,808 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Historical study of context-window management in a shipping coding assistant

**Not recommended for**

- Any new work - the repository is ARCHIVED

**Strengths**

- Apache-2.0 public snapshot of a real production coding agent
- Useful for studying how context selection was engineered in practice

**Weaknesses**

- ARCHIVED (verified 2026-09-15): read-only, no patches, no security fixes

**Related projects**

- continuedev/continue
- cline/cline
- All-Hands-AI/OpenHands

## Verification notes

ARCHIVED by owner: read-only, receives no fixes or security patches. Do not start new work on it; look for the successor project. The original seed slug sourcegraph/cody now 404s. Verified replacement: sourcegraph/cody-public-snapshot, archived. Recorded as a discontinuation, not as a recommendation.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug sourcegraph/cody-public-snapshot
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
