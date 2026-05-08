# Tholem-Cursor-Kit

Minimal 2026 Cursor kit: migration work lives here while legacy sources stay under `legacy-system/`. Operational runtime for this repo should be developed under `staging/.cursor/` (rules, agents, skills).

## Governance and migration docs

Canonical strategy and Phase 1 planning (do not duplicate under `dev-docs/`):

- [docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md](docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md)
- [docs/migration/Phase-1-Minimal-Runtime-Foundation-Plan.md](docs/migration/Phase-1-Minimal-Runtime-Foundation-Plan.md)

`migration-manifest.yaml` classifies every file under `legacy-system/`. Validate layout with:

```bash
python scripts/validate_setup.py
```

See [INSTALL.md](INSTALL.md) and [QUICKSTART.md](QUICKSTART.md) for install notes (placeholders until Phase 2).
