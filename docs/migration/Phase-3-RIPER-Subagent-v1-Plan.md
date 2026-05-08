# Phase 3: RIPER/Subagent v1 Plan

## Purpose

Define the planning and governance work for Phase 3 of the 2026 migration, focused on:
- limited RIPER/subagent v1 topology rollout,
- Innovate checkpoint enforcement inside Planning (no new agent),
- explicit ownership boundaries for runtime agent surfaces,
- deterministic handoff and review behavior,
- and concise runtime artifact enforcement at scale.

This document is planning-only and does not implement runtime topology changes.

## Preconditions

Phase 3 planning assumes all Phase 2 requirements are complete and accepted:
- `docs/migration/phase-2/phase-2-signoff.md` declares `Phase 2 Status: ACCEPTED`.
- Bootstrap inference, review gate, and continuity contracts are approved.
- `INSTALL.md`, `QUICKSTART.md`, and `README.md` follow Tier A/Tier B policy.
- `python scripts/validate_setup.py --mode kit` passes with zero errors.

## Scope

### In Scope
- Define the v1 RIPER/subagent topology contract and role boundaries.
- Define an auditable Innovate checkpoint embedded in Planning.
- Define orchestration and phase handoff requirements for multi-agent execution.
- Define ownership-hardening rules to avoid duplicated authority across agent surfaces.
- Define runtime artifact concision rules for v1 agent/rules/skill updates.
- Define Phase 3 validation extensions for `scripts/validate_setup.py`.

### Out of Scope
- Shipping optional hooks and advanced/enterprise packs (Phase 4).
- Expanding to broad multi-agent orchestration beyond limited v1 topology.
- Introducing a standalone Innovate agent in v1.
- Reworking Phase 1 classification matrix or Phase 2 bootstrap contracts.
- Introducing non-deterministic automation that bypasses review checkpoints.

## Source of Truth

Use these sections in `docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md`:
- `## 4.2 RIPER Evolution (High Priority)`
- `## 4.5 Documentation Maintenance (Medium Priority)`
- `## 7. Phased Rollout and Acceptance` (Phase 3)
- `## 8. Validation Checklist`

Also reference:
- `docs/migration/Phase-2-Bootstrap-Hardening-Plan.md`
- `docs/migration/phase-2/*` sign-off evidence
- `migration-manifest.yaml`

## Phase 3 Objectives

1. Define a minimal, stable RIPER/subagent v1 topology with explicit boundaries.
2. Make Innovate behavior auditable via a Planning checkpoint without adding a new role.
3. Establish deterministic orchestration and handoff requirements between roles.
4. Eliminate ownership ambiguity across reviewer, documentation, and governance surfaces.
5. Keep runtime artifacts operational-only and concise as topology scales.
6. Define and approve Phase 3 validation checks in kit and install modes.
7. Establish Phase 3 exit criteria and sign-off owners.

## Workstreams

### A) RIPER/Subagent v1 Topology Contract
- Define allowed v1 roles and responsibilities for RIPER lifecycle coverage.
- Define required inputs/outputs per role and prohibited cross-role behavior.
- Define Planning-stage Innovate checkpoint fields and skip policy for trivial changes.
- Define boundaries for parallel execution so role scope remains deterministic.

Deliverable:
- `RIPER/Subagent v1 Topology Contract` document with role-level responsibilities.

### B) Orchestration and Handoff Protocol
- Define orchestration sequence and required handoff summary format between phases.
- Define evidence requirements for completed phase outputs before next-phase execution.
- Define when Innovate checkpoint evidence is mandatory in Planning handoff.
- Define fail-safe behavior for missing, conflicting, or incomplete handoff artifacts.

Deliverable:
- `Orchestration and Handoff Checklist` with pass/fail criteria.

### C) Ownership-Hardening and Decision Rights
- Define single-primary-owner policy for overlapping surfaces (review vs documentation vs governance).
- Define escalation path for policy conflicts and role contention.
- Define ownership for Innovate checkpoint policy and exception decisions.
- Define approval boundaries for runtime topology updates vs docs-only changes.

Deliverable:
- `Ownership Boundary Matrix` with primary/approver/consulted roles.

### D) Runtime Artifact Concision Enforcement
- Define required brevity and operational-only requirements for runtime files impacted by Phase 3.
- Define prohibited runtime content patterns (narrative expansion, cleanup-prone examples, duplicate guidance).
- Define references policy so explanatory content lives in `docs/` while runtime remains enforceable.

