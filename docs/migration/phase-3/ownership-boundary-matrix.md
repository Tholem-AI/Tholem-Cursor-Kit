# Phase 3 Ownership Boundary Matrix

## Purpose

Eliminate duplicated authority across runtime topology, documentation continuity, and migration governance decisions.

## Boundary Rules

- One primary owner per decision surface.
- Approver and consulted roles are explicit and non-overlapping.
- Policy conflicts escalate through governance path before implementation.

## Matrix

| Decision Surface | Primary Owner | Approver | Consulted | Escalation |
|---|---|---|---|---|
| RIPER/subagent v1 topology definitions | RIPER and Subagents | Migration Governance | Runtime Core | Governance dispute review |
| Innovate checkpoint policy (embedded in Planning) | RIPER and Subagents | Migration Governance | Runtime Core, Documentation and Examples | Governance dispute review |
| Runtime enforceability and artifact concision | Runtime Core | Migration Governance | RIPER and Subagents | Governance dispute review |
| Handoff/reporting documentation format | Documentation and Examples | Migration Governance | RIPER and Subagents | Governance dispute review |
| Phase 3 acceptance criteria and release gate | Migration Governance | Migration Governance | Runtime Core, Documentation and Examples, RIPER and Subagents | Final governance ruling |

## Anti-Ambiguity Requirements

- Reviewer surfaces do not own documentation policy by default.
- Documentation surfaces do not override runtime policy enforcement.
- Topology owners do not bypass governance release criteria.
- Innovate checkpoint exception decisions follow the same primary-owner and escalation rules.

## Validation Evidence

Validation passes when:
- each decision surface has one primary owner,
- no duplicate primary ownership exists in the matrix,
- escalation path is explicit for all surfaces.

## Ownership

- Primary Owner: Migration Governance
- Approvers: Runtime Core, Documentation and Examples, RIPER and Subagents
