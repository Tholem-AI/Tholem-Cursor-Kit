# Proposed Improvements for Integrated Cursor AI Agent Rules System (2026 Update)

**Repository:** https://github.com/Tholem-AI/Tholem-Cursor-Kit  
**Current Status:** Legacy and 2026 patterns are mixed  
**Target:** Minimal runtime `.cursor/`, requirements-driven bootstrap, no manual cleanup artifacts

---

## Executive Summary

This update keeps the kit low friction while removing cleanup-heavy artifacts from runtime files.

Key outcomes:
- Runtime `.cursor/` contains operational content only.
- Technology stack constraints are inferred from project inputs, then review-gated.
- Documentation continuity is always-on baseline behavior, with Generate Memories additive.
- Legacy files are migrated with a deterministic matrix and full manifest.

---

## 1. Installation Philosophy (2026)

**Default path (Tier A):**
1. Copy minimal `.cursor/` into project root.
2. Start using the kit.

**Bootstrap path (Tier B):**
1. Add design/requirements artifacts if available.
2. Run a single bootstrap prompt.
3. Review proposed changes before apply.

Canonical prompt:

> Bootstrap this project using the included bootstrap-project skill. Analyze design and requirements docs if present, initialize ROADMAP.md, populate required placeholders, and propose all changes for review before applying.

---

## 2. Runtime vs Reference Boundary

### Runtime package (`.cursor/`)
Must include only:
- Required runtime rules
- Required runtime agents/subagents
- Required runtime skills
- Required placeholders and enforceable policy

Must exclude:
- Tutorial prose
- Long examples intended for deletion
- Narrative documentation

### Reference package (`docs/`, `examples/`, templates)
Contains:
- Explanations, rationale, walkthroughs
- Optional patterns and demonstrations
- Migration references and implementation notes

---

## 3. Legacy Transition Strategy

Use a temporary `legacy-system/` container in migration branches only.

Workflow:
1. Inventory all legacy files.
2. Classify each file: `runtime`, `docs`, or `deprecated`.
3. Build the new runtime package from `runtime` files only.
4. Move explanatory content to docs/examples/templates.
5. Add replacement/sunset notes for deprecated files.

Release rules:
- First public commit must not include the temporary legacy container.
- If parity checks fail, use a short-lived migration branch or prerelease tag.

---

## 4. Major Technical Improvements

### 4.1 2026 Surface Alignment (High Priority)
- Keep runtime-compatible support for rules, skills, subagents, and optional hooks.
- Keep guidance for AGENTS.md and memory behavior in reference docs.
- Avoid bundling optional enterprise automation into default install.

### 4.2 RIPER Evolution (High Priority)
- Deliver limited v1 subagent topology first (small, role-focused).
- Add orchestration gradually, after baseline install/bootstrapping is stable.

### 4.3 Task Management (Medium-High Priority)
- Shift from cleanup-heavy task artifacts to `ROADMAP.md` lifecycle.
- Keep updates deterministic and review-gated.

### 4.4 Memory System (Medium Priority, Default-On Documentation Baseline)
- Documentation continuity is the default baseline, always enabled.
- For users not using Generate Memories, rules/agents/skills must still persist state through docs and roadmap updates.
- Integration requirements:
  - **Rules:** enforce update checkpoints for `ROADMAP.md` and required docs after major changes.
  - **Agents/Subagents:** emit concise handoff summaries for completed phases.
  - **Skills:** bootstrap/updater workflows write deterministic context summaries.
- Generate Memories is additive and should be enabled by default where available and privacy policy permits; it does not replace documentation hygiene.

### 4.5 Documentation Maintenance (Medium Priority)
- Keep documentation ownership explicit (single primary owner).
- Prevent duplicate ownership between `reviewer-agent` and `documentation-maintainer`.

### 4.6 Technology Stack Updates (High Priority, Bootstrap-Derived)
- Remove fixed-version-first policy as primary behavior.
- Stack/version constraints are populated by bootstrap using this precedence:
  1. Project requirements/design docs
  2. Detected project config files
  3. Conservative fallback defaults
- Bootstrap writes inferred stack constraints to runtime placeholders and presents a review diff before apply.
- Fallback defaults are assumptions for missing metadata, not mandatory target versions.

---

## 5. Specific File Changes (Complete Root Register)

All current project-root files are listed with explicit disposition.

