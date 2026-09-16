---
id: agent-skills-skill-format
title: "The SKILL.md format: what the fields mean and why each one exists"
domain: agent-skills
summary: >-
  Field-by-field reference for the SKILL.md contract used across the 36 skills in this repository —
  required frontmatter, the body section order, progressive disclosure into references/, and the
  rules that keep a skill loadable and gradeable.
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
tags: [skill-format, agent-skills, frontmatter, schema, progressive-disclosure, authoring]
applies_to: [skills, agent-skill-collections]
audience: [both]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
sections:
  - heading: The contract
    anchor: "#the-contract"
    purpose: overview
  - heading: Required frontmatter
    anchor: "#required-frontmatter"
    purpose: implementation
  - heading: Body sections
    anchor: "#body-sections"
    purpose: implementation
  - heading: Progressive disclosure
    anchor: "#progressive-disclosure"
    purpose: decision
  - heading: Authoring rules
    anchor: "#authoring-rules"
    purpose: pitfalls
estimated_tokens: 2055
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [skill-authoring, skill-curation]
related_repositories: [anthropics/skills, openai/skills, obra/superpowers, VoltAgent/awesome-agent-skills]
related:
  - knowledge/agent-engineering/framework-comparison.md
  - knowledge/ai-engineering/knowledge-base-architecture.md
  - schemas/skill.schema.json
  - skills/AGENTS.md
sources:
  - title: "JSON Schema Specification, 2020-12 draft"
    url: https://json-schema.org/draft/2020-12/release-notes
    type: specification
    organization: JSON Schema
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "schemas/skill.schema.json is written in this dialect with additionalProperties: false, which is what makes an unknown frontmatter key a build failure."
  - title: "anthropics/skills"
    url: https://github.com/anthropics/skills
    type: github-repository
    organization: Anthropic
    claim_type: fact
    confidence: high
    verified_at: 2026-09-15
    note: "Public example collection of the SKILL.md convention. Returns license: null — reference only, do not redistribute."
---

# The SKILL.md Format

## The contract

A skill is a **procedure an agent can execute**, not a document a human reads. That distinction
drives every rule below. It means a skill must state when to use it, when not to, what it needs,
what it produces, how it fails, and how to know it worked — and it must fit in a context window
alongside the task it is being used for.

Skills live at `skills/<kebab-name>/SKILL.md`, one directory per skill, with optional
`references/`, `assets/` and `scripts/` alongside. Validated by
[`schemas/skill.schema.json`](../../schemas/skill.schema.json).

## Required frontmatter

```yaml
---
name: kebab-case-name           # must match the directory name
version: 1.0.0                  # SemVer; MAJOR = breaking change to the procedure
description: >-                 # one sentence: what it does and when to reach for it
category: coding                # see the schema enum
status: active                  # active | experimental | deprecated | draft
confidence: high                # very-high | high | medium | low
claim_type: recommendation      # fact | recommendation | experiment | opinion | hypothesis
source_type: methodology        # what kind of source backs it
updated: 2026-09-15             # date of last content change
verified_at: 2026-09-15         # date the cited sources were last actually reached
expires_at: 2027-03-15          # re-verify after this; see freshness-policy.md
tags: [...]
applies_to: [...]               # what kinds of work it applies to
priority: 1                     # load order when several skills are relevant
requires: []                    # other skills this one depends on
conflicts_with: []              # skills whose guidance contradicts this one
estimated_tokens: 1200          # measured, not guessed — CI warns on drift
sections:                       # the section map an agent uses to load part of the file
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
provenance:
  content_class: original       # original | derived | curated | generated
  generated_by: null
  human_reviewed: true
sources: []                     # required when confidence is high or very-high
related_skills: []
related_repositories: []
tests: []                       # how the skill itself is known to work
---
```

The three fields agents skip and should not:

```text
estimated_tokens   tells the loader what this costs before loading it. Must equal the measured
                   value; CI warns when it drifts, because a wrong estimate defeats budgeting.
sections           lets an agent load one section instead of the whole file. Without it, the
                   progressive-disclosure design cannot work.
conflicts_with     the only structural way to surface contradictory guidance instead of letting
                   the agent silently pick one.
```

