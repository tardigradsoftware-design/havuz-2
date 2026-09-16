# Test cases — `skill-authoring`

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
GIVEN    A task inside this skill's stated purpose: Write a skill that an agent can execute under context pressure. A skill is a procedure, not an essay: it states when to use it, when not to, what it needs, what it does,
WHEN     the agent executes `skill-authoring` end to end on that task
THEN     the workflow runs in its stated order — "NAME IT FOR THE PROCEDURE, NOT THE DOMAIN" through to "RECORD PROVENANCE"; and before delivery these specific conditions hold: "the name describes a procedure, not a domain"; "the quality checklist is the exit gate and is checkable"; "both validators pass with zero errors"
FAIL IF  "the name describes a procedure, not a domain" is false, or "both validators pass with zero errors" is false, or the result is delivered before "RECORD PROVENANCE" has run
```

## Case 2 — Declines: The content is a fact, a reference or an explanation.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The content is a fact, a reference or an explanation.
WHEN     the agent considers `skill-authoring` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "That is a knowledge article, not a skill."
FAIL IF  the skill is run on a task where "The content is a fact, a reference or an explanation.", and the consequence that exclusion states follows — "That is a knowledge article, not a skill."; or `skill-authoring` is declined without naming that exclusion
```

## Case 3 — Declines: The procedure has two independent halves.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The procedure has two independent halves.
WHEN     the agent considers `skill-authoring` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "That is two skills joined by requires, or a workflow."
FAIL IF  the skill is run on a task where "The procedure has two independent halves.", and the consequence that exclusion states follows — "That is two skills joined by requires, or a workflow."; or `skill-authoring` is declined without naming that exclusion
```

## Case 4 — Declines: Nobody has performed the procedure.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Nobody has performed the procedure.
WHEN     the agent considers `skill-authoring` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Write it after doing it, or it will describe an intention."
FAIL IF  the skill is run on a task where "Nobody has performed the procedure.", and the consequence that exclusion states follows — "Write it after doing it, or it will describe an intention."; or `skill-authoring` is declined without naming that exclusion
```

