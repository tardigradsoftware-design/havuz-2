# Test cases — `repository-analysis`

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
GIVEN    A task inside this skill's stated purpose: Answer two questions with evidence: **how does this codebase actually work**, and **is it safe and sensible to depend on it**. The README describes intent.
WHEN     the agent executes `repository-analysis` end to end on that task
THEN     and before delivery these specific conditions hold: "Canonical identity confirmed; final slug and ref recorded"; "Security posture checked: SECURITY.md, advisories, defaults, scorecard"; "Every claim cited or marked GENERATED"
FAIL IF  "Canonical identity confirmed; final slug and ref recorded" is false, or "Every claim cited or marked GENERATED" is false, or "Security posture checked: SECURITY.md, advisories, defaults, scorecard" is false
```

## Case 2 — Declines: A repository you already know well and that has not changed — reuse the…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A repository you already know well and that has not changed — reuse the cached assessment
WHEN     the agent considers `repository-analysis` for that task
THEN     the skill is not selected, because this task is the excluded case "A repository you already know well and that has not changed — reuse the cached assessment", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A repository you already know well and that has not changed — reuse the cached assessment"; or `repository-analysis` is declined without naming that exclusion
```

## Case 3 — Declines: Judging a project solely to satisfy a style preference

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Judging a project solely to satisfy a style preference
WHEN     the agent considers `repository-analysis` for that task
THEN     the skill is not selected, because this task is the excluded case "Judging a project solely to satisfy a style preference", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Judging a project solely to satisfy a style preference"; or `repository-analysis` is declined without naming that exclusion
```

## Case 4 — Declines: As a substitute for security-audit when security is the actual question

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As a substitute for security-audit when security is the actual question
WHEN     the agent considers `repository-analysis` for that task
THEN     the skill is not selected, because this task is the excluded case "As a substitute for security-audit when security is the actual question", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As a substitute for security-audit when security is the actual question"; or `repository-analysis` is declined without naming that exclusion
```

## Case 5 — Detects: README TRUST

```text
GIVEN    A run of this skill in which the known failure mode is present: README TRUST
WHEN     the agent executes `repository-analysis` and reaches the point where this failure occurs
THEN     "README TRUST" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Believing the feature list without running the quickstart."
FAIL IF  "README TRUST" appears in the work and is reported as complete — specifically "Believing the feature list without running the quickstart."
```

## Case 6 — Detects: STAR RANKING

```text
GIVEN    A run of this skill in which the known failure mode is present: STAR RANKING
WHEN     the agent executes `repository-analysis` and reaches the point where this failure occurs
THEN     "STAR RANKING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Equating popularity with fitness."
FAIL IF  "STAR RANKING" appears in the work and is reported as complete — specifically "Equating popularity with fitness."
```

## Case 7 — Detects: FORK CONFUSION

```text
GIVEN    A run of this skill in which the known failure mode is present: FORK CONFUSION
WHEN     the agent executes `repository-analysis` and reaches the point where this failure occurs
THEN     "FORK CONFUSION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Analysing a fork and reporting the upstream's reputation."
FAIL IF  "FORK CONFUSION" appears in the work and is reported as complete — specifically "Analysing a fork and reporting the upstream's reputation."
```

## Case 8 — Detects: STALE SNAPSHOT

```text
GIVEN    A run of this skill in which the known failure mode is present: STALE SNAPSHOT
WHEN     the agent executes `repository-analysis` and reaches the point where this failure occurs
THEN     "STALE SNAPSHOT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Assessing `main` while your lockfile pins a two-year-old tag."
FAIL IF  "STALE SNAPSHOT" appears in the work and is reported as complete — specifically "Assessing `main` while your lockfile pins a two-year-old tag."
```

## Case 9 — Detects: LICENSE ASSUMPTION

```text
GIVEN    A run of this skill in which the known failure mode is present: LICENSE ASSUMPTION
WHEN     the agent executes `repository-analysis` and reaches the point where this failure occurs
THEN     "LICENSE ASSUMPTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Reading the badge instead of the file; missing `license: null`."
FAIL IF  "LICENSE ASSUMPTION" appears in the work and is reported as complete — specifically "Reading the badge instead of the file; missing `license: null`."
```

