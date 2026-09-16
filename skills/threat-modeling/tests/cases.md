# Test cases — `threat-modeling`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Answer in writing, before building: what can go wrong, who would want it to, what it would cost, and what is being done about it. Skipping this does not remove the threats; it removes the record of which ones were accept…
WHEN     the agent selects and executes the `threat-modeling` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: The data flows are unknown

```text
GIVEN    A task that looks like a match but is the excluded case: A threat model against a vague description produces vague threats. Draw
WHEN     the agent considers the `threat-modeling` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The goal is compliance evidence rather than risk reduction

```text
GIVEN    A task that looks like a match but is the excluded case: Produce the artifact the standard asks
WHEN     the agent considers the `threat-modeling` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: A penetration test or an audit is what is needed

```text
GIVEN    A task that looks like a match but is the excluded case: Those verify controls against a live system; this
WHEN     the agent considers the `threat-modeling` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Modeled services instead of flows

```text
GIVEN    A run in which the known failure mode is present — Modeled services instead of flows
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is detected by "no boundary crossings in the diagram" and the documented response is applied: redraw around data movement; boxes hide the crossings
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: Mitigations before enumeration

```text
GIVEN    A run in which the known failure mode is present — Mitigations before enumeration
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is detected by ""we use TLS" appears with no threat attached" and the documented response is applied: return to step 2; the control answers a question nobody asked
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Threats without mechanisms

```text
GIVEN    A run in which the known failure mode is present — Threats without mechanisms
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is detected by "register entries are one word ("injection")" and the documented response is applied: expand each to actor, path, action and impact
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: STARTING WITH CONTROLS

```text
GIVEN    A situation that invites the anti-pattern: A list of technologies in use is not a threat model.
WHEN     the agent applies `threat-modeling`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: MODELING THE ORG CHART

```text
GIVEN    A situation that invites the anti-pattern: Service boxes without data flows hide every crossing.
WHEN     the agent applies `threat-modeling`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
