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

## Handoff schema

- `phase`
- `inputs`
- `decision`
- `evidence`
- `open_risks`

## Guardrails

- Skip innovate checkpoint only for explicitly trivial changes.
- Keep phase outputs concise and machine-auditable.
- Escalate policy contradictions before execution continues.
