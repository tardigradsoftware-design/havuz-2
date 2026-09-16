# Test cases — `research-synthesis`

Every clause below is derived from this skill's own body text. Nothing here is a
generic control that would read the same for a different skill:

| Case kind | Derived from | What it asserts |
|---|---|---|
| Applies | Purpose, Workflow step titles, Quality Checklist items | the named checklist conditions hold and the named steps ran |
| Declines | each `When NOT to Use` exclusion | the exclusion is honoured and the alternative it names is used |
| Detects | each `Failure Modes` entry, with its own detection signal and response | the failure is caught by that signal and answered by that response |
| Avoids | each `Anti-Patterns` entry, with the consequence it states | the anti-pattern is absent for the reason this skill gives |

Quoted text is the skill's own wording. A case whose quoted material could be
lifted from another skill is a defect and should be reported, not relaxed.

Regenerate: `python3 scripts/generate-index/generate_skill_tests.py`
Measure distinctness: `python3 scripts/generate-index/generate_skill_tests.py --report`

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):


## Case 1 — Applies to the task it was written for

```text
GIVEN    A task inside this skill's stated purpose: Turn N investigations into **one answer a decision-maker can act on**, without losing the provenance of any claim or hiding any disagreement. Synthesis is not summarisation. A summary compresses what was said;
WHEN     the agent executes `research-synthesis` end to end on that task
THEN     and before delivery these specific conditions hold: "Answer and confidence in the first paragraph; recommendation conditional"; "Arguments against" section present and genuinely strong"; "Filed with frontmatter conforming to schemas/frontmatter.schema.json"
FAIL IF  "Answer and confidence in the first paragraph; recommendation conditional" is false, or "Filed with frontmatter conforming to schemas/frontmatter.schema.json" is false, or "Arguments against" section present and genuinely strong" is false
```

## Case 2 — Declines: A single well-sourced fact — cite it directly

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A single well-sourced fact — cite it directly
WHEN     the agent considers `research-synthesis` for that task
THEN     the skill is not selected, because this task is the excluded case "A single well-sourced fact — cite it directly", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A single well-sourced fact — cite it directly"; or `research-synthesis` is declined without naming that exclusion
```

## Case 3 — Declines: Before the research exists: synthesis without inputs produces plausible…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Before the research exists: synthesis without inputs produces plausible fiction
WHEN     the agent considers `research-synthesis` for that task
THEN     the skill is not selected, because this task is the excluded case "Before the research exists: synthesis without inputs produces plausible fiction", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Before the research exists: synthesis without inputs produces plausible fiction"; or `research-synthesis` is declined without naming that exclusion
```

