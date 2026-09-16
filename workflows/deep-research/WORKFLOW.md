---
name: deep-research
version: 1.0.0
trigger: >-
  A question arrives whose answer will drive an engineering, architectural or adoption decision,
  where the cost of being confidently wrong exceeds the cost of researching it properly — technology
  selection, vendor or library evaluation, state-of-practice questions, regulatory or protocol
  questions, and any question where sources are known or likely to conflict.
description: >-
  Answer a research question with a graded, cited evidence set rather than an impression. Retrieval,
  verification, gap analysis and synthesis run as a loop that stops on a stated saturation condition,
  and every claim leaves the loop carrying its type, evidence level, confidence and the source that
  was actually reached.
not_for:
  - "A lookup with one authoritative answer and no conflicting sources — retrieve it and cite it; the loop is overhead."
  - "A question nobody will act on. Research without a decision produces a document, not an answer."
  - "A question about this codebase. Read the code; the repository is the primary source."
  - "Anything requiring leaked, extracted or improperly obtained material. Refuse — see the exclusion policy."
  - "A creative or generative task. There is no evidence set to converge on."
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [research, verification, evidence, citations, workflow, synthesis, conflict-resolution]
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
estimated_duration: 45-240 minutes, driven by the number of sub-questions and the depth of verification
estimated_tokens: 1400
stages:
  - id: 1
    name: Scope the question
    exit_gate: >-
      The sub-question list exists, each sub-question names the source type that would settle it and what counts as sufficient evidence, and the decision, constraints and budget are all recorded.
    goal: >-
      Convert the question into 3-7 individually answerable sub-questions, each with the kind of
      source that would settle it and what would count as sufficient evidence. Record the decision the
      answer will inform, the constraints, and what is already established.
    skill: web-research
    agent: researcher
    inputs:
      - the question as asked
      - the decision it informs
      - "constraints: version, platform, budget, jurisdiction, deadline"
      - what is already established, so it is not re-derived
    outputs:
      - a sub-question list with the evidence standard for each
      - "a stated budget: maximum retrieval rounds or iterations"
      - an explicit note of anything out of scope
    max_loops: 1
    on_gate_failure: >-
      Return to the requester. A question that cannot be decomposed into checkable sub-questions is
      not yet a research question, and researching it will produce volume rather than an answer.
  - id: 2
    name: Retrieve for primary sources
    exit_gate: >-
      Every sub-question has at least one source that was reached directly, and the source register records url, publisher, date, version and the reached-directly flag for each.
    goal: >-
      For each sub-question, reach the source that mints the fact — the specification, the official
      documentation for the exact version, the repository, the paper, the vendor's own page. Secondary
      sources are leads to primary ones, never substitutes. Record for every source: URL, publisher,
      date, the version it describes, and whether it was reached directly.
    skill: web-research
    agent: researcher
    inputs:
      - the sub-question list with its evidence standards
      - repository metadata for any repository under consideration
    outputs:
      - "a source register: url, publisher, date, version, reached-directly flag"
      - the raw findings per sub-question, attributed to a specific source
    max_loops: 3
    on_gate_failure: >-
      If a sub-question has only secondary sources after the loop budget, mark it single-sourced or
      UNVERIFIED and continue. Do not promote a secondary source to primary by re-labelling it.
  - id: 3
    name: Verify identity, date and standing
    exit_gate: >-
      Every source in the register has an identity confirmation and a verified_at date, its recency has been judged against the claim's shelf life, and anything unverifiable has been quarantined as UNVERIFIED rather than carried forward.
    goal: >-
      Confirm each source is what it appears to be — title, authors or publisher, identifier, version,
      date — then judge its date against the claim's shelf life rather than the source's prestige, and
      check its standing: authority, lifecycle status, license, self-interest.
    skill: evidence-validation
    agent: fact-checker
    inputs:
      - the source register
      - the freshness windows per claim class
      - the scoring rules and their hard overrides
    outputs:
      - a per-source verification record with a verified_at date
      - lifecycle and license findings for any repository involved
      - a list of sources that could not be verified, quarantined rather than deleted
    max_loops: 2
    on_gate_failure: >-
      Quarantine the unverifiable material as UNVERIFIED, exclude it from the active evidence set, and
      record what would make it gradeable. An unverifiable claim is not a weak claim; it is not a claim.
  - id: 4
    name: Extract graded claims
    exit_gate: >-
      Every finding appears in the claim table as a single checkable claim with claim_type, evidence_level, confidence, and the specific source that supports that claim. Nothing rests on a trailing reference list.
    goal: >-
      Rewrite each finding as a single checkable claim and tag it: claim_type (fact, recommendation,
      experiment, opinion, hypothesis), evidence_level, confidence. Attach the specific source that
      supports THAT claim — a reference list at the end of a report supports nothing.
    skill: research-synthesis
    agent: researcher
    inputs:
      - the verified findings
      - the claim taxonomy and evidence levels
    outputs:
      - "a claim table: claim, type, evidence level, confidence, supporting sources, verified_at"
      - a flag on every claim that rests on a single source
    max_loops: 2
    on_gate_failure: >-
      A finding that cannot be written as a checkable claim is not a finding. Return it to the retrieve
      stage with the specific gap named, or drop it with a note.
  - id: 5
    name: Seek independent corroboration
    exit_gate: >-
      Every load-bearing claim has either an independent second source with the independence judgement stated, or an explicit single-sourced flag with confidence capped at medium.
    goal: >-
      For every claim that will carry weight in the decision, find a second source with different
      provenance. Different provenance, not a different URL: three blogs restating one changelog are
      one source. Record where corroboration does not exist — single-sourced is a finding, not a
      defect to hide.
    skill: evidence-validation
    agent: fact-checker
    inputs:
      - the claim table with its single-source flags
      - the decision, to determine which claims carry weight
    outputs:
      - corroboration status per load-bearing claim, with the independence judgement stated
      - an updated confidence for any claim that remains single-sourced
    max_loops: 2
    on_gate_failure: >-
      Cap confidence at medium for any load-bearing claim that remains single-sourced, and say so in the
      report. Do not raise confidence because the claim is plausible or because it was repeated.
  - id: 6
    name: Resolve conflicts by precedence
    exit_gate: >-
      Every disagreement between sources appears in the conflict register with the precedence rule applied, what was relied on, and what would settle it. No minority view has been dropped.
    goal: >-
      Where sources disagree, apply the precedence order — primary source reached directly, official
      documentation, peer-reviewed research, independent corroboration, reputable secondary analysis,
      community sources, and unsourced model output last, labelled GENERATED. Equal rank with genuine
      disagreement is a conflict: record both, state which was relied on and why, and say what would
      settle it.
    skill: evidence-validation
    agent: fact-checker
    inputs:
      - the claim table and the source register
      - the precedence order
    outputs:
      - "a conflict register: the sources, what each says, the rule applied, what was relied on, and what would settle it"
      - a check that no minority view was silently dropped
    max_loops: 2
    on_gate_failure: >-
      Escalate the conflict as unresolved. An unresolved conflict reported honestly is a usable answer;
      one silently resolved in favour of the more convenient source is not.
  - id: 7
    name: Self-critique the evidence set
    exit_gate: >-
      The critique record answers each of the five attack questions, and every gap that matters to the decision has either been closed by further retrieval or is listed as unresolved.
    goal: >-
      Attack the evidence set before synthesising: which claim would change the decision if it were
      wrong, and is it the best-verified one; where is the reliance on a single source; what was not
      looked for because it would have been inconvenient; which claim is really an inference dressed as
      a finding; what would a competent dissenter point to.
    skill: reasoning-strategies
    agent: researcher
    inputs:
      - the claim table, conflict register and corroboration status
    outputs:
      - a critique record with the answers to each question
      - additional retrieval tasks for any gap that matters to the decision
    max_loops: 2
    on_gate_failure: >-
      If the critique produces no gaps on a non-trivial question, it was not a critique. Re-run it
      against the specific decision rather than the general topic.
  - id: 8
    name: Stop on saturation, not on exhaustion
    exit_gate: >-
      The stopping condition is recorded as either saturation (two rounds that changed nothing) or budget exhaustion, and what remains unresolved is listed.
    goal: >-
      Stop when two consecutive retrieval rounds add no claim that changes the answer or its confidence,
      or when the budget is reached. Record which condition stopped the loop, and what remains
      unresolved. An incomplete answer with a stated gap is usable; a complete answer with unstated gaps
      is not.
    skill: research-synthesis
    agent: researcher
    inputs:
      - the retrieval log and the budget
    outputs:
      - the stopping condition that was met, with evidence for it
      - the list of what remains unresolved and why
    max_loops: 1
    on_gate_failure: >-
      If neither condition is met and the budget is exhausted, stop anyway and report the budget as the
      reason. Running past budget produces volume, not confidence.
  - id: 9
    name: Synthesise and report
    exit_gate: >-
      The report contains all seven parts including a non-empty UNKNOWN section, the answer addresses the stated decision, and a recommendation is given or its absence is justified by the evidence.
    goal: >-
      Produce the report: the answer with an overall confidence and its largest caveat; the answer
      against each stated constraint; the claim table; the conflict register; the UNKNOWN section; the
      method actually followed including dead ends and deviations; and the recommendation restated
      against the decision. State the answer first and restate it last — attention over a long document
      is unevenly distributed.
    skill: research-synthesis
    agent: researcher
    inputs:
      - every artifact produced by the preceding stages
    outputs:
      - the research report in the seven-part structure
      - a recommendation, or an explicit statement that the evidence does not support one and what would
    max_loops: 2
    on_gate_failure: >-
      If the report cannot state what would change the recommendation, the analysis has not identified
      its own load-bearing assumptions. Return to the critique stage.
