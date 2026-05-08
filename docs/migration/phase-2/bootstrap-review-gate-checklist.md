# Phase 2 Bootstrap Review Gate Checklist

## Purpose

Define mandatory review requirements for bootstrap-proposed changes before any apply step.

## Required Review Artifact

Every bootstrap run must produce a proposal artifact before apply that includes:
- changed files list,
- placeholder/value updates by file,
- rationale and evidence source per change,
- unresolved assumptions and open questions,
- explicit apply/no-apply checkpoint.

## Pass/Fail Checklist

### Pass criteria
- [ ] Proposal artifact exists and is readable.
- [ ] Every changed file is listed.
- [ ] Every placeholder update has rationale and evidence source.
- [ ] Fallback-derived values are marked as assumptions.
- [ ] Conflicts are surfaced, not auto-resolved silently.
- [ ] User review checkpoint is explicit before apply.

### Fail criteria
- [ ] Bootstrap applies changes without review output.
- [ ] Proposal omits file-level change visibility.
- [ ] Evidence mapping is missing for one or more updates.
- [ ] Assumption-based values are unlabeled.
- [ ] Conflicts are silently overwritten.

## Required Proposal Format (Minimum)

1. Context summary
2. Detected inputs
3. Proposed changes (path + placeholder + value + source)
4. Assumptions and conflicts
5. Review decision prompt

## Validation Evidence

Validation passes when:
- review artifact is always present,
- proposal structure is complete,
- no silent apply behavior is observed in bootstrap workflow.

## Ownership

- Primary Owner: Migration Governance
- Runtime Behavior Approver: Runtime Core
- Documentation Format Approver: Documentation and Examples
