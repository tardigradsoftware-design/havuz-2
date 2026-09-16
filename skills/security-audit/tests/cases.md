# Test cases — `security-audit`

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
GIVEN    A task inside this skill's stated purpose: Find the defects that matter, in the order they matter, with a recommendation an engineer can execute today. A security audit is not a list of everything that could theoretically go wrong;
WHEN     the agent executes `security-audit` end to end on that task
THEN     and before delivery these specific conditions hold: "Threat model drawn with trust boundaries before code was read"; "Findings ranked; CRITICAL blocks release"; "No security primitive hand-rolled; escalation used where one was needed"
FAIL IF  "Threat model drawn with trust boundaries before code was read" is false, or "No security primitive hand-rolled; escalation used where one was needed" is false, or "Findings ranked; CRITICAL blocks release" is false
```

## Case 2 — Declines: As a substitute for a penetration test on a system where one is required

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As a substitute for a penetration test on a system where one is required
WHEN     the agent considers `security-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "As a substitute for a penetration test on a system where one is required", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As a substitute for a penetration test on a system where one is required"; or `security-audit` is declined without naming that exclusion
```

## Case 3 — Declines: On code with no attack surface (a pure local script with no inputs) — say so…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: On code with no attack surface (a pure local script with no inputs) — say so and skip
WHEN     the agent considers `security-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "On code with no attack surface (a pure local script with no inputs) — say so and skip", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "On code with no attack surface (a pure local script with no inputs) — say so and skip"; or `security-audit` is declined without naming that exclusion
```

## Case 4 — Declines: To generate a long list of theoretical findings with no exploitability…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: To generate a long list of theoretical findings with no exploitability analysis: that produces alert fatigue and hides the real issue
WHEN     the agent considers `security-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "To generate a long list of theoretical findings with no exploitability analysis: that produces alert fatigue and hides the real issue", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "To generate a long list of theoretical findings with no exploitability analysis: that produces alert fatigue and hides the real issue"; or `security-audit` is declined without naming that exclusion
```

## Case 5 — Detects: CHECKLIST THEATRE

```text
GIVEN    A run of this skill in which the known failure mode is present: CHECKLIST THEATRE
WHEN     the agent executes `security-audit` and reaches the point where this failure occurs
THEN     "CHECKLIST THEATRE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Marking items without reading the code. Fix: cite file:line per item."
FAIL IF  "CHECKLIST THEATRE" appears in the work and is reported as complete — specifically "Marking items without reading the code. Fix: cite file:line per item."
```

## Case 6 — Detects: THEORETICAL FLOOD

```text
GIVEN    A run of this skill in which the known failure mode is present: THEORETICAL FLOOD
WHEN     the agent executes `security-audit` and reaches the point where this failure occurs
THEN     "THEORETICAL FLOOD" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "80 LOW findings hiding 1 CRITICAL. Fix: exploitability required."
FAIL IF  "THEORETICAL FLOOD" appears in the work and is reported as complete — specifically "80 LOW findings hiding 1 CRITICAL. Fix: exploitability required."
```

## Case 7 — Detects: SCANNER AS AUDIT

```text
GIVEN    A run of this skill in which the known failure mode is present: SCANNER AS AUDIT
WHEN     the agent executes `security-audit` and reaches the point where this failure occurs
THEN     "SCANNER AS AUDIT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Treating SAST/dependency output as the answer. Fix: triage every hit. FALSE NEGATIVE COMFORT "The scanner found nothing." Scanners miss logic and authz bugs — the majority of real incidents."
FAIL IF  "SCANNER AS AUDIT" appears in the work and is reported as complete — specifically "Treating SAST/dependency output as the answer. Fix: triage every hit. FALSE NEGATIVE COMFORT "The scanner found nothing." Scanners miss logic and authz bugs — the…"
```

## Case 8 — Detects: SCOPE DRIFT

```text
GIVEN    A run of this skill in which the known failure mode is present: SCOPE DRIFT
WHEN     the agent executes `security-audit` and reaches the point where this failure occurs
THEN     "SCOPE DRIFT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Auditing the framework instead of the application's use of it."
FAIL IF  "SCOPE DRIFT" appears in the work and is reported as complete — specifically "Auditing the framework instead of the application's use of it."
```

## Case 9 — Detects: HISTORY BLINDNESS

```text
GIVEN    A run of this skill in which the known failure mode is present: HISTORY BLINDNESS
WHEN     the agent executes `security-audit` and reaches the point where this failure occurs
THEN     "HISTORY BLINDNESS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Checking the working tree but not git history for secrets."
FAIL IF  "HISTORY BLINDNESS" appears in the work and is reported as complete — specifically "Checking the working tree but not git history for secrets."
```

## Case 10 — Detects: AGENT BLINDNESS

```text
GIVEN    A run of this skill in which the known failure mode is present: AGENT BLINDNESS
WHEN     the agent executes `security-audit` and reaches the point where this failure occurs
THEN     "AGENT BLINDNESS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Auditing the web app and ignoring the agent that can execute code."
FAIL IF  "AGENT BLINDNESS" appears in the work and is reported as complete — specifically "Auditing the web app and ignoring the agent that can execute code."
```

## Case 11 — Detects: FIX WITHOUT PROOF

```text
GIVEN    A run of this skill in which the known failure mode is present: FIX WITHOUT PROOF
WHEN     the agent executes `security-audit` and reaches the point where this failure occurs
THEN     "FIX WITHOUT PROOF" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Remediation claimed, never verified by the stated test."
FAIL IF  "FIX WITHOUT PROOF" appears in the work and is reported as complete — specifically "Remediation claimed, never verified by the stated test."
```

## Case 12 — Avoids: Client-side "admin only" rendering as an authorisation control

```text
GIVEN    A situation that invites the anti-pattern "Client-side "admin only" rendering as an authorisation control"
WHEN     the agent applies `security-audit` in that situation
THEN     "Client-side "admin only" rendering as an authorisation control" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Client-side "admin only" rendering as an authorisation control" appears in the output; or it is absent by accident, with nothing in `security-audit` having ruled it out
```

## Case 13 — Avoids: `WHERE user_id = ?` present on one query and absent on its three siblings

```text
GIVEN    A situation that invites the anti-pattern "`WHERE user_id = ?` present on one query and absent on its three siblings"
WHEN     the agent applies `security-audit` in that situation
THEN     "`WHERE user_id = ?` present on one query and absent on its three siblings" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`WHERE user_id = ?` present on one query and absent on its three siblings" appears in the output; or it is absent by accident, with nothing in `security-audit` having ruled it out
```

## Case 14 — Avoids: A JWT verified for signature but not for `exp`, `aud` or `iss`

```text
GIVEN    A situation that invites the anti-pattern "A JWT verified for signature but not for `exp`, `aud` or `iss`"
WHEN     the agent applies `security-audit` in that situation
THEN     "A JWT verified for signature but not for `exp`, `aud` or `iss`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A JWT verified for signature but not for `exp`, `aud` or `iss`" appears in the output; or it is absent by accident, with nothing in `security-audit` having ruled it out
```

## Case 15 — Avoids: `verify=False` "temporarily" in production HTTP clients

```text
GIVEN    A situation that invites the anti-pattern "`verify=False` "temporarily" in production HTTP clients"
WHEN     the agent applies `security-audit` in that situation
THEN     "`verify=False` "temporarily" in production HTTP clients" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`verify=False` "temporarily" in production HTTP clients" appears in the output; or it is absent by accident, with nothing in `security-audit` having ruled it out
```

## Case 16 — Avoids: Secrets in `.env` committed to the repository, then deleted in a later commit

```text
GIVEN    A situation that invites the anti-pattern "Secrets in `.env` committed to the repository, then deleted in a later commit"
WHEN     the agent applies `security-audit` in that situation
THEN     "Secrets in `.env` committed to the repository, then deleted in a later commit" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Secrets in `.env` committed to the repository, then deleted in a later commit" appears in the output; or it is absent by accident, with nothing in `security-audit` having ruled it out
```

## Case 17 — Avoids: Logging the full request body on an auth endpoint

```text
GIVEN    A situation that invites the anti-pattern "Logging the full request body on an auth endpoint"
WHEN     the agent applies `security-audit` in that situation
THEN     "Logging the full request body on an auth endpoint" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Logging the full request body on an auth endpoint" appears in the output; or it is absent by accident, with nothing in `security-audit` having ruled it out
```

## Case 18 — Avoids: An agent with `shell: true` and no allowlist,

```text
GIVEN    A situation that invites the anti-pattern "An agent with `shell: true` and no allowlist, triggered by inbound email content"
WHEN     the agent applies `security-audit` in that situation
THEN     "An agent with `shell: true` and no allowlist, triggered by inbound email content" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "An agent with `shell: true` and no allowlist, triggered by inbound email content" appears in the output; or it is absent by accident, with nothing in `security-audit` having ruled it out
```

## Case 19 — Avoids: A wildcard CORS origin combined with credentialed requests

```text
GIVEN    A situation that invites the anti-pattern "A wildcard CORS origin combined with credentialed requests"
WHEN     the agent applies `security-audit` in that situation
THEN     "A wildcard CORS origin combined with credentialed requests" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A wildcard CORS origin combined with credentialed requests" appears in the output; or it is absent by accident, with nothing in `security-audit` having ruled it out
```

## Case 20 — Avoids: "We use a framework, so injection is impossible"

```text
GIVEN    A situation that invites the anti-pattern "We use a framework, so injection is impossible"
WHEN     the agent applies `security-audit` in that situation
THEN     "We use a framework, so injection is impossible" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "We use a framework, so injection is impossible" appears in the output; or it is absent by accident, with nothing in `security-audit` having ruled it out
```

## Case 21 — Avoids: Vendoring a leaked system prompt as a research reference

```text
GIVEN    A situation that invites the anti-pattern "Vendoring a leaked system prompt as a research reference"
WHEN     the agent applies `security-audit` in that situation
THEN     "Vendoring a leaked system prompt as a research reference" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Vendoring a leaked system prompt as a research reference" appears in the output; or it is absent by accident, with nothing in `security-audit` having ruled it out
```
