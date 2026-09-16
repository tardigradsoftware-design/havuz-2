# Test cases — `research-before-code`

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
GIVEN    A task inside this skill's stated purpose: Stop the agent from treating its training data as a sufficient specification. The default failure is not laziness, it is confidence: an agent that has seen a thousand `next-auth` examples will write a plausible authentication flow for a…
WHEN     the agent executes `research-before-code` end to end on that task
THEN     and before delivery these specific conditions hold: "Task restated with implicit choices named"; "Research Decision Record written before the first line of implementation code"; "Risk class justified in one line"
FAIL IF  "Task restated with implicit choices named" is false, or "Risk class justified in one line" is false, or "Research Decision Record written before the first line of implementation code" is false
```

## Case 2 — Declines: A one-line typo fix or a rename with compiler verification

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A one-line typo fix or a rename with compiler verification
WHEN     the agent considers `research-before-code` for that task
THEN     the skill is not selected, because this task is the excluded case "A one-line typo fix or a rename with compiler verification", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A one-line typo fix or a rename with compiler verification"; or `research-before-code` is declined without naming that exclusion
```

## Case 3 — Declines: Purely local refactoring whose correctness is proved by the existing test…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Purely local refactoring whose correctness is proved by the existing test suite
WHEN     the agent considers `research-before-code` for that task
THEN     the skill is not selected, because this task is the excluded case "Purely local refactoring whose correctness is proved by the existing test suite", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Purely local refactoring whose correctness is proved by the existing test suite"; or `research-before-code` is declined without naming that exclusion
```

## Case 4 — Declines: Throwaway spikes explicitly labelled as disposable (but say so in the output)

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Throwaway spikes explicitly labelled as disposable (but say so in the output)
WHEN     the agent considers `research-before-code` for that task
THEN     the skill is not selected, because this task is the excluded case "Throwaway spikes explicitly labelled as disposable (but say so in the output)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Throwaway spikes explicitly labelled as disposable (but say so in the output)"; or `research-before-code` is declined without naming that exclusion
```

## Case 5 — Declines: Tasks inside a codebase whose conventions are already documented in AGENTS.md…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Tasks inside a codebase whose conventions are already documented in AGENTS.md — read the project's own instructions instead of researching the internet
WHEN     the agent considers `research-before-code` for that task
THEN     the skill is not selected, because this task is the excluded case "Tasks inside a codebase whose conventions are already documented in AGENTS.md — read the project's own instructions instead of researching the internet", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Tasks inside a codebase whose conventions are already documented in AGENTS.md — read the project's own instructions instead of researching the…"; or `research-before-code` is declined without naming that exclusion
```

## Case 6 — Declines: When the human has already pinned the exact library,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When the human has already pinned the exact library, version and pattern: research the version's API, not the choice
WHEN     the agent considers `research-before-code` for that task
THEN     the skill is not selected, because this task is the excluded case "When the human has already pinned the exact library, version and pattern: research the version's API, not the choice", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When the human has already pinned the exact library, version and pattern: research the version's API, not the choice"; or `research-before-code` is declined without naming that exclusion
```

## Case 7 — Detects: RESEARCH THEATRE

```text
GIVEN    A run of this skill in which the known failure mode is present: RESEARCH THEATRE
WHEN     the agent executes `research-before-code` and reaches the point where this failure occurs
THEN     "RESEARCH THEATRE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Searching a lot and citing nothing. Fix: the evidence table is mandatory."
FAIL IF  "RESEARCH THEATRE" appears in the work and is reported as complete — specifically "Searching a lot and citing nothing. Fix: the evidence table is mandatory."
```

## Case 8 — Detects: CONFIRMATION SEARCH

```text
GIVEN    A run of this skill in which the known failure mode is present: CONFIRMATION SEARCH
WHEN     the agent executes `research-before-code` and reaches the point where this failure occurs
THEN     "CONFIRMATION SEARCH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Only looking for sources that agree with the first idea. Fix: stage 3 requires a rejected option with a reason."
FAIL IF  "CONFIRMATION SEARCH" appears in the work and is reported as complete — specifically "Only looking for sources that agree with the first idea. Fix: stage 3 requires a rejected option with a reason."
```

## Case 9 — Detects: STALE OFFICIAL DOCS

```text
GIVEN    A run of this skill in which the known failure mode is present: STALE OFFICIAL DOCS
WHEN     the agent executes `research-before-code` and reaches the point where this failure occurs
THEN     "STALE OFFICIAL DOCS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Reading a docs page for v4 while installing v6. Fix: record the version the doc describes, next to the URL."
FAIL IF  "STALE OFFICIAL DOCS" appears in the work and is reported as complete — specifically "Reading a docs page for v4 while installing v6. Fix: record the version the doc describes, next to the URL."
```

## Case 10 — Detects: STAR-DRIVEN CHOICE