| Path | Classification | Planned Action | Reason | Owner | Validation |
|---|---|---|---|---|---|
| `.gitignore` | static | Keep as-is unless new generated paths appear | Repo hygiene baseline | Migration Governance | Git status remains clean during bootstrap runs |
| `090-completed_tasks.mdc` | docs | Move historical/completed-task guidance to reference docs; keep runtime lean | Not required for runtime behavior | Documentation and Examples | Confirm references preserved in docs |
| `011-cursor_project_rules.mdc` | runtime | Update placeholders to bootstrap-derived stack constraints; remove fixed-version prose | Runtime policy file, now requirements-driven | Runtime Core | Placeholder population appears in reviewed bootstrap diff |
| `022-cursor_git_rules.mdc` | runtime | Retain operational git safety rules; trim explanatory examples | Required runtime guardrails | Runtime Core | Rule loads and applies without manual cleanup |
| `021-cursor_environment_rules.mdc` | runtime | Keep operational environment constraints; move explanatory walkthroughs to docs | Runtime policy only in `.cursor/` | Runtime Core | No long tutorial content in runtime file |
| `CONTRIBUTING.md` | docs | Update to new migration + runtime/reference boundary workflow | Contributor process documentation | Documentation and Examples | Contributor flow matches sections 2 and 3 |
| `012-learned_memories.mdc` | deprecated | Deprecate runtime use; migrate memory continuity expectations into docs + runtime checkpoints | Replaced by documentation-baseline memory policy | Migration Governance | Replacement path documented and referenced |
| `032-cursor_quality_rules.mdc` | runtime | Keep enforceable quality gates; remove narrative examples | Runtime quality behavior remains required | Runtime Core | File remains operational-only |
| `EXAMPLES.md` | docs | Expand as primary example location for patterns removed from runtime files | Central reference location for demos | Documentation and Examples | Runtime files reference this path instead of embedding examples |
| `030-cursor_task_rules.mdc` | runtime | Align to `ROADMAP.md` lifecycle; remove task-list duplication | Runtime task policy should be deterministic | Runtime Core | No conflicting task system remains |
| `README.md` | docs | Refresh installation summary and bootstrap expectations | Public entrypoint for low-friction install | Documentation and Examples | Steps align with section 1 |
| `013-cursor_riper_rules.mdc` | runtime | Keep minimal RIPER operational rules; avoid broad orchestration text | Runtime should stay concise | RIPER and Subagents | Works with v1 limited topology |
| `010-cursor_general_rules.mdc` | runtime | Keep foundational runtime constraints; move explanatory rationale to docs | Runtime baseline | Runtime Core | No cleanup-prone sample blocks remain |
| `LICENSE` | static | Keep as-is | Legal artifact | Migration Governance | File unchanged in release comparison |
| `031-cursor_memory_rules.mdc` | runtime | Update to enforce documentation-first continuity checkpoints; Generate Memories additive | Implements section 4.4 baseline | Runtime Core | Checkpoints trigger documented update behavior |
| `040-cursor_organization_rules.mdc` | runtime | Keep organizational constraints that affect runtime behavior; move narrative process notes out | Maintain runtime clarity | Runtime Core | Runtime-only content confirmed |
| `020-task_list.mdc` | deprecated | Deprecate/remove in favor of `ROADMAP.md` model and updater workflows | Superseded by deterministic roadmap lifecycle | Migration Governance | Deprecation note and successor path documented |
| `091-learned_memories_archive.mdc` | docs | Archive as reference-only historical material outside runtime payload | Historical context, not runtime | Documentation and Examples | Linked from migration docs as archive |
| `docs/migration/Cursor-Rules-System-2026-Improvements-Overview.md` | docs | Keep as canonical strategy document; maintain consistency with migration matrix and section 5 | Governance source | Migration Governance | Cross-check passes with runtime policy and manifest schema |
| `docs/migration/Phase-1-Minimal-Runtime-Foundation-Plan.md` | docs | Planning-only Phase 1 blueprint; source sections reference the overview | Phase 1 governance | Migration Governance | Linked from README and overview |
| `migration-manifest.yaml` | static | Track legacy-system inventory and classification through migration | Traceability for parity gates | Migration Governance | Validates with `python scripts/validate_setup.py` (kit repo) |
| `scripts/README.md` | docs | Update script usage docs to support migration validation and parity checks | Developer support docs | Documentation and Examples | Script docs map to validation column actions |
| `scripts/validate_setup.py` | runtime | Update validation checks for runtime/reference boundary and no-cleanup acceptance | Enforces migration quality gates | Migration Governance | Script validates required acceptance criteria |

