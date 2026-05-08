# Phase 3 RIPER/Subagent v1 Topology Contract

## Purpose

Define the limited, deterministic v1 topology for RIPER-oriented subagent collaboration.

## Scope Boundary

This contract applies to v1 only:
- establish essential role boundaries,
- keep orchestration minimal and reviewable,
- avoid broad autonomous expansion before Phase 4.

## Allowed v1 Roles

- **Research role:** gathers evidence and constraints.
- **Planning role:** runs the Innovate checkpoint, then converts evidence into scoped execution plans.
- **Execution role:** applies approved implementation changes.
- **Review role:** validates quality, risk, and policy conformance.

Note:
- Innovate is a required checkpoint inside Planning, not a standalone v1 agent.

## Role Input/Output Contract

Each role must emit:
- concise context summary,
- explicit decisions taken,
- unresolved assumptions or blockers,
- handoff payload for the next role.

Planning-specific Innovate checkpoint outputs (when applicable):
- `alternatives_considered` (minimum 2 viable options, including baseline/current approach when relevant),
- `tradeoff_summary` (cost, risk, complexity, and maintainability per option),
- `selected_approach` (chosen option with rationale),
- `rejected_options_reason` (concise rationale for non-selected options),
- `confidence_and_unknowns` (confidence level and unresolved assumptions).

Skip policy:
- Innovate checkpoint may be skipped only for trivial changes.
- Skip must be explicit as `checkpoint_skipped: trivial_change`.

## Prohibited Behavior

- Silent role switching without explicit handoff output.
- Unbounded role fan-out outside declared v1 topology.
- Cross-role authority overrides without documented escalation.
- Non-deterministic output ordering in role proposals.
- Final planning output for applicable work without Innovate checkpoint fields.
- Silent checkpoint skip with no explicit skip reason.

## Determinism Requirements

- Identical inputs should produce equivalent role-level proposals.
- Handoff output ordering is stable and reproducible.
- Review checkpoints remain explicit before apply.

## Validation Evidence

Validation passes when:
- role boundaries are documented and non-overlapping,
- required role outputs are explicitly defined,
- prohibited behaviors are listed and enforceable,
- Innovate checkpoint requirements and skip policy are explicit,
- topology remains limited to v1 scope.

## Ownership

- Primary Owner: RIPER and Subagents
- Approver: Migration Governance
- Runtime Policy Approver: Runtime Core
