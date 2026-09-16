# Test cases — `prompt-injection-defense`

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
GIVEN    A task inside this skill's stated purpose: Design so that a successful injection cannot do much. A model has one channel — tokens in, tokens out — so instructions and data are processed by the same mechanism and cannot be reliably separated.
WHEN     the agent executes `prompt-injection-defense` end to end on that task
THEN     the workflow runs in its stated order — "ANSWER THE BLAST-RADIUS QUESTION FIRST" through to "TEST IT"; and before delivery these specific conditions hold: "the blast-radius question was answered per tool, in writing"; "tool arguments are validated against a schema and policy before execution"; "adversarial injection cases are in the evaluation suite and pass"
FAIL IF  "the blast-radius question was answered per tool, in writing" is false, or "adversarial injection cases are in the evaluation suite and pass" is false, or the result is delivered before "TEST IT" has run
```

## Case 2 — Declines: The model has no tools and no access to private data.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The model has no tools and no access to private data.
WHEN     the agent considers `prompt-injection-defense` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Then the worst outcome is a wrong or embarrassing answer — handle it with output policy and abuse tooling, not this skill."
FAIL IF  the skill is run on a task where "The model has no tools and no access to private data.", and the consequence that exclusion states follows — "Then the worst outcome is a wrong or embarrassing answer — handle it with output policy and abuse tooling, not this skill."; or `prompt-injection-defense` is declined without naming that exclusion
```

## Case 3 — Declines: The proposal is a denylist, a keyword filter or a hardened system prompt as…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The proposal is a denylist, a keyword filter or a hardened system prompt as the primary control.
WHEN     the agent considers `prompt-injection-defense` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Those are likelihood reductions and are evadable; the structural controls come first."
FAIL IF  the skill is run on a task where "The proposal is a denylist, a keyword filter or a hardened system prompt as the primary control.", and the consequence that exclusion states follows — "Those are likelihood reductions and are evadable; the structural controls come first."; or `prompt-injection-defense` is declined without naming that exclusion
```

## Case 4 — Declines: The system processes only trusted, first-party content with no external…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The system processes only trusted, first-party content with no external ingestion.
WHEN     the agent considers `prompt-injection-defense` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Re-check this assumption: a user's own uploaded document is untrusted content."
FAIL IF  the skill is run on a task where "The system processes only trusted, first-party content with no external ingestion.", and the consequence that exclusion states follows — "Re-check this assumption: a user's own uploaded document is untrusted content."; or `prompt-injection-defense` is declined without naming that exclusion
```

