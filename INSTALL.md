# Installation Guide (2026)

This is the canonical setup and quickstart guide for the Tholem Cursor Kit.

## Quickstart (Fast Path)

1. Copy runtime surfaces into active project paths:
   - `.cursor/rules`
   - `.cursor/agents`
   - `.cursor/skills`
   - `.agents/skills` (only if your setup uses that surface)
2. Start using the kit immediately.
3. Optionally run bootstrap if you want requirements-driven setup.

## Tier A: Default Install (Low Friction)

1. Copy the minimal runtime package into active Cursor project paths (`.cursor/rules`, `.cursor/agents`, `.cursor/skills`; include `.agents/skills` when using that skills surface).
2. Start using the kit immediately.

Tier A is the default path and does not require bootstrap.

## Tier B: Optional Bootstrap (Requirements-Driven)

Use Tier B when you want stack-aware placeholder population and initial planning docs.

1. Add project context artifacts if available (for example `requirements.md`,
   PRD files, ADRs, architecture notes, API specs, implementation constraints,
   or design docs).
2. Run the canonical bootstrap prompt:

> Bootstrap this project using the included bootstrap-project skill. Auto-discover relevant requirements and context docs in the repository, initialize or update ROADMAP.md, generate docs/File-Structure-Reference.md and docs/Project-Constraints.md, populate required placeholders, and present a reviewable plan/diff before final acceptance. If critical context is ambiguous or missing, ask me to @-attach the most relevant files (for example PRD, ADR, architecture notes, API specs, or constraints docs) before applying changes.

3. Review the proposed changes before applying anything.

## Mandatory Review Gate

Bootstrap must be review-gated:
- in Plan Mode, review and approve the build plan before implementation,
- in Agent mode, review generated diffs/checkpoints and accept or request changes,
- never accept inferred values silently; confirm assumptions and unresolved conflicts first.

## Inference Precedence

Bootstrap should infer stack/version constraints in this order:
1. project requirements/design docs,
2. detected project configuration files,
3. conservative fallback defaults (explicitly labeled as assumptions).

## What This Guide Avoids

- No cleanup-heavy post-install steps.
- No deletion-first workflow.
- No requirement to manually remove bootstrap artifacts from runtime files.
- No dependency on undocumented memory automation behavior; documentation continuity remains mandatory.

## Notes on validation

- Normal installation does not require migration-governance scripts.
- Review generated changes before applying them, especially during bootstrap.

## Testing-phase disclaimer

This framework is in testing and may produce behavior that differs from default
Cursor agent behavior. Results can be unpredictable and should be reviewed
manually before use. See [README.md](README.md) for framework context and
[LICENSE](LICENSE) for legal terms and limitations.
