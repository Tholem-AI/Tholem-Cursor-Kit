# Phase 4 Validation Rubric

## Purpose

Define validation requirements for Phase 4 optional advanced packs, hooks guardrails, and post-v1 topology expansion gates.

## Required Artifacts

- `docs/migration/phase-4/optional-pack-architecture-contract.md`
- `docs/migration/phase-4/hooks-guardrails-and-activation-checklist.md`
- `docs/migration/phase-4/advanced-topology-expansion-contract.md`
- `docs/migration/phase-4/optional-pack-documentation-continuity-baseline.md`
- `docs/migration/phase-4/phase-4-validation-rubric.md`
- `docs/migration/phase-4/phase-4-signoff.md`

## Criterion 1: Optional Pack Architecture Boundary Integrity

- Default runtime and optional-pack boundaries are explicit and enforceable.
- Optional activation path is explicit and auditable.
- Missing-prerequisite fallback behavior is defined.

## Criterion 2: Hooks Guardrail Enforcement

- Hooks remain opt-in with explicit activation behavior.
- Safety, rollback, and side-effect visibility expectations are defined.
- Prohibited hook patterns are explicitly documented.

## Criterion 3: Advanced Topology Determinism and Scope Control

- Advanced post-v1 expansion remains optional and bounded.
- Deterministic orchestration and handoff expectations are explicit.
- Fallback to baseline v1 behavior is defined.

## Criterion 4: Optional-Pack Documentation Continuity

- Advanced docs are separated from baseline install docs.
- Continuity checkpoints are defined for policy and behavior changes.
- Runtime/doc policy consistency remains explicit.

## Criterion 5: Phase 4 Sign-off

- `phase-4-signoff.md` exists.
- Sign-off status is explicitly tracked.
- Final acceptance requires `Phase 4 Status: ACCEPTED`.

## Script Mapping

`scripts/validate_setup.py --mode kit` should report:
- artifact presence for all required Phase 4 files,
- criteria mapping for the five Phase 4 criteria above,
- explicit status line for Phase 4 sign-off.

## Approval

Validation rubric is approved when:
1. Required Phase 4 artifacts are present.
2. Criteria mapping is implemented in validation output.
3. Phase 4 sign-off has been reviewed by governance owners.

## Ownership

- Primary Owner: Migration Governance
- Approvers: Runtime Core, Documentation and Examples, RIPER and Subagents
