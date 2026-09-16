---
name: research-synthesis
version: 1.0.0
description: >-
  Combine multiple investigations into one decision-ready report — reconciling conflicts, separating
  fact from inference, attributing every claim, and stating what remains unknown.
category: research
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [research, synthesis, reporting, meta-analysis, conflicts, decision-support]
applies_to: [any]
priority: 79
requires: [web-research, evidence-validation]
conflicts_with: []
estimated_tokens: 2478
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Synthesis rules
    anchor: "#synthesis-rules"
    purpose: implementation
  - heading: Report structure
    anchor: "#report-structure"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    url: https://arxiv.org/abs/2307.03172
    type: research-paper
    published: 2023-07-06
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Justifies leading with the conclusion and keeping the evidence set small and ordered."
related_skills: [web-research, evidence-validation, competitive-analysis, research-before-code, documentation]
related_repositories: [assafelovic/gpt-researcher, huggingface/awesome-papers]
tests: 6
---

# Research Synthesis

## Purpose

Turn N investigations into **one answer a decision-maker can act on**, without losing the
provenance of any claim or hiding any disagreement.

Synthesis is not summarisation. A summary compresses what was said; a synthesis decides what
is true, for which conditions, with what confidence, and what would change the answer.

## When to Use

```text
□ Several searches, papers, repositories or expert inputs must produce one conclusion
□ A decision requires a written recommendation with its evidence attached
□ Findings disagree and the disagreement must be resolved or explicitly preserved
□ Research must be handed to someone who was not present for it
□ Recording research into this knowledge base (knowledge/, research-archive/)
```

## When NOT to Use

```text
✗ A single well-sourced fact — cite it directly
✗ Before the research exists: synthesis without inputs produces plausible fiction
✗ When the decision-maker needs the raw material, not your interpretation — provide both
```

## Inputs

```text
question(s)      the framed questions each investigation answered
findings         claims with their sources, dates, types and confidence levels
conflicts        where sources disagree, and how they disagree
gaps             what nobody established
decision         what will be done with the synthesis — this determines the required depth
audience         expert or non-expert; this determines the vocabulary, not the rigour
```

## Synthesis rules

```text
1  LEAD WITH THE ANSWER.   The reader's first paragraph is the conclusion and its confidence.
                           Evidence follows. Burying the answer is a courtesy to nobody.
                           (Also the practical reason: attention is U-shaped over position —
                           arXiv:2307.03172.)

2  ONE CLAIM, ONE LINEAGE. Every claim carries its source(s), date, type and confidence.
                           A claim whose provenance is lost during synthesis becomes a rumour.

3  RECONCILE EXPLICITLY.   Where sources agree, say so and note the independence level.
                           Where they disagree, do not average, do not pick silently:
                           record both, diagnose the difference (version drift, scope,
                           measurement method, incentive, one is simply wrong), state which
                           you rely on and why, and say what would settle it.

4  SEPARATE THE EPISTEMIC LEVELS.  Label each statement:
                           FACT            verified from a primary source
                           INFERENCE       your reasoning from facts — show the reasoning
                           HYPOTHESIS      untested; state how it would be tested
                           OPINION         a judgement; say whose and on what basis
                           GENERATED       model output with no source. Never presented as fact.
                           Mixing these is the single most common synthesis defect.

5  SCOPE EVERY CONCLUSION. "For X, under conditions Y, as of date Z." An unscoped conclusion
                           will be applied outside its validity and blamed on the research.

6  QUANTIFY WHERE POSSIBLE, AND SHOW THE METHOD. A number without a measurement method,
                           sample and date is decoration.

7  DISCONFIRMING EVIDENCE IS MANDATORY. State the strongest argument against your conclusion.
                           A synthesis with no disconfirming section is advocacy.

8  NAME THE GAPS.          What is unknown, why it matters, what would resolve it, and how much
                           it would cost to find out. Gaps are findings.

9  RECOMMEND CONDITIONALLY. "Do A if <conditions>; do B if <other conditions>; revisit when
                           <trigger>." Unconditional recommendations from partial evidence are
                           overconfidence.

10 WRITE FOR RETRIEVAL.    Self-contained sections, explicit headings, dates and versions inline.
                           A chunk read in isolation six months from now must still be correct
                           and comprehensible. (This repository's frontmatter enforces this.)
```

## Report structure

