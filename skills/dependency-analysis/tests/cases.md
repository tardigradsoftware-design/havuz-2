# Test cases — `dependency-analysis`

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
GIVEN    A task inside this skill's stated purpose: Know exactly what your project depends on, what each dependency costs you, and what happens when one of them changes, is compromised, or dies.
WHEN     the agent executes `dependency-analysis` end to end on that task
THEN     and before delivery these specific conditions hold: "Full resolved graph enumerated from the lockfile, including build/dev/install-time deps"; "Weight measured (install size, bundle contribution, cold start), not estimated"; "Deep review scheduled quarterly; advisory alerts within one day"
FAIL IF  "Full resolved graph enumerated from the lockfile, including build/dev/install-time deps" is false, or "Deep review scheduled quarterly; advisory alerts within one day" is false, or "Weight measured (install size, bundle contribution, cold start), not estimated" is false
```

## Case 2 — Declines: A throwaway script with a couple of well-known dependencies

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A throwaway script with a couple of well-known dependencies
WHEN     the agent considers `dependency-analysis` for that task
THEN     the skill is not selected, because this task is the excluded case "A throwaway script with a couple of well-known dependencies", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A throwaway script with a couple of well-known dependencies"; or `dependency-analysis` is declined without naming that exclusion
```

## Case 3 — Declines: As a reason to remove all dependencies — zero-dependency is not automatically…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As a reason to remove all dependencies — zero-dependency is not automatically safer, it just moves the code into your repo where nobody audits it
WHEN     the agent considers `dependency-analysis` for that task
THEN     the skill is not selected, because this task is the excluded case "As a reason to remove all dependencies — zero-dependency is not automatically safer, it just moves the code into your repo where nobody audits it", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As a reason to remove all dependencies — zero-dependency is not automatically safer, it just moves the code into your repo where nobody audits it"; or `dependency-analysis` is declined without naming that exclusion
```

## Case 4 — Detects: MANIFEST-ONLY REVIEW

```text
GIVEN    A run of this skill in which the known failure mode is present: MANIFEST-ONLY REVIEW
WHEN     the agent executes `dependency-analysis` and reaches the point where this failure occurs
THEN     "MANIFEST-ONLY REVIEW" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Analysing declared deps and missing the 400 transitive ones."
FAIL IF  "MANIFEST-ONLY REVIEW" appears in the work and is reported as complete — specifically "Analysing declared deps and missing the 400 transitive ones."
```

## Case 5 — Detects: RANGE TRUST

```text
GIVEN    A run of this skill in which the known failure mode is present: RANGE TRUST
WHEN     the agent executes `dependency-analysis` and reaches the point where this failure occurs
THEN     "RANGE TRUST" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "We declare ^1.2.0" — the resolved version is what ships. Read the lockfile."
FAIL IF  "RANGE TRUST" appears in the work and is reported as complete — specifically "We declare ^1.2.0" — the resolved version is what ships. Read the lockfile."
```

## Case 6 — Detects: SCANNER AS VERDICT

```text
GIVEN    A run of this skill in which the known failure mode is present: SCANNER AS VERDICT
WHEN     the agent executes `dependency-analysis` and reaches the point where this failure occurs
THEN     "SCANNER AS VERDICT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Merging whatever the scanner says, or ignoring it entirely. UNREACHABLE COMPLACENCY Dismissing a critical CVE as unreachable without proving the code path."
FAIL IF  "SCANNER AS VERDICT" appears in the work and is reported as complete — specifically "Merging whatever the scanner says, or ignoring it entirely. UNREACHABLE COMPLACENCY Dismissing a critical CVE as unreachable without proving the code path."
```

## Case 7 — Detects: TYPOSQUAT

```text
GIVEN    A run of this skill in which the known failure mode is present: TYPOSQUAT
WHEN     the agent executes `dependency-analysis` and reaches the point where this failure occurs
THEN     "TYPOSQUAT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A package one character from the real one."
FAIL IF  "TYPOSQUAT" appears in the work and is reported as complete — specifically "A package one character from the real one."
```

## Case 8 — Detects: LICENSE BY BADGE

```text
GIVEN    A run of this skill in which the known failure mode is present: LICENSE BY BADGE
WHEN     the agent executes `dependency-analysis` and reaches the point where this failure occurs
THEN     "LICENSE BY BADGE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Trusting a README badge instead of the license file; missing `null`."
FAIL IF  "LICENSE BY BADGE" appears in the work and is reported as complete — specifically "Trusting a README badge instead of the license file; missing `null`."
```

## Case 9 — Detects: AGPL SURPRISE

```text
GIVEN    A run of this skill in which the known failure mode is present: AGPL SURPRISE
WHEN     the agent executes `dependency-analysis` and reaches the point where this failure occurs
THEN     "AGPL SURPRISE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Discovering a network-copyleft transitive after launch."
FAIL IF  "AGPL SURPRISE" appears in the work and is reported as complete — specifically "Discovering a network-copyleft transitive after launch."
```

## Case 10 — Detects: DUPLICATE STACK

```text
GIVEN    A run of this skill in which the known failure mode is present: DUPLICATE STACK
WHEN     the agent executes `dependency-analysis` and reaches the point where this failure occurs
THEN     "DUPLICATE STACK" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Three date libraries, two fetch clients, four test runners."
FAIL IF  "DUPLICATE STACK" appears in the work and is reported as complete — specifically "Three date libraries, two fetch clients, four test runners."
```

## Case 11 — Detects: ABANDONED CRITICAL

```text
GIVEN    A run of this skill in which the known failure mode is present: ABANDONED CRITICAL
WHEN     the agent executes `dependency-analysis` and reaches the point where this failure occurs
THEN     "ABANDONED CRITICAL" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A single-maintainer package holding up authentication, unnoticed."
FAIL IF  "ABANDONED CRITICAL" appears in the work and is reported as complete — specifically "A single-maintainer package holding up authentication, unnoticed."
```

## Case 12 — Detects: FOREVER-PINNED

```text
GIVEN    A run of this skill in which the known failure mode is present: FOREVER-PINNED
WHEN     the agent executes `dependency-analysis` and reaches the point where this failure occurs
THEN     "FOREVER-PINNED" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Pinning so tightly that security updates cannot land."
FAIL IF  "FOREVER-PINNED" appears in the work and is reported as complete — specifically "Pinning so tightly that security updates cannot land."
```

## Case 13 — Detects: NO REMOVAL PLAN

```text
GIVEN    A run of this skill in which the known failure mode is present: NO REMOVAL PLAN
WHEN     the agent executes `dependency-analysis` and reaches the point where this failure occurs
THEN     "NO REMOVAL PLAN" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Adopting without knowing the exit cost."
FAIL IF  "NO REMOVAL PLAN" appears in the work and is reported as complete — specifically "Adopting without knowing the exit cost."
```

## Case 14 — Avoids: `npm audit` output pasted into a ticket with no triage

```text
GIVEN    A situation that invites the anti-pattern "`npm audit` output pasted into a ticket with no triage"
WHEN     the agent applies `dependency-analysis` in that situation
THEN     "`npm audit` output pasted into a ticket with no triage" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`npm audit` output pasted into a ticket with no triage" appears in the output; or it is absent by accident, with nothing in `dependency-analysis` having ruled it out
```

## Case 15 — Avoids: Depending on a git branch or a mutable tag in production

```text
GIVEN    A situation that invites the anti-pattern "Depending on a git branch or a mutable tag in production"
WHEN     the agent applies `dependency-analysis` in that situation
THEN     "Depending on a git branch or a mutable tag in production" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Depending on a git branch or a mutable tag in production" appears in the output; or it is absent by accident, with nothing in `dependency-analysis` having ruled it out
```

## Case 16 — Avoids: Adding a 3 MB dependency for one 10-line function

```text
GIVEN    A situation that invites the anti-pattern "Adding a 3 MB dependency for one 10-line function"
WHEN     the agent applies `dependency-analysis` in that situation
THEN     "Adding a 3 MB dependency for one 10-line function" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Adding a 3 MB dependency for one 10-line function" appears in the output; or it is absent by accident, with nothing in `dependency-analysis` having ruled it out
```

## Case 17 — Avoids: Shipping a product with an AGPL transitive and no legal review

```text
GIVEN    A situation that invites the anti-pattern "Shipping a product with an AGPL transitive and no legal review"
WHEN     the agent applies `dependency-analysis` in that situation
THEN     "Shipping a product with an AGPL transitive and no legal review" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Shipping a product with an AGPL transitive and no legal review" appears in the output; or it is absent by accident, with nothing in `dependency-analysis` having ruled it out
```

## Case 18 — Avoids: Vendoring a package that has no license file

```text
GIVEN    A situation that invites the anti-pattern "Vendoring a package that has no license file"
WHEN     the agent applies `dependency-analysis` in that situation
THEN     "Vendoring a package that has no license file" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Vendoring a package that has no license file" appears in the output; or it is absent by accident, with nothing in `dependency-analysis` having ruled it out
```

## Case 19 — Avoids: Three date libraries in one bundle

```text
GIVEN    A situation that invites the anti-pattern "Three date libraries in one bundle"
WHEN     the agent applies `dependency-analysis` in that situation
THEN     "Three date libraries in one bundle" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Three date libraries in one bundle" appears in the output; or it is absent by accident, with nothing in `dependency-analysis` having ruled it out
```

## Case 20 — Avoids: Ignoring a package's ownership change because "it's probably fine"

```text
GIVEN    A situation that invites the anti-pattern "Ignoring a package's ownership change because "it's probably fine"
WHEN     the agent applies `dependency-analysis` in that situation
THEN     "Ignoring a package's ownership change because "it's probably fine" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Ignoring a package's ownership change because "it's probably fine" appears in the output; or it is absent by accident, with nothing in `dependency-analysis` having ruled it out
```

## Case 21 — Avoids: Auto-merging major-version bumps of a runtime dependency

```text
GIVEN    A situation that invites the anti-pattern "Auto-merging major-version bumps of a runtime dependency"
WHEN     the agent applies `dependency-analysis` in that situation
THEN     "Auto-merging major-version bumps of a runtime dependency" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Auto-merging major-version bumps of a runtime dependency" appears in the output; or it is absent by accident, with nothing in `dependency-analysis` having ruled it out
```