## Case 10 — Detects: HEALTH THEATRE

```text
GIVEN    A run of this skill in which the known failure mode is present: HEALTH THEATRE
WHEN     the agent executes `repository-analysis` and reaches the point where this failure occurs
THEN     "HEALTH THEATRE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Counting commits without checking whether CI passes or issues get answers."
FAIL IF  "HEALTH THEATRE" appears in the work and is reported as complete — specifically "Counting commits without checking whether CI passes or issues get answers."
```

## Case 11 — Detects: NO EXIT PLAN

```text
GIVEN    A run of this skill in which the known failure mode is present: NO EXIT PLAN
WHEN     the agent executes `repository-analysis` and reaches the point where this failure occurs
THEN     "NO EXIT PLAN" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Adopting without knowing the removal cost."
FAIL IF  "NO EXIT PLAN" appears in the work and is reported as complete — specifically "Adopting without knowing the removal cost."
```

## Case 12 — Detects: SURFACE MAP

```text
GIVEN    A run of this skill in which the known failure mode is present: SURFACE MAP
WHEN     the agent executes `repository-analysis` and reaches the point where this failure occurs
THEN     "SURFACE MAP" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Describing the directory tree instead of the control flow."
FAIL IF  "SURFACE MAP" appears in the work and is reported as complete — specifically "Describing the directory tree instead of the control flow."
```

## Case 13 — Avoids: "40k stars, must be good"

```text
GIVEN    A situation that invites the anti-pattern "40k stars, must be good"
WHEN     the agent applies `repository-analysis` in that situation
THEN     "40k stars, must be good" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "40k stars, must be good" appears in the output; or it is absent by accident, with nothing in `repository-analysis` having ruled it out
```

## Case 14 — Avoids: Recommending an archived project without saying it is archived

```text
GIVEN    A situation that invites the anti-pattern "Recommending an archived project without saying it is archived"
WHEN     the agent applies `repository-analysis` in that situation
THEN     "Recommending an archived project without saying it is archived" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Recommending an archived project without saying it is archived" appears in the output; or it is absent by accident, with nothing in `repository-analysis` having ruled it out
```

## Case 15 — Avoids: Vendoring a repository that has no license file

```text
GIVEN    A situation that invites the anti-pattern "Vendoring a repository that has no license file"
WHEN     the agent applies `repository-analysis` in that situation
THEN     "Vendoring a repository that has no license file" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Vendoring a repository that has no license file" appears in the output; or it is absent by accident, with nothing in `repository-analysis` having ruled it out
```

## Case 16 — Avoids: Reading the directory listing and calling it an architecture review

```text
GIVEN    A situation that invites the anti-pattern "Reading the directory listing and calling it an architecture review"
WHEN     the agent applies `repository-analysis` in that situation
THEN     "Reading the directory listing and calling it an architecture review" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Reading the directory listing and calling it an architecture review" appears in the output; or it is absent by accident, with nothing in `repository-analysis` having ruled it out
```

## Case 17 — Avoids: Assessing `main` when production pins `v1.4.2`

```text
GIVEN    A situation that invites the anti-pattern "Assessing `main` when production pins `v1.4.2`"
WHEN     the agent applies `repository-analysis` in that situation
THEN     "Assessing `main` when production pins `v1.4.2`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Assessing `main` when production pins `v1.4.2`" appears in the output; or it is absent by accident, with nothing in `repository-analysis` having ruled it out
```

## Case 18 — Avoids: Ignoring install-time scripts in a dependency

```text
GIVEN    A situation that invites the anti-pattern "Ignoring install-time scripts in a dependency"
WHEN     the agent applies `repository-analysis` in that situation
THEN     "Ignoring install-time scripts in a dependency" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Ignoring install-time scripts in a dependency" appears in the output; or it is absent by accident, with nothing in `repository-analysis` having ruled it out
```

## Case 19 — Avoids: Reporting a health snapshot without the observation date

```text
GIVEN    A situation that invites the anti-pattern "Reporting a health snapshot without the observation date"
WHEN     the agent applies `repository-analysis` in that situation
THEN     "Reporting a health snapshot without the observation date" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Reporting a health snapshot without the observation date" appears in the output; or it is absent by accident, with nothing in `repository-analysis` having ruled it out
```
