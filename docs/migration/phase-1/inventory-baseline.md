# Phase 1 Inventory Baseline

This artifact captures the baseline inventory used for Phase 1 governance sign-off.

## Scope

- Repository root files that define migration governance and kit behavior.
- Full legacy snapshot under `legacy-system/`.

## Root Inventory Baseline

| Path | Type | Owner Candidate | Notes |
|---|---|---|---|
| `.gitignore` | static | Migration Governance | Repository hygiene baseline |
| `README.md` | docs | Documentation and Examples | Canonical migration pointers |
| `INSTALL.md` | docs | Documentation and Examples | Placeholder until Phase 2 |
| `QUICKSTART.md` | docs | Documentation and Examples | Placeholder until Phase 2 |
| `LICENSE` | static | Migration Governance | Canonical legal file |
| `migration-manifest.yaml` | static | Migration Governance | Legacy inventory + classification source |
| `scripts/README.md` | docs | Documentation and Examples | Validation script usage |
| `scripts/validate_setup.py` | runtime | Migration Governance | Phase 1 parity and structural gate |
| `docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md` | docs | Migration Governance | Canonical strategy register/matrix |
| `docs/migration/Phase-1-Minimal-Runtime-Foundation-Plan.md` | docs | Migration Governance | Phase 1 objectives and exit criteria |
| `docs/migration/phase-1/*` | docs | Migration Governance | Phase 1 completion artifacts |
| `docs/*` (non-migration) | docs | Documentation and Examples | Future reference surface |
| `examples/` | docs | Documentation and Examples | Optional examples surface |
| `staging/.cursor/*` | runtime-foundation | Runtime Core | Runtime development skeleton |

## Legacy Inventory Baseline

Legacy inventory is complete and manifest-backed via `migration-manifest.yaml`.

- Total files under `legacy-system/`: 19
- Coverage expectation: every file under `legacy-system/` appears exactly once in manifest entries.
- Validation gate: `python scripts/validate_setup.py --mode kit`

## Exit Criteria Mapping

- Supports exit criterion: "All root files are classified with owner and reason."
- Supports exit criterion: "Ambiguous items are resolved or explicitly blocked with an owner/action."
