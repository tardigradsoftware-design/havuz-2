---
id: harbor-framework--terminal-bench-1
title: "harbor-framework/terminal-bench-1"
domain: evaluation
summary: >-
  harbor-framework/terminal-bench-1 — STABLE, tier B,
  2,582 stars, license Apache-2.0, quality 6.89/10, trust 5.76/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "evaluation", "github-repository", "terminal"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.5, "maintenance": 7.5, "adoption": 10.0, "documentation": 5.07, "reproducibility": 8.0, "security": 3.5, "recency": 9.1, "evidence": 6.0}
  quality_score: 6.89
  trust_score: 5.76
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "harbor-framework/terminal-bench-1 on GitHub"
    url: https://github.com/harbor-framework/terminal-bench-1
    type: github-repository
    organization: harbor-framework
    license: Apache-2.0
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# harbor-framework/terminal-bench-1

🔵 STABLE · tier **B** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> A benchmark for LLMs on complicated tasks in the terminal

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/harbor-framework/terminal-bench-1> |
| Owner | harbor-framework (Organization) |
| Official upstream | no |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 2,582 (checked 2026-09-15) |
| Forks | 570 |
| Open issues | 319 |
| Contributors | 93 |
| Last push | 2026-07-11 (66 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.tbench.ai](https://www.tbench.ai) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 7.5 |
| adoption | 10.0 |
| documentation | 5.07 |
| reproducibility | 8.0 |
| security | 3.5 |
| recency | 9.1 |
| evidence | 6.0 |
| **quality_score** (weighted) | **6.89** |
| **trust_score** | **5.76** |

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
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 6,846 bytes |

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

Repository moved: `laude-institute/terminal-bench` -> `harbor-framework/terminal-bench-1`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. Reference implementation published with a benchmark. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug harbor-framework/terminal-bench-1
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
