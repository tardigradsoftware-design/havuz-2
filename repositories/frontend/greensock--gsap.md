---
id: greensock--gsap
title: "greensock/GSAP"
domain: frontend
summary: >-
  greensock/GSAP — MAINTENANCE, tier NO-LICENSE,
  28,520 stars, license NONE, quality 6.08/10, trust 4.33/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["animation", "frontend", "github-repository", "motion"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 9.0, "maintenance": 5.0, "adoption": 10.0, "documentation": 5.02, "reproducibility": 1.0, "security": 5.0, "recency": 7.81, "evidence": 1.5}
  quality_score: 6.08
  trust_score: 4.33
  tier: NO-LICENSE
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "greensock/GSAP on GitHub"
    url: https://github.com/greensock/GSAP
    type: github-repository
    organization: greensock
    license: NONE
    license_risk: no-license-do-not-redistribute
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# greensock/GSAP

🟡 MAINTENANCE · tier **NO-LICENSE** · maintenance-mode · confidence **medium**

> _Upstream description, quoted as published and not verified here:_
>
> GSAP (GreenSock Animation Platform), a JavaScript animation library for the modern web

> ⚠️ **LICENSE RISK — `no-license-do-not-redistribute`.** GitHub detected **no license file**
> on 2026-09-21. Default copyright applies, so all rights are reserved: **reference and link only**.
> Do not vendor, copy, quote at length, or redistribute any file from this repository, however
> useful it looks. A high star count does not create a license.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/greensock/GSAP> |
| Owner | greensock (Organization) |
| Official upstream | yes |
| Language | JavaScript |
| License | `NONE` |
| Stars | 28,520 (checked 2026-09-21) |
| Forks | 2,205 |
| Open issues | 5 |
| Contributors | 3 |
| Last push | 2026-04-13 (160 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | [https://gsap.com](https://gsap.com) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 5.0 |
| adoption | 10.0 |
| documentation | 5.02 |
| reproducibility | 1.0 |
| security | 5.0 |
| recency | 7.81 |
| evidence | 1.5 |
| **quality_score** (weighted) | **6.08** |
| **trust_score** | **4.33** |

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
| security md | yes |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 6,199 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-21) and must be
re-checked against your own constraints._

**Recommended for**

- Complex timeline animation, scroll-driven sequences, SVG path animation

**Not recommended for**

- Simple one-off transitions where CSS or Motion is enough
- Blindly vendoring: GitHub detected no license file on 2026-09-15

**Strengths**

- The most capable general-purpose web animation library
- Long track record, huge body of examples
- Pushed 155 days before verification

**Weaknesses**

- No license detected by the GitHub API on 2026-09-15 - the terms changed over time, so read the current license on the official site before vendoring or redistributing
- Larger than CSS/Motion for simple cases

**Related projects**

- motiondivision/motion
- mrdoob/three.js
- pmndrs/react-three-fiber

## Verification notes

No push in 160 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting. NO LICENSE FILE DETECTED by GitHub. Copyright defaults to all-rights-reserved: do not vendor, copy or redistribute code from this repository. Reference and link only. License status must be confirmed on gsap.com before any vendoring. This record deliberately states the API observation, not a remembered license name.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug greensock/GSAP
python3 scripts/generate-index/generate_repository_cards.py --category frontend
```
