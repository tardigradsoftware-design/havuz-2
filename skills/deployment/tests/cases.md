# Test cases — `deployment`

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
GIVEN    A task inside this skill's stated purpose: Make releasing **boring, frequent and reversible**. The goal is not a successful deploy; it is a deploy process where a failure is detected in minutes, contained automatically,
WHEN     the agent executes `deployment` end to end on that task
THEN     and before delivery these specific conditions hold: "Artifact built once, reproducibly, content-addressed, promoted unchanged through environments"; "Instant kill switch verified by rehearsal, not assumed"; "Every deploy recorded: what, when, who, strategy, metrics moved"
FAIL IF  "Artifact built once, reproducibly, content-addressed, promoted unchanged through environments" is false, or "Every deploy recorded: what, when, who, strategy, metrics moved" is false, or "Instant kill switch verified by rehearsal, not assumed" is false
```

## Case 2 — Declines: Local development iteration — optimise that loop separately (fast,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Local development iteration — optimise that loop separately (fast, hot-reloading, no gates)
WHEN     the agent considers `deployment` for that task
THEN     the skill is not selected, because this task is the excluded case "Local development iteration — optimise that loop separately (fast, hot-reloading, no gates)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Local development iteration — optimise that loop separately (fast, hot-reloading, no gates)"; or `deployment` is declined without naming that exclusion
```

