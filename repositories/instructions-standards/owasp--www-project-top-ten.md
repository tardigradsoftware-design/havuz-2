---
id: owasp--www-project-top-ten
title: "OWASP/www-project-top-ten"
domain: instructions-standards
summary: >-
  OWASP/www-project-top-ten — MAINTENANCE, tier NO-LICENSE,
  1,443 stars, license NONE, quality 5.04/10, trust 3.2/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: low
claim_type: fact
evidence_level: verified-github-api
tags: ["github-repository", "instructions-standards", "owasp", "security", "standard"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 3.0, "adoption": 10.0, "documentation": 3.0, "reproducibility": 1.0, "security": 2.5, "recency": 6.38, "evidence": 2.0}
  quality_score: 5.04
  trust_score: 3.2
  tier: NO-LICENSE
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "OWASP/www-project-top-ten on GitHub"
    url: https://github.com/OWASP/www-project-top-ten
    type: github-repository
    organization: OWASP
    license: NONE
    license_risk: no-license-do-not-redistribute
    confidence: low
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# OWASP/www-project-top-ten

🟡 MAINTENANCE · tier **NO-LICENSE** · maintenance-mode · confidence **low**

> _Upstream description, quoted as published and not verified here:_
>
> OWASP Foundation Web Respository

> ⚠️ **LICENSE RISK — `no-license-do-not-redistribute`.** GitHub detected **no license file**
> on 2026-09-15. Default copyright applies, so all rights are reserved: **reference and link only**.
> Do not vendor, copy, quote at length, or redistribute any file from this repository, however
> useful it looks. A high star count does not create a license.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/OWASP/www-project-top-ten> |
| Owner | OWASP (Organization) |
| Official upstream | yes |
| Language | HTML |
| License | `NONE` |
| Stars | 1,443 (checked 2026-09-15) |
| Forks | 278 |
| Open issues | 43 |
| Contributors | 14 |
| Last push | 2025-12-24 (264 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `docs` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 3.0 |
| adoption | 10.0 |
| documentation | 3.0 |
| reproducibility | 1.0 |
| security | 2.5 |
| recency | 6.38 |
| evidence | 2.0 |
| **quality_score** (weighted) | **5.04** |
| **trust_score** | **3.2** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | no |
| docs | yes |
| tests | no |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 0 bytes |

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

No push in 264 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting. NO LICENSE FILE DETECTED by GitHub. Copyright defaults to all-rights-reserved: do not vendor, copy or redistribute code from this repository. Reference and link only.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug OWASP/www-project-top-ten
python3 scripts/generate-index/generate_repository_cards.py --category instructions-standards
```
