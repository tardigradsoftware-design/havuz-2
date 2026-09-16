---
id: decision-matrix-template
title: "Decision matrix template: comparing options on weighted, scored criteria"
domain: architecture
summary: >-
  The weighted decision matrix used alongside ADRs when several options must be compared — how to
  choose criteria, weight them before scoring, score against evidence rather than preference, and
  recognise when the matrix is being used to justify a decision already made.
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
tags: [decision-matrix, comparison, weighting, scoring, architecture, decision-record, selection]
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
  - decision-records/adr-template.md
  - knowledge/architecture/build-vs-adopt.md
  - knowledge/ai-engineering/source-scoring.md
sources:
  - title: "Documenting Architecture Decisions"
    url: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
    type: methodology
    organization: Cognitect
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "The ADR practice this matrix feeds; the matrix is the comparison evidence, the ADR is the decision and its reasoning."
---

# Decision Matrix — <the decision being made>

Use this when an ADR has three or more genuine options and the choice must be defensible. The matrix
is the evidence; the ADR is the decision. A matrix without an ADR is a spreadsheet, and an ADR without
a matrix is an assertion.

---

```text
Decision:      <the question being answered, phrased so the options are answers to it>
Date:          YYYY-MM-DD
Deciders:      who scored, who owns the outcome
Constraint:    <any hard requirement that eliminates options before scoring — license, residency,
                budget ceiling, existing estate>
```

## Step 1 — Eliminate on hard constraints, before scoring

An option that fails a hard constraint is out, and no score can rescue it. Doing this first prevents
the common failure where an attractive option accumulates enough points to outweigh a disqualifier.

| Option | Hard constraint check | Result |
|---|---|---|
| <option A> | <license compatible? data residency? budget? maintainable by this team?> | PASS / ELIMINATED (reason) |
| <option B> | | |

Hard constraints in this repository always include: license permitting the intended use (`license: null`
means do-not-redistribute), lifecycle status (`archived` means do-not-depend), and the exclusion policy
in [`knowledge/security/llm-security/excluded-sources.md`](../knowledge/security/llm-security/excluded-sources.md).

## Step 2 — Choose the criteria

Criteria come from the requirements, not from the options. If a criterion exists only to favour one
option, it is advocacy.

```text
RULES
  5-9 criteria.   Fewer and the comparison is shallow; more and the weights become noise.
  Independent.    Two criteria that measure the same thing double-count it. "Performance" and
                  "latency" are one criterion.
  Observable.     Each must be scoreable from evidence: a measurement, a document, a scored record.
                  "Community feel" is not scoreable.
  Weighted BEFORE scoring.  Weighting after seeing the scores is how a matrix is reverse-engineered
                  to justify a decision already made. Write the weights down first.
```

## Step 3 — Weight the criteria

Weights sum to 1.00 and reflect the requirements, not the preferences.

| Criterion | Weight | Why this weight |
|---|---:|---|
| <fit to requirements> | 0.25 | <the requirement it maps to> |
| <total cost of ownership> | 0.20 | |
| <maintenance and lifecycle risk> | 0.20 | |
| <security and compliance> | 0.15 | |
| <team capability and ramp-up> | 0.10 | |
| <exit cost / reversibility> | 0.10 | |
| **Total** | **1.00** | |

Exit cost is a criterion, and it is the one most often omitted. An option that scores well and cannot
be left is a different proposition from one that can.

## Step 4 — Score against evidence

Score 1-5 per criterion. Every score has an evidence note; a score without one is an opinion and is
marked as such.

| Criterion | Weight | Option A | Evidence | Option B | Evidence | Option C | Evidence |
|---|---:|---:|---|---:|---|---:|---|
| <criterion> | 0.25 | 4 | <measurement, document, or scored record> | 3 | | 5 | |
| | | | | | | | |
| **Weighted total** | 1.00 | **?.??** | | **?.??** | | **?.??** | |

