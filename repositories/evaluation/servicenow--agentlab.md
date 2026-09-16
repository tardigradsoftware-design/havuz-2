---
id: servicenow--agentlab
title: "ServiceNow/AgentLab"
domain: evaluation
summary: >-
  ServiceNow/AgentLab — STABLE, tier B,
  634 stars, license NOASSERTION, quality 6.96/10, trust 5.94/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "evaluation", "evaluation-framework", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.5, "maintenance": 7.0, "adoption": 9.57, "documentation": 6.44, "reproducibility": 8.6, "security": 3.0, "recency": 9.19, "evidence": 6.5}
  quality_score: 6.96
  trust_score: 5.94
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "ServiceNow/AgentLab on GitHub"
    url: https://github.com/ServiceNow/AgentLab
    type: github-repository
    organization: ServiceNow
    license: NOASSERTION
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# ServiceNow/AgentLab

🔵 STABLE · tier **B** · published-artifact · confidence **medium**

> AgentLab: An open-source framework for developing, testing, and benchmarking web agents on diverse tasks, designed for scalability and reproducibility.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/ServiceNow/AgentLab> |
| Owner | ServiceNow (Organization) |
| Official upstream | no |
| Language | Python |
| License | `NOASSERTION` |
| Stars | 634 (checked 2026-09-15) |
| Forks | 130 |
| Open issues | 36 |
| Contributors | 16 |
| Last push | 2026-07-17 (59 days before verification) |
| Latest release | v0.4.2 (2026-01-20) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 7.0 |
| adoption | 9.57 |
| documentation | 6.44 |
| reproducibility | 8.6 |
| security | 3.0 |
| recency | 9.19 |
| evidence | 6.5 |
| **quality_score** (weighted) | **6.96** |
| **trust_score** | **5.94** |

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
| contributing | no |
| root entries | yes |
| README size | 17,286 bytes |

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

Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine. Reference implementation published with a benchmark. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug ServiceNow/AgentLab
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
