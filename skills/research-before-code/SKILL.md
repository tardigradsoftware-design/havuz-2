---
name: research-before-code
version: 1.0.0
description: >-
  Force an agent to understand, search, compare, verify and plan before writing any implementation
  code. Converts "start coding" into "establish evidence, choose a proven approach, then implement".
category: research
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [research, planning, evidence, anti-hallucination, workflow-gate, meta]
applies_to: [any]
priority: 95
requires: [web-research, evidence-validation, dont-reinvent-the-wheel]
conflicts_with: []
estimated_tokens: 2816
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: When to Use
    anchor: "#when-to-use"
    purpose: when-to-use
  - heading: When NOT to Use
    anchor: "#when-not-to-use"
    purpose: when-to-use
  - heading: Inputs
    anchor: "#inputs"
    purpose: overview
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Failure Modes
    anchor: "#failure-modes"
    purpose: pitfalls
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
  - heading: Anti-Patterns
    anchor: "#anti-patterns"
    purpose: pitfalls
  - heading: References
    anchor: "#references"
    purpose: references
  - heading: Evaluation Criteria
    anchor: "#evaluation-criteria"
    purpose: validation
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    url: https://arxiv.org/abs/2210.03629
    type: research-paper
    organization: Princeton University / Google
    published: 2022-10-06
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Interleaving reasoning with external lookups reduces hallucination and error propagation versus reasoning alone."
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    url: https://arxiv.org/abs/2307.03172
    type: research-paper
    organization: Stanford / UC Berkeley / Samaya AI
    published: 2023-07-06
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Justifies the small, high-relevance evidence set instead of dumping everything found."
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    url: https://arxiv.org/abs/2303.11366
    type: research-paper
    published: 2023-03-20
    license: CC BY 4.0
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Basis for the explicit retry-with-reflection rule when a gate fails."
related_skills: [web-research, evidence-validation, dont-reinvent-the-wheel, project-planning, repository-analysis]
related_repositories: [assafelovic/gpt-researcher, oraios/serena, upstash/context7]
tests: 19
---

# Research Before Code

## Purpose

Stop the agent from treating its training data as a sufficient specification.

The default failure is not laziness, it is confidence: an agent that has seen a
thousand `next-auth` examples will write a plausible authentication flow for a
library version that changed two releases ago. This skill inserts a mandatory
evidence phase between *understanding the request* and *writing implementation code*.

It produces one artifact — a **Research Decision Record** — that states what was
investigated, what was found, what was chosen, what was rejected and why, and what
remains uncertain. Implementation is not allowed to start until that record exists
and its gates pass.

## When to Use

```text
□ Any task that will produce code you intend to keep
□ Any task naming a specific library, framework, API, cloud service or protocol
□ Any task where the cost of being wrong exceeds the cost of checking
□ Any task where the request contains an implicit technology choice
   ("build me auth", "add caching", "make it fast")
□ Any task where you are about to write a utility that smells like it should exist
□ Migrations, upgrades, and anything touching security, payments or data integrity
```

## When NOT to Use

```text
✗ A one-line typo fix or a rename with compiler verification
✗ Purely local refactoring whose correctness is proved by the existing test suite
✗ Throwaway spikes explicitly labelled as disposable (but say so in the output)
✗ Tasks inside a codebase whose conventions are already documented in AGENTS.md —
  read the project's own instructions instead of researching the internet
✗ When the human has already pinned the exact library, version and pattern:
  research the version's API, not the choice
```

Skipping research is a decision. Record it: `research_skipped: <reason>`.

## Inputs

```text
task            the request, verbatim, plus any constraints stated
codebase        current stack, versions, existing patterns (package.json, requirements.txt,
                go.mod, AGENTS.md, lockfiles)
constraints     deadline, budget, deployment target, compliance, team skill
risk_class      low | medium | high  (high = security, payments, data loss, auth, migrations)
```

## Required Context

