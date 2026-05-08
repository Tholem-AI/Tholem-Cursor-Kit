# Phase 1: Minimal Runtime Foundation Plan

## Purpose

Define the planning and governance work for Phase 1 of the 2026 migration, focused on:
- full file inventory,
- deterministic classification using the migration matrix,
- runtime payload minimization design,
- and release-gate readiness criteria.

This document is planning-only and does not start implementation.

## Scope

### In Scope
- Build and approve the Phase 1 execution blueprint.
- Map all current project-root files to `runtime`, `docs`, `deprecated`, or `static`.
- Define required acceptance checks for a minimal runtime payload.
- Define manifest structure and ownership expectations.

### Out of Scope
- Editing/migrating `.mdc`, skill, agent, or script files.
- Deleting or moving legacy files.
- Implementing bootstrap behavior changes.
- Implementing Phase 2+ features.

## Source of Truth

Use these sections in `docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md`:
- `## 2. Runtime vs Reference Boundary`
- `## 5. Specific File Changes (Complete Root Register)`
- `## 6. Hard Migration Decision Matrix`
- `## 7. Phased Rollout and Acceptance` (Phase 1 + release gate)
- `## 8. Validation Checklist`

## Phase 1 Objectives

1. Confirm an accurate inventory of all current root files.
2. Produce a reviewed classification map for each file.
3. Define the minimal runtime package contract (`.cursor/` operational-only).
4. Define a manifest schema and evidence requirements for each file decision.
5. Establish Phase 1 exit criteria and sign-off owners.

## Workstreams

### A) Inventory and Baseline Capture
- Capture current root file list and current classification candidates.
- Identify files with ambiguous ownership or mixed content types.

Deliverable:
- `Inventory Baseline` table (planning artifact).

### B) Matrix Classification Review
- Apply hard migration matrix in first-match order.
- Resolve tie-breakers (`runtime` vs `docs`) with default-to-`docs` policy.
- Mark unresolved items requiring owner sign-off.

Deliverable:
- `Classification Decision Log` (planning artifact).

### C) Runtime Payload Contract Definition
- Define what is allowed in runtime files (operational logic + placeholders only).
- Define prohibited runtime content (tutorial prose, cleanup-prone examples).
- Define no-cleanup proof requirements.

Deliverable:
- `Runtime Contract Checklist` (planning artifact).

### D) Manifest and Validation Design
- Finalize manifest fields:
  - `legacyPath`
  - `classification`
  - `reason`
  - `owner`
  - `replacement`
  - `validation`
- Define evidence expectations per field.

Deliverable:
- `Manifest Spec` and `Validation Rubric` (planning artifacts).

### Deliverables Location

Phase 1 governance artifacts are maintained in:

- `docs/migration/phase-1/inventory-baseline.md`
- `docs/migration/phase-1/classification-decision-log.md`
- `docs/migration/phase-1/runtime-contract-checklist.md`
- `docs/migration/phase-1/manifest-spec-and-validation-rubric.md`
- `docs/migration/phase-1/phase-1-signoff.md`

## Owners and Decision Rights

- **Migration Governance (primary approver):**
  - final classification disputes,
  - release-gate readiness,
  - parity criteria approval.
- **Runtime Core (approver for runtime):**
  - confirms runtime necessity and no-cleanup compliance.
- **Documentation and Examples (approver for docs):**
  - confirms reference relocation targets and documentation completeness.

## Exit Criteria (Phase 1 Complete)

Phase 1 is complete when all are true:
- All root files are classified with owner and reason.
- All `runtime` classifications include no-cleanup proof criteria.
- Manifest schema and validation rubric are approved.
- Ambiguous items are resolved or explicitly blocked with an owner/action.
- Release gate requirements for legacy-container removal are documented and accepted.

## Risks and Mitigations

- **Risk:** Over-classifying to `runtime` causes future cleanup burden.  
  **Mitigation:** Default ambiguous decisions to `docs`; require runtime sign-off.

- **Risk:** Ownership overlap causes contradictory decisions.  
  **Mitigation:** Single primary decision owner per file in decision log.

- **Risk:** Incomplete manifest fields reduce traceability.  
  **Mitigation:** Make all manifest fields mandatory before Phase 1 sign-off.

## Execution Sequence (Planning)

1. Approve inventory baseline format.
2. Review classifications file-by-file against matrix.
3. Resolve ambiguous items via owner sign-off.
4. Approve runtime contract checklist.
5. Approve manifest spec and validation rubric.
6. Sign off Phase 1 exit criteria.

## Completion Workflow

1. Ensure all deliverables under `docs/migration/phase-1/` are present and current.
2. Run `python scripts/validate_setup.py --mode kit`.
3. If validation passes with zero errors, record final sign-off in `docs/migration/phase-1/phase-1-signoff.md`.
4. Mark "Phase 1 Status: ACCEPTED" in the sign-off document.

## Handoff to Phase 2

Phase 2 can start only after Phase 1 sign-off and includes:
- bootstrap hardening,
- requirements-driven stack inference enforcement,
- and documentation continuity baseline enforcement.