---

## 6. Hard Migration Decision Matrix

Apply in order. First match wins.

### Rule 1: `runtime` (all must be true)
- Required for runtime behavior (rule enforcement, agent/subagent invocation, skill execution, or required validation).
- Contains operational logic only (no tutorial prose or cleanup-prone examples).
- Works after copy with no manual edits beyond declared placeholders.

### Rule 2: `docs` (any true)
- Primarily explanatory, instructional, or optional-pattern content.
- Contains sample content expected to be edited/deleted by users.
- Supports understanding rather than runtime execution.

### Rule 3: `deprecated` (any true)
- Superseded by newer runtime components/processes.
- Conflicts with minimal runtime policy or ownership clarity.
- No active install path depends on it after migration.

Tie-breakers:
- If uncertain between `runtime` and `docs`, classify as `docs`.
- `runtime` requires explicit owner sign-off and no-cleanup proof.
- Unowned files cannot remain `runtime`.

Manifest fields per file:
- `legacyPath`
- `classification`
- `reason`
- `owner`
- `replacement`
- `validation`

---

## 7. Phased Rollout and Acceptance

### Phase 1: Runtime Foundation
- Inventory files and classify with matrix.
- Minimize runtime payload.

### Phase 2: Bootstrap Hardening
- Enforce requirements-driven stack inference and review-gated placeholder updates.
- Enforce documentation continuity baseline.

### Phase 3: RIPER/Subagent v1
- Limited topology, clear ownership, concise runtime artifacts.

### Phase 4: Optional Advanced Packs
- Hooks and advanced/enterprise extras remain opt-in.

Final release gate:
- No temporary legacy container in first public commit.
- Manifest complete for all root files.
- Section 5 register and runtime payload are consistent.

---

## 8. Validation Checklist

- Install remains low friction (copy `.cursor/`, optional one prompt).
- No runtime file requires post-bootstrap cleanup.
- Section 4.4 behavior is default-on for documentation continuity.
- Section 4.6 behavior is requirements/design-driven and review-gated.
- Section 5 includes every current root file with explicit action.
- No contradictions between runtime policy, migration matrix, and file register.
# Proposed Solutions for Scope Audit: 2026 Improvements

**Repository:** https://github.com/Tholem-AI/Tholem-Cursor-Kit  
**Current Status:** Legacy system contains runtime + reference content mixed together  
**Target:** Minimal runtime `.cursor/` package, zero cleanup customization, phased migration

---

## 1) Purpose and Scope Boundaries

This document defines how to modernize the kit for 2026 while keeping installation and customization low friction.

In scope:
- Runtime package minimization (`.cursor/` only operational content)
- Install and bootstrap flow
- Legacy migration strategy
- Workstream phasing and ownership boundaries

Out of scope for initial public release:
- Full enterprise-only feature packs
- Large optional automation bundles that increase default install friction

---

## 2) Measurable Success Criteria

The update is considered successful only when all criteria are true:

- Install path requires at most 3 manual steps.
- Default install remains: copy `.cursor/` into project root.
- Optional bootstrap path uses one canonical prompt with user review before applying changes.
- Runtime `.cursor/` files contain operational logic and placeholders only (no tutorial prose or long examples).
- Bootstrap customization requires zero manual artifact cleanup in runtime files.
- Every migrated legacy file is classified in a migration manifest as `runtime`, `docs`, or `deprecated`.
- First public commit includes no temporary legacy container artifacts.

---

## 3) Runtime Payload Policy (`.cursor/` Minimum Contract)

The copyable `.cursor/` package must include only:
- Required rules for runtime behavior
- Required subagent definitions for runtime behavior
- Required skills for runtime behavior
- Required hook configuration only if explicitly part of default runtime (otherwise opt-in)

The copyable `.cursor/` package must not include:
- Tutorial walkthroughs
- Verbose examples intended for deletion
- Narrative documentation that belongs in `docs/`

If a file is not required for runtime behavior, it must not be in the copyable `.cursor/`.

---

## 4) Documentation and Example Separation Policy

All explanatory content is separated from runtime content:

- `docs/`: Concept explanations, decision rationale, migration guidance
- `examples/`: Demonstration patterns and optional variations
- Templates: Reusable starter artifacts users intentionally instantiate

Operational rule/agent/skill files should reference docs briefly rather than embedding long instructions.

---

## 5) Low-Friction Install Experience

### Tier A (Default)
1. Copy minimal `.cursor/` into project root.
2. Start using the kit.

