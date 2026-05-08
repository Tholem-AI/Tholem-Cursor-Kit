# Tholem-Cursor-Kit

Minimal 2026 Cursor kit: migration work lives here while legacy sources stay under `legacy-system/`. Operational runtime for this repo should be developed under `staging/.cursor/` (rules, agents, skills).

## Governance and migration docs

Canonical strategy and Phase 1 planning (do not duplicate under `dev-docs/`):

- [docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md](docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md)
- [docs/migration/Phase-1-Minimal-Runtime-Foundation-Plan.md](docs/migration/Phase-1-Minimal-Runtime-Foundation-Plan.md)
- [docs/migration/Phase-2-Bootstrap-Hardening-Plan.md](docs/migration/Phase-2-Bootstrap-Hardening-Plan.md)
- [docs/migration/Phase-3-RIPER-Subagent-v1-Plan.md](docs/migration/Phase-3-RIPER-Subagent-v1-Plan.md)

`migration-manifest.yaml` classifies every file under `legacy-system/`. Validate layout with:

```bash
python scripts/validate_setup.py
```

Phase 1 completion record:

- [docs/migration/phase-1/phase-1-signoff.md](docs/migration/phase-1/phase-1-signoff.md)

## Phase 2 closure

- Status: `ACCEPTED` (2026-05-08)
- Sign-off: [docs/migration/phase-2/phase-2-signoff.md](docs/migration/phase-2/phase-2-signoff.md)
- Validation gate: `python scripts/validate_setup.py --mode kit`
- Recorded result: `Passed: 39`, `Warnings: 0`, `Errors: 0`
- Mapping outcome: all six Phase 2 criteria `[PASS]`

## Phase 3 closure

- Status: `ACCEPTED` (2026-05-08)
- Sign-off: [docs/migration/phase-3/phase-3-signoff.md](docs/migration/phase-3/phase-3-signoff.md)
- Validation gate: `python scripts/validate_setup.py --mode kit`
- Recorded result: `Passed: 47`, `Warnings: 0`, `Errors: 0`
- Mapping outcome: all six Phase 3 criteria `[PASS]` (including Innovate checkpoint auditability)

See [INSTALL.md](INSTALL.md) and [QUICKSTART.md](QUICKSTART.md) for canonical Tier A/Tier B install and bootstrap guidance.