## Body sections

Order is fixed, because the loader and the reviewer both depend on it:

```text
1.  Purpose                 what problem this solves, in two or three sentences
2.  When to Use             the conditions that make this the right skill
3.  When NOT to Use         the conditions that look similar but are not — the highest-value
                            section in the file, and the one most often omitted
4.  Inputs                  what must be available before starting, with types
5.  Workflow                numbered steps. Each step has an action and an observable result.
6.  Failure Modes           what goes wrong, how it is detected, what to do about it
7.  Quality Checklist       the gate before declaring done
8.  Anti-Patterns           the specific mistakes this skill exists to prevent
9.  References              the sources, with what each one supports
10. Related Skills          what to load next or instead
11. Evaluation Criteria     how to tell whether the output was good
```

Steps in the workflow must be executable as written. "Consider the tradeoffs" is not a step;
"list the options in a table with cost, risk and reversibility, then pick the one that is
reversible unless a stated constraint forbids it" is.

## Progressive disclosure

A skill body has a token budget — 2500, with CI warning above 135% of it. The budget is not
arbitrary: it is what allows an agent to hold several relevant skills in context at once.

```text
STAYS IN SKILL.md          the decision logic, the step sequence, the failure modes, the
                           quality gate, the anti-patterns. What is needed to run the procedure.

MOVES TO references/       long lookup tables, exhaustive catalogues, full checklists, extended
                           worked examples, vendor-specific detail. What is needed at one step.
```

Five skills in this repository carry a `references/` directory for exactly this reason —
ai-slop-detection (the symptom catalogue), security-audit (the full checklist), seo-audit (the
seven layers), deployment (rollout strategies) and agent-memory-design (the memory taxonomy). In
each case the moved file states that it is loaded when the relevant step is reached, and the skill
body keeps a pointer plus enough summary to know when to load it.

Reference files are validated against the knowledge schema, carry their own frontmatter and their
own sources, and link back to the parent skill in `related_skills`.

## Authoring rules

```text
1. One skill, one procedure.    If the file needs "part A" and "part B", it is two skills joined
                                by requires, or a workflow.
2. Name the negative case.      "When NOT to Use" is mandatory and must name the lookalike
                                situation, not restate the positive condition.
3. Every claim carries provenance.  confidence: high or very-high requires sources[]. CI warns
                                otherwise. Downgrading the confidence is a legitimate fix;
                                inventing a source is not.
4. Never copy external content. Summarise and link, respecting the upstream license. Several of
                                the most useful public skill collections have no license at all
                                (anthropics/skills, openai/skills) — they are reference-only.
5. Measure, don't estimate, estimated_tokens. The validator computes it; the frontmatter must
                                match.
6. Date everything.             updated, verified_at and expires_at are all required. A skill with
                                no expiry will be trusted forever, which is the failure the
                                freshness policy exists to prevent.
7. Prefer reversible steps.     A workflow step that mutates state says so and states how to undo
                                it. Tier-3 actions route to a human.
8. Write for the reader who is  an agent under context pressure. Short paragraphs, tables for
                                enumerations, code fences for exact syntax, no rhetorical padding.
```

## References

- [`schemas/skill.schema.json`](../../schemas/skill.schema.json) — the enforced contract
- [`skills/AGENTS.md`](../../AGENTS.md) — directory-level guidance for authors
- [`knowledge/ai-engineering/knowledge-base-architecture.md`](../ai-engineering/knowledge-base-architecture.md)
- [`knowledge/ai-engineering/freshness-policy.md`](../ai-engineering/freshness-policy.md) · [`source-scoring.md`](../ai-engineering/source-scoring.md)
- [`knowledge/security/llm-security/excluded-sources.md`](../security/llm-security/excluded-sources.md) — what may not be copied in
- [`agents/skill-curator/AGENT.md`](../../agents/skill-curator/AGENT.md) — admission review
- <https://github.com/anthropics/skills> · <https://github.com/openai/skills> · <https://github.com/obra/superpowers> · <https://github.com/VoltAgent/awesome-agent-skills>
