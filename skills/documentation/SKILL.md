---
name: documentation
version: 1.0.0
description: >-
  Write documentation that answers a specific reader's specific question — typed by purpose
  (tutorial, how-to, reference, explanation), verified against the code, and maintained by the
  same pipeline as the code.
category: coding
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [documentation, writing, readme, api-docs, adr, dx, maintenance]
applies_to: [any]
priority: 80
requires: []
conflicts_with: []
estimated_tokens: 2733
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: The four documentation types
    anchor: "#the-four-documentation-types"
    purpose: decision
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Diátaxis — a systematic framework for technical documentation"
    url: https://diataxis.fr/
    type: methodology
    organization: Canonical / Daniele Procida
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Not fetched in this run; the four-type model is widely adopted. Verify the current site before quoting section names."
  - title: "Write the Docs"
    url: https://www.writethedocs.org/
    type: community
    confidence: medium
    claim_type: recommendation
    verified_at: 2026-09-15
related_skills: [code-review, api-design, research-synthesis, release-engineering, frontend-design]
related_repositories: [facebook/docusaurus, squidfunk/mkdocs-material, fern-api/fern, stoplightio/spectral]
tests: 6
---

# Documentation

## Purpose

Answer a specific reader's specific question at the moment they have it, in a form they can
act on. Documentation fails in two directions: it does not exist, or it exists and is wrong —
and wrong documentation is worse than none, because it is trusted.

## When to Use

```text
□ Shipping anything another person (or agent) will use without you in the room
□ After a decision that future readers will otherwise reverse by accident (an ADR)
□ When the same question has been answered twice in chat
□ Before a handover, release or onboarding wave
□ When onboarding time has grown and nobody knows why
```

## When NOT to Use

```text
✗ To document code that should be deleted or made self-explanatory
✗ To produce volume: a docs site nobody reads is maintenance debt with extra steps
✗ As a substitute for a readable API or a good error message
```

## The four documentation types