### Tier B (Optional Bootstrap)
1. Add design/requirements documents (if available).
2. Run one canonical bootstrap prompt using `bootstrap-project`.
3. Review proposed changes before applying.

### Tier C (Advanced Team Workflows)
- Template repository / subtree / submodule workflows for larger teams.

---

## 6) Canonical Bootstrap Prompt and Outputs

Canonical prompt:

> Bootstrap this project using the included bootstrap-project skill. Analyze design and requirements docs if present, initialize ROADMAP.md, populate required placeholders, and propose all changes for review before applying.

Required bootstrap outputs:
- `ROADMAP.md` initialized
- Required placeholders populated in runtime files
- Documentation skeleton created or updated in docs area
- Proposed changes presented for user review

Prohibited bootstrap behavior:
- Injecting cleanup-prone examples into runtime `.cursor/` files
- Silent application of changes without review

---

## 7) Workstreams and Ownership Boundaries

### A. Runtime Core
- Maintains runtime rules/agents/skills required for execution
- Enforces minimum runtime contract

### B. Documentation and Examples
- Owns `docs/`, `examples/`, templates
- No runtime policy logic embedded in documentation artifacts

### C. RIPER and Subagents
- Delivers limited v1 topology first
- Avoids broad multi-agent expansion in initial phase

### D. Hooks (Opt-In Pack)
- Provides optional hooks guidance and examples
- Includes strict guardrails for matcher scope, fail behavior, and loop limits

### E. Migration Governance
- Owns legacy manifest, classification decisions, and parity gates

Single-owner rule: no duplicated authority between `reviewer-agent` and `documentation-maintainer`; one must be primary.

---

## 8) Legacy Rules System Transition Plan

During migration only, use a temporary container for legacy content:
- Example container: `legacy-system/`
- Purpose: preserve full legacy source while extracting minimal runtime package

Strict extraction workflow:
1. Inventory all legacy files.
2. Classify each file via the hard migration matrix.
3. Build new runtime `.cursor/` from `runtime` files only.
4. Move explanatory content to docs/examples/templates.
5. Mark deprecated files with replacement path and sunset note.

Release guardrails:
- Legacy container exists only in migration branches.
- First public commit removes the legacy container after parity checks pass.
- If parity fails, ship a short-lived migration branch or prerelease tag instead of mixed structures.

---

## 9) Hard Migration Decision Matrix

Apply in order. First match wins.

### Rule 1: `runtime` (all must be true)
- File is required for runtime behavior (rule enforcement, subagent invocation, or skill execution).
- File does not contain tutorial prose, long examples, or cleanup-prone scaffold text.
- File can be used after copy with no manual edits beyond declared placeholders.

### Rule 2: `docs` (any true)
- File primarily explains concepts, walkthroughs, or optional patterns.
- File includes sample content users are expected to delete or heavily rewrite.
- File is reference material instead of required runtime logic.

### Rule 3: `deprecated` (any true)
- File duplicates behavior replaced by new components.
- File conflicts with minimal runtime policy or creates ownership ambiguity.
- No active install path depends on file after migration.

Tie-breakers:
- If unsure between `runtime` and `docs`, choose `docs`.
- `runtime` requires owner sign-off plus no-cleanup proof.
- Unowned files cannot remain in `runtime`.

Required manifest fields per file:
- `classification`: `runtime` | `docs` | `deprecated`
- `reason`: one sentence tied to matrix rule
- `owner`: responsible maintainer/workstream
- `replacement`: new path or successor component (if non-runtime)
- `validation`: proof step (loads in Cursor, bootstrap output check, or deprecation note)

---

## 10) Proposed Phased Rollout

### Phase 1: Minimal Runtime Foundation
- Legacy inventory and classification
- Temporary legacy container in migration branch
- Runtime payload minimization

Exit criteria:
- Runtime package passes minimal contract
- Initial migration manifest exists

### Phase 2: Bootstrap and Install Hardening
- Canonical install docs and quickstart
- Bootstrap output guarantees
- No-artifact-cleanup acceptance checks

Exit criteria:
- Bootstrap path is deterministic and review-gated
- Install steps meet <=3 target

### Phase 3: RIPER/Subagent v1
- Limited role topology first
- Clear boundaries between runtime logic and documentation

Exit criteria:
- v1 workflow is stable and non-bloated

### Phase 4: Hooks + Advanced/Enterprise Extras (Opt-In)
- Hooks examples and guardrails
- Advanced features gated behind opt-in paths

