# Using Subagents

Subagents let you delegate scoped work to role-focused agents while keeping the main thread concise and reviewable.

## What Are Subagents?

A subagent is an agent profile defined by a markdown file with frontmatter. In this kit, those definitions are staged under `staging/.cursor/agents/` and then copied into `.cursor/agents/` for active use.

Each subagent should:

- Own a clear responsibility boundary
- Return evidence-backed output for the next phase
- Avoid overlapping policy with rules

## Kit-Shipped Subagents (Source of Truth)

The staged runtime currently ships these agent files:

- `research-agent` (`staging/.cursor/agents/research-agent.md`)
- `planner-agent` (`staging/.cursor/agents/planner-agent.md`)
- `executor-agent` (`staging/.cursor/agents/executor-agent.md`)
- `reviewer-agent` (`staging/.cursor/agents/reviewer-agent.md`)

Role intent at a glance:

- **Research**: read-only discovery and evidence capture
- **Planner**: execution-ready plan plus innovate checkpoint for non-trivial work
- **Executor**: implementation slices with validator-gated progression
- **Reviewer**: final quality/risk/readiness review

## Platform Subagents vs Kit Subagents

Cursor may expose additional built-in/tooling-oriented subagents (for example exploration or shell helpers), but those are platform capabilities, not kit-authored runtime artifacts. Treat `staging/.cursor/agents/` as the canonical list for this repository.

See [Cursor Docs](https://cursor.com/docs) for current platform behavior.

## Customize Subagents Safely

Subagents are markdown contracts with YAML frontmatter:

```markdown
---
name: security-auditor
description: Reviews code for security vulnerabilities before release.
model: inherit
readonly: true
is_background: false
---

Purpose: perform evidence-backed security review.
```

Recommended workflow:

1. Copy staged runtime into active `.cursor/agents/`.
2. Duplicate an existing profile as your baseline.
3. Keep role boundaries tight (research/planning/execution/review).
4. Validate prompt behavior on a small scoped task before broad use.
5. Roll back to staged baseline if behavior drifts.

## Invocation Patterns

### Natural-Language Delegation

> "Use the `research-agent` to map the current auth flow, then hand findings to `planner-agent`."

### Parallel Execution Slice

> "Use parallel `executor-agent` runs for independent modules, then route all outputs through `reviewer-agent`."

## Best Practices

1. Keep descriptions specific so routing remains predictable.
2. Preserve evidence-first outputs for every handoff.
3. Use read-only mode for pure research/audit roles when appropriate.
4. Pair subagents with RIPER checkpoints instead of ad-hoc delegation.
5. Use hooks only when deterministic lifecycle control is required.

## Related

- [RIPER + Subagents Workflow](riper-with-subagents.md)
- [Using Hooks Effectively](using-hooks.md)
- [Cursor Docs](https://cursor.com/docs)