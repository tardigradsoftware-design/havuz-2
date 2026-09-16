---
id: stanfordmlgroup--medagentbench
title: "stanfordmlgroup/MedAgentBench"
domain: evaluation
summary: >-
  stanfordmlgroup/MedAgentBench — STABLE, tier C,
  328 stars, license MIT, quality 4.89/10, trust 3.69/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: low
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "benchmark", "evaluation", "github-repository", "medical"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.5, "maintenance": 3.0, "adoption": 8.77, "documentation": 4.8, "reproducibility": 4.5, "security": 3.5, "recency": 5.93, "evidence": 1.5}
  quality_score: 4.89
  trust_score: 3.69
  tier: C
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "stanfordmlgroup/MedAgentBench on GitHub"
    url: https://github.com/stanfordmlgroup/MedAgentBench
    type: github-repository
    organization: stanfordmlgroup
    license: MIT
    license_risk: none
    confidence: low
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# stanfordmlgroup/MedAgentBench

🔵 STABLE · tier **C** · published-artifact · confidence **low**

> _Upstream description, quoted as published and not verified here:_
>
> MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/stanfordmlgroup/MedAgentBench> |
| Owner | stanfordmlgroup (Organization) |
| Official upstream | no |
| Language | Python |
| License | `MIT` |
| Stars | 328 (checked 2026-09-15) |
| Forks | 67 |
| Open issues | 6 |
| Contributors | — |
| Last push | 2025-11-21 (297 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://ai.nejm.org/doi/full/10.1056/AIdbp2500144](https://ai.nejm.org/doi/full/10.1056/AIdbp2500144) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 3.0 |
| adoption | 8.77 |
| documentation | 4.8 |
| reproducibility | 4.5 |
| security | 3.5 |
| recency | 5.93 |
| evidence | 1.5 |
| **quality_score** (weighted) | **4.89** |
| **trust_score** | **3.69** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 3,653 bytes |

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

Reference implementation published with a benchmark. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug stanfordmlgroup/MedAgentBench
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
