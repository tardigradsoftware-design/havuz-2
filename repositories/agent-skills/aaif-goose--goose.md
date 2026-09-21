---
id: aaif-goose--goose
title: "aaif-goose/goose"
domain: agent-skills
summary: >-
  aaif-goose/goose — ACTIVE, tier S,
  54,520 stars, license Apache-2.0, quality 8.18/10, trust 7.27/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "coding-agent", "github-repository", "mcp"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 5.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.79, "reproducibility": 10.0, "security": 6.0, "recency": 10.0, "evidence": 8.0}
  quality_score: 8.18
  trust_score: 7.27
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "aaif-goose/goose on GitHub"
    url: https://github.com/aaif-goose/goose
    type: github-repository
    organization: aaif-goose
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# aaif-goose/goose

🟢 ACTIVE · tier **S** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/aaif-goose/goose> |
| Owner | aaif-goose (Organization) |
| Official upstream | no |
| Language | Rust |
| License | `Apache-2.0` |
| Stars | 54,520 (checked 2026-09-21) |
| Forks | 6,286 |
| Open issues | 401 |
| Contributors | 453 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v1.51.0 (2026-09-17) |
| Archived | no |
| Fork | no |
| Homepage | [https://goose-docs.ai/](https://goose-docs.ai/) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.79 |
| reproducibility | 10.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.18** |
| **trust_score** | **7.27** |

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
| examples | yes |
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 3,449 bytes |

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

Repository moved: `block/goose` -> `aaif-goose/goose`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug aaif-goose/goose
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
