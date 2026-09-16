---
id: swe-agent--swe-agent
title: "SWE-agent/SWE-agent"
domain: agent-skills
summary: >-
  SWE-agent/SWE-agent — STABLE, tier S,
  20,333 stars, license MIT, quality 8.12/10, trust 7.23/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "benchmark", "coding-agent", "github-repository", "research"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.18, "reproducibility": 9.0, "security": 6.0, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.12
  trust_score: 7.23
  tier: S
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "SWE-agent/SWE-agent on GitHub"
    url: https://github.com/SWE-agent/SWE-agent
    type: github-repository
    organization: SWE-agent
    license: MIT
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# SWE-agent/SWE-agent

🔵 STABLE · tier **S** · published-artifact · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. \[NeurIPS 2024\]

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/SWE-agent/SWE-agent> |
| Owner | SWE-agent (Organization) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 20,333 (checked 2026-09-15) |
| Forks | 2,218 |
| Open issues | 111 |
| Contributors | 97 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | v1.1.0 (2025-05-22) |
| Archived | no |
| Fork | no |
| Homepage | [https://swe-agent.com](https://swe-agent.com) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `research-artifact` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.18 |
| reproducibility | 9.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.12** |
| **trust_score** | **7.23** |

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
| README size | 8,158 bytes |

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

Repository moved: `princeton-nlp/SWE-agent` -> `SWE-agent/SWE-agent`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. Reference implementation published with a research-artifact. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug SWE-agent/SWE-agent
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
