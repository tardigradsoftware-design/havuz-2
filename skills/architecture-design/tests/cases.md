# Test cases — `architecture-design`

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
GIVEN    A task inside this skill's stated purpose: Produce an architecture whose decisions were made explicitly, are written down, and can be argued with — rather than one assembled from defaults and framework conventions. The deliverable is not a diagram;
WHEN     the agent executes `architecture-design` end to end on that task
THEN     the workflow runs in its stated order — "STATE THE REQUIREMENTS AS NUMBERS" through to "STATE THE NON-GOALS AND THE DEFERRALS"; and before delivery these specific conditions hold: "every requirement is a number with a percentile or a rate, marked hard or aspirational"; "the irreversible decisions have ADRs with alternatives and reasoning"; "the design can be read by someone who was not in the room"
FAIL IF  "every requirement is a number with a percentile or a rate, marked hard or aspirational" is false, or "the design can be read by someone who was not in the room" is false, or the result is delivered before "STATE THE NON-GOALS AND THE DEFERRALS" has run
```

## Case 2 — Declines: The change is local and reversible — a function, a component,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The change is local and reversible — a function, a component, an internal module boundary.
WHEN     the agent considers `architecture-design` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Refactoring skill applies; architecture does not."
FAIL IF  the skill is run on a task where "The change is local and reversible — a function, a component, an internal module boundary.", and the consequence that exclusion states follows — "Refactoring skill applies; architecture does not."; or `architecture-design` is declined without naming that exclusion
```

## Case 3 — Declines: The real question is build vs adopt for one capability.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The real question is build vs adopt for one capability.
WHEN     the agent considers `architecture-design` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Use dont-reinvent-the-wheel and competitive-analysis, then return here only if the answer is "build"."
FAIL IF  the skill is run on a task where "The real question is build vs adopt for one capability.", and the consequence that exclusion states follows — "Use dont-reinvent-the-wheel and competitive-analysis, then return here only if the answer is "build"."; or `architecture-design` is declined without naming that exclusion
```

## Case 4 — Declines: Performance is the question and nothing has been measured.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Performance is the question and nothing has been measured.
WHEN     the agent considers `architecture-design` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Profile first; architecture decisions made against an unmeasured bottleneck are guesses with a diagram attached."
FAIL IF  the skill is run on a task where "Performance is the question and nothing has been measured.", and the consequence that exclusion states follows — "Profile first; architecture decisions made against an unmeasured bottleneck are guesses with a diagram attached."; or `architecture-design` is declined without naming that exclusion
```

