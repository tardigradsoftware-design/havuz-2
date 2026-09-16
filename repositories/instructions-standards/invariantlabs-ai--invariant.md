---
id: invariantlabs-ai--invariant
title: "invariantlabs-ai/invariant"
domain: instructions-standards
summary: >-
  invariantlabs-ai/invariant — MAINTENANCE, tier B,
  456 stars, license Apache-2.0, quality 6.12/10, trust 5.84/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-security", "github-repository", "guardrails", "instructions-standards"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.5, "maintenance": 3.0, "adoption": 9.06, "documentation": 4.93, "reproducibility": 6.0, "security": 4.5, "recency": 6.63, "evidence": 4.0}
  quality_score: 6.12
  trust_score: 5.84
  tier: B
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "invariantlabs-ai/invariant on GitHub"
    url: https://github.com/invariantlabs-ai/invariant
    type: github-repository
    organization: invariantlabs-ai
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

# invariantlabs-ai/invariant

🟡 MAINTENANCE · tier **B** · maintenance-mode · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> Guardrails for secure and robust agent development

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/invariantlabs-ai/invariant> |
| Owner | invariantlabs-ai (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `Apache-2.0` |
| Stars | 456 (checked 2026-09-15) |
| Forks | 49 |
| Open issues | 13 |
| Contributors | 10 |
| Last push | 2026-01-12 (246 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://invariantlabs.ai](https://invariantlabs.ai) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 3.0 |
| adoption | 9.06 |
| documentation | 4.93 |
| reproducibility | 6.0 |
| security | 4.5 |
| recency | 6.63 |
| evidence | 4.0 |
| **quality_score** (weighted) | **6.12** |
| **trust_score** | **5.84** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | yes |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 5,139 bytes |

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

No push in 246 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug invariantlabs-ai/invariant
python3 scripts/generate-index/generate_repository_cards.py --category instructions-standards
```