quality_gates:
  - gate: every claim has a source that was actually reached and that supports that specific claim
    checked_by: fact-checker
    on_failure: the claim is downgraded to UNVERIFIED or removed; it is not left in with a citation that does not support it
  - gate: no conflict was silently resolved
    checked_by: fact-checker
    on_failure: restore the minority view to the conflict register with the precedence reasoning
  - gate: confidence matches the evidence level actually achieved
    checked_by: fact-checker
    on_failure: downgrade the confidence; never upgrade the evidence level to match the confidence
  - gate: recency was judged against the claim's shelf life, not the source's prestige
    checked_by: fact-checker
    on_failure: re-window the claim, re-verify it, or mark it stale
  - gate: the UNKNOWN section is present and non-empty, or explains why nothing is unknown
    checked_by: researcher
    on_failure: the report is not deliverable; a report with no unknowns on a hard question did not look
  - gate: the answer addresses the stated decision, not a broader or more convenient question
    checked_by: researcher
    on_failure: re-answer the question asked, or state explicitly why it cannot be answered as asked
  - gate: nothing relies on excluded material
    checked_by: fact-checker
    on_failure: remove it and record the exclusion; public reachability is not permission
artifacts:
  - the research report, in the seven-part structure
  - the claim table with per-claim provenance
  - the source register with reached-directly and verified_at flags
  - the conflict register
  - the critique record
  - the retrieval log, including dead ends
  - new knowledge articles or corrections for anything durable discovered
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related:
  - knowledge/research/verification-workflow.md
  - knowledge/research/source-conflict-case-study.md
  - knowledge/ai-engineering/source-scoring.md
  - knowledge/ai-engineering/freshness-policy.md
  - prompts/research/deep-research-loop.md
  - workflows/research-before-coding/WORKFLOW.md
