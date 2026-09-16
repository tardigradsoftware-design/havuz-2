# Test cases — `frontend-implementation`

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
GIVEN    A task inside this skill's stated purpose: Turn an approved design into code that stays correct under real content, real networks and real devices. This skill assumes the design exists — if it does not, run [`frontend-design`](../frontend-design/SKILL.md) first.
WHEN     the agent executes `frontend-implementation` end to end on that task
THEN     and before delivery these specific conditions hold: "Rendering strategy chosen per route, recorded with the reason"; "No request waterfalls; dependent fetches hoisted or parallelised"; "Third-party scripts allowlisted with a measured cost"
FAIL IF  "Rendering strategy chosen per route, recorded with the reason" is false, or "Third-party scripts allowlisted with a measured cost" is false, or "No request waterfalls; dependent fetches hoisted or parallelised" is false
```

## Case 2 — Declines: Producing the visual design itself — frontend-design

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Producing the visual design itself — frontend-design
WHEN     the agent considers `frontend-implementation` for that task
THEN     the skill is not selected, because this task is the excluded case "Producing the visual design itself — frontend-design", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Producing the visual design itself — frontend-design"; or `frontend-implementation` is declined without naming that exclusion
```

## Case 3 — Declines: Defining the token/component system — design-systems

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Defining the token/component system — design-systems
WHEN     the agent considers `frontend-implementation` for that task
THEN     the skill is not selected, because this task is the excluded case "Defining the token/component system — design-systems", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Defining the token/component system — design-systems"; or `frontend-implementation` is declined without naming that exclusion
```

## Case 4 — Declines: Backend concerns except at the contract boundary — see api-design /…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Backend concerns except at the contract boundary — see api-design / backend-engineering
WHEN     the agent considers `frontend-implementation` for that task
THEN     the skill is not selected, because this task is the excluded case "Backend concerns except at the contract boundary — see api-design / backend-engineering", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Backend concerns except at the contract boundary — see api-design / backend-engineering"; or `frontend-implementation` is declined without naming that exclusion
```

## Case 5 — Detects: DESIGN DRIFT

```text
GIVEN    A run of this skill in which the known failure mode is present: DESIGN DRIFT
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "DESIGN DRIFT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Implemented pixels diverge from tokens; hard-coded values creep in. Fix: lint against raw values; visual regression tests."
FAIL IF  "DESIGN DRIFT" appears in the work and is reported as complete — specifically "Implemented pixels diverge from tokens; hard-coded values creep in. Fix: lint against raw values; visual regression tests."
```

## Case 6 — Detects: STATE MISPLACEMENT

```text
GIVEN    A run of this skill in which the known failure mode is present: STATE MISPLACEMENT
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "STATE MISPLACEMENT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Server state duplicated in a global store; URL state in useState. Fix: the four-kinds rule, applied at review."
FAIL IF  "STATE MISPLACEMENT" appears in the work and is reported as complete — specifically "Server state duplicated in a global store; URL state in useState. Fix: the four-kinds rule, applied at review."
```

## Case 7 — Detects: USE-EFFECT FETCHING

```text
GIVEN    A run of this skill in which the known failure mode is present: USE-EFFECT FETCHING
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "USE-EFFECT FETCHING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No cache, no dedupe, race conditions, waterfalls."
FAIL IF  "USE-EFFECT FETCHING" appears in the work and is reported as complete — specifically "No cache, no dedupe, race conditions, waterfalls."
```

## Case 8 — Detects: MANUAL TYPES

```text
GIVEN    A run of this skill in which the known failure mode is present: MANUAL TYPES
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "MANUAL TYPES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Hand-copied API types that silently diverge from the contract."
FAIL IF  "MANUAL TYPES" appears in the work and is reported as complete — specifically "Hand-copied API types that silently diverge from the contract."
```

## Case 9 — Detects: HAPPY-PATH ONLY

```text
GIVEN    A run of this skill in which the known failure mode is present: HAPPY-PATH ONLY
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "HAPPY-PATH ONLY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No empty, error or partial states — the app breaks on the first 500."
FAIL IF  "HAPPY-PATH ONLY" appears in the work and is reported as complete — specifically "No empty, error or partial states — the app breaks on the first 500."
```

## Case 10 — Detects: HYDRATION MISMATCH

```text
GIVEN    A run of this skill in which the known failure mode is present: HYDRATION MISMATCH
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "HYDRATION MISMATCH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Server and client render differently (Date.now, locale, random, storage)."
FAIL IF  "HYDRATION MISMATCH" appears in the work and is reported as complete — specifically "Server and client render differently (Date.now, locale, random, storage)."
```

## Case 11 — Detects: WATERFALL FETCHING

```text
GIVEN    A run of this skill in which the known failure mode is present: WATERFALL FETCHING
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "WATERFALL FETCHING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Sequential dependent requests that could be parallel or hoisted. IMAGE DIMENSION GUESS Missing width/height → CLS on every page."
FAIL IF  "WATERFALL FETCHING" appears in the work and is reported as complete — specifically "Sequential dependent requests that could be parallel or hoisted. IMAGE DIMENSION GUESS Missing width/height → CLS on every page."
```

## Case 12 — Detects: FONT SWAP SHIFT

```text
GIVEN    A run of this skill in which the known failure mode is present: FONT SWAP SHIFT
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "FONT SWAP SHIFT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Unreserved space for webfonts."
FAIL IF  "FONT SWAP SHIFT" appears in the work and is reported as complete — specifically "Unreserved space for webfonts."
```

