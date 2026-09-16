---
id: ai-engineering-superpowers-analysis
title: "obra/superpowers: an analysis of a large public agent-skill collection"
domain: ai-engineering
summary: >-
  A structural analysis of the superpowers repository — its skill format, directory conventions, progressive-disclosure approach and licensing — as a comparison point for this repository's own skill contract, based on observable repository facts retrieved 2026-09-15.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [agent-skills, superpowers, skill-format, analysis, comparison, provenance, agentic-coding]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/agent-skills/skill-format.md, knowledge/ai-engineering/source-scoring.md]
sources:
  - title: "obra/superpowers"
    url: https://github.com/obra/superpowers
    type: github-repository
    organization: obra
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Observable facts retrieved from the GitHub API on 2026-09-15: star count, pushed_at, license, default branch, topic list and directory structure. Content analysis is a summary with attribution, not a copy."
---
# obra/superpowers — Analysis

## Why this repository is analysed

`obra/superpowers` is one of the largest and most-starred public collections of agent skills, which
makes it the most useful comparison point for this repository's own skill contract. The analysis below
is built from observable repository facts retrieved from the GitHub API on 2026-09-15 and from a
structural reading of its conventions — summarised and attributed, not copied.

```text
Retrieved 2026-09-15 via the GitHub API (see metadata/repositories.json for the scored record):
  stars            ~287,000 at the time of retrieval, with stars_checked_at recorded
  maintenance      actively pushed; maintenance component scored at the top of its band
  category         agent-skill collection, repo_kind: skill-collection
```

Star counts are snapshots and carry a checked_at date. They are recorded here because the size of the
collection is relevant to the analysis, not because popularity is a quality signal — the scoring model
in [`../source-scoring.md`](../source-scoring.md) weights adoption at 15% precisely so that it cannot
dominate.

## What it does well

```text
SKILL AS A DIRECTORY, NOT A FILE.   Each skill is a directory containing the skill document plus
                                    supporting material — references, examples, scripts. This is the
                                    progressive-disclosure structure: the entry document stays small
                                    and the detail is loaded when the step that needs it is reached.
                                    This repository adopts the same layout, and enforces it with a
                                    token budget plus a CI warning.

NARROW, NAMED SKILLS.               Skills are named for a specific procedure rather than a domain.
                                    A narrow skill is loadable, testable and composable; a domain-sized
                                    one is none of those. This repository's 36 skills follow the same
                                    rule — one procedure per skill.

WHEN TO USE / WHEN NOT TO USE.      Explicit applicability conditions, including the negative case. The
                                    negative case is the higher-value half: it prevents a plausible
                                    skill from being applied to a lookalike situation. Required in this
                                    repository's SKILL.md contract for the same reason.

COMPOSITION OVER HIERARCHY.         Skills reference other skills rather than nesting inside them, so a
                                    workflow is assembled from small parts. This repository expresses the
                                    same thing as requires and conflicts_with in frontmatter, which
                                    makes the graph machine-readable rather than prose-readable.

PLAIN MARKDOWN, NO BUILD STEP.      Skills are readable by an agent with a file reader and no tooling.
                                    Retained here: the metadata layer is JSON and the content layer is
                                    markdown, with generation flowing one way only.
```

## Where this repository differs, and why

```text
MACHINE-VALIDATED FRONTMATTER.      This repository requires YAML frontmatter validated against a JSON
                                    Schema with additionalProperties: false, so an unknown key fails the
                                    build. A prose convention decays; a schema does not. The tradeoff is
                                    authoring friction, paid once per skill.

EXPLICIT PROVENANCE AND EXPIRY.     Every artifact carries claim_type, evidence_level, verified_at and
                                    expires_at. A skill collection without dates cannot distinguish a
                                    current procedure from a two-year-old one, and agent tooling changes
                                    on a 90-day cycle. See ../freshness-policy.md.

CITED SOURCES WITH GRADES.          confidence: high or very-high requires a sources block; CI warns
                                    otherwise. The alternative is a corpus where every statement carries
                                    the same implicit confidence.

STRUCTURAL INDEXES, GENERATED.      Indexes here are derived from frontmatter by scripts, so they cannot
                                    drift from the content. A hand-maintained index in a large
                                    collection eventually describes a previous version of itself.

LICENSING STATED EXPLICITLY.        This repository is licensed (see LICENSE and LICENSE-CODE) and marks
                                    every third-party reference with its license and any redistribution
                                    restriction. Two of the most prominent skill collections in this
                                    space — anthropics/skills and openai/skills — return license: null
                                    from the GitHub API and are therefore reference-only here: summarise
                                    and link, never vendor or redistribute. superpowers' own license is
                                    recorded in its card at
                                    repositories/agent-skills/obra--superpowers.md.
```

## What to take from it

```text
1. The directory-per-skill layout with references/ is the right structure for progressive disclosure,
   and it is validated here by a token budget rather than left to author discipline.
2. Narrow, procedure-named skills compose; domain-named ones do not.
3. An explicit "when NOT to use" section is the highest-value part of a skill document.
4. Plain markdown readable without tooling is worth preserving even in a heavily-schema'd repository —
   the schema constrains the frontmatter, not the body.
5. A large public collection is a source of conventions to evaluate, not content to copy. Read it,
   summarise it with attribution, respect its license, and write your own.
```

## What not to conclude

```text
✗ That its size validates its conventions.    Adoption measures attention. The conventions are worth
  adopting because they solve the loading, composition and staleness problems — which is a separate
  argument.
✗ That any specific skill's content is current. A skill collection without verified_at and expires_at
  per artifact cannot answer this, which is the gap this repository's frontmatter exists to close.
✗ That the absence of a schema is a defect.    It is a different tradeoff: lower authoring friction,
  weaker guarantees. For a personal collection that is often right; for a corpus intended as shared
  long-term memory retrieved by agents, it is not.
```

## References

- [`repositories/agent-skills/obra--superpowers.md`](../../../repositories/agent-skills/obra--superpowers.md) — the scored card with live metadata
- [`knowledge/agent-skills/skill-format.md`](../../agent-skills/skill-format.md) — this repository's SKILL.md contract
- [`knowledge/ai-engineering/source-scoring.md`](../source-scoring.md) · [`../freshness-policy.md`](../freshness-policy.md) · [`../repository-status.md`](../repository-status.md)
- [`knowledge/security/llm-security/excluded-sources.md`](../../security/llm-security/excluded-sources.md) — license-null handling and the exclusion policy
- [`skills/skill-authoring/SKILL.md`](../../../skills/skill-authoring/SKILL.md) · [`agents/skill-curator/AGENT.md`](../../../agents/skill-curator/AGENT.md)
- <https://github.com/obra/superpowers> · <https://github.com/anthropics/skills> · <https://github.com/openai/skills> · <https://github.com/VoltAgent/awesome-agent-skills>
