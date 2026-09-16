---
name: skill-authoring
version: 1.0.0
description: >-
  Author a SKILL.md that an agent can execute: define one procedure, write the frontmatter contract, structure the body for progressive disclosure, cite sources for every high-confidence claim, and validate it before committing.
category: meta
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [skill-authoring, agent-skills, frontmatter, progressive-disclosure, documentation, meta]
applies_to: [skills, knowledge-base]
priority: 6
requires: []
conflicts_with: []
estimated_tokens: 2224
sections:
  - heading: "Purpose"
    anchor: "#purpose"
    purpose: overview
  - heading: "When to Use"
    anchor: "#when-to-use"
    purpose: when-to-use
  - heading: "When NOT to Use"
    anchor: "#when-not-to-use"
    purpose: pitfalls
  - heading: "Workflow"
    anchor: "#workflow"
    purpose: implementation
  - heading: "Failure Modes"
    anchor: "#failure-modes"
    purpose: pitfalls
  - heading: "Quality Checklist"
    anchor: "#quality-checklist"
    purpose: checklist
  - heading: "Anti-Patterns"
    anchor: "#anti-patterns"
    purpose: pitfalls
  - heading: "References"
    anchor: "#references"
    purpose: references
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "JSON Schema Specification, 2020-12 draft"
    url: https://json-schema.org/draft/2020-12/release-notes
    type: specification
    organization: "JSON Schema"
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The dialect schemas/skill.schema.json is written in; additionalProperties: false is what makes an unknown frontmatter key a build failure."
  - title: "obra/superpowers"
    url: https://github.com/obra/superpowers
    type: github-repository
    organization: "obra"
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "A large public agent-skill collection whose directory-per-skill layout, narrow naming and explicit applicability conditions inform steps 1, 2 and 9."
  - title: "Semantic Versioning 2.0.0"
    url: https://semver.org/
    type: specification
    license: CC BY 3.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The version field convention: MAJOR marks a breaking change to the procedure."
related_skills: [skill-curation, documentation, context-engineering]
related_repositories: []
tests: 24
---
# Skill Authoring

## Purpose

Write a skill that an agent can execute under context pressure. A skill is a procedure, not an essay:
it states when to use it, when not to, what it needs, what it does, how it fails and how to know it
worked — and it fits in a context window alongside the task it serves.

## When to Use

```text
✓ a repeatable procedure exists that agents keep re-deriving or getting wrong
✓ an existing skill is too broad, too long or missing its negative case
✓ a workflow needs a step that no current skill covers
✓ knowledge has accreted that belongs in a procedure rather than an article
```

## When NOT to Use

```text
✗ The content is a fact, a reference or an explanation. That is a knowledge article, not a skill.
✗ The procedure has two independent halves. That is two skills joined by requires, or a workflow.
✗ Nobody has performed the procedure. Write it after doing it, or it will describe an intention.
✗ The only content is a checklist with no conditions for use. Checklists belong inside a skill.
```

## Workflow

