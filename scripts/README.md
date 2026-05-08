# Scripts

## `validate_setup.py`

Supports two modes:

| Mode | When | What it checks |
|------|------|----------------|
| **kit** | Run inside **Tholem-Cursor-Kit** (repo with `migration-manifest.yaml`) | Every `legacy-system/` file is listed in the manifest; governance docs exist under `docs/migration/`; `staging/.cursor/` skeleton; root `LICENSE` |
| **install** | Run in a **consumer project** with legacy rules in `.cursor/rules/` | Required `.mdc` filenames, placeholders, cross-references |

Auto-detection: if `migration-manifest.yaml` exists → kit; else if `.cursor/rules/` exists → install.

```bash
# From repository root (kit)
python scripts/validate_setup.py
python scripts/validate_setup.py --mode kit

# From a project that copied the legacy rules into .cursor/rules/
python scripts/validate_setup.py --mode install --project-root /path/to/project
```

### Requirements

- Python 3.9+ (stdlib only; no PyYAML required — `migration-manifest.yaml` is parsed with a small built-in parser)

### Legacy copy

The script under `legacy-system/scripts/validate_setup.py` is the pre-migration validator. Use the **root** `scripts/validate_setup.py` for kit and migration checks.
