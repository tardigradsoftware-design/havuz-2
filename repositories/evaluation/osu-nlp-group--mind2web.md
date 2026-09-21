---
id: osu-nlp-group--mind2web
title: "OSU-NLP-Group/Mind2Web"
domain: evaluation
summary: >-
  OSU-NLP-Group/Mind2Web — STABLE, tier B,
  1,028 stars, license MIT, quality 6.01/10, trust 5.6/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["dataset", "evaluation", "github-repository", "web-agent"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.5, "maintenance": 3.0, "adoption": 10.0, "documentation": 7.48, "reproducibility": 4.5, "security": 4.5, "recency": 5.62, "evidence": 1.5}
  quality_score: 6.01
  trust_score: 5.6
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "OSU-NLP-Group/Mind2Web on GitHub"
    url: https://github.com/OSU-NLP-Group/Mind2Web
    type: github-repository
    organization: OSU-NLP-Group
    license: MIT
    license_risk: none
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# OSU-NLP-Group/Mind2Web

🔵 STABLE · tier **B** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> \[NeurIPS'23 Spotlight\] "Mind2Web: Towards a Generalist Agent for the Web" -- the first LLM-based web agent and benchmark for generalist web agents

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/OSU-NLP-Group/Mind2Web> |
| Owner | OSU-NLP-Group (Organization) |
| Official upstream | yes |
| Language | Jupyter Notebook |
| License | `MIT` |
| Stars | 1,028 (checked 2026-09-21) |
| Forks | 123 |
| Open issues | 12 |
| Contributors | 8 |
| Last push | 2025-11-05 (320 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://osu-nlp-group.github.io/Mind2Web/](https://osu-nlp-group.github.io/Mind2Web/) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 3.0 |
| adoption | 10.0 |
| documentation | 7.48 |
| reproducibility | 4.5 |
| security | 4.5 |
| recency | 5.62 |
| evidence | 1.5 |
| **quality_score** (weighted) | **6.01** |
| **trust_score** | **5.6** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | no |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 17,760 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug OSU-NLP-Group/Mind2Web
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
