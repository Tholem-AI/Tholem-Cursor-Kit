# Quickstart

Fastest path to first successful use.

## 1) Copy Runtime Package

Copy minimal runtime files into active Cursor paths (`.cursor/rules`, `.cursor/agents`, `.cursor/skills`; add `.agents/skills` when using that skills surface).

## 2) Start Using the Kit

Open Cursor in your project and begin normal workflows immediately.

## 3) Optional: Run Bootstrap for Requirements-Driven Setup

If your project has design/requirements docs and you want inferred placeholders and roadmap initialization, run:

> Bootstrap this project using the included bootstrap-project skill. Analyze design and requirements docs if present, initialize ROADMAP.md, populate required placeholders, and present a reviewable plan/diff before final acceptance.

Before accepting changes, review the proposal output:
- changed files,
- inferred values and their evidence,
- assumptions and unresolved conflicts.

## Notes

- Bootstrap is optional; Tier A remains fully supported.
- Review gating is required: Plan Mode review occurs before build; Agent mode review occurs through diffs/checkpoints during execution.
- Fallback-derived values are assumptions and should be confirmed.