## Case 5 — Declines: The task is red-teaming for disclosure purposes on a system you do not own or…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The task is red-teaming for disclosure purposes on a system you do not own or are not authorised to test.
WHEN     the agent considers `prompt-injection-defense` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "That is prohibited."
FAIL IF  the skill is run on a task where "The task is red-teaming for disclosure purposes on a system you do not own or are not authorised to test.", and the consequence that exclusion states follows — "That is prohibited."; or `prompt-injection-defense` is declined without naming that exclusion
```

## Case 6 — Detects: Worst case is unacceptable

```text
GIVEN    A run of this skill in which the known failure mode is present: Worst case is unacceptable
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "a tool can delete, send or pay without a gate" — and the response applied is the documented one: "remove the capability or add an external gate; do not proceed"
FAIL IF  "Worst case is unacceptable" reaches the output because "a tool can delete, send or pay without a gate" was never checked; or it is caught but the response taken is not "remove the capability or add an external gate; do not proceed"
```

## Case 7 — Detects: Gate is inside the model

```text
GIVEN    A run of this skill in which the known failure mode is present: Gate is inside the model
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "approval depends on the model deciding to ask" — and the response applied is the documented one: "move the gate to a wrapper or policy engine"
FAIL IF  "Gate is inside the model" reaches the output because "approval depends on the model deciding to ask" was never checked; or it is caught but the response taken is not "move the gate to a wrapper or policy engine"
```

## Case 8 — Detects: Standing admin credential

```text
GIVEN    A run of this skill in which the known failure mode is present: Standing admin credential
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "one token for everything" — and the response applied is the documented one: "scope per task, short-lived"
FAIL IF  "Standing admin credential" reaches the output because "one token for everything" was never checked; or it is caught but the response taken is not "scope per task, short-lived"
```

## Case 9 — Detects: Fence treated as a boundary

```text
GIVEN    A run of this skill in which the known failure mode is present: Fence treated as a boundary
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the prompt says to ignore instructions in content" — and the response applied is the documented one: "keep it, and stop relying on it; add steps 2, 3, 6"
FAIL IF  "Fence treated as a boundary" reaches the output because "the prompt says to ignore instructions in content" was never checked; or it is caught but the response taken is not "keep it, and stop relying on it; add steps 2, 3, 6"
```

## Case 10 — Detects: Exfiltration path unnoticed

```text
GIVEN    A run of this skill in which the known failure mode is present: Exfiltration path unnoticed
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "read tool plus send tool both granted" — and the response applied is the documented one: "review the pair; restrict the send side"
FAIL IF  "Exfiltration path unnoticed" reaches the output because "read tool plus send tool both granted" was never checked; or it is caught but the response taken is not "review the pair; restrict the send side"
```

## Case 11 — Detects: Memory write unprotected

```text
GIVEN    A run of this skill in which the known failure mode is present: Memory write unprotected
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "injected content persisted" — and the response applied is the documented one: "add write-path review"
FAIL IF  "Memory write unprotected" reaches the output because "injected content persisted" was never checked; or it is caught but the response taken is not "add write-path review"
```

## Case 12 — Detects: No action budget

```text
GIVEN    A run of this skill in which the known failure mode is present: No action budget
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "a loop issued thousands of calls" — and the response applied is the documented one: "add budgets, backoff, a breaker"
FAIL IF  "No action budget" reaches the output because "a loop issued thousands of calls" was never checked; or it is caught but the response taken is not "add budgets, backoff, a breaker"
```

## Case 13 — Detects: Cannot reconstruct the incident

```text
GIVEN    A run of this skill in which the known failure mode is present: Cannot reconstruct the incident
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no per-call log" — and the response applied is the documented one: "logging is the missing control and the cheapest one"
FAIL IF  "Cannot reconstruct the incident" reaches the output because "no per-call log" was never checked; or it is caught but the response taken is not "logging is the missing control and the cheapest one"
```

## Case 14 — Detects: Tests pass, adversarial cases absent

```text
GIVEN    A run of this skill in which the known failure mode is present: Tests pass, adversarial cases absent
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "evaluation suite has no injection tasks" — and the response applied is the documented one: "add them with known correct behaviour"
FAIL IF  "Tests pass, adversarial cases absent" reaches the output because "evaluation suite has no injection tasks" was never checked; or it is caught but the response taken is not "add them with known correct behaviour"
```

## Case 15 — Avoids: SYSTEM-PROMPT HARDENING AS THE ONLY CONTROL

```text
GIVEN    A situation that invites the anti-pattern "SYSTEM-PROMPT HARDENING AS THE ONLY CONTROL", whose stated consequence is: Instruction-following is the exploited capability; the same mechanism makes the mitigation unreliable.
WHEN     the agent applies `prompt-injection-defense` in that situation
THEN     "SYSTEM-PROMPT HARDENING AS THE ONLY CONTROL" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Instruction-following is the exploited capability; the same mechanism makes the mitigation unreliable."
FAIL IF  "SYSTEM-PROMPT HARDENING AS THE ONLY CONTROL" appears in the output — that is, "Instruction-following is the exploited capability; the same mechanism makes the mitigation unreliable."; or it is absent by accident, with nothing in `prompt-injection-defense` having ruled it out
```

## Case 16 — Avoids: DENYLISTS AND KEYWORD FILTERS

```text
GIVEN    A situation that invites the anti-pattern "DENYLISTS AND KEYWORD FILTERS", whose stated consequence is: Evaded by paraphrase, translation, encoding, images, or splitting a payload across two tool results.
WHEN     the agent applies `prompt-injection-defense` in that situation
THEN     "DENYLISTS AND KEYWORD FILTERS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Evaded by paraphrase, translation, encoding, images, or splitting a payload across two tool results. Automated suffix attacks make hand-written lists obsolete before they ship."
FAIL IF  "DENYLISTS AND KEYWORD FILTERS" appears in the output — that is, "Evaded by paraphrase, translation, encoding, images, or splitting a payload across two tool results."; or it is absent by accident, with nothing in `prompt-injection-defense` having ruled it out
```

## Case 17 — Avoids: ASKING THE MODEL IF IT IS SAFE TO PROCEED

```text
GIVEN    A situation that invites the anti-pattern "ASKING THE MODEL IF IT IS SAFE TO PROCEED", whose stated consequence is: The component under attack is the component being asked.
WHEN     the agent applies `prompt-injection-defense` in that situation
THEN     "ASKING THE MODEL IF IT IS SAFE TO PROCEED" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The component under attack is the component being asked."
FAIL IF  "ASKING THE MODEL IF IT IS SAFE TO PROCEED" appears in the output — that is, "The component under attack is the component being asked."; or it is absent by accident, with nothing in `prompt-injection-defense` having ruled it out
```

## Case 18 — Avoids: A GUARD MODEL AS THE ONLY CONTROL

```text
GIVEN    A situation that invites the anti-pattern "A GUARD MODEL AS THE ONLY CONTROL", whose stated consequence is: Useful as a signal; still probabilistic, and now also injectable.
WHEN     the agent applies `prompt-injection-defense` in that situation
THEN     "A GUARD MODEL AS THE ONLY CONTROL" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Useful as a signal; still probabilistic, and now also injectable."
FAIL IF  "A GUARD MODEL AS THE ONLY CONTROL" appears in the output — that is, "Useful as a signal; still probabilistic, and now also injectable."; or it is absent by accident, with nothing in `prompt-injection-defense` having ruled it out
```

## Case 19 — Avoids: TRUSTING A TOOL'S DOCUMENTED CAPABILITIES

```text
GIVEN    A situation that invites the anti-pattern "TRUSTING A TOOL'S DOCUMENTED CAPABILITIES", whose stated consequence is: Enumerate the runtime surface and diff it on upgrade.
WHEN     the agent applies `prompt-injection-defense` in that situation
THEN     "TRUSTING A TOOL'S DOCUMENTED CAPABILITIES" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Enumerate the runtime surface and diff it on upgrade."
FAIL IF  "TRUSTING A TOOL'S DOCUMENTED CAPABILITIES" appears in the output — that is, "Enumerate the runtime surface and diff it on upgrade."; or it is absent by accident, with nothing in `prompt-injection-defense` having ruled it out
```

## Case 20 — Avoids: "IT ONLY READS, SO IT IS SAFE." Read plus send is exfiltration

```text
GIVEN    A situation that invites the anti-pattern "IT ONLY READS, SO IT IS SAFE." Read plus send is exfiltration"
WHEN     the agent applies `prompt-injection-defense` in that situation
THEN     "IT ONLY READS, SO IT IS SAFE." Read plus send is exfiltration" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "IT ONLY READS, SO IT IS SAFE." Read plus send is exfiltration" appears in the output; or it is absent by accident, with nothing in `prompt-injection-defense` having ruled it out
```

## Case 21 — Avoids: DESIGNING FOR PREVENTION ONLY

```text
GIVEN    A situation that invites the anti-pattern "DESIGNING FOR PREVENTION ONLY", whose stated consequence is: Assume success and design the blast radius; prevention-only designs fail completely the first time they fail.
WHEN     the agent applies `prompt-injection-defense` in that situation
THEN     "DESIGNING FOR PREVENTION ONLY" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Assume success and design the blast radius; prevention-only designs fail completely the first time they fail."
FAIL IF  "DESIGNING FOR PREVENTION ONLY" appears in the output — that is, "Assume success and design the blast radius; prevention-only designs fail completely the first time they fail."; or it is absent by accident, with nothing in `prompt-injection-defense` having ruled it out
```

## Case 22 — Avoids: NO TESTS

```text
GIVEN    A situation that invites the anti-pattern "NO TESTS", whose stated consequence is: A defence nobody has attacked is a hypothesis.
WHEN     the agent applies `prompt-injection-defense` in that situation
THEN     "NO TESTS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A defence nobody has attacked is a hypothesis."
FAIL IF  "NO TESTS" appears in the output — that is, "A defence nobody has attacked is a hypothesis."; or it is absent by accident, with nothing in `prompt-injection-defense` having ruled it out
```
