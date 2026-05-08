# Phase 4 Hooks Guardrails and Activation Checklist

## Purpose

Define safe, auditable hook usage for optional advanced packs without impacting default runtime behavior.

## Activation Policy

- Hooks are opt-in only.
- Activation method and scope must be explicit.
- Hook deactivation path must be documented and reversible.

## Guardrails

- Hooks must preserve review-before-apply behavior.
- Hooks must report intended side effects before execution.
- Hooks must fail safely when prerequisites are missing.
- Hooks must honor ownership and escalation boundaries.

## Pass/Fail Checklist

### Pass criteria
- [ ] Hook activation is explicit and opt-in.
- [ ] Trigger surfaces and side effects are documented.
- [ ] Rollback/deactivation behavior is documented and testable.
- [ ] Hook behavior is review-gated before apply.
- [ ] Missing prerequisites produce safe fallback behavior.
- [ ] Ownership and escalation path are declared.

### Fail criteria
- [ ] Hook behavior activates without explicit opt-in.
- [ ] Side effects are hidden, undocumented, or non-auditable.
- [ ] Hook behavior bypasses review checkpoints.
- [ ] Rollback path is missing or destructive.
- [ ] Hook failures break baseline install/runtime flow.
- [ ] Policy conflicts have no escalation owner.

## Prohibited Hook Patterns

- Silent destructive file operations.
- Hidden network calls or policy-changing side effects.
- Auto-apply actions that bypass human review.
- Cross-surface authority overrides with no governance record.

## Validation Evidence

Validation passes when:
- hook policy is explicit and opt-in,
- safety and rollback behavior are auditable,
- prohibited patterns are explicitly blocked,
- default runtime remains unaffected when hooks are disabled.

## Ownership

- Primary Owner: Runtime Core
- Governance Approver: Migration Governance
- Documentation Approver: Documentation and Examples
