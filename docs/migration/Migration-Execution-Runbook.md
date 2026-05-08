# Migration Execution Runbook

## Purpose

This is the canonical execution document for implementing the migration from `legacy-system/` to `staging/.cursor/`.

Use this runbook for operational decisions, migration sequencing, and release gating.  
Use `docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md` as strategy/history context.

## Authority Order

When guidance conflicts, apply sources in this order:

1. `migration-manifest.yaml` (row-level source of truth for disposition)
2. Phase sign-offs and validation rubrics under `docs/migration/phase-1/` through `docs/migration/phase-4/`
3. `scripts/validate_setup.py` output (`python scripts/validate_setup.py --mode kit`)
4. `docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md` (reference strategy)

## Core Inputs

- `migration-manifest.yaml`
- `docs/migration/Phase-1-Minimal-Runtime-Foundation-Plan.md`
- `docs/migration/Phase-2-Bootstrap-Hardening-Plan.md`
- `docs/migration/Phase-3-RIPER-Subagent-v1-Plan.md`
- `docs/migration/Phase-4-Optional-Advanced-Packs-Plan.md`
- `docs/migration/phase-1/phase-1-signoff.md`
- `docs/migration/phase-2/phase-2-signoff.md`
- `docs/migration/phase-3/phase-3-signoff.md`
- `docs/migration/phase-4/phase-4-signoff.md`
- `scripts/validate_setup.py`

## Pre-Migration Start Gate (Required Before Step 1)

Before branch-safe execution begins, all of the following must be true:

1. `migration-manifest.yaml` includes required per-row tracking fields:
   - `status`
   - `statusHistory`
   - `statusNotes`
   - `evidenceRef`
2. Each row status is initialized at minimum to `addressed-not-migrated` when owner/path/evidence method are already defined.
3. Each `statusHistory` follows the canonical order with no skipped states:
   - `unaddressed -> addressed-not-migrated -> migrated -> verified`
4. `python scripts/validate_setup.py --mode kit` passes with:
   - `Errors: 0`
   - row-status transition integrity checks passing.
5. Documentation and install guidance are aligned to current Cursor behavior:
   - recognized active runtime surfaces (`.cursor/rules`, `.cursor/agents`, `.cursor/skills`, and `.agents/skills` where applicable),
   - mode-specific review semantics (Plan Mode review-before-build, Agent mode diff/checkpoint review during execution),
   - staging-runtime guidance explicitly treated as a workflow convention, not a native activation surface.

If any requirement above is not satisfied, migration execution is blocked.

## Manifest Row Status Model

Every `migration-manifest.yaml` row must be tracked with one status:

- `unaddressed`: row exists, no implementation action recorded.
- `addressed-not-migrated`: owner, approach, and evidence plan are defined; migration action not yet completed.
- `migrated`: replacement/disposition action is executed to the target path or target state.
- `verified`: migration action is validated by command/evidence and cross-doc consistency checks.

Required tracking metadata per row:
- `statusHistory`: transition path captured as ordered states.
- `statusNotes`: concise current-state note for operators/reviewers.
- `evidenceRef`: primary artifact path or command evidence pointer.

Transition rule:
- `unaddressed -> addressed-not-migrated -> migrated -> verified`
- Rows must not skip directly to `verified`.

Release gate rule:
- Public release readiness requires `verified` for every manifest row.

## Phase-to-Runbook Mapping

### Phase 1 (Foundation)
- Inputs: inventory baseline, classification decision log, runtime contract checklist, manifest rubric.
- Gate: `Phase 1 Status: ACCEPTED`.
- Output to implementation: approved classification baseline + manifest structure used to process each row.

### Phase 2 (Bootstrap Hardening)
- Inputs: inference contract, review-gate checklist, continuity baseline, install hardening checklist.
- Gate: `Phase 2 Status: ACCEPTED`.
- Output to implementation: review-before-apply and no-cleanup constraints that govern extraction and updates.

### Phase 3 (RIPER/Subagent v1)
- Inputs: topology contract, handoff checklist, ownership matrix, runtime concision checklist.
- Gate: `Phase 3 Status: ACCEPTED`.
- Output to implementation: deterministic runtime role boundaries and handoff/ownership controls.

### Phase 4 (Optional Advanced Packs)
- Inputs: optional-pack architecture contract, hooks guardrails, advanced topology expansion contract, optional-pack documentation continuity baseline.
- Gate: `Phase 4 Status: ACCEPTED`.
- Output to implementation: opt-in advanced features with no default-path regression.

## Branch-Safe Execution Workflow

1. Parse all manifest rows and assign each an initial status (`unaddressed` by default).
2. Move each row to `addressed-not-migrated` once owner, implementation path, and evidence method are recorded.
3. For rows with `classification: runtime`, migrate content into `staging/.cursor/{rules,agents,skills}` and mark `migrated`.
4. For rows with `classification: docs`, `deprecated`, or `static`, execute replacement/sunset/static-keep actions and mark `migrated`.
5. Run `python scripts/validate_setup.py --mode kit` and cross-check phase/rubric/signoff consistency.
6. Promote rows to `verified` only when objective evidence exists and no policy contradiction remains.
7. Record non-`verified` rows and blockers in migration notes/signoff updates.

## Legacy Retention and Removal Gate

`legacy-system/` retention is required during migration until both conditions are true:

- `staging/.cursor/` is populated and self-sufficient for required runtime behavior.
- Every manifest row has reached `verified`.

After both conditions are true:

- `legacy-system/` becomes removable.
- Removal must occur before first public release commit/tag.
- Any non-`verified` row remains an explicit release blocker.

## Definition of Done (Implementation Complete)

Migration implementation is complete only when all are true:

- `staging/.cursor/` is self-sufficient for required runtime behavior.
- Every `migration-manifest.yaml` row is `verified`.
- Manifest parity is confirmed for runtime/docs/deprecated/static dispositions.
- No contradiction exists across manifest, phase artifacts, and validator expectations.
- Release-gate checklist is complete, including legacy-container removal readiness.

## Post-Phase-4 Next Steps

1. Complete extraction coverage so all runtime rows are migrated into `staging/.cursor/`.
2. Drive all non-runtime rows (`docs`, `deprecated`, `static`) to `verified` with evidence.
3. Maintain validator clean state on each iteration:
   - `python scripts/validate_setup.py --mode kit`
4. Keep `legacy-system/` until all rows are `verified`; then plan removal before public release.
5. Finalize public release checklist with manifest parity and policy consistency signoff.

## Evidence Cross-Links

- Strategy reference: `docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md`
- Phase 4 plan: `docs/migration/Phase-4-Optional-Advanced-Packs-Plan.md`
- Phase 4 sign-off: `docs/migration/phase-4/phase-4-signoff.md`
- Validator: `scripts/validate_setup.py`