## Case 5 — Declines: The system does not yet have a stated requirement.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The system does not yet have a stated requirement.
WHEN     the agent considers `architecture-design` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Architecture without numbers is decoration."
FAIL IF  the skill is run on a task where "The system does not yet have a stated requirement.", and the consequence that exclusion states follows — "Architecture without numbers is decoration."; or `architecture-design` is declined without naming that exclusion
```

## Case 6 — Detects: Requirements were adjectives

```text
GIVEN    A run of this skill in which the known failure mode is present: Requirements were adjectives
WHEN     the agent executes `architecture-design` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no percentile, rate or target appears in the document" — and the response applied is the documented one: "stop and obtain numbers; do not design against "fast"
FAIL IF  "Requirements were adjectives" reaches the output because "no percentile, rate or target appears in the document" was never checked; or it is caught but the response taken is not "stop and obtain numbers; do not design against "fast"
```

## Case 7 — Detects: Boundaries follow the org chart, not the data

```text
GIVEN    A run of this skill in which the known failure mode is present: Boundaries follow the org chart, not the data
WHEN     the agent executes `architecture-design` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "one entity written by three services" — and the response applied is the documented one: "re-cut along data ownership; accept the reorganisation cost"
FAIL IF  "Boundaries follow the org chart, not the data" reaches the output because "one entity written by three services" was never checked; or it is caught but the response taken is not "re-cut along data ownership; accept the reorganisation cost"
```

## Case 8 — Detects: Consistency assumed uniform

```text
GIVEN    A run of this skill in which the known failure mode is present: Consistency assumed uniform
WHEN     the agent executes `architecture-design` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the system is strongly consistent" applied to analytics too" — and the response applied is the documented one: "assign per data type; state staleness budgets"
FAIL IF  "Consistency assumed uniform" reaches the output because "the system is strongly consistent" applied to analytics too" was never checked; or it is caught but the response taken is not "assign per data type; state staleness budgets"
```

## Case 9 — Detects: Retries without a budget

```text
GIVEN    A run of this skill in which the known failure mode is present: Retries without a budget
WHEN     the agent executes `architecture-design` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "retry count unbounded, no breaker" — and the response applied is the documented one: "add exponential backoff with jitter, a budget, a breaker"
FAIL IF  "Retries without a budget" reaches the output because "retry count unbounded, no breaker" was never checked; or it is caught but the response taken is not "add exponential backoff with jitter, a budget, a breaker"
```

## Case 10 — Detects: Irreversible decisions taken casually

```text
GIVEN    A run of this skill in which the known failure mode is present: Irreversible decisions taken casually
WHEN     the agent executes `architecture-design` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no ADR, no alternatives recorded" — and the response applied is the documented one: "write the ADR now, before the exit cost is paid"
FAIL IF  "Irreversible decisions taken casually" reaches the output because "no ADR, no alternatives recorded" was never checked; or it is caught but the response taken is not "write the ADR now, before the exit cost is paid"
```

## Case 11 — Detects: Observability deferred

```text
GIVEN    A run of this skill in which the known failure mode is present: Observability deferred
WHEN     the agent executes `architecture-design` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "we will add tracing later" — and the response applied is the documented one: "tracing added later does not cover the boundaries that were already built"
FAIL IF  "Observability deferred" reaches the output because "we will add tracing later" was never checked; or it is caught but the response taken is not "tracing added later does not cover the boundaries that were already built"
```

## Case 12 — Detects: Architecture by framework default

```text
GIVEN    A run of this skill in which the known failure mode is present: Architecture by framework default
WHEN     the agent executes `architecture-design` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the design is a description of the framework's conventions" — and the response applied is the documented one: "state what the framework decided for you and whether it was reviewed"
FAIL IF  "Architecture by framework default" reaches the output because "the design is a description of the framework's conventions" was never checked; or it is caught but the response taken is not "state what the framework decided for you and whether it was reviewed"
```

## Case 13 — Avoids: DIAGRAM-FIRST DESIGN

```text
GIVEN    A situation that invites the anti-pattern "DIAGRAM-FIRST DESIGN", whose stated consequence is: Boxes and arrows without the decisions behind them. The diagram is the output of the reasoning, not a substitute for it.
WHEN     the agent applies `architecture-design` in that situation
THEN     "DIAGRAM-FIRST DESIGN" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Boxes and arrows without the decisions behind them. The diagram is the output of the reasoning, not a substitute for it."
FAIL IF  "DIAGRAM-FIRST DESIGN" appears in the output — that is, "Boxes and arrows without the decisions behind them. The diagram is the output of the reasoning, not a substitute for it."; or it is absent by accident, with nothing in `architecture-design` having ruled it out
```

## Case 14 — Avoids: RESUME-DRIVEN ARCHITECTURE

```text
GIVEN    A situation that invites the anti-pattern "RESUME-DRIVEN ARCHITECTURE", whose stated consequence is: Adopting a technology because it is interesting rather than because a stated requirement demands it.
WHEN     the agent applies `architecture-design` in that situation
THEN     "RESUME-DRIVEN ARCHITECTURE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Adopting a technology because it is interesting rather than because a stated requirement demands it."
FAIL IF  "RESUME-DRIVEN ARCHITECTURE" appears in the output — that is, "Adopting a technology because it is interesting rather than because a stated requirement demands it."; or it is absent by accident, with nothing in `architecture-design` having ruled it out
```

## Case 15 — Avoids: DISTRIBUTED MONOLITH

```text
GIVEN    A situation that invites the anti-pattern "DISTRIBUTED MONOLITH", whose stated consequence is: Services split so finely that every change touches several and every request crosses five boundaries, with none of the independence that justified the split.
WHEN     the agent applies `architecture-design` in that situation
THEN     "DISTRIBUTED MONOLITH" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Services split so finely that every change touches several and every request crosses five boundaries, with none of the independence that justified the split."
FAIL IF  "DISTRIBUTED MONOLITH" appears in the output — that is, "Services split so finely that every change touches several and every request crosses five boundaries, with none of the independence that justified the split."; or it is absent by accident, with nothing in `architecture-design` having ruled it out
```

## Case 16 — Avoids: PREMATURE ABSTRACTION

```text
GIVEN    A situation that invites the anti-pattern "PREMATURE ABSTRACTION", whose stated consequence is: A plugin system, an extension mechanism or a generic engine built before a second concrete case exists. Two examples is the minimum for finding the real seam.
WHEN     the agent applies `architecture-design` in that situation
THEN     "PREMATURE ABSTRACTION" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A plugin system, an extension mechanism or a generic engine built before a second concrete case exists. Two examples is the minimum for finding the real seam."
FAIL IF  "PREMATURE ABSTRACTION" appears in the output — that is, "A plugin system, an extension mechanism or a generic engine built before a second concrete case exists. Two examples is the minimum for finding the real seam."; or it is absent by accident, with nothing in `architecture-design` having ruled it out
```

## Case 17 — Avoids: SHARED DATABASE AS AN INTEGRATION MECHANISM

```text
GIVEN    A situation that invites the anti-pattern "SHARED DATABASE AS AN INTEGRATION MECHANISM", whose stated consequence is: Two services writing one table couples them more tightly than an API would, invisibly, and with no versioning.
WHEN     the agent applies `architecture-design` in that situation
THEN     "SHARED DATABASE AS AN INTEGRATION MECHANISM" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Two services writing one table couples them more tightly than an API would, invisibly, and with no versioning."
FAIL IF  "SHARED DATABASE AS AN INTEGRATION MECHANISM" appears in the output — that is, "Two services writing one table couples them more tightly than an API would, invisibly, and with no versioning."; or it is absent by accident, with nothing in `architecture-design` having ruled it out
```

## Case 18 — Avoids: "WE'LL SCALE LATER." Deferring is legitimate;

```text
GIVEN    A situation that invites the anti-pattern "WE'LL SCALE LATER." Deferring is legitimate; deferring without naming the axis and the…"
WHEN     the agent applies `architecture-design` in that situation
THEN     "WE'LL SCALE LATER." Deferring is legitimate; deferring without naming the axis and the…" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "WE'LL SCALE LATER." Deferring is legitimate; deferring without naming the axis and the…" appears in the output; or it is absent by accident, with nothing in `architecture-design` having ruled it out
```

## Case 19 — Avoids: DESIGNING FOR THE DEMO PATH

```text
GIVEN    A situation that invites the anti-pattern "DESIGNING FOR THE DEMO PATH", whose stated consequence is: The architecture that works for one tenant with 100 rows and fails for the tenant with 10 million.
WHEN     the agent applies `architecture-design` in that situation
THEN     "DESIGNING FOR THE DEMO PATH" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The architecture that works for one tenant with 100 rows and fails for the tenant with 10 million."
FAIL IF  "DESIGNING FOR THE DEMO PATH" appears in the output — that is, "The architecture that works for one tenant with 100 rows and fails for the tenant with 10 million."; or it is absent by accident, with nothing in `architecture-design` having ruled it out
```

## Case 20 — Avoids: NO RECORD

```text
GIVEN    A situation that invites the anti-pattern "NO RECORD", whose stated consequence is: A decision made in a meeting and never written is re-litigated by the next engineer, without the reasoning that rejected the plausible alternative.
WHEN     the agent applies `architecture-design` in that situation
THEN     "NO RECORD" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A decision made in a meeting and never written is re-litigated by the next engineer, without the reasoning that rejected the plausible alternative."
FAIL IF  "NO RECORD" appears in the output — that is, "A decision made in a meeting and never written is re-litigated by the next engineer, without the reasoning that rejected the plausible alternative."; or it is absent by accident, with nothing in `architecture-design` having ruled it out
```