Before searching, load — in this order, stopping as soon as the question is answered:

```text
1. the repository's own AGENTS.md / CLAUDE.md / .cursor/rules  (project truth beats internet truth)
2. lockfiles and manifests                                      (actual installed versions)
3. indexes/topics.md                                            (does this KB already know?)
4. metadata/repositories.json filtered by category + tags       (is there a proven tool?)
5. gotchas/ and failure-modes/ for the domain                   (what breaks?)
6. only then: external search
```

Never invert this order. External search is the most expensive and least specific source.

## Workflow

```text
UNDERSTAND → SEARCH → COMPARE → VERIFY → PLAN → IMPLEMENT → TEST → REVIEW
```

### Stage 1 — UNDERSTAND

Restate the task in your own words and list the decisions it forces.

```text
Deliverable:      <what artifact exists at the end>
Implicit choices: <every technology/pattern decision the request assumes>
Unknowns:         <what you cannot answer from the codebase alone>
Risk class:       <low|medium|high + why>
Success test:     <the observable condition that means "done">
```

**Exit gate:** at least one implicit choice is named, or the task is explicitly
`research_skipped` with a reason.

### Stage 2 — SEARCH

For each unknown, run the [`web-research`](../web-research/SKILL.md) skill.
Minimum coverage:

```text
□ official documentation for the current major version
□ the official repository's README + CHANGELOG + open issues mentioning your error/symptom
□ at least one independent source (a second project, a paper, a maintainer post)
□ this knowledge base (indexes/, knowledge/, gotchas/)
```

Record every candidate with its URL, publication date and source type.

**Exit gate:** ≥2 independent sources per load-bearing unknown, or the unknown is
marked `UNRESOLVED` with an explicit statement of what would resolve it.

### Stage 3 — COMPARE

Fill a decision matrix — never a vibe. One row per candidate option.

```markdown
| Option | Maturity | License | Fit to constraints | Cost to adopt | Cost to remove | Risk |
|---|---|---|---|---|---|---|
```

Use the [`decision-records/matrix-template.md`](../../decision-records/matrix-template.md)
template. Include **"do nothing / hand-roll"** as a row — it is usually wrong, but
writing it down is what makes the alternative falsifiable.

**Exit gate:** at least two options compared, and the rejected ones have a stated reason.

### Stage 4 — VERIFY

Apply [`evidence-validation`](../evidence-validation/SKILL.md) to the chosen option:

```text
□ Does the repository exist? (resolve the URL, do not trust the memory of it)
□ Is it archived / abandoned / in maintenance mode?
□ What license? Can we vendor it?
□ Does the version we plan to use actually have the API we plan to call?
□ Is there a SECURITY.md? Any open advisory?
□ Does an independent source corroborate the claim we are relying on?
```

Prefer `metadata/repositories.json` over a fresh guess: it already carries
`status`, `tier`, `license_risk`, `trust_score` and `stars_checked_at`.

**Exit gate:** every load-bearing claim in the plan has `confidence` ≥ medium and a
`verified_at` date. Anything below is either re-verified or removed from the plan.

### Stage 5 — PLAN

Write the Research Decision Record:

```markdown
## Research Decision Record — <task>
Date / researcher:      2026-09-15 / <agent>
Risk class:             high

### Decision
Use <option> at <version> for <purpose>.

### Why
<the two or three constraints that decided it>

### Rejected
- <option B> — <specific reason, with source>
- hand-rolling — <specific reason>

### Evidence
| Claim | Source | Type | Verified | Confidence |
|---|---|---|---|---|

### Open risks
- <what could still be wrong, and how we would detect it>

### Implementation plan
1. <step> — gate: <observable condition>
2. …

### Validation plan
- <the tests that prove it worked>
```

**Exit gate:** a reader who was not present could execute the plan without asking questions.

### Stage 6 — IMPLEMENT

