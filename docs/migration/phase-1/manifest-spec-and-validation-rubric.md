# Manifest Spec and Validation Rubric

Phase 1 canonical schema and acceptance rubric for `migration-manifest.yaml`.

## Manifest Schema

Required fields per entry:

- `legacyPath`
- `classification` (`runtime` | `docs` | `deprecated` | `static`)
- `reason`
- `owner`
- `replacement`
- `validation`

Additional metadata:

- `manifestVersion`
- `manifestReview` (reviewedBy, reviewedOn, approvedBy)

## Validation Rubric

## 1) Completeness

- Every file under `legacy-system/` is represented by exactly one manifest entry.
- No manifest entry points to a non-existent `legacyPath`.

## 2) Field quality

- All required fields are non-empty.
- `classification` value is in allowed set.
- `owner` corresponds to declared workstream authority.

## 3) Runtime compliance

- Every `classification: runtime` entry includes explicit no-cleanup proof marker:
  - Marker token: `[NO_CLEANUP_PROOF]`
  - Required in `validation` field text.

## 4) Governance consistency

- Manifest decisions are consistent with section 5 register and section 6 matrix in:
  - `docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md`
- Phase 1 artifacts exist under `docs/migration/phase-1/`.

## Approval

Approval is granted when:

1. `python scripts/validate_setup.py --mode kit` returns zero errors.
2. `docs/migration/phase-1/phase-1-signoff.md` marks all exit criteria as complete.

## Exit Criteria Mapping

- Supports exit criterion: "Manifest schema and validation rubric are approved."
