# Bootstrap Flow Deep Dive

The `bootstrap-project` skill is the most powerful feature in the Tholem Cursor Kit. It turns a blank or partially documented project into a fully initialized workspace with minimal effort.

## When to Use Bootstrap

Use bootstrap when you have:

- A new project with design documents, PRDs, ADRs, or requirements
- An existing project that needs better structure and documentation
- A project where you want the agent to infer tech stack, quality commands, and initial task list from context

## The Canonical Bootstrap Prompt

```
Bootstrap this project using the included bootstrap-project skill. Auto-discover relevant requirements and context docs in the repository, initialize or update ROADMAP.md, generate docs/File-Structure-Reference.md and docs/Project-Constraints.md, populate required placeholders, and present a reviewable plan/diff before final acceptance. If critical context is ambiguous or missing, ask me to @-attach the most relevant files before applying changes.
```

## What Bootstrap Creates

| Output                        | Description |
|-------------------------------|-------------|
| `ROADMAP.md`                  | Living task list with priorities and status |
| `docs/File-Structure-Reference.md` | Auto-generated map of the project layout |
| `docs/Project-Constraints.md` | Inferred tech stack, quality commands, and architectural constraints |
| Proposed placeholder updates  | Suggests placeholder population changes (for example `[PROJECT_NAME]`, `[MAIN_LANGUAGE]`, quality commands) with evidence for review |
| `docs/` directory             | Created when missing so generated docs have a stable location |

## Inference Inputs

Bootstrap primarily infers information from:

1. Explicit project documents (`design-doc.md`, `requirements.md`, PRD, ADR, architecture notes)
2. Detected configuration files (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, etc.)
3. Conservative fallback defaults (clearly labeled as assumptions) when evidence is incomplete

The exact weighting is model- and context-dependent; treat this as guidance rather than a hard deterministic order.

## Mandatory Review Gate

Bootstrap **never** applies changes silently. You must:

- Review the proposed `ROADMAP.md` and documentation
- Approve or modify the inferred tech stack and quality commands
- Confirm any assumptions the bootstrap made
- Ensure existing `README.md` content is preserved (bootstrap should only create it when missing)

This preserves the safety-first philosophy of the kit.

## Tips for Best Results

1. **Provide rich context** — The more design documents you give it, the better the output.
2. **Use Plan Mode first** — For complex projects, start in Plan Mode so you can review the high-level plan before execution.
3. **Iterate** — If the first bootstrap misses something, just run it again with additional context.
4. **Don't fight it** — If bootstrap makes a wrong assumption, correct it in the review step rather than trying to prevent it.

## After Bootstrap

Once bootstrap completes successfully, you should:

- Review and commit the generated `ROADMAP.md`
- Verify that quality commands in the rules actually work in your project
- Start using the kit normally (subagents, hooks, RIPER, etc.)

## Related

- [Installation Guide](../INSTALL.md)
- [Using Subagents](using-subagents.md)
- [Using Hooks Effectively](using-hooks.md)
- [RIPER + Subagents Workflow](riper-with-subagents.md)
- [Cursor Docs](https://cursor.com/docs)