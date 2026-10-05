---
id: foundationagents--metagpt
title: "FoundationAgents/MetaGPT"
domain: agent-frameworks
summary: >-
  FoundationAgents/MetaGPT — MAINTENANCE, tier A,
  70,745 stars, license MIT, quality 7.02/10, trust 6.2/10.
  Verified against the GitHub API on 2026-10-05.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-frameworks", "github-repository", "multi-agent", "sdlc"]
version: 1.0.0
updated: 2026-10-05
verified_at: 2026-10-05
expires_at: 2026-11-19
scoring:
  components: {"authority": 6.0, "maintenance": 4.0, "adoption": 10.0, "documentation": 6.68, "reproducibility": 10.0, "security": 6.0, "recency": 6.48, "evidence": 8.0}
  quality_score: 7.02
  trust_score: 6.2
  tier: A
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-05
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "FoundationAgents/MetaGPT on GitHub"
    url: https://github.com/FoundationAgents/MetaGPT
    type: github-repository
    organization: FoundationAgents
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

# FoundationAgents/MetaGPT

🟡 MAINTENANCE · tier **A** · maintenance-mode · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming

## Facts (verified 2026-10-05 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/FoundationAgents/MetaGPT> |
| Owner | FoundationAgents (Organization) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 70,745 (checked 2026-10-05) |
| Forks | 8,989 |
| Open issues | 143 |
| Contributors | 116 |
| Last push | 2026-01-21 (257 days before verification) |
| Latest release | v0.8.1 (2024-04-22) |
| Archived | no |
| Fork | no |
| Homepage | [https://atoms.dev/](https://atoms.dev/) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 4.0 |
| adoption | 10.0 |
| documentation | 6.68 |
| reproducibility | 10.0 |
| security | 6.0 |
| recency | 6.48 |
| evidence | 8.0 |
| **quality_score** (weighted) | **7.02** |
| **trust_score** | **6.2** |

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
| contributing | no |
| root entries | yes |
| README size | 8,215 bytes |

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

Repository moved: `geekan/MetaGPT` -> `FoundationAgents/MetaGPT`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. No push in 257 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug FoundationAgents/MetaGPT
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
