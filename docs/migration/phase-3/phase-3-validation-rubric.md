# Phase 3 Validation Rubric

## Purpose

Define validation requirements for Phase 3 RIPER/subagent v1 planning and governance gates.

## Required Artifacts

- `docs/migration/phase-3/riper-subagent-v1-topology-contract.md`
- `docs/migration/phase-3/orchestration-and-handoff-checklist.md`
- `docs/migration/phase-3/ownership-boundary-matrix.md`
- `docs/migration/phase-3/runtime-artifact-concision-checklist.md`
- `docs/migration/phase-3/phase-3-validation-rubric.md`
- `docs/migration/phase-3/phase-3-signoff.md`

## Criterion 1: Topology Contract Completeness

- v1 role boundaries are explicit and non-overlapping.
- Required role outputs are defined.
- Innovate checkpoint is explicit in Planning (no standalone v1 Innovate agent).
- Prohibited behaviors are documented.

## Criterion 2: Orchestration and Handoff Enforcement

- Handoff artifact format is explicit.
- Phase transition evidence requirements are defined.
- Planning handoff includes auditable Innovate checkpoint outputs when applicable.
- Review-gated behavior is preserved.

## Criterion 3: Ownership Boundary Hardening

- One primary owner exists per decision surface.
- Escalation path is explicit for policy conflicts.
- Duplicated authority is prevented.

## Criterion 4: Runtime Artifact Concision

- Runtime files are operational-only.
- Narrative/explanatory text is externalized to docs.
- Runtime/doc policy boundaries remain consistent.

## Criterion 5: Phase 3 Sign-off

- `phase-3-signoff.md` exists.
- Sign-off status is explicitly tracked.
- Final acceptance requires `Phase 3 Status: ACCEPTED`.

## Script Mapping

`scripts/validate_setup.py --mode kit` should report:
- artifact presence for all required Phase 3 files,
- criteria mapping for the five Phase 3 criteria above, including Innovate checkpoint auditability in Criteria 1 and 2,
- explicit status line for Phase 3 sign-off.

## Approval

Validation rubric is approved when:
1. Required Phase 3 artifacts are present.
2. Criteria mapping is implemented in validation output.
3. Phase 3 sign-off has been reviewed by governance owners.

## Ownership

- Primary Owner: Migration Governance
- Approvers: Runtime Core, Documentation and Examples, RIPER and Subagents
