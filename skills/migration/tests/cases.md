# Test cases — `migration`

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
GIVEN    A task inside this skill's stated purpose: Change a system that is running, has data, and has users — without a moment where it is broken. The core technique is the same for schema changes, framework upgrades, vendor switches, data moves and rewrites: **run both, prove parity,
WHEN     the agent executes `migration` end to end on that task
THEN     and before delivery these specific conditions hold: "From/to states versioned; invariants named; all consumers enumerated (including reports,"; "Read switch behind a flag with per-cohort rollout and an instant kill switch"; "Docs, runbooks and tests updated; retrospective filed"
FAIL IF  "From/to states versioned; invariants named; all consumers enumerated (including reports," is false, or "Docs, runbooks and tests updated; retrospective filed" is false, or "Read switch behind a flag with per-cohort rollout and an instant kill switch" is false
```

## Case 2 — Declines: A greenfield system with no data and no users — just change it

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A greenfield system with no data and no users — just change it
WHEN     the agent considers `migration` for that task
THEN     the skill is not selected, because this task is the excluded case "A greenfield system with no data and no users — just change it", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A greenfield system with no data and no users — just change it"; or `migration` is declined without naming that exclusion
```

## Case 3 — Declines: A reversible, low-blast-radius change behind a normal deploy

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A reversible, low-blast-radius change behind a normal deploy
WHEN     the agent considers `migration` for that task
THEN     the skill is not selected, because this task is the excluded case "A reversible, low-blast-radius change behind a normal deploy", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A reversible, low-blast-radius change behind a normal deploy"; or `migration` is declined without naming that exclusion
```

## Case 4 — Declines: When the honest answer is "delete it": removing a system is a different plan

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When the honest answer is "delete it": removing a system is a different plan
WHEN     the agent considers `migration` for that task
THEN     the skill is not selected, because this task is the excluded case "When the honest answer is "delete it": removing a system is a different plan", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When the honest answer is "delete it": removing a system is a different plan"; or `migration` is declined without naming that exclusion
```

## Case 5 — Detects: BIG-BANG CUTOVER

```text
GIVEN    A run of this skill in which the known failure mode is present: BIG-BANG CUTOVER
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "BIG-BANG CUTOVER" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "One unrehearsable moment holding all the risk."
FAIL IF  "BIG-BANG CUTOVER" appears in the work and is reported as complete — specifically "One unrehearsable moment holding all the risk."
```

## Case 6 — Detects: REHEARSAL ON TOY DATA

```text
GIVEN    A run of this skill in which the known failure mode is present: REHEARSAL ON TOY DATA
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "REHEARSAL ON TOY DATA" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Passes on 500 rows; fails on 50M (duration, locks, memory, edge cases)."
FAIL IF  "REHEARSAL ON TOY DATA" appears in the work and is reported as complete — specifically "Passes on 500 rows; fails on 50M (duration, locks, memory, edge cases)."
```

## Case 7 — Detects: PHASES IN ONE DEPLOY

```text
GIVEN    A run of this skill in which the known failure mode is present: PHASES IN ONE DEPLOY
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "PHASES IN ONE DEPLOY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No rollback boundary; a failure requires a full revert of everything."
FAIL IF  "PHASES IN ONE DEPLOY" appears in the work and is reported as complete — specifically "No rollback boundary; a failure requires a full revert of everything."
```

## Case 8 — Detects: NON-IDEMPOTENT BACKFILL

```text
GIVEN    A run of this skill in which the known failure mode is present: NON-IDEMPOTENT BACKFILL
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "NON-IDEMPOTENT BACKFILL" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A crash mid-run leaves a half-migrated, unrecoverable state."
FAIL IF  "NON-IDEMPOTENT BACKFILL" appears in the work and is reported as complete — specifically "A crash mid-run leaves a half-migrated, unrecoverable state."
```

## Case 9 — Detects: UNBOUNDED BACKFILL

```text
GIVEN    A run of this skill in which the known failure mode is present: UNBOUNDED BACKFILL
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "UNBOUNDED BACKFILL" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "One transaction over the whole table; locks and replication lag."
FAIL IF  "UNBOUNDED BACKFILL" appears in the work and is reported as complete — specifically "One transaction over the whole table; locks and replication lag."
```

## Case 10 — Detects: NO SHADOW READ

```text
GIVEN    A run of this skill in which the known failure mode is present: NO SHADOW READ
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "NO SHADOW READ" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Parity assumed instead of measured; differences discovered by users."
FAIL IF  "NO SHADOW READ" appears in the work and is reported as complete — specifically "Parity assumed instead of measured; differences discovered by users."
```

## Case 11 — Detects: PREMATURE CONTRACT

```text
GIVEN    A run of this skill in which the known failure mode is present: PREMATURE CONTRACT
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "PREMATURE CONTRACT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Dropping the old column in the same release that stopped writing it."
FAIL IF  "PREMATURE CONTRACT" appears in the work and is reported as complete — specifically "Dropping the old column in the same release that stopped writing it."
```

## Case 12 — Detects: FORGOTTEN CONSUMERS

```text
GIVEN    A run of this skill in which the known failure mode is present: FORGOTTEN CONSUMERS
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "FORGOTTEN CONSUMERS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A report, cron job, backup or another team's service still reads the old path."
FAIL IF  "FORGOTTEN CONSUMERS" appears in the work and is reported as complete — specifically "A report, cron job, backup or another team's service still reads the old path."
```

## Case 13 — Detects: MIXED-VERSION IGNORANCE

```text
GIVEN    A run of this skill in which the known failure mode is present: MIXED-VERSION IGNORANCE
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "MIXED-VERSION IGNORANCE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Old code meets the new schema during rollout and breaks."
FAIL IF  "MIXED-VERSION IGNORANCE" appears in the work and is reported as complete — specifically "Old code meets the new schema during rollout and breaks."
```

