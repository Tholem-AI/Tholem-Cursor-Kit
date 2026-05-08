# Phase 3 Orchestration and Handoff Checklist

## Purpose

Define minimum orchestration and handoff requirements for RIPER/subagent v1 execution.

## Required Handoff Artifact

Each phase transition must include:
- phase completion summary,
- evidence and outputs produced,
- unresolved assumptions/conflicts,
- explicit next-phase entry criteria.

Planning handoff must additionally include Innovate checkpoint fields when applicable:
- `alternatives_considered`,
- `tradeoff_summary`,
- `selected_approach`,
- `rejected_options_reason`,
- `confidence_and_unknowns`.

For trivial changes, Planning may skip the checkpoint only with:
- `checkpoint_skipped: trivial_change`.

## Pass/Fail Checklist

### Pass criteria
- [ ] Handoff artifact exists for each phase transition.
- [ ] Handoff includes completed work and evidence links.
- [ ] Unresolved assumptions and conflicts are explicitly labeled.
- [ ] Next phase has explicit entry criteria and owner.
- [ ] Review checkpoint is visible before apply operations.
- [ ] Planning handoff includes Innovate checkpoint fields when applicable.
- [ ] Checkpoint skip, when used, is explicit and justified as trivial.

### Fail criteria
- [ ] Missing handoff artifact between phases.
- [ ] Outputs handed off without evidence mapping.
- [ ] Assumptions/conflicts omitted or buried.
- [ ] Next phase starts without declared entry criteria.
- [ ] Silent apply behavior bypasses review checkpoint.
- [ ] Applicable planning output lacks alternatives/tradeoff evidence.
- [ ] Innovate checkpoint is skipped without explicit `checkpoint_skipped: trivial_change`.

## Required Handoff Format (Minimum)

1. Context and objective
2. Completed outputs and evidence
3. Open issues and assumptions
4. Innovate checkpoint outputs (or explicit skip marker for trivial changes)
5. Next phase entry criteria
6. Owner and escalation path

## Validation Evidence

Validation passes when:
- every phase transition is handoff-backed,
- handoff format includes all required sections,
- Innovate checkpoint outputs are auditable in planning handoff,
- review-gated behavior is preserved across orchestration.

## Ownership

- Primary Owner: RIPER and Subagents
- Governance Approver: Migration Governance
- Runtime Consistency Approver: Runtime Core
