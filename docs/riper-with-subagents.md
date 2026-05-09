# RIPER + Subagents Workflow

This guide explains how to run RIPER using the staged subagent topology in this repository.

## The Problem with Classic RIPER

Traditional RIPER (Research → Innovate → Plan → Execute → Review) works well for small-to-medium tasks, but struggles with large, multi-file refactors because:

- The main agent’s context gets bloated
- Parallel work is difficult
- Error recovery is slow

## The Solution: RIPER + Subagents

Use role-specific subagents with evidence-first handoffs.

### Recommended Subagent Roles

| Phase | Agent | Parallel? | Notes |
|------|------|------|------|
| Research | `research-agent` | Yes | Use multiple researchers for independent discovery slices. |
| Innovate checkpoint | `planner-agent` | No | Innovate is embedded in planning for non-trivial work. |
| Plan | `planner-agent` | No | Produces execution-ready milestones and validation gates. |
| Execute | `executor-agent` | Yes | Parallelize only independent workstreams. |
| Review | `reviewer-agent` | No | Final quality gate with severity-ordered findings. |

## Recommended Workflow

### 1. Research Phase (Parallel)

```
Use the research-agent subagent to explore the current authentication flow, database schema, and existing API patterns. Run 2–3 research agents in parallel if needed.
```

### 2. Innovate Checkpoint Inside Planning

```
Use planner-agent to evaluate at least two viable approaches (including baseline when relevant), summarize tradeoffs, and select one approach before plan finalization.
```

### 3. Plan Phase (Sequential)

The main agent (or `planner-agent`) synthesizes research + innovation into a clear plan with:
- Exact files to modify
- Order of changes
- Dependencies
- Testing strategy

### 4. Execute Phase (Parallel — The Big Win)

```
Break the approved plan into independent workstreams and run executor-agent in parallel only where coupling is low.
```

### 5. Review Phase (Sequential)

```
Use the reviewer-agent to validate all changes against the approved plan. Run quality checks and present a final summary.
```

## Implementation Tips

### Use the `riper-orchestrator` Skill

The kit includes a `riper-orchestrator` skill that guides RIPER sequencing and evidence-first handoffs:

- Trigger scoped research for non-trivial work
- Run innovate checkpoint when alternatives materially affect design
- Enforce milestones and validator gates
- Require review and documentation continuity checks before closure

### Example Prompt

> "Use the riper-orchestrator skill to implement the notification system: run scoped research first, perform innovate checkpoint during planning, execute independent slices in parallel where safe, and finish with reviewer-agent."

## Handoff Checklist

At each phase boundary, include:

- `phase`
- `inputs`
- `decision`
- `evidence`
- `open_risks`

## When to Skip Subagents

- **Simple tasks** (< 20 lines, single file) — Just use normal RIPER or even direct execution
- **Tight coupling** — When changes in one file immediately affect another, sequential execution is safer
- **High-stakes security work** — Sometimes you want the main agent to stay in full control

## Best Practices

1. **Parallelize discovery and execution selectively** — Favor independence over speed.
2. **Keep innovate in planning** — Use planner checkpoint fields for non-trivial changes.
3. **Always end with Review** — Reviewer output should be severity-first with residual risks.
4. **Preserve evidence at every handoff** — Missing evidence should block closure.
5. **Use Plan Mode first for larger work** — Approve approach before implementation slices.

## Related

- [Using Subagents](using-subagents.md)
- [Using Hooks Effectively](using-hooks.md)
- [Cursor Docs](https://cursor.com/docs)