Mixing these in one page is the root cause of most bad documentation. Each has a different
reader, purpose, form and failure mode. (Model: Diátaxis — <https://diataxis.fr/>.)

```text
TUTORIAL        learning-oriented. A lesson that takes a beginner to a working result.
                form: steps, guaranteed to succeed, no choices, no explanation of why
                test: does the reader finish with something that works, and confidence?
                fails when: it branches, it explains theory, a step silently depends on context

HOW-TO GUIDE    task-oriented. Solves a specific problem for someone who already knows the basics.
                form: a titled problem, a numbered solution, alternatives, troubleshooting
                test: can a reader with the problem find and complete it?
                fails when: it assumes the tutorial's context, it omits the version it applies to

REFERENCE       information-oriented. Describes what exists, precisely and completely.
                form: structured, consistent, generated from code where possible, no narrative
                test: is every parameter, type, error, endpoint and default present and correct?
                fails when: it teaches, it opines, it drifts from the implementation

EXPLANATION     understanding-oriented. Why the system is the way it is; the context and the
                alternatives considered.
                form: prose, discussion, tradeoffs, links to evidence; no instructions
                test: does a reader afterwards make better decisions than before?
                fails when: it contains steps, it defends rather than explains
```

Every page declares its type. If a page needs two types, split it and link.

## Special documents

```text
README          the entry point, in this order: what it is (one sentence, no adjectives) ·
                why it exists / what problem · should you use it (and should you NOT) ·
                quickstart that actually runs · install · link to each doc type ·
                status and maintenance · license · where to get help.
                Test the quickstart on a clean machine, every release. Time it.
AGENTS.md       machine-readable operating instructions for agents working in the repo:
                commands to build/test/lint, conventions, boundaries, what must never be
                changed, where knowledge lives. Verified by execution, not by reading.
                See this repository's AGENTS.md for a worked example.
ADR             one decision, one file, immutable once accepted: context · options considered ·
                decision · consequences · status · date · deciders. Superseded ADRs are
                amended with a link, never rewritten. See decision-records/.
CHANGELOG       per release, grouped Added / Changed / Deprecated / Removed / Fixed / Security,
                with migration notes for every breaking change. Written for the reader
                upgrading, not for the author remembering.
CONTRIBUTING    how to set up, the definition of done, review expectations, how to propose
                a change, and the code of conduct link.
SECURITY.md     scope, disclosure channel, response SLA, supported versions, and the
                policy on what this project will and will not contain.
```

## Workflow

```text
IDENTIFY READER → CHOOSE TYPE → OUTLINE → WRITE → VERIFY → PUBLISH → MAINTAIN
```

```text
1 READER       Name the reader and the question. "A backend engineer adopting this library,
               asking how to authenticate a service-to-service call." One reader, one question
               per page. If you cannot name them, you do not know what to write.
2 TYPE         Pick from the four. Declare it at the top of the page.
3 OUTLINE      List the headings before the prose. An outline that does not answer the
               question will not become prose that does.
4 WRITE        Concrete over abstract · one idea per sentence · active voice ·
               the reader's vocabulary, not the implementer's · code that runs, copied from
               a real test · state the version and date the content applies to ·
               say what NOT to do and why (the most-read part of any guide) ·
               link instead of duplicating — one definition per fact.
5 VERIFY       Run every command, example and link. On a clean environment. Record the date
               and environment verified. An unverified example is a bug with prose around it.
6 PUBLISH      Discoverable: search works, navigation reflects the reader's task, the URL is
               stable. Versioned documentation per release where behaviour differs by version.
7 MAINTAIN     Docs live with the code, are reviewed in the same PR, and are regenerated
               where possible. Add a freshness field and a review date; scan for staleness
               in CI; treat a docs bug report with the same SLA as a code bug.
               Delete docs for deleted features in the same PR.
```

### Writing for agents as readers

Increasingly the first reader is a model. The same discipline applies, plus:

```text
□ Machine-readable frontmatter: what the file is, what it applies to, when it was verified,
  when it expires (see schemas/frontmatter.schema.json)
□ Stable anchors and explicit headings — retrieval is heading-driven
□ Self-contained sections: a chunk retrieved in isolation must still make sense and must
  carry its scope and date
□ No pronoun references across sections; no "as above"
□ Facts stated with their conditions, never as bare assertions ("in v3+, when X, then Y")
□ Explicit unknowns: an agent will fill a gap with a plausible invention
□ Deterministic commands with expected output, so an agent can verify success
```

## Failure Modes

```text
TYPE MIXING           A tutorial that stops to explain architecture; a reference that teaches.
UNVERIFIED EXAMPLES   Copied from an older version; fails on the first try.
NO VERSION SCOPE      Correct for v2, wrong for v4, undated.
README AS PITCH       Adjectives and badges, no quickstart, no "should you not use this".
DUPLICATED FACTS      The same instruction in four places; they drift and contradict.
GENERATED-ONLY DOCS   API reference with no explanation, how-to or tutorial.
ORPHANED PAGES        Written once, never linked, never found.
CHANGELOG AS GIT LOG  "fix stuff", "update" — useless to someone upgrading.
ADR REWRITING         Editing an accepted decision so the reasoning is lost.
DOC ROT               No owner, no review date, no staleness scan.
AGENT-HOSTILE PROSE   "As mentioned earlier" — retrieved in isolation, it means nothing.
```

## Quality Checklist

```text
□ Reader and question named per page; one of each
□ Type declared and honoured; no mixing within a page
□ Outline reviewed before prose was written
□ Concrete, active, version-scoped, in the reader's vocabulary
□ Every command and example executed on a clean environment; verification date recorded
□ Every link resolves; no duplicated facts (one definition, linked from elsewhere)
□ README: what/why/should-you/quickstart/status/license/help, in that order
□ ADRs immutable, with context, options, decision, consequences, date, deciders
□ CHANGELOG grouped by change class, with migration notes for breaking changes
□ AGENTS.md commands verified by execution
□ Published with working search, task-shaped navigation and stable versioned URLs
□ Freshness/review date in frontmatter; staleness scanned in CI
□ Docs reviewed in the same PR as the code they describe
□ Deleted features' docs deleted in the same PR
□ Written to survive isolated retrieval (no cross-section pronouns, self-contained chunks)
```

## Anti-Patterns

```text
✗ "Simply run the following command" — for a reader who has never seen the tool
✗ A README whose first paragraph is three adjectives
✗ An example whose output was never observed
✗ Documentation without a version or a date
✗ A CHANGELOG entry reading "various fixes"
✗ Rewriting an ADR instead of superseding it
✗ The same installation instructions in six files
✗ "See above" in a document designed to be retrieved in chunks
```

## References

- Diátaxis — <https://diataxis.fr/> · Write the Docs — <https://www.writethedocs.org/>
- [`code-review`](../code-review/SKILL.md) · [`api-design`](../api-design/SKILL.md) · [`research-synthesis`](../research-synthesis/SKILL.md)
- [`AGENTS.md`](../../AGENTS.md) · [`CONTRIBUTING.md`](../../CONTRIBUTING.md) · [`SECURITY.md`](../../SECURITY.md)
- [`decision-records/`](../../decision-records/) — ADR template
- [`schemas/frontmatter.schema.json`](../../schemas/frontmatter.schema.json) · [`scripts/update/check_staleness.py`](../../scripts/update/check_staleness.py)
- [`knowledge/agent-skills/`](../../knowledge/agent-skills/) — documentation as agent memory

## Related Skills

`code-review` · `api-design` · `research-synthesis` · `release-engineering` ·
`agent-memory-design` · `documentation`

## Evaluation Criteria

```text
1. Task completion: a new reader completes the quickstart unaided, first try (target 100%).
2. Verification rate: 100% of examples executed against the documented version.
3. Staleness: fraction of pages past review date (target < 5%).
4. Type purity: 0 pages mixing documentation types.
5. Support deflection: reduction in repeat questions after publication.
6. Agent retrievability: isolated chunks of the doc still yield correct answers.
```

Test cases in [`tests/`](tests/).
