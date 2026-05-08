# Phase 2 Validation Rubric

## Purpose

Define validation requirements for Phase 2 bootstrap and install hardening gates.

## Required Artifacts

- `docs/migration/phase-2/bootstrap-inference-contract.md`
- `docs/migration/phase-2/bootstrap-review-gate-checklist.md`
- `docs/migration/phase-2/documentation-continuity-baseline.md`
- `docs/migration/phase-2/install-quickstart-hardening-checklist.md`
- `docs/migration/phase-2/phase-2-validation-rubric.md`
- `docs/migration/phase-2/phase-2-signoff.md`

## Criterion 1: Inference Contract Completeness

- Precedence order is explicit and deterministic.
- Required evidence mapping is defined.
- Conflict behavior is review-gated and non-silent.

## Criterion 2: Review Gate Enforcement

- Proposal artifact exists before apply.
- Proposal includes file-level change visibility.
- Assumptions and conflicts are clearly labeled.

## Criterion 3: Documentation Continuity Baseline

- Baseline is default-on and independent of optional memory features.
- Required continuity checkpoints are defined.
- `ROADMAP.md` and docs update expectations are explicit.

## Criterion 4: Install/Quickstart Hardening

- Install docs describe Tier A/Tier B flow.
- Review-before-apply behavior is explicit.
- Placeholder-only state for install docs is eliminated.

## Criterion 5: Phase 2 Sign-off

- `phase-2-signoff.md` exists.
- Sign-off status is explicitly tracked.
- Final acceptance requires `Phase 2 Status: ACCEPTED`.

## Script Mapping

`scripts/validate_setup.py --mode kit` should report:
- artifact presence for all required Phase 2 files,
- criteria mapping for the five Phase 2 criteria above,
- explicit status line for Phase 2 sign-off.

## Approval

Validation rubric is approved when:
1. Required Phase 2 artifacts are present.
2. Criteria mapping is implemented in validation output.
3. Phase 2 sign-off has been reviewed by governance owners.

## Ownership

- Primary Owner: Migration Governance
- Approvers: Runtime Core, Documentation and Examples
