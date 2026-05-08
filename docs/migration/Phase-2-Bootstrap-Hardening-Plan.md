# Phase 2: Bootstrap and Install Hardening Plan

## Purpose

Define the planning and governance work for Phase 2 of the 2026 migration, focused on:
- requirements-driven bootstrap hardening,
- deterministic and review-gated placeholder updates,
- documentation continuity baseline enforcement,
- and install experience hardening for both kit and consumer modes.

This document is planning-only and does not implement runtime content changes.

## Preconditions

Phase 2 planning assumes all Phase 1 requirements are complete and accepted:
- `docs/migration/phase-1/phase-1-signoff.md` declares `Phase 1 Status: ACCEPTED`.
- `migration-manifest.yaml` is complete and schema-valid.
- `staging/.cursor/{rules,agents,skills}` skeleton exists.
- `python scripts/validate_setup.py --mode kit` passes with zero errors.

## Scope

### In Scope
- Define Phase 2 acceptance contract for bootstrap behavior.
- Define stack inference precedence and evidence requirements.
- Define review-gate requirements before applying bootstrap edits.
- Define documentation continuity baseline requirements.
- Define install and quickstart hardening requirements.
- Define Phase 2 validation extensions for `scripts/validate_setup.py`.

### Out of Scope
- Implementing full RIPER/subagent v1 topology changes (Phase 3).
- Shipping optional hooks/advanced packs (Phase 4).
- Reworking legacy inventory/classification rules finalized in Phase 1.
- Large runtime refactors not required for bootstrap hardening.

## Source of Truth

Use these sections in `docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md`:
- `## 1. Installation Philosophy (2026)`
- `## 4.4 Memory System (Default-On Documentation Baseline)`
- `## 4.6 Technology Stack Updates (Bootstrap-Derived)`
- `## 7. Phased Rollout and Acceptance` (Phase 2)
- `## 8. Validation Checklist`

Also reference:
- `docs/migration/Phase-1-Minimal-Runtime-Foundation-Plan.md`
- `docs/migration/phase-1/*` sign-off evidence
- `migration-manifest.yaml`

## Phase 2 Objectives

1. Enforce deterministic bootstrap stack inference from project evidence.
2. Require review-gated placeholder updates before applying bootstrap changes.
3. Enforce documentation continuity baseline independent of Generate Memories.
4. Harden install documentation to maintain low-friction adoption.
5. Define and approve Phase 2 validation checks in kit and install modes.
6. Establish Phase 2 exit criteria and sign-off owners.

## Workstreams

### A) Bootstrap Inference Contract
- Define precedence for stack/version constraints:
  1. Requirements/design documentation,
  2. detected project configuration files,
  3. conservative fallback defaults.
- Define what must be captured in bootstrap output (detected inputs, inferred values, unresolved assumptions).
- Define failure behavior when required evidence is missing or conflicting.

Deliverable:
- `Bootstrap Inference Contract` document with explicit precedence and fallback rules.

### B) Review-Gated Change Application
- Define mandatory review artifact for bootstrap runs (proposed change diff before apply).
- Define required fields in bootstrap proposal summary:
  - files changed,
  - placeholders updated,
  - rationale per update,
  - unresolved questions/assumptions.
- Define prohibited behavior: silent apply with no review checkpoint.

Deliverable:
- `Bootstrap Review Gate Checklist` with pass/fail criteria.

### C) Documentation Continuity Baseline
- Define default-on documentation update checkpoints after major changes.
- Define minimum required continuity artifacts:
  - `ROADMAP.md` lifecycle updates,
  - focused docs updates for decisions and handoff context.
- Confirm Generate Memories remains additive, not required for continuity.

Deliverable:
- `Documentation Continuity Baseline` contract and examples.

### D) Install and Quickstart Hardening
- Replace placeholders in `INSTALL.md` and `QUICKSTART.md` with canonical Tier A/Tier B flows.
- Ensure the default path remains:
  1. copy minimal `.cursor/`,
  2. optional single bootstrap prompt,
  3. review changes before apply.