## Case 5 — Declines: The only content is a checklist with no conditions for use.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The only content is a checklist with no conditions for use.
WHEN     the agent considers `skill-authoring` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Checklists belong inside a skill."
FAIL IF  the skill is run on a task where "The only content is a checklist with no conditions for use.", and the consequence that exclusion states follows — "Checklists belong inside a skill."; or `skill-authoring` is declined without naming that exclusion
```

## Case 6 — Detects: Named for a domain

```text
GIVEN    A run of this skill in which the known failure mode is present: Named for a domain
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "every task in that domain matches" — and the response applied is the documented one: "rename for the procedure"
FAIL IF  "Named for a domain" reaches the output because "every task in that domain matches" was never checked; or it is caught but the response taken is not "rename for the procedure"
```

## Case 7 — Detects: No negative case

```text
GIVEN    A run of this skill in which the known failure mode is present: No negative case
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the skill is applied to lookalike situations" — and the response applied is the documented one: "write "When NOT to Use" naming them"
FAIL IF  "No negative case" reaches the output because "the skill is applied to lookalike situations" was never checked; or it is caught but the response taken is not "write "When NOT to Use" naming them"
```

## Case 8 — Detects: Body over budget

```text
GIVEN    A run of this skill in which the known failure mode is present: Body over budget
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "validator warns above 135% of 2500 tokens" — and the response applied is the documented one: "move lookup material into references/"
FAIL IF  "Body over budget" reaches the output because "validator warns above 135% of 2500 tokens" was never checked; or it is caught but the response taken is not "move lookup material into references/"
```

## Case 9 — Detects: Steps are aspirations

```text
GIVEN    A run of this skill in which the known failure mode is present: Steps are aspirations
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no observable result per step" — and the response applied is the documented one: "rewrite each as action plus result"
FAIL IF  "Steps are aspirations" reaches the output because "no observable result per step" was never checked; or it is caught but the response taken is not "rewrite each as action plus result"
```

## Case 10 — Detects: High confidence, no sources

```text
GIVEN    A run of this skill in which the known failure mode is present: High confidence, no sources
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "validator warns" — and the response applied is the documented one: "add sources or downgrade confidence"
FAIL IF  "High confidence, no sources" reaches the output because "validator warns" was never checked; or it is caught but the response taken is not "add sources or downgrade confidence"
```

## Case 11 — Detects: estimated_tokens guessed

```text
GIVEN    A run of this skill in which the known failure mode is present: estimated_tokens guessed
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "drift warning" — and the response applied is the documented one: "set it to the measured value"
FAIL IF  "estimated_tokens guessed" reaches the output because "drift warning" was never checked; or it is caught but the response taken is not "set it to the measured value"
```

## Case 12 — Detects: Sections map missing

```text
GIVEN    A run of this skill in which the known failure mode is present: Sections map missing
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the loader cannot select a section" — and the response applied is the documented one: "add an entry per heading"
FAIL IF  "Sections map missing" reaches the output because "the loader cannot select a section" was never checked; or it is caught but the response taken is not "add an entry per heading"
```

## Case 13 — Detects: Two procedures in one file

```text
GIVEN    A run of this skill in which the known failure mode is present: Two procedures in one file
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the body needs "part A" and "part B" — and the response applied is the documented one: "split, and join with requires"
FAIL IF  "Two procedures in one file" reaches the output because "the body needs "part A" and "part B" was never checked; or it is caught but the response taken is not "split, and join with requires"
```

## Case 14 — Detects: Copied upstream content

```text
GIVEN    A run of this skill in which the known failure mode is present: Copied upstream content
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "license risk, and provenance is wrong" — and the response applied is the documented one: "summarise with attribution and link"
FAIL IF  "Copied upstream content" reaches the output because "license risk, and provenance is wrong" was never checked; or it is caught but the response taken is not "summarise with attribution and link"
```

## Case 15 — Detects: Not validated

```text
GIVEN    A run of this skill in which the known failure mode is present: Not validated
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "CI fails later" — and the response applied is the documented one: "run both validators before committing"
FAIL IF  "Not validated" reaches the output because "CI fails later" was never checked; or it is caught but the response taken is not "run both validators before committing"
```

## Case 16 — Avoids: AN ESSAY WITH A FRONTMATTER

```text
GIVEN    A situation that invites the anti-pattern "AN ESSAY WITH A FRONTMATTER", whose stated consequence is: Explanatory prose an agent must interpret rather than execute.
WHEN     the agent applies `skill-authoring` in that situation
THEN     "AN ESSAY WITH A FRONTMATTER" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Explanatory prose an agent must interpret rather than execute."
FAIL IF  "AN ESSAY WITH A FRONTMATTER" appears in the output — that is, "Explanatory prose an agent must interpret rather than execute."; or it is absent by accident, with nothing in `skill-authoring` having ruled it out
```

## Case 17 — Avoids: DOMAIN-NAMED SKILLS

```text
GIVEN    A situation that invites the anti-pattern "DOMAIN-NAMED SKILLS", whose stated consequence is: Unselectable, because everything matches.
WHEN     the agent applies `skill-authoring` in that situation
THEN     "DOMAIN-NAMED SKILLS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Unselectable, because everything matches."
FAIL IF  "DOMAIN-NAMED SKILLS" appears in the output — that is, "Unselectable, because everything matches."; or it is absent by accident, with nothing in `skill-authoring` having ruled it out
```

## Case 18 — Avoids: OMITTING THE NEGATIVE CASE

```text
GIVEN    A situation that invites the anti-pattern "OMITTING THE NEGATIVE CASE", whose stated consequence is: The skill gets applied everywhere and fails where it should not have been used.
WHEN     the agent applies `skill-authoring` in that situation
THEN     "OMITTING THE NEGATIVE CASE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The skill gets applied everywhere and fails where it should not have been used."
FAIL IF  "OMITTING THE NEGATIVE CASE" appears in the output — that is, "The skill gets applied everywhere and fails where it should not have been used."; or it is absent by accident, with nothing in `skill-authoring` having ruled it out
```

## Case 19 — Avoids: ONE GIANT FILE

```text
GIVEN    A situation that invites the anti-pattern "ONE GIANT FILE", whose stated consequence is: Defeats progressive disclosure; an agent loads 6,000 tokens to use 1,500.
WHEN     the agent applies `skill-authoring` in that situation
THEN     "ONE GIANT FILE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Defeats progressive disclosure; an agent loads 6,000 tokens to use 1,500."
FAIL IF  "ONE GIANT FILE" appears in the output — that is, "Defeats progressive disclosure; an agent loads 6,000 tokens to use 1,500."; or it is absent by accident, with nothing in `skill-authoring` having ruled it out
```

## Case 20 — Avoids: UNDATED

```text
GIVEN    A situation that invites the anti-pattern "UNDATED", whose stated consequence is: No verified_at or expires_at means it will be trusted forever. See the freshness policy.
WHEN     the agent applies `skill-authoring` in that situation
THEN     "UNDATED" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "No verified_at or expires_at means it will be trusted forever. See the freshness policy."
FAIL IF  "UNDATED" appears in the output — that is, "No verified_at or expires_at means it will be trusted forever. See the freshness policy."; or it is absent by accident, with nothing in `skill-authoring` having ruled it out
```

## Case 21 — Avoids: UNSOURCED CONFIDENCE

```text
GIVEN    A situation that invites the anti-pattern "UNSOURCED CONFIDENCE", whose stated consequence is: "high" with nothing behind it is a claim about the author's certainty.
WHEN     the agent applies `skill-authoring` in that situation
THEN     "UNSOURCED CONFIDENCE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "high" with nothing behind it is a claim about the author's certainty."
FAIL IF  "UNSOURCED CONFIDENCE" appears in the output — that is, "high" with nothing behind it is a claim about the author's certainty."; or it is absent by accident, with nothing in `skill-authoring` having ruled it out
```

## Case 22 — Avoids: COPYING AN UPSTREAM COLLECTION

```text
GIVEN    A situation that invites the anti-pattern "COPYING AN UPSTREAM COLLECTION", whose stated consequence is: Several have no license; and a copy loses the reasoning that made the original work.
WHEN     the agent applies `skill-authoring` in that situation
THEN     "COPYING AN UPSTREAM COLLECTION" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Several have no license; and a copy loses the reasoning that made the original work."
FAIL IF  "COPYING AN UPSTREAM COLLECTION" appears in the output — that is, "Several have no license; and a copy loses the reasoning that made the original work."; or it is absent by accident, with nothing in `skill-authoring` having ruled it out
```

## Case 23 — Avoids: NO FAILURE MODES

```text
GIVEN    A situation that invites the anti-pattern "NO FAILURE MODES", whose stated consequence is: The agent cannot self-diagnose, so it retries the same failing approach.
WHEN     the agent applies `skill-authoring` in that situation
THEN     "NO FAILURE MODES" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The agent cannot self-diagnose, so it retries the same failing approach."
FAIL IF  "NO FAILURE MODES" appears in the output — that is, "The agent cannot self-diagnose, so it retries the same failing approach."; or it is absent by accident, with nothing in `skill-authoring` having ruled it out
```

## Case 24 — Avoids: GUESSED TOKEN COUNTS

```text
GIVEN    A situation that invites the anti-pattern "GUESSED TOKEN COUNTS", whose stated consequence is: The loader budgets on this number; a wrong one defeats the design.
WHEN     the agent applies `skill-authoring` in that situation
THEN     "GUESSED TOKEN COUNTS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The loader budgets on this number; a wrong one defeats the design."
FAIL IF  "GUESSED TOKEN COUNTS" appears in the output — that is, "The loader budgets on this number; a wrong one defeats the design."; or it is absent by accident, with nothing in `skill-authoring` having ruled it out
```