```markdown
# <Question> — synthesis <date>

## Answer
<2–5 sentences: the conclusion, its confidence, and the conditions it holds under>

## Recommendation
<conditional: do X if …; do Y if …; revisit when …>

## Confidence and basis
| claim | level (FACT/INFERENCE/HYPOTHESIS/OPINION) | source(s) | date | confidence |
<the load-bearing claims only; the full evidence table is below or linked>

## Findings
### <theme 1>
<narrative, with inline citations>
### <theme 2>

## Conflicts
### Conflict: <question>
- A (<type>, <publisher>, <date>): "<quote>"
- B (<type>, <publisher>, <date>): "<quote>"
- Difference: <precise>
- Likely cause: <version drift | scope | method | incentive | error>
- Relied upon: <which, and why>
- Settled by: <the experiment or primary source>

## Arguments against
<the strongest disconfirming evidence and how much it weakens the conclusion>

## Unknowns
| gap | why it matters | how to resolve | cost | priority |

## Method
<queries run, sources opened and discarded, inclusion/exclusion criteria, budget spent,
 limitations of the method itself>

## Evidence table
| # | claim | source | type | publisher | page date | verified_at | confidence |

## Re-verification
<date and trigger: what would make this synthesis stale>
```

## Failure Modes

```text
SUMMARY NOT SYNTHESIS      Restating each source in turn; no conclusion, no reconciliation.
PROVENANCE LOSS            Claims survive the synthesis; their sources and dates do not.
CONFLICT ERASURE           Averaging, or quietly choosing the convenient side.
LEVEL COLLAPSE             Inference presented as fact; model output presented as sourced.
UNSCOPED CONCLUSION        "Use X" with no conditions, applied where it does not hold.
CONFIRMATION SYNTHESIS     Disconfirming evidence omitted or footnoted.
FALSE COMPLETENESS         No unknowns section, so the reader assumes full coverage.
METHOD OMISSION            Nobody can tell what was searched or what was excluded.
STALENESS INVISIBLE        No re-verification trigger; the report is trusted past its life.
RECENCY BIAS               The newest source wins regardless of quality or scope.
PRESTIGE BIAS              The most famous source wins regardless of measurement method.
VOLUME AS RIGOUR           Forty citations for a claim that needed two good ones.
```

## Quality Checklist

```text
□ Answer and confidence in the first paragraph; recommendation conditional
□ Every claim has source(s), date, type and confidence
□ Epistemic level labelled per statement: FACT / INFERENCE / HYPOTHESIS / OPINION / GENERATED
□ Agreements noted with their independence level; disagreements recorded in the conflict format
□ No averaging of conflicting numbers; no silent side-picking
□ Every conclusion scoped to conditions and a date
□ Numbers carry their measurement method, sample and date
□ "Arguments against" section present and genuinely strong
□ Unknowns listed with resolution path, cost and priority
□ Method section: queries, sources opened and discarded, criteria, budget, limitations
□ Full evidence table included or linked
□ Re-verification date and staleness trigger stated
□ Written to survive isolated retrieval: self-contained sections, inline versions and dates
□ Filed with frontmatter conforming to schemas/frontmatter.schema.json
```

## Anti-Patterns

```text
✗ "Sources suggest that…" with no named source
✗ A confidence level attached to the report rather than to individual claims
✗ Deleting the disagreeing source because it complicates the narrative
✗ Presenting an unscoped recommendation as universal
✗ Omitting the method because it "would be too long"
✗ Writing the conclusion last and burying it in the final paragraph
✗ Citing forty sources for a claim that two would establish
✗ A synthesis with no unknowns section
```

## References

- [`web-research`](../web-research/SKILL.md) · [`evidence-validation`](../evidence-validation/SKILL.md)
- [`competitive-analysis`](../competitive-analysis/SKILL.md) · [`documentation`](../documentation/SKILL.md)
- [`knowledge/research/`](../../knowledge/research/) · [`research-archive/`](../../research-archive/)
- [`knowledge/research/source-conflict-case-study.md`](../../knowledge/research/source-conflict-case-study.md)
- [`schemas/frontmatter.schema.json`](../../schemas/frontmatter.schema.json)
- Lost in the Middle, arXiv:2307.03172 (verified 2026-09-15)

## Related Skills

`web-research` · `evidence-validation` · `competitive-analysis` · `research-before-code` ·
`documentation` · `agent-memory-design`

## Evaluation Criteria

```text
1. Actionability: the decision-maker can act without asking a follow-up question.
2. Provenance completeness: 100% of claims carry source, date and confidence.
3. Conflict fidelity: 100% of known disagreements appear in the report, unreconciled-by-omission.
4. Level discipline: 0 inferences or generated statements presented as facts.
5. Independent reproduction: a second researcher reaches a compatible conclusion from the
   evidence table.
6. Durability: the synthesis is not invalidated within its re-verification window by
   information available at the time of writing.
```

Test cases in [`tests/`](tests/).