- Ensure instructions avoid cleanup-heavy or deletion-first workflows.

Deliverable:
- `Install/Quickstart Hardening` checklist mapped to docs updates.

### E) Validation and Gate Expansion
- Define Phase 2 checks to be added to `scripts/validate_setup.py`:
  - presence and completeness of Phase 2 artifacts,
  - bootstrap review-gate evidence checks,
  - continuity baseline criteria checks.
- Define output mapping similar to Phase 1 criterion reporting.

Deliverable:
- `Phase 2 Validation Rubric` and script update requirements.

## Deliverables Location

Phase 2 governance artifacts should be maintained in:

- `docs/migration/phase-2/bootstrap-inference-contract.md`
- `docs/migration/phase-2/bootstrap-review-gate-checklist.md`
- `docs/migration/phase-2/documentation-continuity-baseline.md`
- `docs/migration/phase-2/install-quickstart-hardening-checklist.md`
- `docs/migration/phase-2/phase-2-validation-rubric.md`
- `docs/migration/phase-2/phase-2-signoff.md`

## Owners and Decision Rights

- **Migration Governance (primary approver):**
  - approves Phase 2 exit criteria and release-gate readiness,
  - resolves scope and policy conflicts between workstreams.
- **Runtime Core (approver for runtime policy and bootstrap enforcement):**
  - approves inference precedence implementation and review-gate runtime behavior.
- **Documentation and Examples (approver for continuity/install docs):**
  - approves install, quickstart, and continuity artifacts.
- **RIPER and Subagents (consulted):**
  - confirms Phase 2 constraints preserve clean handoff into Phase 3 topology work.

## Exit Criteria (Phase 2 Complete)

Phase 2 is complete when all are true:
- Bootstrap stack inference precedence is documented, approved, and unambiguous.
- Bootstrap updates are review-gated with explicit proposal artifacts before apply.
- Documentation continuity baseline is defined and enforced independent of Generate Memories.
- `INSTALL.md` and `QUICKSTART.md` are no longer placeholders and match Tier A/Tier B flow.
- Phase 2 validation rubric is approved and mapped to `validate_setup.py` checks.
- `docs/migration/phase-2/phase-2-signoff.md` declares `Phase 2 Status: ACCEPTED`.

## Risks and Mitigations

- **Risk:** Bootstrap inference is nondeterministic across projects.  
  **Mitigation:** Enforce precedence order and require explicit assumptions in review output.

- **Risk:** Silent or oversized bootstrap changes reduce trust.  
  **Mitigation:** Require pre-apply diff summary and structured approval checkpoint.

- **Risk:** Documentation continuity relies on optional memory features.  
  **Mitigation:** Keep docs + roadmap updates as mandatory baseline behavior.

- **Risk:** Install docs drift from runtime policy.  
  **Mitigation:** Gate Phase 2 sign-off on install/quickstart policy conformance checks.

## Execution Sequence (Planning)

1. Approve Phase 2 artifact structure and owners.
2. Approve bootstrap inference contract and fallback rules.
3. Approve review-gate checklist and proposal format.
4. Approve documentation continuity baseline contract.
5. Approve install/quickstart hardening checklist.
6. Approve Phase 2 validation rubric and script mapping.
7. Record final sign-off as `Phase 2 Status: ACCEPTED`.

## Completion Workflow

1. Ensure all deliverables under `docs/migration/phase-2/` are present and current.
2. Run `python scripts/validate_setup.py --mode kit`.
3. Confirm zero errors and all Phase 2 criteria pass in the validation summary.
4. Record sign-off in `docs/migration/phase-2/phase-2-signoff.md`.

## Handoff to Phase 3

Phase 3 can start only after Phase 2 sign-off and includes:
- RIPER/subagent v1 limited topology rollout,
- ownership-hardening for runtime agent surfaces,
- and concise runtime artifact enforcement at scale.