Exit criteria:
- Default install remains unaffected by advanced packs

Release gate:
- Remove temporary legacy container before first public commit
- Confirm manifest parity and validation checklist completion

---

## 11) Validation Checklist

- No duplicated ownership across skills/agents/docs automation.
- No umbrella section mixing unrelated surfaces without concrete deliverables.
- Every major claim has measurable acceptance criteria.
- Default install remains copy `.cursor/` + optional single bootstrap prompt.
- Runtime `.cursor/` files contain operational logic only.
- Explanations/examples are externalized to docs/examples/templates.
- Bootstrap customization requires zero manual runtime cleanup.
- Hooks guidance includes matcher/failClosed/loop_limit guardrails when enabled.
- Legacy files are fully classified and tracked in migration manifest.
- First public commit contains no temporary legacy container artifacts.

---

## 12) Appendix: Migration Manifest Schema and Change Register

Migration manifest schema:

```yaml
legacyPath: string
classification: runtime | docs | deprecated
reason: string
owner: string
replacement: string
validation: string
```

Initial change register targets:
- Rewrite install narrative around minimal runtime copy model
- Remove runtime-embedded example prose
- Add migration and deprecation mapping for legacy files
- Phase and scope RIPER/subagent rollout
- Keep hooks optional and policy-guarded
# Proposed Improvements for Integrated Cursor AI Agent Rules System (2026 Update)

**Repository:** https://github.com/Tholem-AI/Tholem-Cursor-Kit
**Current Status:** Last updated May 2025  
**Target:** Modernize for Cursor 2026 with low-friction installation

---

## Executive Summary

The original system is still excellent in its core philosophy (safety-first design, modular rules, cross-rule integration, and structured RIPER methodology). However, Cursor has evolved significantly since May 2025.

**New Core Philosophy for 2026:**
- **Ultra-low friction installation** — Simple drop of the `.cursor/` folder
- **Smart first-use automation** — `bootstrap-project` skill creates necessary files automatically
- **Single-prompt advanced setup** — Design doc + requirements doc drives intelligent initialization
- **Clean development workflow** — Use a staging directory so rules don't load while editing

**Key Changes:**
- Move from pre-included templates → Intelligent bootstrap on first use
- Evolve RIPER using Subagents for better parallelism
- Replace heavy task lists with `ROADMAP.md` + automation
- Full support for 2026 features (Subagents, Skills, Hooks, AGENTS.md, etc.)
- Add staging directory for safe development

---

## 1. New Installation Philosophy (2026)

**Goal:** Make the system extremely easy to adopt while remaining powerful.

### Primary Installation Method: Simple Drop-In + Bootstrap

1. Copy the entire `.cursor/` folder into the project root
2. (Recommended) Drop your `design-doc.md` and `requirements.md` into the project
3. Run this single prompt:

> "Bootstrap this project using my design documents. Create ROADMAP.md, populate all placeholders, and set up the initial documentation structure."

The `bootstrap-project` skill then:
- Creates `ROADMAP.md` with initial tasks
- Populates placeholders in the rules
- Sets up `docs/` folder structure
- Runs a lightweight RIPER analysis
- Presents changes for user review

This is the **recommended default experience** — true low-friction installation.

### Alternative: Manual Copy + Staging

Users can also manually copy the `.cursor/` folder and customize files themselves.

---

## 2. Staging Directory (Development Workflow)

**Purpose:** Allow safe editing of the rules without them loading in your main project.

**Recommended simple structure:**

```
staging/
└── .cursor/
    ├── rules/
    ├── agents/
    ├── skills/
    └── ...
```

**Why this works:**
- Cursor only loads rules from the **project root** (`.cursor/rules/`)
- Rules inside `staging/.cursor/` are ignored during development
- When ready to test, copy the folder:
  ```bash
  cp -r staging/.cursor/ /path/to/your-project/
  ```

This is the cleanest and simplest development approach.

---

## 3. Updated File Structure (2026)

```
Integrated-Cursor-AI-Agent-Rules-System/
├── README.md
├── INSTALL.md
├── QUICKSTART.md
├── docs/                              ← Documentation only (no templates)
│   ├── 01-installation.md
│   ├── 02-customization.md
│   ├── 03-bootstrap-flow.md
│   └── ...
├── staging/
├   ── .cursor/                           ← The actual system (what users copy into project root)
│     ├── rules/
│     ├── agents/
│     ├── skills/
│     │   ├── bootstrap-project/         ← Core first-time setup skill
│     │   ├── roadmap-updater/
│     │   └── documentation-maintainer/
│     └── ...
├── examples/
└── LICENSE
```

