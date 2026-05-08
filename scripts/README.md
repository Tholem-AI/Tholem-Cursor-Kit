# Scripts

## `validate_setup.py`

Supports two modes:

| Mode | When | What it checks |
|------|------|----------------|
| **kit** | Run inside **Tholem-Cursor-Kit** (repo with `migration-manifest.yaml`) | Manifest schema + legacy parity, runtime no-cleanup markers, required `docs/migration/phase-1/` artifacts, required `staging/.cursor/{rules,agents,skills}` skeleton, root `LICENSE`, and Phase 1 exit-criteria mapping summary |
| **install** | Run in a **consumer project** with legacy rules in `.cursor/rules/` | Required `.mdc` filenames, placeholders, cross-references |

Auto-detection: if `migration-manifest.yaml` exists -> kit; else if `.cursor/rules/` exists -> install.

```bash
# From repository root (kit)
python scripts/validate_setup.py
python scripts/validate_setup.py --mode kit

# From a project that copied the legacy rules into .cursor/rules/
python scripts/validate_setup.py --mode install --project-root /path/to/project
```

### Phase 1 strict requirements (kit mode)

Kit mode is a hard gate for Phase 1 sign-off:

- Every file under `legacy-system/` must be listed in `migration-manifest.yaml`.
- Every manifest entry must include all required fields.
- Every `classification: runtime` entry must include `[NO_CLEANUP_PROOF]` in `validation`.
- Required Phase 1 artifacts must exist:
  - `docs/migration/phase-1/inventory-baseline.md`
  - `docs/migration/phase-1/classification-decision-log.md`
  - `docs/migration/phase-1/runtime-contract-checklist.md`
  - `docs/migration/phase-1/manifest-spec-and-validation-rubric.md`
  - `docs/migration/phase-1/phase-1-signoff.md`
- Required staging skeleton must exist:
  - `staging/.cursor/rules/`
  - `staging/.cursor/agents/`
  - `staging/.cursor/skills/`

### Troubleshooting

- **Missing no-cleanup marker:** add `[NO_CLEANUP_PROOF]` to `validation` text of each runtime manifest entry.
- **Missing Phase 1 artifact:** create the missing file under `docs/migration/phase-1/`.
- **Missing staging skeleton:** create `staging/.cursor/{rules,agents,skills}`.
- **Sign-off not accepted:** ensure `docs/migration/phase-1/phase-1-signoff.md` contains the exact line `Phase 1 Status: ACCEPTED`.

### Requirements

- Python 3.9+ (stdlib only; no PyYAML required).

### Legacy copy

The script under `legacy-system/scripts/validate_setup.py` is the pre-migration validator. Use root `scripts/validate_setup.py` for Phase 1 governance and migration checks.
