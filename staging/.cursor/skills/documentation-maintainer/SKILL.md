---
name: documentation-maintainer
description: Keep runtime documentation aligned with implemented behavior when docs drift or policy changes are detected.
paths:
  - "docs/**/*.md"
  - "README.md"
  - "INSTALL.md"
---

# documentation-maintainer

Keep runtime-facing documentation in sync with implemented behavior.

Primary ownership: documentation continuity policy and content updates for
runtime docs.

## When to use

- Use when implementation or policy changes can make docs stale or contradictory.

## Required behavior

1. Detect docs impacted by runtime or policy changes.
2. Propose focused updates to keep install and framework docs aligned.
3. Keep generated project baseline docs aligned with current implementation:
   - `docs/File-Structure-Reference.md`
   - `docs/Project-Constraints.md`
   - `README.md` when present
4. Ensure evidence pointers in docs remain valid and specific.
5. Report stale or contradictory guidance as blockers.
6. Accept reviewer escalation when documentation remediation is required.

## Guardrails

- Prefer precise updates over broad rewrites.
- Preserve authority order references when documenting policy decisions.
- Do not claim validation outcomes without command evidence.