## Case 3 — Declines: As a substitute for a migration plan when data changes are involved (see…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As a substitute for a migration plan when data changes are involved (see migration)
WHEN     the agent considers `deployment` for that task
THEN     the skill is not selected, because this task is the excluded case "As a substitute for a migration plan when data changes are involved (see migration)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As a substitute for a migration plan when data changes are involved (see migration)"; or `deployment` is declined without naming that exclusion
```

## Case 4 — Detects: REBUILD PER ENVIRONMENT

```text
GIVEN    A run of this skill in which the known failure mode is present: REBUILD PER ENVIRONMENT
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "REBUILD PER ENVIRONMENT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Staging tested a different artifact than production received. `latest` IN PRODUCTION Non-reproducible, non-rollbackable."
FAIL IF  "REBUILD PER ENVIRONMENT" appears in the work and is reported as complete — specifically "Staging tested a different artifact than production received. `latest` IN PRODUCTION Non-reproducible, non-rollbackable."
```

## Case 5 — Detects: CONFIG IN THE ARTIFACT

```text
GIVEN    A run of this skill in which the known failure mode is present: CONFIG IN THE ARTIFACT
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "CONFIG IN THE ARTIFACT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "One build per environment; secrets in images."
FAIL IF  "CONFIG IN THE ARTIFACT" appears in the work and is reported as complete — specifically "One build per environment; secrets in images."
```

## Case 6 — Detects: UNVALIDATED CONFIG

```text
GIVEN    A run of this skill in which the known failure mode is present: UNVALIDATED CONFIG
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "UNVALIDATED CONFIG" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The app boots, misbehaves, and the error surfaces as a business bug."
FAIL IF  "UNVALIDATED CONFIG" appears in the work and is reported as complete — specifically "The app boots, misbehaves, and the error surfaces as a business bug."
```

## Case 7 — Detects: SCHEMA WITH CODE

```text
GIVEN    A run of this skill in which the known failure mode is present: SCHEMA WITH CODE
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "SCHEMA WITH CODE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Old instances meet a new schema mid-rollout."
FAIL IF  "SCHEMA WITH CODE" appears in the work and is reported as complete — specifically "Old instances meet a new schema mid-rollout."
```

## Case 8 — Detects: NO MIXED-VERSION TESTING

```text
GIVEN    A run of this skill in which the known failure mode is present: NO MIXED-VERSION TESTING
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "NO MIXED-VERSION TESTING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Rolling update assumes compatibility it never verified."
FAIL IF  "NO MIXED-VERSION TESTING" appears in the work and is reported as complete — specifically "Rolling update assumes compatibility it never verified."
```

## Case 9 — Detects: UNWATCHED CANARY

```text
GIVEN    A run of this skill in which the known failure mode is present: UNWATCHED CANARY
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "UNWATCHED CANARY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A percentage rollout with no comparison is a slow rolling update."
FAIL IF  "UNWATCHED CANARY" appears in the work and is reported as complete — specifically "A percentage rollout with no comparison is a slow rolling update."
```

## Case 10 — Detects: HEALTH CHECK LYING

```text
GIVEN    A run of this skill in which the known failure mode is present: HEALTH CHECK LYING
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "HEALTH CHECK LYING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Readiness green while dependencies are broken; or liveness probing dependencies, turning an outage into a restart storm."
FAIL IF  "HEALTH CHECK LYING" appears in the work and is reported as complete — specifically "Readiness green while dependencies are broken; or liveness probing dependencies, turning an outage into a restart storm."
```

## Case 11 — Detects: NO DEPLOY MARKERS

```text
GIVEN    A run of this skill in which the known failure mode is present: NO DEPLOY MARKERS
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "NO DEPLOY MARKERS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A regression nobody can attribute to a release."
FAIL IF  "NO DEPLOY MARKERS" appears in the work and is reported as complete — specifically "A regression nobody can attribute to a release."
```

## Case 12 — Detects: MANUAL ROLLBACK

```text
GIVEN    A run of this skill in which the known failure mode is present: MANUAL ROLLBACK
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "MANUAL ROLLBACK" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Rollback requires a rebuild and 20 minutes."
FAIL IF  "MANUAL ROLLBACK" appears in the work and is reported as complete — specifically "Rollback requires a rebuild and 20 minutes."
```

## Case 13 — Detects: EFFECT BLINDNESS

```text
GIVEN    A run of this skill in which the known failure mode is present: EFFECT BLINDNESS
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "EFFECT BLINDNESS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Code rolled back; the duplicate payments were not."
FAIL IF  "EFFECT BLINDNESS" appears in the work and is reported as complete — specifically "Code rolled back; the duplicate payments were not."
```

## Case 14 — Detects: FLAG DEBT

```text
GIVEN    A run of this skill in which the known failure mode is present: FLAG DEBT
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "FLAG DEBT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Forty live flags, nobody knows which are still needed."
FAIL IF  "FLAG DEBT" appears in the work and is reported as complete — specifically "Forty live flags, nobody knows which are still needed."
```

## Case 15 — Detects: PIPELINE AS A SNOWFLAKE

```text
GIVEN    A run of this skill in which the known failure mode is present: PIPELINE AS A SNOWFLAKE
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "PIPELINE AS A SNOWFLAKE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "CI configuration changed without review, with production credentials."
FAIL IF  "PIPELINE AS A SNOWFLAKE" appears in the work and is reported as complete — specifically "CI configuration changed without review, with production credentials."
```

## Case 16 — Detects: WEEKEND HERO DEPLOYS

```text
GIVEN    A run of this skill in which the known failure mode is present: WEEKEND HERO DEPLOYS
WHEN     the agent executes `deployment` and reaches the point where this failure occurs
THEN     "WEEKEND HERO DEPLOYS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The process is a person, not a pipeline."
FAIL IF  "WEEKEND HERO DEPLOYS" appears in the work and is reported as complete — specifically "The process is a person, not a pipeline."
```

## Case 17 — Avoids: `docker pull app:latest` on a production host

```text
GIVEN    A situation that invites the anti-pattern "`docker pull app:latest` on a production host"
WHEN     the agent applies `deployment` in that situation
THEN     "`docker pull app:latest` on a production host" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`docker pull app:latest` on a production host" appears in the output; or it is absent by accident, with nothing in `deployment` having ruled it out
```

## Case 18 — Avoids: A `.env` file baked into the image

```text
GIVEN    A situation that invites the anti-pattern "A `.env` file baked into the image"
WHEN     the agent applies `deployment` in that situation
THEN     "A `.env` file baked into the image" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A `.env` file baked into the image" appears in the output; or it is absent by accident, with nothing in `deployment` having ruled it out
```

## Case 19 — Avoids: Deploying the schema migration in the same release as the code that uses it

```text
GIVEN    A situation that invites the anti-pattern "Deploying the schema migration in the same release as the code that uses it"
WHEN     the agent applies `deployment` in that situation
THEN     "Deploying the schema migration in the same release as the code that uses it" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Deploying the schema migration in the same release as the code that uses it" appears in the output; or it is absent by accident, with nothing in `deployment` having ruled it out
```

## Case 20 — Avoids: A canary at 5% that nobody monitors

```text
GIVEN    A situation that invites the anti-pattern "A canary at 5% that nobody monitors"
WHEN     the agent applies `deployment` in that situation
THEN     "A canary at 5% that nobody monitors" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A canary at 5% that nobody monitors" appears in the output; or it is absent by accident, with nothing in `deployment` having ruled it out
```

## Case 21 — Avoids: A liveness probe that queries the database

```text
GIVEN    A situation that invites the anti-pattern "A liveness probe that queries the database"
WHEN     the agent applies `deployment` in that situation
THEN     "A liveness probe that queries the database" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A liveness probe that queries the database" appears in the output; or it is absent by accident, with nothing in `deployment` having ruled it out
```

## Case 22 — Avoids: "Roll back" meaning "rebuild the previous commit"

```text
GIVEN    A situation that invites the anti-pattern "Roll back" meaning "rebuild the previous commit"
WHEN     the agent applies `deployment` in that situation
THEN     "Roll back" meaning "rebuild the previous commit" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Roll back" meaning "rebuild the previous commit" appears in the output; or it is absent by accident, with nothing in `deployment` having ruled it out
```

## Case 23 — Avoids: Friday evening deploys by one person who knows the steps

```text
GIVEN    A situation that invites the anti-pattern "Friday evening deploys by one person who knows the steps"
WHEN     the agent applies `deployment` in that situation
THEN     "Friday evening deploys by one person who knows the steps" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Friday evening deploys by one person who knows the steps" appears in the output; or it is absent by accident, with nothing in `deployment` having ruled it out
```

## Case 24 — Avoids: A CI workflow with a long-lived production key in a repository secret

```text
GIVEN    A situation that invites the anti-pattern "A CI workflow with a long-lived production key in a repository secret"
WHEN     the agent applies `deployment` in that situation
THEN     "A CI workflow with a long-lived production key in a repository secret" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A CI workflow with a long-lived production key in a repository secret" appears in the output; or it is absent by accident, with nothing in `deployment` having ruled it out
```

## Case 25 — Avoids: Leaving the compatibility shim in place "just in case", forever

```text
GIVEN    A situation that invites the anti-pattern "Leaving the compatibility shim in place "just in case", forever"
WHEN     the agent applies `deployment` in that situation
THEN     "Leaving the compatibility shim in place "just in case", forever" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Leaving the compatibility shim in place "just in case", forever" appears in the output; or it is absent by accident, with nothing in `deployment` having ruled it out
```
