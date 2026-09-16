# Test cases — `dont-reinvent-the-wheel`

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
GIVEN    A task inside this skill's stated purpose: Before writing a non-trivial component, prove that writing it is the right choice. The default should be **adopt**, and **build** should require an argument. This is not "always use a library".
WHEN     the agent executes `dont-reinvent-the-wheel` end to end on that task
THEN     and before delivery these specific conditions hold: "All six questions asked and answered in writing"; "ESCALATE used for any crypto/auth/payment/identity primitive"; "Escape hatch documented for anything hand-rolled"
FAIL IF  "All six questions asked and answered in writing" is false, or "Escape hatch documented for anything hand-rolled" is false, or "ESCALATE used for any crypto/auth/payment/identity primitive" is false
```

## Case 2 — Declines: Genuinely novel domain logic that has no prior art (your business rules)

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Genuinely novel domain logic that has no prior art (your business rules)
WHEN     the agent considers `dont-reinvent-the-wheel` for that task
THEN     the skill is not selected, because this task is the excluded case "Genuinely novel domain logic that has no prior art (your business rules)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Genuinely novel domain logic that has no prior art (your business rules)"; or `dont-reinvent-the-wheel` is declined without naming that exclusion
```

## Case 3 — Declines: Thin glue under 30 lines where a dependency would cost more than it saves

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Thin glue under 30 lines where a dependency would cost more than it saves
WHEN     the agent considers `dont-reinvent-the-wheel` for that task
THEN     the skill is not selected, because this task is the excluded case "Thin glue under 30 lines where a dependency would cost more than it saves", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Thin glue under 30 lines where a dependency would cost more than it saves"; or `dont-reinvent-the-wheel` is declined without naming that exclusion
```

## Case 4 — Declines: A hard constraint already rules out third-party code (air-gapped, licensing,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A hard constraint already rules out third-party code (air-gapped, licensing, certification) — record the constraint and proceed
WHEN     the agent considers `dont-reinvent-the-wheel` for that task
THEN     the skill is not selected, because this task is the excluded case "A hard constraint already rules out third-party code (air-gapped, licensing, certification) — record the constraint and proceed", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A hard constraint already rules out third-party code (air-gapped, licensing, certification) — record the constraint and proceed"; or `dont-reinvent-the-wheel` is declined without naming that exclusion
```