## Case 4 — Declines: When the decision-maker needs the raw material,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When the decision-maker needs the raw material, not your interpretation — provide both
WHEN     the agent considers `research-synthesis` for that task
THEN     the skill is not selected, because this task is the excluded case "When the decision-maker needs the raw material, not your interpretation — provide both", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When the decision-maker needs the raw material, not your interpretation — provide both"; or `research-synthesis` is declined without naming that exclusion
```

## Case 5 — Detects: SUMMARY NOT SYNTHESIS

```text
GIVEN    A run of this skill in which the known failure mode is present: SUMMARY NOT SYNTHESIS
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "SUMMARY NOT SYNTHESIS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Restating each source in turn; no conclusion, no reconciliation."
FAIL IF  "SUMMARY NOT SYNTHESIS" appears in the work and is reported as complete — specifically "Restating each source in turn; no conclusion, no reconciliation."
```

## Case 6 — Detects: PROVENANCE LOSS

```text
GIVEN    A run of this skill in which the known failure mode is present: PROVENANCE LOSS
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "PROVENANCE LOSS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Claims survive the synthesis; their sources and dates do not."
FAIL IF  "PROVENANCE LOSS" appears in the work and is reported as complete — specifically "Claims survive the synthesis; their sources and dates do not."
```

## Case 7 — Detects: CONFLICT ERASURE

```text
GIVEN    A run of this skill in which the known failure mode is present: CONFLICT ERASURE
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "CONFLICT ERASURE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Averaging, or quietly choosing the convenient side."
FAIL IF  "CONFLICT ERASURE" appears in the work and is reported as complete — specifically "Averaging, or quietly choosing the convenient side."
```

## Case 8 — Detects: LEVEL COLLAPSE

```text
GIVEN    A run of this skill in which the known failure mode is present: LEVEL COLLAPSE
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "LEVEL COLLAPSE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Inference presented as fact; model output presented as sourced."
FAIL IF  "LEVEL COLLAPSE" appears in the work and is reported as complete — specifically "Inference presented as fact; model output presented as sourced."
```

## Case 9 — Detects: UNSCOPED CONCLUSION

```text
GIVEN    A run of this skill in which the known failure mode is present: UNSCOPED CONCLUSION
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "UNSCOPED CONCLUSION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Use X" with no conditions, applied where it does not hold."
FAIL IF  "UNSCOPED CONCLUSION" appears in the work and is reported as complete — specifically "Use X" with no conditions, applied where it does not hold."
```

## Case 10 — Detects: CONFIRMATION SYNTHESIS

```text
GIVEN    A run of this skill in which the known failure mode is present: CONFIRMATION SYNTHESIS
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "CONFIRMATION SYNTHESIS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Disconfirming evidence omitted or footnoted."
FAIL IF  "CONFIRMATION SYNTHESIS" appears in the work and is reported as complete — specifically "Disconfirming evidence omitted or footnoted."
```

## Case 11 — Detects: FALSE COMPLETENESS

```text
GIVEN    A run of this skill in which the known failure mode is present: FALSE COMPLETENESS
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "FALSE COMPLETENESS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No unknowns section, so the reader assumes full coverage."
FAIL IF  "FALSE COMPLETENESS" appears in the work and is reported as complete — specifically "No unknowns section, so the reader assumes full coverage."
```

## Case 12 — Detects: METHOD OMISSION

```text
GIVEN    A run of this skill in which the known failure mode is present: METHOD OMISSION
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "METHOD OMISSION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Nobody can tell what was searched or what was excluded."
FAIL IF  "METHOD OMISSION" appears in the work and is reported as complete — specifically "Nobody can tell what was searched or what was excluded."
```

## Case 13 — Detects: STALENESS INVISIBLE

```text
GIVEN    A run of this skill in which the known failure mode is present: STALENESS INVISIBLE
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "STALENESS INVISIBLE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No re-verification trigger; the report is trusted past its life."
FAIL IF  "STALENESS INVISIBLE" appears in the work and is reported as complete — specifically "No re-verification trigger; the report is trusted past its life."
```

## Case 14 — Detects: RECENCY BIAS

```text
GIVEN    A run of this skill in which the known failure mode is present: RECENCY BIAS
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "RECENCY BIAS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The newest source wins regardless of quality or scope."
FAIL IF  "RECENCY BIAS" appears in the work and is reported as complete — specifically "The newest source wins regardless of quality or scope."
```

## Case 15 — Detects: PRESTIGE BIAS

```text
GIVEN    A run of this skill in which the known failure mode is present: PRESTIGE BIAS
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "PRESTIGE BIAS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The most famous source wins regardless of measurement method."
FAIL IF  "PRESTIGE BIAS" appears in the work and is reported as complete — specifically "The most famous source wins regardless of measurement method."
```

## Case 16 — Detects: VOLUME AS RIGOUR

```text
GIVEN    A run of this skill in which the known failure mode is present: VOLUME AS RIGOUR
WHEN     the agent executes `research-synthesis` and reaches the point where this failure occurs
THEN     "VOLUME AS RIGOUR" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Forty citations for a claim that needed two good ones."
FAIL IF  "VOLUME AS RIGOUR" appears in the work and is reported as complete — specifically "Forty citations for a claim that needed two good ones."
```

## Case 17 — Avoids: "Sources suggest that…" with no named source

```text
GIVEN    A situation that invites the anti-pattern "Sources suggest that…" with no named source"
WHEN     the agent applies `research-synthesis` in that situation
THEN     "Sources suggest that…" with no named source" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Sources suggest that…" with no named source" appears in the output; or it is absent by accident, with nothing in `research-synthesis` having ruled it out
```

## Case 18 — Avoids: A confidence level attached to the report rather than to individual claims

```text
GIVEN    A situation that invites the anti-pattern "A confidence level attached to the report rather than to individual claims"
WHEN     the agent applies `research-synthesis` in that situation
THEN     "A confidence level attached to the report rather than to individual claims" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A confidence level attached to the report rather than to individual claims" appears in the output; or it is absent by accident, with nothing in `research-synthesis` having ruled it out
```

## Case 19 — Avoids: Deleting the disagreeing source because it complicates the narrative

```text
GIVEN    A situation that invites the anti-pattern "Deleting the disagreeing source because it complicates the narrative"
WHEN     the agent applies `research-synthesis` in that situation
THEN     "Deleting the disagreeing source because it complicates the narrative" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Deleting the disagreeing source because it complicates the narrative" appears in the output; or it is absent by accident, with nothing in `research-synthesis` having ruled it out
```

## Case 20 — Avoids: Presenting an unscoped recommendation as universal

```text
GIVEN    A situation that invites the anti-pattern "Presenting an unscoped recommendation as universal"
WHEN     the agent applies `research-synthesis` in that situation
THEN     "Presenting an unscoped recommendation as universal" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Presenting an unscoped recommendation as universal" appears in the output; or it is absent by accident, with nothing in `research-synthesis` having ruled it out
```

## Case 21 — Avoids: Omitting the method because it "would be too long"

```text
GIVEN    A situation that invites the anti-pattern "Omitting the method because it "would be too long"
WHEN     the agent applies `research-synthesis` in that situation
THEN     "Omitting the method because it "would be too long" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Omitting the method because it "would be too long" appears in the output; or it is absent by accident, with nothing in `research-synthesis` having ruled it out
```

## Case 22 — Avoids: Writing the conclusion last and burying it in the final paragraph

```text
GIVEN    A situation that invites the anti-pattern "Writing the conclusion last and burying it in the final paragraph"
WHEN     the agent applies `research-synthesis` in that situation
THEN     "Writing the conclusion last and burying it in the final paragraph" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Writing the conclusion last and burying it in the final paragraph" appears in the output; or it is absent by accident, with nothing in `research-synthesis` having ruled it out
```

## Case 23 — Avoids: Citing forty sources for a claim that two would establish

```text
GIVEN    A situation that invites the anti-pattern "Citing forty sources for a claim that two would establish"
WHEN     the agent applies `research-synthesis` in that situation
THEN     "Citing forty sources for a claim that two would establish" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Citing forty sources for a claim that two would establish" appears in the output; or it is absent by accident, with nothing in `research-synthesis` having ruled it out
```

## Case 24 — Avoids: A synthesis with no unknowns section

```text
GIVEN    A situation that invites the anti-pattern "A synthesis with no unknowns section"
WHEN     the agent applies `research-synthesis` in that situation
THEN     "A synthesis with no unknowns section" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A synthesis with no unknowns section" appears in the output; or it is absent by accident, with nothing in `research-synthesis` having ruled it out
```
