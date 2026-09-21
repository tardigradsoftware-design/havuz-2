---
id: tencent--aicgseceval
title: "Tencent/AICGSecEval"
domain: evaluation
summary: >-
  Tencent/AICGSecEval — STABLE, tier B,
  659 stars, license NOASSERTION, quality 6.45/10, trust 5.56/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["ai-generated-code", "benchmark", "evaluation", "github-repository", "security"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 6.0, "maintenance": 5.5, "adoption": 9.59, "documentation": 7.39, "reproducibility": 6.1, "security": 3.0, "recency": 8.37, "evidence": 5.0}
  quality_score: 6.45
  trust_score: 5.56
  tier: B
  maturity: published-artifact
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "Tencent/AICGSecEval on GitHub"
    url: https://github.com/Tencent/AICGSecEval
    type: github-repository
    organization: Tencent
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# Tencent/AICGSecEval

🔵 STABLE · tier **B** · published-artifact · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> A.S.E (AICGSecEval) is a repository-level AI-generated code security evaluation benchmark developed by Tencent Wukong Code Security Team.

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/Tencent/AICGSecEval> |
| Owner | Tencent (Organization) |
| Official upstream | no |
| Language | Python |
| License | `NOASSERTION` |
| Stars | 659 (checked 2026-09-21) |
| Forks | 112 |
| Open issues | 6 |
| Contributors | 28 |
| Last push | 2026-05-25 (119 days before verification) |
| Latest release | report-v1.0 (2025-12-17) |
| Archived | no |
| Fork | no |
| Homepage | [https://aicgseceval.tencent.com](https://aicgseceval.tencent.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `benchmark` (static artifact — quiet history is expected) |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 5.5 |
| adoption | 9.59 |
| documentation | 7.39 |
| reproducibility | 6.1 |
| security | 3.0 |
| recency | 8.37 |
| evidence | 5.0 |
| **quality_score** (weighted) | **6.45** |
| **trust_score** | **5.56** |

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
| contributing | no |
| root entries | yes |
| README size | 16,633 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-21) and must be
re-checked against your own constraints._

**Recommended for**

- Repository-level security evaluation of AI-generated code
- Building a security gate into an agent's validation phase

**Not recommended for**

- Treating a passing score as a substitute for human security review

**Strengths**

- Targets exactly the risk this knowledge base cares about: insecure AI-generated code
- From a major lab

**Weaknesses**

- Benchmark, so contamination and coverage limits apply
- Modest adoption (659 stars verified)

**Related projects**

- NVIDIA/garak
- promptfoo/promptfoo
- OWASP/Top10

## Verification notes

Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine. Reference implementation published with a benchmark. Quiet commit history is expected and is NOT evidence of abandonment; the value is the paper/method, not the maintenance. Discovered via topic:agent+topic:benchmark search on 2026-09-15.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug Tencent/AICGSecEval
python3 scripts/generate-index/generate_repository_cards.py --category evaluation
```
