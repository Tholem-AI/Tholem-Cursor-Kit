# Phase 3 Runtime Artifact Concision Checklist

## Purpose

Keep runtime files concise and operational-only while Phase 3 expands RIPER/subagent surfaces.

## Runtime Concision Policy

Runtime files must include:
- enforceable operational logic,
- declared placeholders and required constraints,
- minimal references to docs for explanatory context.

Runtime files must not include:
- tutorial walkthroughs,
- long examples expected to be edited/deleted,
- duplicated narrative policy already owned by docs.

## Checklist

### Runtime content checks
- [ ] Runtime files remain operational-only.
- [ ] Explanatory narrative is externalized to docs.
- [ ] No cleanup-prone scaffold prose is introduced.
- [ ] Placeholder usage remains deterministic and review-gated.

### Cross-surface consistency checks
- [ ] Runtime references point to canonical docs paths.
- [ ] No contradictory policy text exists between runtime and docs.
- [ ] New v1 topology artifacts do not bloat default runtime install flow.

## Validation Evidence

Validation passes when:
- runtime artifacts remain concise and enforceable,
- docs own explanatory content,
- runtime/doc boundaries remain consistent with migration policy.

## Ownership

- Primary Owner: Runtime Core
- Documentation Boundary Approver: Documentation and Examples
- Governance Approver: Migration Governance
