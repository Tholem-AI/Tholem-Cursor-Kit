# Runtime Contract Checklist (Phase 1)

This checklist defines Phase 1 runtime contract evidence for governance validation.

## Runtime Contract

Runtime artifacts must satisfy all checks:

1. Required for runtime behavior.
2. Operational-only content (no tutorial prose, no cleanup-prone samples).
3. Works after copy with no manual edits beyond declared placeholders.
4. Has explicit owner.
5. Has explicit no-cleanup proof.

## No-Cleanup Proof Convention

- Manifest marker: `[NO_CLEANUP_PROOF]`
- Location: `migration-manifest.yaml` `validation` field for each `classification: runtime` entry.
- Validation gate: `scripts/validate_setup.py --mode kit` errors if marker is missing for runtime entries.

## Checklist

| Check | Evidence Source | Gate |
|---|---|---|
| Runtime entry has owner | `migration-manifest.yaml` `owner` | Script schema check |
| Runtime entry has reason | `migration-manifest.yaml` `reason` | Script schema check |
| Runtime entry has replacement path | `migration-manifest.yaml` `replacement` | Script schema check |
| Runtime entry has no-cleanup proof marker | `migration-manifest.yaml` `validation` | Script runtime proof check |
| Staging runtime skeleton exists | `staging/.cursor/{rules,agents,skills}` | Script structural check |

## Exit Criteria Mapping

- Supports exit criterion: "All `runtime` classifications include no-cleanup proof criteria."
