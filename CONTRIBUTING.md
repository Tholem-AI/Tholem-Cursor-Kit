# Contributing to Tholem-Cursor-Kit

This repository maintains the 2026 Tholem Cursor runtime framework.

## Contribution Scope

- Runtime behavior belongs in `staging/.cursor/`.
- User-facing guidance belongs in root docs (`README.md`, `INSTALL.md`,
  `CONTRIBUTING.md`).
- Keep runtime artifacts concise, operational, and free of tutorial bloat.

## Workflow Expectations

1. Keep rule/agent/skill boundaries clear and avoid duplicated policy logic.
2. Keep documentation aligned with actual runtime behavior.
3. Keep changes small, reviewable, and evidence-backed.
4. Flag contradictions or unclear behavior before continuing broad edits.

## Pull Request Guidelines

- Keep changes small and reviewable.
- Explain why runtime behavior changed, not just what changed.
- Update relevant docs when behavior or usage expectations shift.

## Quality Expectations

- Validate modified flows with appropriate checks for the affected scope.
- Avoid introducing stale references to removed or deprecated surfaces.