sources:
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    url: https://arxiv.org/abs/2307.03172
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Attention over long input is unevenly distributed — the reason the synthesise stage states the answer first and restates it last, and why the claim table exists as a compact structure rather than as prose."
  - title: "arXiv:2201.11903 — Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    url: https://arxiv.org/abs/2201.11903
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Verified against the primary source on 2026-09-15 (v6, 2023-01-10). One of two identifiers an aggregator returned a wrong title for, which is the empirical basis for the verify stage's identity check."
---

# Deep Research

```text
  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
  │ 1 SCOPE  │──▶│2 RETRIEVE│──▶│3 VERIFY  │──▶│4 EXTRACT │
  └──────────┘   └────▲─────┘   └──────────┘   └────┬─────┘
       │              │                              │
       │              │        ┌──────────────┐      ▼
       │              └────────│ 7 CRITIQUE   │  ┌──────────┐
       │   gaps found          └──────▲───────┘  │5 CORROB- │
       │                              │          │  ORATE   │
       │                       ┌──────┴───────┐  └────┬─────┘
       │                       │ 6 RESOLVE    │◀──────┘
       │                       │   CONFLICTS  │
       │                       └──────────────┘
       ▼
  ┌──────────┐   ┌────────────┐
  │ 8 STOP   │──▶│9 SYNTHESISE│──▶  report + claim table + conflict register
  └──────────┘   └────────────┘
```

## Key principles

```text
1. DECOMPOSE BEFORE RETRIEVING.   Retrieval against an undecomposed question returns whatever the
   search engine favours. Sub-questions make the gap visible before it is filled.
2. PRIMARY OVER SECONDARY, ALWAYS. A secondary source inherits the errors of its primary and adds its
   own. Identity is checked because aggregators demonstrably return wrong metadata for valid
   identifiers.
3. PROVENANCE PER CLAIM, NOT PER DOCUMENT.  A trailing reference list is decoration. Each claim names
   the source that supports it, so the support can be checked.
4. SHELF LIFE IS A PROPERTY OF THE CLAIM.  A 2019 complexity result is current; a 2024 post on
   framework defaults is already suspect. Prestige does not confer durability.
5. INDEPENDENCE MEANS DIFFERENT PROVENANCE.  Restatement chains are the commonest false corroboration
   and the reason a source count is not a confidence level.
6. CONFLICTS ARE RECORDED, NOT HIDDEN.  Suppressing the minority view destroys what a later reader
   needs in order to re-decide, and hides that a decision was made under uncertainty.
7. PERMISSION TO NOT KNOW.  A required UNKNOWN section is what makes the rest of the output
   trustworthy. A report with no unknowns on a hard question is a report that did not look.
8. STOP ON SATURATION.  Two rounds that change nothing is the stopping rule; exhaustion of interest is
   not, and cannot be audited.
9. EXCLUSIONS APPLY REGARDLESS OF POPULARITY.  Leaked or improperly obtained material is refused at any
   star count. Popularity does not launder provenance.
```

