---
name: bootstrap-project
description: Bootstrap a project from requirements and design artifacts when initial setup, placeholder population, or roadmap initialization is requested.
---

# bootstrap-project

Bootstrap a project from available design and requirements inputs with review-first output.

## When to use

- Use when initializing a project baseline or reconciling missing setup artifacts.

## Inputs

- `requirements.md` and/or design docs if present
- Existing repository structure and configuration files

## Required behavior

1. Infer initial runtime context from explicit project artifacts.
2. Ensure `docs/` exists when missing.
3. Initialize or update `ROADMAP.md` with deterministic checkpoints.
4. Create `README.md` only if it does not already exist.
5. Generate `docs/File-Structure-Reference.md` from observed repository structure.
6. Generate `docs/Project-Constraints.md` from requirements/design artifacts and
   detected project configuration files.
7. Propose placeholder population and generated-document changes with evidence.
8. Present a reviewable change summary before final acceptance.

## Guardrails

- Label assumptions clearly when evidence is missing.
- Label inferred constraints and structure assumptions explicitly in generated
  docs.
- Do not silently overwrite existing governance decisions.
- Do not overwrite an existing `README.md` during bootstrap.
- Prefer minimal safe defaults when uncertainty remains.
