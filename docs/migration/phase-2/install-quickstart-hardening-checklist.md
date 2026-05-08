# Phase 2 Install and Quickstart Hardening Checklist

## Purpose

Harden user-facing install guidance so it aligns with 2026 low-friction policy and bootstrap review safeguards.

## Canonical Flow Requirements

### Tier A (Default)
1. Copy minimal `.cursor/` into project root.
2. Start using the kit.

### Tier B (Optional Bootstrap)
1. Add requirements/design docs if available.
2. Run canonical bootstrap prompt.
3. Review proposed changes before apply.

## Checklist

### INSTALL.md
- [ ] Describes Tier A and Tier B clearly.
- [ ] Includes canonical bootstrap prompt.
- [ ] States review-before-apply requirement.
- [ ] Avoids cleanup-heavy post-install instructions.

### QUICKSTART.md
- [ ] Provides shortest path to first successful use.
- [ ] Includes optional bootstrap path without forcing it.
- [ ] Mentions evidence-based inference and review gate.
- [ ] Avoids contradictory workflow steps.

### Cross-doc consistency
- [ ] `README.md`, `INSTALL.md`, and `QUICKSTART.md` are consistent.
- [ ] Flow wording matches migration overview policy sections.
- [ ] No legacy cleanup/deletion-first guidance remains.

## Validation Evidence

Validation passes when:
- placeholder status in install docs is removed,
- canonical Tier A/Tier B flow appears in both install docs,
- review-gated bootstrap behavior is explicitly documented.

## Ownership

- Primary Owner: Documentation and Examples
- Policy Approver: Migration Governance
- Runtime Consistency Approver: Runtime Core