```text
SCORING DISCIPLINE
  Score each option against the criterion, not against the other options. Anchoring to a rival
    produces spread that means nothing.
  1 = fails the requirement · 3 = meets it · 5 = materially exceeds it. Define the anchors once and
    use them consistently.
  Where an option is a repository, take the score from metadata/repositories.json rather than
    re-judging it: trust_score, tier, status, license_risk. See
    knowledge/ai-engineering/source-scoring.md.
  Unknown is scored as UNKNOWN and handled in step 6 — not as 3. A neutral score for an unknown
    hides the gap in the analysis.
```

## Step 5 — Sensitivity check

The winner is only meaningful if it survives a plausible change in the weights.

```text
□ Remove the highest-weighted criterion. Does the winner change? If yes, the decision rests on one
  judgement and that judgement needs scrutiny.
□ Shift each weight by ±0.05 in turn. Does the ranking flip? If a small shift flips it, the options
  are effectively tied and the honest conclusion is "either, choose on a criterion not in the matrix".
□ Score the runner-up as if every UNKNOWN were a 3 and the winner as if every UNKNOWN were a 2. Does
  the order hold? If not, resolving the unknowns is the next action, not the decision.
```

## Step 6 — Record the unknowns

| Unknown | Affects | How it would be resolved | By when |
|---|---|---|---|
| <what is not known> | <which criterion and which option> | <the experiment, spike, quote or measurement that settles it> | <date> |

An unknown that could change the outcome is a reason to defer the decision or to run the spike — not a
reason to guess. Record it either way; a decision made over an unstated unknown is unauditable.

## Step 7 — Write the conclusion

```text
DECISION      <the option chosen>
WHY           <the one or two criteria that decided it — not the total, which is a summary>
TRADED AWAY   <what was knowingly given up, and why that was acceptable>
REOPENS IF    <the observable condition that would force this decision to be revisited>
REVIEW DATE   <derived from the shelf life of the assumptions, per the freshness policy>
```

The total score does not make the decision; it disciplines it. A conclusion that says "option B won
with 4.12" is not a conclusion — it reports arithmetic. Name the criterion that decided it.

---

# When a matrix is the wrong tool

```text
✗ TWO OPTIONS, ONE OBVIOUS.     Write the reasoning in the ADR directly. A matrix for two options is
  ceremony.
✗ THE CRITERIA ARE UNKNOWABLE.  A genuinely novel problem where nobody can score anything produces a
  table of guesses with false precision. Spike first, then score.
✗ THE DECISION IS ALREADY MADE. A matrix built to justify a conclusion produces weights chosen after
  the scores. This is the most common misuse and it is worse than no matrix, because it launders a
  preference as an analysis. Detect it by asking whether the weights were written down before scoring.
✗ THE OPTIONS ARE NOT COMPARABLE. Different problem framings cannot be scored on one axis. Reframe the
  question first.
✗ A REVERSIBLE, LOW-STAKES CHOICE. Decide, try it, and change it. The matrix costs more than the error.
```

## References

- [`adr-template.md`](adr-template.md) — the decision record this matrix supports
- [`knowledge/architecture/build-vs-adopt.md`](../knowledge/architecture/build-vs-adopt.md) — the most common decision this is used for
- [`knowledge/ai-engineering/source-scoring.md`](../knowledge/ai-engineering/source-scoring.md) — scoring repository options from observable facts
- [`knowledge/agent-engineering/framework-comparison.md`](../knowledge/agent-engineering/framework-comparison.md) — a worked comparison
- [`skills/architecture-design/SKILL.md`](../skills/architecture-design/SKILL.md) · [`skills/competitive-analysis/SKILL.md`](../skills/competitive-analysis/SKILL.md) · [`skills/repository-analysis/SKILL.md`](../skills/repository-analysis/SKILL.md)
- [`workflows/architecture-review/WORKFLOW.md`](../workflows/architecture-review/WORKFLOW.md)
- Nygard, "Documenting Architecture Decisions" — <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>
