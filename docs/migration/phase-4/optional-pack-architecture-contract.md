# Phase 4 Optional Pack Architecture Contract

## Purpose

Define the packaging and activation boundaries that keep advanced capabilities optional while preserving a minimal default runtime.

## Boundary Model

- Default runtime remains baseline and operational-only.
- Optional packs are additive and must never auto-activate.
- Enterprise-oriented extras are isolated to opt-in surfaces.
- Default install documentation and behavior must remain unchanged by optional-pack presence.

## Required Architecture Rules

1. **Activation is explicit**
   - Optional packs require an explicit enablement signal.
   - No implicit enablement by file discovery or background automation.

2. **Separation is enforceable**
   - Optional-pack artifacts remain under dedicated advanced pack surfaces.
   - Baseline runtime paths must not depend on optional-pack files.

3. **Dependencies are declared**
   - Each optional pack defines prerequisites, supported contexts, and fallback behavior.
   - Missing prerequisites must degrade safely without blocking default flow.

4. **Review remains mandatory**
   - Optional-pack changes are review-gated before apply.
   - Proposed changes must include file-level impact and rollback notes.

## Prohibited Patterns

- Silent activation of hooks or advanced orchestration paths.
- Runtime-default references that require optional pack artifacts to function.
- Packaging that mixes baseline and advanced policy in a single non-separable artifact.
- Optional-pack behavior that bypasses review or ownership controls.

## Validation Evidence

Validation passes when:
- optional-pack boundaries are explicit and non-overlapping with default runtime,
- activation path is explicit opt-in and auditable,
- fallback behavior is defined for missing prerequisites,
- prohibited patterns are documented and testable.

## Ownership

- Primary Owner: Runtime Core
- Governance Approver: Migration Governance
- Consulted: RIPER and Subagents, Documentation and Examples
