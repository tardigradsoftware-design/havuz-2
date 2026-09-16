---
id: adr-template
title: "ADR template: recording a decision with its reasoning and its review date"
domain: architecture
summary: >-
  The architecture decision record template used in this repository — context, options with their
  costs, the decision, the reasoning, what would reopen it, and the review date — plus the rules
  that make an ADR useful rather than ceremonial.
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
tags: [adr, decision-record, architecture, documentation, templates, reasoning]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-09-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related:
  - decision-records/matrix-template.md
  - knowledge/architecture/build-vs-adopt.md
  - knowledge/architecture/system-design-checklist.md
sources:
  - title: "Documenting Architecture Decisions"
    url: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
    type: methodology
    organization: Cognitect
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "Michael Nygard's original ADR formulation — title, context, decision, status, consequences. The template here extends it with alternatives-considered, reversibility and a review date."
---

# ADR-NNNN: <Short imperative summary of the decision>

Copy everything below the line into `decision-records/NNNN-<slug>.md`. Numbering is sequential and
never reused; a superseded ADR keeps its number.

---

```text
Status:        proposed | accepted | superseded by ADR-NNNN | deprecated
Date:          YYYY-MM-DD (the date the decision was made, not the date it was written up)
Deciders:      who was in the room, and who owns the outcome
Review date:   YYYY-MM-DD (when this must be revisited; derived from the decision's shelf life)
Reversibility: reversible | costly to reverse | irreversible
```

## Context

The situation that forces a decision. Facts and constraints only — no solution, no opinion.

```text
What is true:        the requirements, the volumes, the deadlines, the existing estate
What is constrained:  regulatory, budget, team skills, technology already in place, compatibility
What is uncertain:    the assumptions this decision rests on, each marked ASSUMPTION
What happens if we
  decide nothing:     the default that takes effect by inaction — this is always a decision
```

A context section that already implies the answer is not context, it is advocacy. If the reader can
guess the decision before reaching it, rewrite this section.

## Options considered

Every option that was genuinely considered, including the one chosen and the one that was tempting.
Costs are stated, not adjectives.

| # | Option | Cost | Risk | Reversibility | Fit to requirements |
|---|---|---|---|---|---|
| 1 | <option> | <build/run/maintenance cost> | <what could go wrong> | <exit cost> | <which requirements it meets, which it does not> |
| 2 | <option> | | | | |
| 3 | Do nothing | <the cost of the default> | | | |

"Do nothing" is always option 3 and always has a cost. Omitting it hides the fact that inaction was
available.

Where the options are repositories, libraries or vendors, score them rather than describing them:
[`knowledge/ai-engineering/source-scoring.md`](../knowledge/ai-engineering/source-scoring.md), and
use [`matrix-template.md`](matrix-template.md) for the comparison.

## Decision

One sentence, in the active voice, naming what will be done.

> We will <do X>, because <the one reason that decided it>.

## Reasoning

The argument that connects the context to the decision. This is the section that makes the ADR worth
keeping: it is what a future engineer needs in order to know whether the decision still holds.

```text
Which requirement or constraint dominated, and why it outweighed the others
Which option was rejected for which specific reason — name the plausible alternative and the
  concrete argument against it, not "it was less suitable"
What was traded away knowingly: performance for simplicity, cost for latency, flexibility for
  predictability. There is always a trade; the ADR should say which side was bought.
Which assumptions the decision rests on, and what happens to it if each one turns out false
```

## Consequences

```text
POSITIVE      what becomes possible or cheaper as a result
NEGATIVE      what becomes harder, more expensive or newly risky — stated honestly; an ADR with no
              negative consequences was not a decision, it was a preference
NEUTRAL       what changes that is neither better nor worse, but that people must now know
FOLLOW-UP     the work this decision creates, each with an owner
```

## What would reopen this decision

The conditions under which this decision should be revisited. Concrete and observable, not "if
circumstances change".

```text
- <a volume threshold being crossed>
- <a dependency being archived, relicensed or changing direction>
- <a requirement being added that this design cannot serve>
- <the review date arriving>
```

## Validation

How it will be known that the decision worked, and when that will be checked.

```text
Metric:       <the observable that indicates success or failure>
Target:       <the number>
Checked at:   <the date or the milestone>
```

## References

- The documents, measurements and analyses this decision rests on, each with what it supports.
- Related ADRs: superseded, supersedes, or constrains this one.

---

# Rules for using this template

```text
1. ONE DECISION PER ADR.   Two decisions in one document means one of them cannot be superseded
   independently, which is the whole point of numbering them.
2. WRITE IT WHEN THE DECISION IS MADE, not when the work is finished. A retrospective ADR records
   what happened; a contemporaneous one records what was known, which is what makes it useful.
3. NUMBER THEM SEQUENTIALLY AND NEVER REUSE A NUMBER.   A superseded ADR is kept, marked, and linked
   from its replacement. Deleting one loses the reasoning that prevents the same wrong decision being
   re-made.
4. RECORD THE REJECTED OPTIONS.   The rejected alternative is the most valuable content in the file.
   Without it, the next engineer re-litigates the decision from scratch.
5. STATE REVERSIBILITY EXPLICITLY.   It determines how much effort the decision deserves. Irreversible
   decisions — the data model, the primary language, the storage engine, the public API shape — get the
   most scrutiny; reversible ones should be deferred deliberately rather than decided early.
6. SET A REVIEW DATE FROM THE DECISION'S SHELF LIFE.   A decision resting on a volatile assumption
   (a framework's behaviour, a vendor's pricing, a volume forecast) has a short shelf life. See
   [`knowledge/ai-engineering/freshness-policy.md`](../knowledge/ai-engineering/freshness-policy.md).
7. AN ADR IS IMMUTABLE ONCE ACCEPTED.   Changing your mind is a new ADR that supersedes the old one.
   Editing history makes the record worthless.
8. DO NOT USE AN ADR FOR A PREFERENCE.   "We will use tabs" is a style decision; put it in the linter
   config. An ADR is for a choice with consequences that someone will later question.
```

## References

- [`matrix-template.md`](matrix-template.md) — the comparison table for multi-option decisions
- [`knowledge/architecture/build-vs-adopt.md`](../knowledge/architecture/build-vs-adopt.md) — the decision procedure an ADR usually records
- [`knowledge/architecture/system-design-checklist.md`](../knowledge/architecture/system-design-checklist.md) — the questions whose answers become ADRs
- [`knowledge/ai-engineering/source-scoring.md`](../knowledge/ai-engineering/source-scoring.md) — grading repository options
- [`knowledge/ai-engineering/freshness-policy.md`](../knowledge/ai-engineering/freshness-policy.md) — setting the review date
- [`skills/architecture-design/SKILL.md`](../skills/architecture-design/SKILL.md) · [`workflows/architecture-review/WORKFLOW.md`](../workflows/architecture-review/WORKFLOW.md)
- Nygard, "Documenting Architecture Decisions" — <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>
- adr-tools — <https://github.com/npryce/adr-tools> · MADR — <https://adr.github.io/madr/>
