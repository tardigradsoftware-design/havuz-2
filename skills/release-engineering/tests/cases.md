# Test cases — `release-engineering`

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
GIVEN    A task inside this skill's stated purpose: Make upgrading **predictable for the consumer**. A version number is a promise about what changed and what will not break; a changelog is the evidence;
WHEN     the agent executes `release-engineering` end to end on that task
THEN     and before delivery these specific conditions hold: "Public surface defined in writing; everything else explicitly internal"; "Support window and EOL dates published, including which versions get security fixes"; "Post-release review: consumer breakage, changelog clarity, process time, automation gaps"
FAIL IF  "Public surface defined in writing; everything else explicitly internal" is false, or "Post-release review: consumer breakage, changelog clarity, process time, automation gaps" is false, or "Support window and EOL dates published, including which versions get security fixes" is false
```

## Case 2 — Declines: An internal, single-consumer service with no version contract — coordinate…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: An internal, single-consumer service with no version contract — coordinate directly instead
WHEN     the agent considers `release-engineering` for that task
THEN     the skill is not selected, because this task is the excluded case "An internal, single-consumer service with no version contract — coordinate directly instead", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "An internal, single-consumer service with no version contract — coordinate directly instead"; or `release-engineering` is declined without naming that exclusion
```

## Case 3 — Declines: Continuous deployment of a SaaS frontend where there is no…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Continuous deployment of a SaaS frontend where there is no consumer-installable artifact (but the API and data contracts still need versioning)
WHEN     the agent considers `release-engineering` for that task
THEN     the skill is not selected, because this task is the excluded case "Continuous deployment of a SaaS frontend where there is no consumer-installable artifact (but the API and data contracts still need versioning)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Continuous deployment of a SaaS frontend where there is no consumer-installable artifact (but the API and data contracts still need versioning)"; or `release-engineering` is declined without naming that exclusion
```

## Case 4 — Detects: SEMVER LIE

```text
GIVEN    A run of this skill in which the known failure mode is present: SEMVER LIE
WHEN     the agent executes `release-engineering` and reaches the point where this failure occurs
THEN     "SEMVER LIE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A "patch" release removes a field. One occurrence destroys all trust."
FAIL IF  "SEMVER LIE" appears in the work and is reported as complete — specifically "A "patch" release removes a field. One occurrence destroys all trust."
```

## Case 5 — Detects: UNDEFINED SURFACE

```text
GIVEN    A run of this skill in which the known failure mode is present: UNDEFINED SURFACE
WHEN     the agent executes `release-engineering` and reaches the point where this failure occurs
THEN     "UNDEFINED SURFACE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Everything is public because nothing was declared internal."
FAIL IF  "UNDEFINED SURFACE" appears in the work and is reported as complete — specifically "Everything is public because nothing was declared internal."
```

## Case 6 — Detects: GIT-LOG CHANGELOG

```text
GIVEN    A run of this skill in which the known failure mode is present: GIT-LOG CHANGELOG
WHEN     the agent executes `release-engineering` and reaches the point where this failure occurs
THEN     "GIT-LOG CHANGELOG" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Commit messages published as a changelog; no migration guidance. SILENT BREAKING CHANGE A behaviour change with no changelog entry because "it was a bug fix"."
FAIL IF  "GIT-LOG CHANGELOG" appears in the work and is reported as complete — specifically "Commit messages published as a changelog; no migration guidance. SILENT BREAKING CHANGE A behaviour change with no changelog entry because "it was a bug fix"."
```

## Case 7 — Detects: ENUM TRAP

```text
GIVEN    A run of this skill in which the known failure mode is present: ENUM TRAP
WHEN     the agent executes `release-engineering` and reaches the point where this failure occurs
THEN     "ENUM TRAP" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A new enum value in a minor release breaking exhaustive switches."
FAIL IF  "ENUM TRAP" appears in the work and is reported as complete — specifically "A new enum value in a minor release breaking exhaustive switches."
```

## Case 8 — Detects: NO DEPRECATION PATH

```text
GIVEN    A run of this skill in which the known failure mode is present: NO DEPRECATION PATH
WHEN     the agent executes `release-engineering` and reaches the point where this failure occurs
THEN     "NO DEPRECATION PATH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Features removed with no warning, no window and no codemod."
FAIL IF  "NO DEPRECATION PATH" appears in the work and is reported as complete — specifically "Features removed with no warning, no window and no codemod."
```

## Case 9 — Detects: DEPRECATION SPAM

```text
GIVEN    A run of this skill in which the known failure mode is present: DEPRECATION SPAM
WHEN     the agent executes `release-engineering` and reaches the point where this failure occurs
THEN     "DEPRECATION SPAM" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A warning per call, per request, filling logs and teaching people to ignore it. UNSUPPORTED BY ACCIDENT Nobody knows which versions get security fixes."
FAIL IF  "DEPRECATION SPAM" appears in the work and is reported as complete — specifically "A warning per call, per request, filling logs and teaching people to ignore it. UNSUPPORTED BY ACCIDENT Nobody knows which versions get security fixes."
```

## Case 10 — Detects: UNVERIFIED PUBLISH

```text
GIVEN    A run of this skill in which the known failure mode is present: UNVERIFIED PUBLISH
WHEN     the agent executes `release-engineering` and reaches the point where this failure occurs
THEN     "UNVERIFIED PUBLISH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The registry upload failed or published the wrong artifact; discovered by users."
FAIL IF  "UNVERIFIED PUBLISH" appears in the work and is reported as complete — specifically "The registry upload failed or published the wrong artifact; discovered by users."
```

## Case 11 — Detects: MAJOR WITHOUT A GUIDE

```text
GIVEN    A run of this skill in which the known failure mode is present: MAJOR WITHOUT A GUIDE
WHEN     the agent executes `release-engineering` and reaches the point where this failure occurs
THEN     "MAJOR WITHOUT A GUIDE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Breaking changes announced only in the release itself. VERSION IN TWO PLACES package.json and a constant disagree."
FAIL IF  "MAJOR WITHOUT A GUIDE" appears in the work and is reported as complete — specifically "Breaking changes announced only in the release itself. VERSION IN TWO PLACES package.json and a constant disagree."
```

## Case 12 — Detects: PRE-RELEASE AS PRODUCTION

```text
GIVEN    A run of this skill in which the known failure mode is present: PRE-RELEASE AS PRODUCTION
WHEN     the agent executes `release-engineering` and reaches the point where this failure occurs
THEN     "PRE-RELEASE AS PRODUCTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "`-beta` shipped to everyone because the stable release was late."
FAIL IF  "PRE-RELEASE AS PRODUCTION" appears in the work and is reported as complete — specifically "`-beta` shipped to everyone because the stable release was late."
```

## Case 13 — Avoids: Bumping MINOR for a change you know will break someone

```text
GIVEN    A situation that invites the anti-pattern "Bumping MINOR for a change you know will break someone"
WHEN     the agent applies `release-engineering` in that situation
THEN     "Bumping MINOR for a change you know will break someone" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Bumping MINOR for a change you know will break someone" appears in the output; or it is absent by accident, with nothing in `release-engineering` having ruled it out
```

## Case 14 — Avoids: A changelog entry reading "misc improvements and bug fixes"

```text
GIVEN    A situation that invites the anti-pattern "A changelog entry reading "misc improvements and bug fixes"
WHEN     the agent applies `release-engineering` in that situation
THEN     "A changelog entry reading "misc improvements and bug fixes" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A changelog entry reading "misc improvements and bug fixes" appears in the output; or it is absent by accident, with nothing in `release-engineering` having ruled it out
```

## Case 15 — Avoids: Removing a deprecated field without ever having warned about it

```text
GIVEN    A situation that invites the anti-pattern "Removing a deprecated field without ever having warned about it"
WHEN     the agent applies `release-engineering` in that situation
THEN     "Removing a deprecated field without ever having warned about it" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Removing a deprecated field without ever having warned about it" appears in the output; or it is absent by accident, with nothing in `release-engineering` having ruled it out
```

## Case 16 — Avoids: Publishing the docs for `main` as though they applied to the released version

```text
GIVEN    A situation that invites the anti-pattern "Publishing the docs for `main` as though they applied to the released version"
WHEN     the agent applies `release-engineering` in that situation
THEN     "Publishing the docs for `main` as though they applied to the released version" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Publishing the docs for `main` as though they applied to the released version" appears in the output; or it is absent by accident, with nothing in `release-engineering` having ruled it out
```

## Case 17 — Avoids: A deprecation warning printed on every request

```text
GIVEN    A situation that invites the anti-pattern "A deprecation warning printed on every request"
WHEN     the agent applies `release-engineering` in that situation
THEN     "A deprecation warning printed on every request" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A deprecation warning printed on every request" appears in the output; or it is absent by accident, with nothing in `release-engineering` having ruled it out
```

## Case 18 — Avoids: "We don't support old versions" with no published window

```text
GIVEN    A situation that invites the anti-pattern "We don't support old versions" with no published window"
WHEN     the agent applies `release-engineering` in that situation
THEN     "We don't support old versions" with no published window" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "We don't support old versions" with no published window" appears in the output; or it is absent by accident, with nothing in `release-engineering` having ruled it out
```

## Case 19 — Avoids: Skipping the clean-install verification because the CI build passed

```text
GIVEN    A situation that invites the anti-pattern "Skipping the clean-install verification because the CI build passed"
WHEN     the agent applies `release-engineering` in that situation
THEN     "Skipping the clean-install verification because the CI build passed" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Skipping the clean-install verification because the CI build passed" appears in the output; or it is absent by accident, with nothing in `release-engineering` having ruled it out
```

## Case 20 — Avoids: Two files declaring different versions of the same package

```text
GIVEN    A situation that invites the anti-pattern "Two files declaring different versions of the same package"
WHEN     the agent applies `release-engineering` in that situation
THEN     "Two files declaring different versions of the same package" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Two files declaring different versions of the same package" appears in the output; or it is absent by accident, with nothing in `release-engineering` having ruled it out
```