Follow the plan. When reality contradicts the research, **stop and update the record**
rather than silently improvising. Improvisation is where verified research turns back
into hallucination.

### Stage 7 — TEST

Run the validation plan from stage 5. Add regression tests for each open risk.

### Stage 8 — REVIEW

Compare the outcome to the record. Feed results back:

```text
what worked        → strengthen the pattern or knowledge article
what failed        → gotchas/ or failure-modes/ entry
what was outdated  → re-verify the source and update verified_at
what was missing   → knowledge candidate (goes to experimental/, not core)
```

## Failure Modes

```text
RESEARCH THEATRE     Searching a lot and citing nothing. Fix: the evidence table is mandatory.
CONFIRMATION SEARCH  Only looking for sources that agree with the first idea.
                     Fix: stage 3 requires a rejected option with a reason.
STALE OFFICIAL DOCS  Reading a docs page for v4 while installing v6.
                     Fix: record the version the doc describes, next to the URL.
STAR-DRIVEN CHOICE   Picking the most-starred option regardless of fit or status.
                     Fix: filter by status and license_risk before sorting by stars.
BLOG-ONLY EVIDENCE   Every source is a tutorial. Fix: ≥1 official or primary source per claim.
CONTEXT FLOOD        Pasting every page found into the prompt.
                     Fix: keep only the evidence table; link the rest.
PERPETUAL RESEARCH   Never starting. Fix: cap stage 2-4 at a fixed budget and record open risks.
SILENT IMPROVISATION Abandoning the plan mid-implementation without updating the record.
```

## Quality Checklist

```text
□ Task restated with implicit choices named
□ Project's own instruction files read before the internet
□ ≥2 independent sources per load-bearing unknown
□ Decision matrix includes a rejected option with a reason
□ Every chosen dependency: exists, license known, status known, version pinned
□ Research Decision Record written before the first line of implementation code
□ Open risks listed with a detection method for each
□ Validation plan defined before implementation
□ Outcome fed back into gotchas/ or experimental/ after review
□ Risk class justified in one line
```

## Examples

See [`examples/`](examples/) — `example-001-auth-library.md` walks a full record for
"add authentication to a Next.js + Supabase app", including the rejected option.

## Anti-Patterns

```text
✗ "I'll use X because it's popular" with no source, no version, no license check
✗ Researching the framework but not the version's breaking changes
✗ Writing the plan after the code, as documentation of what was already done
✗ Treating a single high-ranking search result as settled fact
✗ Copying a snippet from a source dated before the library's last major release
✗ Skipping verification because the task "feels small"
```

## References

- [`web-research`](../web-research/SKILL.md) — how to search and cross-check
- [`evidence-validation`](../evidence-validation/SKILL.md) — how to grade a source
- [`dont-reinvent-the-wheel`](../dont-reinvent-the-wheel/SKILL.md) — the reuse gate
- [`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md)
- [`knowledge/research/source-conflict-case-study.md`](../../knowledge/research/source-conflict-case-study.md)
- ReAct, arXiv:2210.03629 — reasoning interleaved with external action reduces hallucination
- Lost in the Middle, arXiv:2307.03172 — why the evidence set stays small and relevant

## Related Skills

`web-research` · `evidence-validation` · `dont-reinvent-the-wheel` · `project-planning` ·
`repository-analysis` · `dependency-analysis`

## Evaluation Criteria

A run of this skill is successful when:

```text
1. The Research Decision Record exists and predates the first implementation commit.
2. Every load-bearing claim in it has a URL, a date and a confidence level.
3. At least one option was rejected with a stated, checkable reason.
4. The implemented solution matches the record, or the record was updated before it diverged.
5. A reviewer can reproduce the decision from the record alone.
```

Measured in [`evaluations/knowledge-base/`](../../evaluations/) task suite: compare
`without-kb` vs `with-kb` on *wrong-API rate*, *reinvented-utility rate* and
*time-to-first-correct-implementation*.
