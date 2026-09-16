---
id: makeplane--plane
title: "makeplane/plane"
domain: frontend
summary: >-
  makeplane/plane — ACTIVE, tier A,
  59,432 stars, license AGPL-3.0, quality 7.54/10, trust 6.62/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["example", "frontend", "github-repository", "project-management", "saas"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.14, "reproducibility": 6.3, "security": 5.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 7.54
  trust_score: 6.62
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "makeplane/plane on GitHub"
    url: https://github.com/makeplane/plane
    type: github-repository
    organization: makeplane
    license: AGPL-3.0
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# makeplane/plane

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> 🔥🔥🔥 Open-source Jira, Linear, Monday, and ClickUp alternative. Plane is a modern project management platform to manage tasks, sprints, docs, and triage.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/makeplane/plane> |
| Owner | makeplane (Organization) |
| Official upstream | no |
| Language | TypeScript |
| License | `AGPL-3.0` |
| Stars | 59,432 (checked 2026-09-15) |
| Forks | 5,750 |
| Open issues | 1,120 |
| Contributors | 164 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v1.4.2 (2026-08-23) |
| Archived | no |
| Fork | no |
| Homepage | http://plane.so |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.14 |
| reproducibility | 6.3 |
| security | 5.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **7.54** |
| **trust_score** | **6.62** |

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
| README size | 7,699 bytes |

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

_No anomalies detected._

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug makeplane/plane
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
