---
name: riper-orchestrator
description: Coordinate RIPER phase flow for non-trivial changes and enforce evidence-first handoffs across research, planning, execution, and review.
---

# riper-orchestrator

Coordinate RIPER phase execution using role-specific agents and evidence-first handoffs.

## When to use

- Use for non-trivial work that benefits from explicit phase handoffs and checkpoints.

## Required behavior

1. Trigger scoped research for non-trivial changes.
2. Run innovate checkpoint when alternatives materially affect design.
3. Produce plan milestones with validator gates.
4. Execute implementation in controlled slices.
5. Perform review and documentation continuity checks before closure.

## Invocation and delegation contract

- Treat this skill as orchestration guidance for the parent agent.
- Delegate to role agents explicitly when phase boundaries are reached:
  - `research-agent` for discovery slices
  - `planner-agent` for innovate checkpoint + execution-ready plan
  - `executor-agent` for approved implementation slices
  - `reviewer-agent` for final severity-first validation
- Skill and subagent linkage is behavioral and prompt-driven, not automatic file binding.

## Handoff schema

- `phase`
- `inputs`
- `decision`
- `evidence`
- `open_risks`

## Handoff template

```markdown
phase: <research|plan|execute|review>
inputs:
  - <upstream artifact or decision>
decision: <what was selected, changed, or validated>
evidence:
  - <file path, command output, or verification artifact>
open_risks:
  - <remaining risk or unresolved blocker; use [] when none>
```

## Parallel trigger phrase template

Use this phrase when execution slices are independent:

```text
Execute approved slices in parallel using executor-agent only for independent modules (<sliceA>, <sliceB>); keep shared-state work sequential; return one handoff per slice using phase/inputs/decision/evidence/open_risks, then run reviewer-agent on merged outputs.
```

## Guardrails

- Skip innovate checkpoint only for explicitly trivial changes.
- Keep phase outputs concise and machine-auditable.
- Escalate policy contradictions before execution continues.