## Scaling the workflow

| Question shape | Stages | Retrieval rounds | Typical effort |
|---|---|---|---|
| Single sub-question, one authoritative source | 1, 2, 3, 9 | 1 | 15-30 min |
| Technology selection, 3-5 sub-questions | all nine | 2-3 | 1-2 h |
| Contested or fast-moving topic | all nine, critique looped | 3+ | 2-4 h |
| Multi-vendor or multi-framework comparison | all nine, plus the decision-matrix template | 3+ | half a day |
| Regulatory, protocol or specification question | all nine, verify looped until the exact clause is reached | 2 | 1-3 h |

The retrieve → verify → extract → corroborate → resolve → critique cycle repeats as a whole when the
critique stage finds a gap that matters. It does not repeat per sub-question; the evidence set is
critiqued as a set, because gaps are usually comparative.

## Failure modes

| Failure | Stage | Detection | Response |
|---|---|---|---|
| Retrieval before decomposition | scope | the sub-question list is missing or was written after the sources | return to scope; discard nothing, but re-derive the list first |
| Secondary sources cited as primary | retrieve, verify | the reached-directly flag is false, or the document does not match its description | reach the primary source or mark the claim single-sourced and cap confidence |
| Wrong document behind a valid identifier | verify | title, authors or version do not match the identifier | the primary source wins; record the conflict and the aggregator as unreliable for that field |
| Date judged by prestige | verify | a specification is flagged stale, or a framework default is treated as durable | re-window against the claim class |
| Claim without a supporting source | extract | the claim table row has no source, or the source does not support that row | downgrade to UNVERIFIED or remove |
| Restatement counted as corroboration | corroborate | two sources share a provenance | count them as one; cap confidence |
| Conflict resolved silently | resolve | the minority view is absent from the report | restore it with the precedence reasoning |
| No critique, or a critique that finds nothing | critique | no gaps on a non-trivial question | re-run against the specific decision rather than the topic |
| Loop stopped on exhaustion | stop | no saturation condition recorded | stop and report the budget as the reason |
| Report with no UNKNOWN section | synthesise | the section is missing or empty without justification | not deliverable |
| Answer to a different question | synthesise | the recommendation does not address the stated decision | re-answer, or state why the question cannot be answered as asked |
| Excluded material used | any | a source matches the exclusion list | remove it and record the exclusion |

## References

- [`prompts/research/deep-research-loop.md`](../../prompts/research/deep-research-loop.md) — the single-prompt form of this workflow
- [`knowledge/research/verification-workflow.md`](../../knowledge/research/verification-workflow.md) — the eight verification steps
- [`knowledge/research/source-conflict-case-study.md`](../../knowledge/research/source-conflict-case-study.md) — a real conflict resolved by this precedence rule
- [`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md) · [`freshness-policy.md`](../../knowledge/ai-engineering/freshness-policy.md) · [`verification-findings.md`](../../knowledge/ai-engineering/verification-findings.md)
- [`knowledge/security/llm-security/excluded-sources.md`](../../knowledge/security/llm-security/excluded-sources.md)
- [`skills/web-research/SKILL.md`](../../skills/web-research/SKILL.md) · [`skills/evidence-validation/SKILL.md`](../../skills/evidence-validation/SKILL.md) · [`skills/research-synthesis/SKILL.md`](../../skills/research-synthesis/SKILL.md) · [`skills/reasoning-strategies/SKILL.md`](../../skills/reasoning-strategies/SKILL.md) · [`skills/repository-analysis/SKILL.md`](../../skills/repository-analysis/SKILL.md)
- [`agents/researcher/AGENT.md`](../../agents/researcher/AGENT.md) · [`agents/fact-checker/AGENT.md`](../../agents/fact-checker/AGENT.md)
- [`workflows/research-before-coding/WORKFLOW.md`](../research-before-coding/WORKFLOW.md) — the code-facing variant
- [`decision-records/matrix-template.md`](../../decision-records/matrix-template.md) — when the research feeds a multi-option decision