Deliverable:
- `Runtime Artifact Concision Checklist` mapped to runtime surfaces.

### E) Validation and Gate Expansion
- Define Phase 3 checks to be added to `scripts/validate_setup.py`:
  - presence and completeness of Phase 3 artifacts,
  - Innovate checkpoint field and skip-policy coverage in planning artifacts,
  - topology/ownership contract conformance checks,
  - runtime-concision and handoff-evidence criteria checks.
- Define output mapping similar to prior phase criterion reporting.

Deliverable:
- `Phase 3 Validation Rubric` and script update requirements.

## Deliverables Location

Phase 3 governance artifacts should be maintained in:

- `docs/migration/phase-3/riper-subagent-v1-topology-contract.md`
- `docs/migration/phase-3/orchestration-and-handoff-checklist.md`
- `docs/migration/phase-3/ownership-boundary-matrix.md`
- `docs/migration/phase-3/runtime-artifact-concision-checklist.md`
- `docs/migration/phase-3/phase-3-validation-rubric.md`
- `docs/migration/phase-3/phase-3-signoff.md`

## Owners and Decision Rights

- **Migration Governance (primary approver):**
  - approves Phase 3 exit criteria and release-gate readiness,
  - resolves ownership or policy conflicts across workstreams.
- **RIPER and Subagents (primary owner for topology):**
  - approves v1 role boundaries, orchestration protocol, and handoff behavior.
- **Runtime Core (approver for enforceability and concision):**
  - approves runtime policy conformance and operational-only runtime artifacts.
- **Documentation and Examples (approver for continuity and reference boundaries):**
  - approves docs ownership boundaries and handoff documentation format.

## Exit Criteria (Phase 3 Complete)

Phase 3 is complete when all are true:
- v1 RIPER/subagent topology contract is documented, approved, and unambiguous.
- Innovate checkpoint requirements are explicit, auditable, and embedded in Planning (no separate agent).
- Orchestration and handoff protocol is reviewable, deterministic, and evidence-backed.
- Ownership boundary matrix eliminates duplicated authority across overlapping surfaces.
- Runtime artifact concision checklist is approved and mapped to impacted runtime files.
- Phase 3 validation rubric is approved and mapped to `validate_setup.py` checks.
- `docs/migration/phase-3/phase-3-signoff.md` declares `Phase 3 Status: ACCEPTED`.

## Risks and Mitigations

- **Risk:** Topology sprawl introduces unnecessary complexity in early rollout.  
  **Mitigation:** Limit v1 roles to essential lifecycle coverage and block non-essential expansion.

- **Risk:** Ownership overlap causes contradictory reviews and stalled decisions.  
  **Mitigation:** Enforce single-primary-owner boundaries with explicit escalation path.

- **Risk:** Runtime files bloat as orchestration guidance grows.  
  **Mitigation:** Keep runtime operational-only and relocate explanatory material to docs.

- **Risk:** Handoffs become non-deterministic and hard to validate.  
  **Mitigation:** Standardize handoff schema and require evidence checks before phase transitions.

- **Risk:** Innovation quality regresses when Innovate is implicit.  
  **Mitigation:** Require auditable Planning checkpoint fields and explicit skip reasons.

## Execution Sequence (Planning)

1. Approve Phase 3 artifact structure and owners.
2. Approve RIPER/subagent v1 topology contract and role boundaries.
3. Approve Innovate checkpoint requirements and skip policy (embedded in Planning).
4. Approve orchestration and handoff checklist.
5. Approve ownership boundary matrix and conflict escalation path.
6. Approve runtime artifact concision checklist.
7. Approve Phase 3 validation rubric and script mapping.
8. Record final sign-off as `Phase 3 Status: ACCEPTED`.

## Completion Workflow

1. Ensure all deliverables under `docs/migration/phase-3/` are present and current.
2. Run `python scripts/validate_setup.py --mode kit`.
3. Confirm zero errors and all Phase 3 criteria pass in the validation summary.
4. Record sign-off in `docs/migration/phase-3/phase-3-signoff.md`.

## Handoff to Phase 4

Phase 4 can start only after Phase 3 sign-off and includes:
- optional hooks and advanced/enterprise packs as opt-in additions,
- strict protection of default install low-friction behavior,
- and packaging boundaries that prevent advanced features from bloating runtime defaults.
