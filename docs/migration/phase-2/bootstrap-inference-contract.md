# Phase 2 Bootstrap Inference Contract

## Purpose

Define deterministic rules for inferring stack and runtime placeholders during bootstrap.

This contract ensures every inferred value is traceable to explicit evidence and reviewable before apply.

## Precedence (Strict Order)

Bootstrap must infer values using this precedence:

1. Requirements and design artifacts in repository docs.
2. Detected project configuration files.
3. Conservative fallback defaults.

If a higher-precedence source provides a value, lower-precedence sources must not override it.

## Accepted Inputs

### A) Requirements and design artifacts
- `requirements.md`
- `design-doc.md`
- equivalent project requirement/design docs referenced in repository docs

### B) Detected configuration files
- language/version files (for example: `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`)
- CI or tool configs that provide unambiguous version constraints

### C) Fallback defaults
- used only when requirements/docs and config evidence are missing
- must be marked as assumptions in the review output

## Inference Output Contract

For each placeholder or inferred policy value, bootstrap must output:
- target file and field/placeholder name,
- inferred value,
- source category (requirements, config, fallback),
- specific evidence reference,
- confidence note or assumption note when fallback is used.

## Conflict Resolution Rules

- If multiple high-precedence sources conflict, bootstrap must not auto-apply.
- Bootstrap must report conflict details and request review decision.
- Conflicts between requirements docs and config files default to requirements docs unless the docs explicitly defer to config.

## Determinism Requirements

- Same inputs must produce the same proposal output.
- Proposal ordering must be stable (sorted by path, then placeholder key).
- Non-deterministic behavior (time-based or random ordering) is prohibited.

## Validation Evidence

Validation passes when:
- precedence is stated and followed,
- every inferred value has evidence mapping,
- fallback assumptions are explicitly labeled,
- conflict behavior is review-gated and non-silent.

## Ownership

- Primary Owner: Runtime Core
- Approver: Migration Governance
- Consulted: Documentation and Examples
