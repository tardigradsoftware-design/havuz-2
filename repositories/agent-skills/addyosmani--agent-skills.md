---
id: addyosmani--agent-skills
title: "addyosmani/agent-skills"
domain: agent-skills
summary: >-
  addyosmani/agent-skills — ACTIVE, tier A,
  101,366 stars, license MIT, quality 7.46/10, trust 6.52/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "engineering", "github-repository", "skills", "web"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 5.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.62, "reproducibility": 7.0, "security": 3.5, "recency": 9.99, "evidence": 5.5}
  quality_score: 7.46
  trust_score: 6.52
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "addyosmani/agent-skills on GitHub"
    url: https://github.com/addyosmani/agent-skills
    type: github-repository
    organization: addyosmani
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-10-05
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-05)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# addyosmani/agent-skills

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Production-grade engineering skills for AI coding agents.

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/addyosmani/agent-skills> |
| Owner | addyosmani (User) |
| Official upstream | no |
| Language | JavaScript |
| License | `MIT` |
| Stars | 101,366 (checked 2026-10-05) |
| Forks | 10,628 |
| Open issues | 121 |
| Contributors | 77 |
| Last push | 2026-10-03 (1 days before verification) |
| Latest release | 0.6.12 (2026-10-03) |
| Archived | no |
| Fork | no |
| Homepage | [https://skills.addy.ie](https://skills.addy.ie) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.62 |
| reproducibility | 7.0 |
| security | 3.5 |
| recency | 9.99 |
| evidence | 5.5 |
| **quality_score** (weighted) | **7.46** |
| **trust_score** | **6.52** |

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
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 25,473 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-10-05) and must be
re-checked against your own constraints._

**Recommended for**

- Production-grade engineering skills for coding agents
- A high-authority reference point for skill quality

**Not recommended for**

- Assuming every skill fits your stack - evaluate individually

**Strengths**

- Author has recognised authority on web engineering
- Very high adoption (94k stars verified)
- Framed as production-grade engineering skills rather than prompt tricks

**Weaknesses**

- Web/frontend weighted
- Rapidly growing star count means content quality may vary between entries

**Related projects**

- anthropics/skills
- obra/superpowers
- VoltAgent/awesome-agent-skills

## Verification notes

Discovered via topic:agent-skills search on 2026-09-15.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug addyosmani/agent-skills
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
