---
id: voltagent--awesome-agent-skills
title: "VoltAgent/awesome-agent-skills"
domain: agent-skills
summary: >-
  VoltAgent/awesome-agent-skills — ACTIVE, tier A,
  34,355 stars, license MIT, quality 7.8/10, trust 7.6/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-skills", "catalog", "discovery", "github-repository", "skills"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.0, "reproducibility": 4.5, "security": 4.5, "recency": 10.0, "evidence": 3.0}
  quality_score: 7.8
  trust_score: 7.6
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "VoltAgent/awesome-agent-skills on GitHub"
    url: https://github.com/VoltAgent/awesome-agent-skills
    type: github-repository
    organization: VoltAgent
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# VoltAgent/awesome-agent-skills

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/VoltAgent/awesome-agent-skills> |
| Owner | VoltAgent (Organization) |
| Official upstream | yes |
| Language | — |
| License | `MIT` |
| Stars | 34,355 (checked 2026-09-15) |
| Forks | 3,651 |
| Open issues | 13 |
| Contributors | 166 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | https://officialskills.sh/ |
| SECURITY.md | no → `no-policy` |
| Repository kind | `catalog` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.0 |
| reproducibility | 4.5 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 3.0 |
| **quality_score** (weighted) | **7.8** |
| **trust_score** | **7.6** |

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
| contributing | yes |
| root entries | yes |
| README size | 219,996 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Seed discovery of skills across Claude, Codex, Cursor, Gemini CLI, Copilot, OpenCode and Windsurf
- Tracking which agent ecosystems have skill catalogues at all

**Not recommended for**

- Trusting any listed skill without verifying it individually
- Assuming inclusion implies quality

**Strengths**

- MIT licensed (rare for awesome-lists)
- 166 contributors - genuinely community-maintained
- Cross-ecosystem coverage rather than single-vendor
- Pushed on the verification date

**Weaknesses**

- It is a catalogue: entries are not individually verified
- No releases, so there is no stable snapshot to cite

**Related projects**

- hesreallyhim/awesome-claude-code
- ComposioHQ/awesome-claude-skills
- VoltAgent/awesome-openclaw-skills
- punkpeye/awesome-mcp-servers

## Verification notes

Verified 2026-09-15: ACTIVE, MIT, 34.3k stars, README ~220 KB. Every skill taken from it is re-verified before entering this repository.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug VoltAgent/awesome-agent-skills
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