```text
GIVEN    A run of this skill in which the known failure mode is present: STAR-DRIVEN CHOICE
WHEN     the agent executes `research-before-code` and reaches the point where this failure occurs
THEN     "STAR-DRIVEN CHOICE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Picking the most-starred option regardless of fit or status. Fix: filter by status and license_risk before sorting by stars."
FAIL IF  "STAR-DRIVEN CHOICE" appears in the work and is reported as complete — specifically "Picking the most-starred option regardless of fit or status. Fix: filter by status and license_risk before sorting by stars."
```

## Case 11 — Detects: BLOG-ONLY EVIDENCE

```text
GIVEN    A run of this skill in which the known failure mode is present: BLOG-ONLY EVIDENCE
WHEN     the agent executes `research-before-code` and reaches the point where this failure occurs
THEN     "BLOG-ONLY EVIDENCE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Every source is a tutorial. Fix: ≥1 official or primary source per claim."
FAIL IF  "BLOG-ONLY EVIDENCE" appears in the work and is reported as complete — specifically "Every source is a tutorial. Fix: ≥1 official or primary source per claim."
```

## Case 12 — Detects: CONTEXT FLOOD

```text
GIVEN    A run of this skill in which the known failure mode is present: CONTEXT FLOOD
WHEN     the agent executes `research-before-code` and reaches the point where this failure occurs
THEN     "CONTEXT FLOOD" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Pasting every page found into the prompt. Fix: keep only the evidence table; link the rest."
FAIL IF  "CONTEXT FLOOD" appears in the work and is reported as complete — specifically "Pasting every page found into the prompt. Fix: keep only the evidence table; link the rest."
```

## Case 13 — Detects: PERPETUAL RESEARCH

```text
GIVEN    A run of this skill in which the known failure mode is present: PERPETUAL RESEARCH
WHEN     the agent executes `research-before-code` and reaches the point where this failure occurs
THEN     "PERPETUAL RESEARCH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Never starting. Fix: cap stage 2-4 at a fixed budget and record open risks. SILENT IMPROVISATION Abandoning the plan mid-implementation without updating the record."
FAIL IF  "PERPETUAL RESEARCH" appears in the work and is reported as complete — specifically "Never starting. Fix: cap stage 2-4 at a fixed budget and record open risks. SILENT IMPROVISATION Abandoning the plan mid-implementation without updating the record."
```

## Case 14 — Avoids: "I'll use X because it's popular" with no source, no version, no license check

```text
GIVEN    A situation that invites the anti-pattern "I'll use X because it's popular" with no source, no version, no license check"
WHEN     the agent applies `research-before-code` in that situation
THEN     "I'll use X because it's popular" with no source, no version, no license check" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "I'll use X because it's popular" with no source, no version, no license check" appears in the output; or it is absent by accident, with nothing in `research-before-code` having ruled it out
```

## Case 15 — Avoids: Researching the framework but not the version's breaking changes

```text
GIVEN    A situation that invites the anti-pattern "Researching the framework but not the version's breaking changes"
WHEN     the agent applies `research-before-code` in that situation
THEN     "Researching the framework but not the version's breaking changes" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Researching the framework but not the version's breaking changes" appears in the output; or it is absent by accident, with nothing in `research-before-code` having ruled it out
```

## Case 16 — Avoids: Writing the plan after the code, as documentation of what was already done

```text
GIVEN    A situation that invites the anti-pattern "Writing the plan after the code, as documentation of what was already done"
WHEN     the agent applies `research-before-code` in that situation
THEN     "Writing the plan after the code, as documentation of what was already done" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Writing the plan after the code, as documentation of what was already done" appears in the output; or it is absent by accident, with nothing in `research-before-code` having ruled it out
```

## Case 17 — Avoids: Treating a single high-ranking search result as settled fact

```text
GIVEN    A situation that invites the anti-pattern "Treating a single high-ranking search result as settled fact"
WHEN     the agent applies `research-before-code` in that situation
THEN     "Treating a single high-ranking search result as settled fact" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Treating a single high-ranking search result as settled fact" appears in the output; or it is absent by accident, with nothing in `research-before-code` having ruled it out
```

## Case 18 — Avoids: Copying a snippet from a source dated before the library's last major release

```text
GIVEN    A situation that invites the anti-pattern "Copying a snippet from a source dated before the library's last major release"
WHEN     the agent applies `research-before-code` in that situation
THEN     "Copying a snippet from a source dated before the library's last major release" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Copying a snippet from a source dated before the library's last major release" appears in the output; or it is absent by accident, with nothing in `research-before-code` having ruled it out
```

## Case 19 — Avoids: Skipping verification because the task "feels small"

```text
GIVEN    A situation that invites the anti-pattern "Skipping verification because the task "feels small"
WHEN     the agent applies `research-before-code` in that situation
THEN     "Skipping verification because the task "feels small" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Skipping verification because the task "feels small" appears in the output; or it is absent by accident, with nothing in `research-before-code` having ruled it out
```
