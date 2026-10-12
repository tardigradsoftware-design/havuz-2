---
id: openclaw--openclaw
title: "openclaw/openclaw"
domain: agent-skills
summary: >-
  openclaw/openclaw — ACTIVE, tier S,
  391,749 stars, license MIT, quality 8.65/10, trust 8.03/10.
  Verified against the GitHub API on 2026-10-12.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-skills", "cross-platform", "github-repository", "harness"]
version: 1.0.0
updated: 2026-10-12
verified_at: 2026-10-12
expires_at: 2026-11-26
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 10.0, "reproducibility": 10.0, "security": 6.0, "recency": 10.0, "evidence": 8.5}
  quality_score: 8.65
  trust_score: 8.03
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-12
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "openclaw/openclaw on GitHub"
    url: https://github.com/openclaw/openclaw
    type: github-repository
    organization: openclaw
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-10-12
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-12)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# openclaw/openclaw

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> The AI that really does things. Any OS. Any Platform. The lobster way. 🦞

## Facts (verified 2026-10-12 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/openclaw/openclaw> |
| Owner | openclaw (Organization) |
| Official upstream | no |
| Language | TypeScript |
| License | `MIT` |
| Stars | 391,749 (checked 2026-10-12) |
| Forks | 82,370 |
| Open issues | 9,547 |
| Contributors | 377 |
| Last push | 2026-10-12 (0 days before verification) |
| Latest release | v2026.10.2 (2026-10-12) |
| Archived | no |
| Fork | no |
| Homepage | [https://openclaw.ai](https://openclaw.ai) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 10.0 |
| reproducibility | 10.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 8.5 |
| **quality_score** (weighted) | **8.65** |
| **trust_score** | **8.03** |

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
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 113,171 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-10-12) and must be
re-checked against your own constraints._

**Recommended for**

- Cross-platform agent execution
- Studying the largest agent-harness ecosystem by adoption

**Not recommended for**

- Assuming its skill ecosystem is individually vetted - see VoltAgent/awesome-openclaw-skills
- Environments that require an OSI-approved license (custom license detected)

**Strengths**

- Largest repository in this registry by stars (389k verified 2026-09-15)
- Pushed on the verification date
- Broad OS/platform support

**Weaknesses**

- Non-SPDX license - read the terms before vendoring
- Enormous ecosystem growth means third-party skills are a supply-chain risk

**Related projects**

- VoltAgent/awesome-openclaw-skills
- hesamsheikh/awesome-openclaw-usecases
- iOfficeAI/AionUi

## Verification notes

Discovered 2026-09-15 via GitHub topic search; not in the original seed list.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug openclaw/openclaw
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