## Case 5 — Declines: Security-critical primitives you are not qualified to write — the answer here…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Security-critical primitives you are not qualified to write — the answer here is never "build", it is "escalate"
WHEN     the agent considers `dont-reinvent-the-wheel` for that task
THEN     the skill is not selected, because this task is the excluded case "Security-critical primitives you are not qualified to write — the answer here is never "build", it is "escalate", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Security-critical primitives you are not qualified to write — the answer here is never "build", it is "escalate"; or `dont-reinvent-the-wheel` is declined without naming that exclusion
```

## Case 6 — Detects: NIH SYNDROME

```text
GIVEN    A run of this skill in which the known failure mode is present: NIH SYNDROME
WHEN     the agent executes `dont-reinvent-the-wheel` and reaches the point where this failure occurs
THEN     "NIH SYNDROME" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Building because the library's API is not to your taste. Fix: WRAP it; taste is not a constraint. DEPENDENCY MAXIMALISM Adding a package for something the stdlib already does."
FAIL IF  "NIH SYNDROME" appears in the work and is reported as complete — specifically "Building because the library's API is not to your taste. Fix: WRAP it; taste is not a constraint."
```

## Case 7 — Detects: ABANDONED ADOPTION

```text
GIVEN    A run of this skill in which the known failure mode is present: ABANDONED ADOPTION
WHEN     the agent executes `dont-reinvent-the-wheel` and reaches the point where this failure occurs
THEN     "ABANDONED ADOPTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Adopting a project that is ARCHIVED or unmaintained. Fix: filter metadata/repositories.json by status before adopting."
FAIL IF  "ABANDONED ADOPTION" appears in the work and is reported as complete — specifically "Adopting a project that is ARCHIVED or unmaintained. Fix: filter metadata/repositories.json by status before adopting."
```

## Case 8 — Detects: FORK AND FORGET

```text
GIVEN    A run of this skill in which the known failure mode is present: FORK AND FORGET
WHEN     the agent executes `dont-reinvent-the-wheel` and reaches the point where this failure occurs
THEN     "FORK AND FORGET" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Forking a library instead of contributing or wrapping. Fix: forks inherit every upstream CVE and none of the fixes."
FAIL IF  "FORK AND FORGET" appears in the work and is reported as complete — specifically "Forking a library instead of contributing or wrapping. Fix: forks inherit every upstream CVE and none of the fixes."
```

## Case 9 — Detects: STAR-DRIVEN ADOPTION

```text
GIVEN    A run of this skill in which the known failure mode is present: STAR-DRIVEN ADOPTION
WHEN     the agent executes `dont-reinvent-the-wheel` and reaches the point where this failure occurs
THEN     "STAR-DRIVEN ADOPTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Choosing by stars, ignoring license, fit and maintenance."
FAIL IF  "STAR-DRIVEN ADOPTION" appears in the work and is reported as complete — specifically "Choosing by stars, ignoring license, fit and maintenance."
```

## Case 10 — Detects: PHANTOM LIBRARY

```text
GIVEN    A run of this skill in which the known failure mode is present: PHANTOM LIBRARY
WHEN     the agent executes `dont-reinvent-the-wheel` and reaches the point where this failure occurs
THEN     "PHANTOM LIBRARY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Citing a package that does not exist. Fix: resolve it in the registry."
FAIL IF  "PHANTOM LIBRARY" appears in the work and is reported as complete — specifically "Citing a package that does not exist. Fix: resolve it in the registry."
```

## Case 11 — Detects: PARTIAL REINVENTION

```text
GIVEN    A run of this skill in which the known failure mode is present: PARTIAL REINVENTION
WHEN     the agent executes `dont-reinvent-the-wheel` and reaches the point where this failure occurs
THEN     "PARTIAL REINVENTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Adopting a library but reimplementing the half you did not read."
FAIL IF  "PARTIAL REINVENTION" appears in the work and is reported as complete — specifically "Adopting a library but reimplementing the half you did not read."
```

## Case 12 — Avoids: "I'll just write a quick JWT verifier" — escalate instead

```text
GIVEN    A situation that invites the anti-pattern "I'll just write a quick JWT verifier" — escalate instead"
WHEN     the agent applies `dont-reinvent-the-wheel` in that situation
THEN     "I'll just write a quick JWT verifier" — escalate instead" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "I'll just write a quick JWT verifier" — escalate instead" appears in the output; or it is absent by accident, with nothing in `dont-reinvent-the-wheel` having ruled it out
```

## Case 13 — Avoids: Adding lodash for one function the runtime already has

```text
GIVEN    A situation that invites the anti-pattern "Adding lodash for one function the runtime already has"
WHEN     the agent applies `dont-reinvent-the-wheel` in that situation
THEN     "Adding lodash for one function the runtime already has" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Adding lodash for one function the runtime already has" appears in the output; or it is absent by accident, with nothing in `dont-reinvent-the-wheel` having ruled it out
```

## Case 14 — Avoids: Writing a retry helper with no jitter and no timeout budget

```text
GIVEN    A situation that invites the anti-pattern "Writing a retry helper with no jitter and no timeout budget"
WHEN     the agent applies `dont-reinvent-the-wheel` in that situation
THEN     "Writing a retry helper with no jitter and no timeout budget" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Writing a retry helper with no jitter and no timeout budget" appears in the output; or it is absent by accident, with nothing in `dont-reinvent-the-wheel` having ruled it out
```

## Case 15 — Avoids: Building an ORM because the existing one's docs were confusing

```text
GIVEN    A situation that invites the anti-pattern "Building an ORM because the existing one's docs were confusing"
WHEN     the agent applies `dont-reinvent-the-wheel` in that situation
THEN     "Building an ORM because the existing one's docs were confusing" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Building an ORM because the existing one's docs were confusing" appears in the output; or it is absent by accident, with nothing in `dont-reinvent-the-wheel` having ruled it out
```

## Case 16 — Avoids: Adopting a 40k-star project archived two years ago

```text
GIVEN    A situation that invites the anti-pattern "Adopting a 40k-star project archived two years ago"
WHEN     the agent applies `dont-reinvent-the-wheel` in that situation
THEN     "Adopting a 40k-star project archived two years ago" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Adopting a 40k-star project archived two years ago" appears in the output; or it is absent by accident, with nothing in `dont-reinvent-the-wheel` having ruled it out
```

## Case 17 — Avoids: Reimplementing RBAC in application code when Postgres RLS is available

```text
GIVEN    A situation that invites the anti-pattern "Reimplementing RBAC in application code when Postgres RLS is available"
WHEN     the agent applies `dont-reinvent-the-wheel` in that situation
THEN     "Reimplementing RBAC in application code when Postgres RLS is available" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Reimplementing RBAC in application code when Postgres RLS is available" appears in the output; or it is absent by accident, with nothing in `dont-reinvent-the-wheel` having ruled it out
```

## Case 18 — Avoids: Writing a date library

```text
GIVEN    A situation that invites the anti-pattern "Writing a date library", whose stated consequence is: Never write a date library.
WHEN     the agent applies `dont-reinvent-the-wheel` in that situation
THEN     "Writing a date library" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Never write a date library."
FAIL IF  "Writing a date library" appears in the output — that is, "Never write a date library."; or it is absent by accident, with nothing in `dont-reinvent-the-wheel` having ruled it out
```
