# Installation Guide (2026)

This guide provides the canonical install flow for the Tholem Cursor Kit.

## Tier A: Default Install (Low Friction)

1. Copy the minimal `.cursor/` runtime package into your project root.
2. Start using the kit immediately.

Tier A is the default path and does not require bootstrap.

## Tier B: Optional Bootstrap (Requirements-Driven)

Use Tier B when you want stack-aware placeholder population and initial planning docs.

1. Add requirements/design artifacts if available (for example `requirements.md`, `design-doc.md`).
2. Run the canonical bootstrap prompt:

> Bootstrap this project using the included bootstrap-project skill. Analyze design and requirements docs if present, initialize ROADMAP.md, populate required placeholders, and propose all changes for review before applying.

3. Review the proposed changes before applying anything.

## Mandatory Review Gate

Bootstrap must be review-gated:
- never apply proposed bootstrap changes silently,
- inspect proposed file changes and inferred values first,
- approve or revise assumptions before apply.

## Inference Precedence

Bootstrap should infer stack/version constraints in this order:
1. project requirements/design docs,
2. detected project configuration files,
3. conservative fallback defaults (explicitly labeled as assumptions).

## What This Guide Avoids

- No cleanup-heavy post-install steps.
- No deletion-first workflow.
- No requirement to manually remove bootstrap artifacts from runtime files.

## Validation

From kit root:

```bash
python scripts/validate_setup.py --mode kit
```

From consumer project root:

```bash
python scripts/validate_setup.py --mode install
```