## Case 13 — Detects: THIRD-PARTY CREEP

```text
GIVEN    A run of this skill in which the known failure mode is present: THIRD-PARTY CREEP
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "THIRD-PARTY CREEP" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "An analytics script costing more than the app."
FAIL IF  "THIRD-PARTY CREEP" appears in the work and is reported as complete — specifically "An analytics script costing more than the app."
```

## Case 14 — Detects: PRIMITIVE REBUILD

```text
GIVEN    A run of this skill in which the known failure mode is present: PRIMITIVE REBUILD
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "PRIMITIVE REBUILD" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A custom modal with broken focus trapping and no escape key."
FAIL IF  "PRIMITIVE REBUILD" appears in the work and is reported as complete — specifically "A custom modal with broken focus trapping and no escape key."
```

## Case 15 — Detects: OVER-ABSTRACTION

```text
GIVEN    A run of this skill in which the known failure mode is present: OVER-ABSTRACTION
WHEN     the agent executes `frontend-implementation` and reaches the point where this failure occurs
THEN     "OVER-ABSTRACTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A <GenericRenderer config={...}/> instead of readable components."
FAIL IF  "OVER-ABSTRACTION" appears in the work and is reported as complete — specifically "A <GenericRenderer config={...}/> instead of readable components."
```

## Case 16 — Avoids: `useEffect(() => { fetch(...) }, [])` with no cache, abort or error handling

```text
GIVEN    A situation that invites the anti-pattern "`useEffect(() => { fetch(...) }, [])` with no cache, abort or error handling"
WHEN     the agent applies `frontend-implementation` in that situation
THEN     "`useEffect(() => { fetch(...) }, [])` with no cache, abort or error handling" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`useEffect(() => { fetch(...) }, [])` with no cache, abort or error handling" appears in the output; or it is absent by accident, with nothing in `frontend-implementation` having ruled it out
```

## Case 17 — Avoids: A modal built from a `<div>` with `onClick` on the backdrop

```text
GIVEN    A situation that invites the anti-pattern "A modal built from a `<div>` with `onClick` on the backdrop"
WHEN     the agent applies `frontend-implementation` in that situation
THEN     "A modal built from a `<div>` with `onClick` on the backdrop" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A modal built from a `<div>` with `onClick` on the backdrop" appears in the output; or it is absent by accident, with nothing in `frontend-implementation` having ruled it out
```

## Case 18 — Avoids: Filter state that vanishes on refresh

```text
GIVEN    A situation that invites the anti-pattern "Filter state that vanishes on refresh"
WHEN     the agent applies `frontend-implementation` in that situation
THEN     "Filter state that vanishes on refresh" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Filter state that vanishes on refresh" appears in the output; or it is absent by accident, with nothing in `frontend-implementation` having ruled it out
```

## Case 19 — Avoids: Hand-writing `interface Order` next to a generated OpenAPI client

```text
GIVEN    A situation that invites the anti-pattern "Hand-writing `interface Order` next to a generated OpenAPI client"
WHEN     the agent applies `frontend-implementation` in that situation
THEN     "Hand-writing `interface Order` next to a generated OpenAPI client" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Hand-writing `interface Order` next to a generated OpenAPI client" appears in the output; or it is absent by accident, with nothing in `frontend-implementation` having ruled it out
```

## Case 20 — Avoids: `style={{ marginTop: 17 }}`

```text
GIVEN    A situation that invites the anti-pattern "`style={{ marginTop: 17 }}`"
WHEN     the agent applies `frontend-implementation` in that situation
THEN     "`style={{ marginTop: 17 }}`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`style={{ marginTop: 17 }}`" appears in the output; or it is absent by accident, with nothing in `frontend-implementation` having ruled it out
```

## Case 21 — Avoids: Rendering a 10,000-row table without virtualisation

```text
GIVEN    A situation that invites the anti-pattern "Rendering a 10,000-row table without virtualisation"
WHEN     the agent applies `frontend-implementation` in that situation
THEN     "Rendering a 10,000-row table without virtualisation" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Rendering a 10,000-row table without virtualisation" appears in the output; or it is absent by accident, with nothing in `frontend-implementation` having ruled it out
```

## Case 22 — Avoids: `any` at the API boundary

```text
GIVEN    A situation that invites the anti-pattern "`any` at the API boundary"
WHEN     the agent applies `frontend-implementation` in that situation
THEN     "`any` at the API boundary" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`any` at the API boundary" appears in the output; or it is absent by accident, with nothing in `frontend-implementation` having ruled it out
```

## Case 23 — Avoids: An `<img>` with no width or height

```text
GIVEN    A situation that invites the anti-pattern "An `<img>` with no width or height"
WHEN     the agent applies `frontend-implementation` in that situation
THEN     "An `<img>` with no width or height" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "An `<img>` with no width or height" appears in the output; or it is absent by accident, with nothing in `frontend-implementation` having ruled it out
```

## Case 24 — Avoids: A global store holding one component's hover state

```text
GIVEN    A situation that invites the anti-pattern "A global store holding one component's hover state"
WHEN     the agent applies `frontend-implementation` in that situation
THEN     "A global store holding one component's hover state" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A global store holding one component's hover state" appears in the output; or it is absent by accident, with nothing in `frontend-implementation` having ruled it out
```