**Key Design Decisions:**
- No pre-created `ROADMAP.md` or `docs/` templates in the repo (keeps it lean)
- The `bootstrap-project` skill creates all necessary files intelligently on first use
- `staging/.cursor/` is used exclusively for development

---

## 4. Major Technical Improvements

### 4.1 2026 Feature Support (High Priority)
- Full documentation and examples for:
  - Subagents (`.cursor/agents/`)
  - Skills (dynamic workflows)
  - AGENTS.md (nested instructions)
  - Hooks (`.cursor/hooks.json`)
  - Generate Memories + Privacy Mode guidance
  - Automations & Background/Cloud Agents

### 4.2 RIPER Evolution (High Priority)
- Refactor RIPER to leverage Subagents
- Create dedicated subagents:
  - `research-agent`
  - `innovate-agent` (parallel execution)
  - `planner-agent`
  - `executor-agent` (parallel for different modules)
  - `reviewer-agent` (enhanced with documentation maintenance)
- Add `riper-orchestrator` skill to coordinate phases

### 4.3 Task Management (Medium-High Priority)
- Deprecate heavy `020-task_list.mdc`
- Replace with `ROADMAP.md` + `roadmap-updater` skill (automatically maintained)

### 4.4 Memory System (Medium Priority)
- Deprecate heavy custom memory files
- Recommend **Generate Memories** when Privacy Mode is off
- Rely on strong documentation + `ROADMAP.md` when Privacy Mode must stay on

### 4.5 Documentation Maintenance (Medium Priority)
- Add `documentation-maintainer` capability (integrated into reviewer-agent)
- Automatically keep `README.md`, `ROADMAP.md`, and `docs/` clean and up to date

### 4.6 Technology Stack Updates (High Priority)
Update minimum versions in `011-cursor_project_rules.mdc`:
- Python: 3.12+
- Node.js: 20+/22+ LTS
- TypeScript: 5.x+ (strict)
- Go: 1.22+
- Rust: 1.80+

---

## 5. Specific File Changes

| File / Component                    | Action                              | Notes |
|-------------------------------------|-------------------------------------|-------|
| `README.md`                         | Major rewrite                       | New installation philosophy + quick start |
| `011-cursor_project_rules.mdc`      | Update versions + modern patterns   | High priority |
| `013-cursor_riper_rules.mdc`        | Evolve with subagent guidance       | Keep core philosophy |
| `020-task_list.mdc`                 | Deprecate or remove                 | Replaced by ROADMAP.md |
| `012-learned_memories.mdc`          | Deprecate                           | Use Generate Memories instead |
| New: `bootstrap-project` skill      | Create                              | Core of new install flow |
| New: `reviewer-agent.md`            | Enhanced version                    | Includes documentation maintenance |
| New: `roadmap-updater` skill        | Create                              | Maintains ROADMAP.md |
| New: Various subagent files         | Create                              | For RIPER + Subagents model |
| New: `staging/` directory           | Add with `.cursor/` inside          | Development workspace |
| `hooks.json` examples               | Add                                 | Practical hook examples |

---

## 6. Priority & Next Steps

### Priority Levels

| Priority     | Items |
|--------------|-------|
| **High**     | Create `bootstrap-project` skill, update tech versions, add 2026 feature coverage, evolve RIPER with subagents |
| **Medium-High** | Add staging directory + documentation, create `roadmap-updater` + enhanced `reviewer-agent` |
| **Medium**   | Hooks examples, memory system guidance, full README refresh |
| **Low**      | Reduce file count, advanced enterprise features |

### Suggested Implementation Order

1. Create `bootstrap-project` skill + update `INSTALL.md` / `QUICKSTART.md`
2. Update `011-cursor_project_rules.mdc` (tech versions)
3. Set up `staging/` directory + documentation
4. Enhance `reviewer-agent` with documentation maintenance
5. Build RIPER + Subagents system
6. Add Hooks examples
7. Full README refresh with new philosophy

---

## 7. Final Vision

The updated system should deliver this experience:

> **"Drop the `.cursor/` folder into any project. Optionally add your design documents. Run one prompt. Everything else is handled intelligently with full user review."**

This preserves the original repo’s greatest strengths (safety-first design, quality gates, structured methodology) while making adoption dramatically easier in 2026.

---