## Case 14 — Detects: FLAG WITH NO KILL SWITCH

```text
GIVEN    A run of this skill in which the known failure mode is present: FLAG WITH NO KILL SWITCH
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "FLAG WITH NO KILL SWITCH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The switch requires a deploy, not a flip."
FAIL IF  "FLAG WITH NO KILL SWITCH" appears in the work and is reported as complete — specifically "The switch requires a deploy, not a flip."
```

## Case 15 — Detects: NO RECONCILIATION

```text
GIVEN    A run of this skill in which the known failure mode is present: NO RECONCILIATION
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "NO RECONCILIATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "It exited successfully" as the parity proof. MIGRATE + CLEAN AT ONCE Two changes, one failure, no attribution."
FAIL IF  "NO RECONCILIATION" appears in the work and is reported as complete — specifically "It exited successfully" as the parity proof. MIGRATE + CLEAN AT ONCE Two changes, one failure, no attribution."
```

## Case 16 — Detects: SILENT ROW DROPS

```text
GIVEN    A run of this skill in which the known failure mode is present: SILENT ROW DROPS
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "SILENT ROW DROPS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Unmigratable rows skipped with no report."
FAIL IF  "SILENT ROW DROPS" appears in the work and is reported as complete — specifically "Unmigratable rows skipped with no report."
```

## Case 17 — Detects: UNDOCUMENTED POINT OF NO RETURN

```text
GIVEN    A run of this skill in which the known failure mode is present: UNDOCUMENTED POINT OF NO RETURN
WHEN     the agent executes `migration` and reaches the point where this failure occurs
THEN     "UNDOCUMENTED POINT OF NO RETURN" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The contract phase executed without sign-off."
FAIL IF  "UNDOCUMENTED POINT OF NO RETURN" appears in the work and is reported as complete — specifically "The contract phase executed without sign-off."
```

## Case 18 — Avoids: "We'll do it Saturday at 2 a.m

```text
GIVEN    A situation that invites the anti-pattern "We'll do it Saturday at 2 a.m", whose stated consequence is: with the team on a call"
WHEN     the agent applies `migration` in that situation
THEN     "We'll do it Saturday at 2 a.m" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "with the team on a call"
FAIL IF  "We'll do it Saturday at 2 a.m" appears in the output — that is, "with the team on a call"; or it is absent by accident, with nothing in `migration` having ruled it out
```

## Case 19 — Avoids: Dropping the old column in the same migration that stops writing it

```text
GIVEN    A situation that invites the anti-pattern "Dropping the old column in the same migration that stops writing it"
WHEN     the agent applies `migration` in that situation
THEN     "Dropping the old column in the same migration that stops writing it" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Dropping the old column in the same migration that stops writing it" appears in the output; or it is absent by accident, with nothing in `migration` having ruled it out
```

## Case 20 — Avoids: A backfill script run by hand, once, with no log and no resume

```text
GIVEN    A situation that invites the anti-pattern "A backfill script run by hand, once, with no log and no resume"
WHEN     the agent applies `migration` in that situation
THEN     "A backfill script run by hand, once, with no log and no resume" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A backfill script run by hand, once, with no log and no resume" appears in the output; or it is absent by accident, with nothing in `migration` having ruled it out
```

## Case 21 — Avoids: Rehearsing on the development database

```text
GIVEN    A situation that invites the anti-pattern "Rehearsing on the development database"
WHEN     the agent applies `migration` in that situation
THEN     "Rehearsing on the development database" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Rehearsing on the development database" appears in the output; or it is absent by accident, with nothing in `migration` having ruled it out
```

## Case 22 — Avoids: Declaring success because the job exited 0

```text
GIVEN    A situation that invites the anti-pattern "Declaring success because the job exited 0"
WHEN     the agent applies `migration` in that situation
THEN     "Declaring success because the job exited 0" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Declaring success because the job exited 0" appears in the output; or it is absent by accident, with nothing in `migration` having ruled it out
```

## Case 23 — Avoids: Migrating and renaming and re-typing in one step

```text
GIVEN    A situation that invites the anti-pattern "Migrating and renaming and re-typing in one step"
WHEN     the agent applies `migration` in that situation
THEN     "Migrating and renaming and re-typing in one step" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Migrating and renaming and re-typing in one step" appears in the output; or it is absent by accident, with nothing in `migration` having ruled it out
```

## Case 24 — Avoids: A feature flag that requires a redeploy to flip

```text
GIVEN    A situation that invites the anti-pattern "A feature flag that requires a redeploy to flip"
WHEN     the agent applies `migration` in that situation
THEN     "A feature flag that requires a redeploy to flip" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A feature flag that requires a redeploy to flip" appears in the output; or it is absent by accident, with nothing in `migration` having ruled it out
```

## Case 25 — Avoids: Forgetting the analytics warehouse that reads the table directly

```text
GIVEN    A situation that invites the anti-pattern "Forgetting the analytics warehouse that reads the table directly"
WHEN     the agent applies `migration` in that situation
THEN     "Forgetting the analytics warehouse that reads the table directly" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Forgetting the analytics warehouse that reads the table directly" appears in the output; or it is absent by accident, with nothing in `migration` having ruled it out
```

## Case 26 — Avoids: Silently skipping rows that failed validation

```text
GIVEN    A situation that invites the anti-pattern "Silently skipping rows that failed validation"
WHEN     the agent applies `migration` in that situation
THEN     "Silently skipping rows that failed validation" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Silently skipping rows that failed validation" appears in the output; or it is absent by accident, with nothing in `migration` having ruled it out
```