```text
1. NAME IT FOR THE PROCEDURE, NOT THE DOMAIN.   "database-optimization" describes what it does;
   "databases" describes a subject. A domain-named skill cannot be selected reliably, because every task
   in that domain looks like a match.

2. WRITE "WHEN NOT TO USE" FIRST.   It is the highest-value section and the one most often omitted. Name
   the lookalike situations — the ones where the skill seems to apply and does not. If you cannot name a
   case where it should not be used, the skill has no boundary and will be over-applied.

3. DECLARE THE FRONTMATTER CONTRACT.   name (matching the directory), version (SemVer), description (one
   sentence: what it does and when to reach for it), category, status, confidence, claim_type,
   evidence_level, source_type, updated, verified_at, expires_at, tags, applies_to, priority, requires,
   conflicts_with, estimated_tokens, sections, provenance, sources, related_skills,
   related_repositories, tests. All of it is validated against schemas/skill.schema.json with
   additionalProperties: false — an unknown key fails the build.

4. CITE SOURCES FOR HIGH-CONFIDENCE CLAIMS.   confidence: high or very-high requires a sources block; CI
   warns otherwise. Each source states what it supports. Downgrading confidence is a legitimate fix;
   inventing a source is not.

5. WRITE THE WORKFLOW AS NUMBERED, EXECUTABLE STEPS.   Each step has an action and an observable result.
   "Consider the tradeoffs" is not a step. "List the options in a table with cost, risk and
   reversibility, then pick the reversible one unless a stated constraint forbids it" is.

6. INCLUDE A FAILURE-MODES TABLE.   Failure, detection, response. A skill without one teaches the
   procedure and not its failure modes, so the agent cannot self-diagnose.

7. WRITE THE QUALITY CHECKLIST AS THE EXIT GATE.   Checkable statements, each answerable yes or no from
   the artifact produced. Not aspirations.

8. LIST THE ANTI-PATTERNS THIS SKILL EXISTS TO PREVENT.   Specific, named, with why each fails. This is
   what makes a skill better than a generic instruction.

9. APPLY PROGRESSIVE DISCLOSURE.   Keep the decision logic, the step sequence, the failure modes and the
   gates in SKILL.md. Move long lookup tables, exhaustive catalogues and extended examples into
   references/<topic>.md, each with its own frontmatter and sources, and state in the body that the file
   is loaded when the relevant step is reached. The body budget is 2500 tokens; CI warns above 135%.

10. FILL THE SECTIONS MAP.   Every body heading gets an entry with its anchor and purpose, so an agent can
   load one section instead of the whole file.

11. MEASURE estimated_tokens.   Do not guess. The validator computes it; set the field to the measured
   value. A wrong estimate defeats the loader's budgeting, which is the point of the field.

12. STATE REVERSIBILITY AND GATES.   Any step that mutates state says so and states how to undo it. Any
   irreversible or externally visible action routes to a human.

13. VALIDATE BEFORE COMMITTING.   python3 scripts/validate/validate_frontmatter.py must report zero
   errors for the new file, and validate_links.py must resolve every reference it makes.

14. RECORD PROVENANCE.   content_class (original, derived, curated, generated), generated_by, and
   human_reviewed. Never copy external content: summarise and link, respecting the upstream license.
   Several of the most useful public skill collections have no license at all and are reference-only.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Named for a domain | every task in that domain matches | rename for the procedure |
| No negative case | the skill is applied to lookalike situations | write "When NOT to Use" naming them |
| Body over budget | validator warns above 135% of 2500 tokens | move lookup material into references/ |
| Steps are aspirations | no observable result per step | rewrite each as action plus result |
| High confidence, no sources | validator warns | add sources or downgrade confidence |
| estimated_tokens guessed | drift warning | set it to the measured value |
| Sections map missing | the loader cannot select a section | add an entry per heading |
| Two procedures in one file | the body needs "part A" and "part B" | split, and join with requires |
| Copied upstream content | license risk, and provenance is wrong | summarise with attribution and link |
| Not validated | CI fails later | run both validators before committing |

## Quality Checklist

```text
□ the name describes a procedure, not a domain
□ "When NOT to Use" names the lookalike cases
□ the frontmatter satisfies schemas/skill.schema.json with no unknown keys
□ every high-confidence claim has a source stating what it supports
□ each workflow step has an action and an observable result
□ the failure-modes table covers detection and response
□ the quality checklist is the exit gate and is checkable
□ anti-patterns are specific to this skill
□ the body is within budget, with reference material in references/
□ the sections map covers every heading
□ estimated_tokens equals the measured value
□ mutating steps state reversibility; irreversible steps gate on a human
□ both validators pass with zero errors
```

## Anti-Patterns

```text
✗ AN ESSAY WITH A FRONTMATTER.   Explanatory prose an agent must interpret rather than execute.
✗ DOMAIN-NAMED SKILLS.   Unselectable, because everything matches.
✗ OMITTING THE NEGATIVE CASE.   The skill gets applied everywhere and fails where it should not have
  been used.
✗ ONE GIANT FILE.   Defeats progressive disclosure; an agent loads 6,000 tokens to use 1,500.
✗ UNDATED.   No verified_at or expires_at means it will be trusted forever. See the freshness policy.
✗ UNSOURCED CONFIDENCE.   "high" with nothing behind it is a claim about the author's certainty.
✗ COPYING AN UPSTREAM COLLECTION.   Several have no license; and a copy loses the reasoning that made
  the original work.
✗ NO FAILURE MODES.   The agent cannot self-diagnose, so it retries the same failing approach.
✗ GUESSED TOKEN COUNTS.   The loader budgets on this number; a wrong one defeats the design.
```

## References

- [`knowledge/agent-skills/skill-format.md`](../../knowledge/agent-skills/skill-format.md) — the field-by-field contract
- [`knowledge/ai-engineering/knowledge-base-architecture.md`](../../knowledge/ai-engineering/knowledge-base-architecture.md) — why the structure is shaped this way
- [`knowledge/ai-engineering/freshness-policy.md`](../../knowledge/ai-engineering/freshness-policy.md) · [`source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md)
- [`knowledge/security/llm-security/excluded-sources.md`](../../knowledge/security/llm-security/excluded-sources.md) — what may not be copied in
- [`knowledge/ai-engineering/agentic-coding/superpowers-analysis.md`](../../knowledge/ai-engineering/agentic-coding/superpowers-analysis.md) — a large public collection compared
- [`skills/skill-curation/SKILL.md`](../skill-curation/SKILL.md) · [`agents/skill-curator/AGENT.md`](../../agents/skill-curator/AGENT.md) · [`workflows/knowledge-base-maintenance/WORKFLOW.md`](../../workflows/knowledge-base-maintenance/WORKFLOW.md)
- [`schemas/skill.schema.json`](../../schemas/skill.schema.json) · [`scripts/validate/validate_frontmatter.py`](../../scripts/validate/validate_frontmatter.py)
