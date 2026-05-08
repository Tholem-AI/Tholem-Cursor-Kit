#!/usr/bin/env python3
"""
Validate Tholem-Cursor-Kit migration layout (manifest + staging) or a consumer
installation under .cursor/rules/.

Usage:
    python scripts/validate_setup.py                    # auto-detect
    python scripts/validate_setup.py --mode kit         # this repository
    python scripts/validate_setup.py --mode install     # project with .cursor/rules
    python scripts/validate_setup.py --project-root ./other --mode install
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# --- shared output -----------------------------------------------------------

class Colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"


class ValidationResult:
    def __init__(self) -> None:
        self.passed = 0
        self.warnings = 0
        self.errors = 0
        self.messages: List[Tuple[str, str]] = []

    def add_pass(self, message: str) -> None:
        self.passed += 1
        self.messages.append(("[PASS]", message))

    def add_warning(self, message: str) -> None:
        self.warnings += 1
        self.messages.append(("[WARN]", message))

    def add_error(self, message: str) -> None:
        self.errors += 1
        self.messages.append(("[ERR ]", message))

    def print_summary(self) -> None:
        print(f"\n{Colors.BOLD}=== VALIDATION SUMMARY ==={Colors.END}")
        print(f"{Colors.GREEN}Passed: {self.passed}{Colors.END}")
        print(f"{Colors.YELLOW}Warnings: {self.warnings}{Colors.END}")
        print(f"{Colors.RED}Errors: {self.errors}{Colors.END}")
        overall = "GOOD" if self.errors == 0 else "NEEDS ATTENTION"
        color = Colors.GREEN if self.errors == 0 else Colors.RED
        print(f"\n{Colors.BOLD}Overall Status: {color}{overall}{Colors.END}")


# --- manifest (PyYAML-free) --------------------------------------------------

_KNOWN_FIELDS = frozenset(
    {
        "legacyPath",
        "classification",
        "reason",
        "owner",
        "replacement",
        "validation",
    }
)
_CLASSIFICATIONS = frozenset({"runtime", "docs", "deprecated", "static"})
NO_CLEANUP_MARKER = "[NO_CLEANUP_PROOF]"
PHASE1_REQUIRED_FILES: Dict[str, str] = {
    "inventory_baseline": "docs/migration/phase-1/inventory-baseline.md",
    "classification_log": "docs/migration/phase-1/classification-decision-log.md",
    "runtime_contract": "docs/migration/phase-1/runtime-contract-checklist.md",
    "manifest_rubric": "docs/migration/phase-1/manifest-spec-and-validation-rubric.md",
    "phase1_signoff": "docs/migration/phase-1/phase-1-signoff.md",
}
PHASE2_REQUIRED_FILES: Dict[str, str] = {
    "inference_contract": "docs/migration/phase-2/bootstrap-inference-contract.md",
    "review_gate": "docs/migration/phase-2/bootstrap-review-gate-checklist.md",
    "continuity_baseline": "docs/migration/phase-2/documentation-continuity-baseline.md",
    "install_hardening": "docs/migration/phase-2/install-quickstart-hardening-checklist.md",
    "validation_rubric": "docs/migration/phase-2/phase-2-validation-rubric.md",
    "phase2_signoff": "docs/migration/phase-2/phase-2-signoff.md",
}
PHASE3_REQUIRED_FILES: Dict[str, str] = {
    "topology_contract": "docs/migration/phase-3/riper-subagent-v1-topology-contract.md",
    "handoff_checklist": "docs/migration/phase-3/orchestration-and-handoff-checklist.md",
    "ownership_matrix": "docs/migration/phase-3/ownership-boundary-matrix.md",
    "runtime_concision": "docs/migration/phase-3/runtime-artifact-concision-checklist.md",
    "validation_rubric": "docs/migration/phase-3/phase-3-validation-rubric.md",
    "phase3_signoff": "docs/migration/phase-3/phase-3-signoff.md",
}
PHASE3_INNOVATE_AUDIT_MARKERS: Dict[str, Tuple[str, ...]] = {
    "topology_contract": (
        "innovate checkpoint",
        "planning-specific innovate checkpoint outputs",
        "checkpoint_skipped: trivial_change",
        "not a standalone v1 agent",
    ),
    "handoff_checklist": (
        "planning handoff must additionally include innovate checkpoint fields when applicable",
        "alternatives_considered",
        "tradeoff_summary",
        "selected_approach",
        "rejected_options_reason",
        "confidence_and_unknowns",
        "checkpoint_skipped: trivial_change",
    ),
}


def parse_migration_manifest(text: str) -> List[Dict[str, str]]:
    entries: List[Dict[str, str]] = []
    current: Optional[Dict[str, str]] = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - legacyPath:"):
            if current:
                entries.append(current)
            _, _, rest = line.partition("legacyPath:")
            current = {"legacyPath": rest.strip()}
        elif current is not None and line.startswith("    ") and ": " in line:
            body = line.strip()
            key, _, val = body.partition(": ")
            key = key.strip()
            if key in _KNOWN_FIELDS and key != "legacyPath":
                current[key] = val.strip()
        elif line.startswith("manifestVersion:") or line.startswith("entries:"):
            continue
    if current:
        entries.append(current)
    return entries


def _extract_status_value(text: str, prefix: str) -> Optional[str]:
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith(prefix):
            _, _, value = line.partition(":")
            return value.strip()
    return None


def load_manifest(project_root: Path) -> List[Dict[str, str]]:
    mf = project_root / "migration-manifest.yaml"
    if not mf.is_file():
        raise FileNotFoundError(mf)
    return parse_migration_manifest(mf.read_text(encoding="utf-8"))


# --- kit repository validation -----------------------------------------------


def _rel_paths_under(root: Path) -> List[str]:
    paths: List[str] = []
    for p in root.rglob("*"):
        if p.is_file():
            paths.append(p.relative_to(root).as_posix())
    return sorted(paths)


def _print_phase1_summary(summary: Dict[str, bool]) -> None:
    print(f"\n{Colors.BOLD}Phase 1 Exit Criteria Mapping:{Colors.END}")
    ordered = [
        ("All root files are classified with owner and reason", "criterion_root_classification"),
        ("All runtime classifications include no-cleanup proof", "criterion_no_cleanup_proof"),
        ("Manifest schema and validation rubric are approved", "criterion_manifest_rubric"),
        ("Ambiguous items resolved/blocked with owner and action", "criterion_ambiguity_resolution"),
        ("Release gate requirements documented and accepted", "criterion_release_gate_acceptance"),
    ]
    for label, key in ordered:
        status = "[PASS]" if summary.get(key, False) else "[ERR ]"
        print(f"  {status} {label}")


def _print_phase2_summary(summary: Dict[str, bool]) -> None:
    print(f"\n{Colors.BOLD}Phase 2 Criteria Mapping:{Colors.END}")
    ordered = [
        ("Bootstrap inference contract complete", "criterion_inference_contract"),
        ("Bootstrap review gate documented", "criterion_review_gate"),
        ("Documentation continuity baseline defined", "criterion_continuity_baseline"),
        ("Install/quickstart hardening artifacts present", "criterion_install_hardening"),
        ("Phase 2 validation rubric present", "criterion_validation_rubric"),
        ("Phase 2 signoff accepted", "criterion_phase2_signoff_accepted"),
    ]
    for label, key in ordered:
        status = "[PASS]" if summary.get(key, False) else "[WARN]"
        print(f"  {status} {label}")


def _print_phase3_summary(summary: Dict[str, bool]) -> None:
    print(f"\n{Colors.BOLD}Phase 3 Criteria Mapping:{Colors.END}")
    ordered = [
        ("RIPER/subagent v1 topology contract complete", "criterion_topology_contract"),
        ("Orchestration and handoff protocol documented", "criterion_handoff_checklist"),
        ("Innovate checkpoint auditable (no new agent)", "criterion_innovate_checkpoint_auditable"),
        ("Ownership boundary matrix defined", "criterion_ownership_boundary"),
        ("Runtime artifact concision policy defined", "criterion_runtime_concision"),
        ("Phase 3 signoff accepted", "criterion_phase3_signoff_accepted"),
    ]
    for label, key in ordered:
        status = "[PASS]" if summary.get(key, False) else "[WARN]"
        print(f"  {status} {label}")


def validate_kit_repo(project_root: Path, result: ValidationResult) -> None:
    print(f"{Colors.BOLD}Kit repository checks (migration manifest + layout)...{Colors.END}")

    try:
        entries = load_manifest(project_root)
    except FileNotFoundError as e:
        result.add_error(f"migration-manifest.yaml missing: {e}")
        return

    if not entries:
        result.add_error("migration-manifest.yaml contains no entries")
        return

    result.add_pass(f"Parsed {len(entries)} manifest entries")

    manifest_paths = []
    schema_errors = 0
    runtime_marker_errors = 0
    for i, ent in enumerate(entries):
        lp = ent.get("legacyPath", "").strip()
        if not lp:
            result.add_error(f"Manifest entry {i} missing legacyPath")
            schema_errors += 1
            continue
        manifest_paths.append(lp)
        p = project_root / lp
        if not p.is_file():
            result.add_error(f"Manifest legacyPath not found: {lp}")
            schema_errors += 1
        else:
            result.add_pass(f"Legacy artifact present: {lp}")

        cls = ent.get("classification", "")
        if cls not in _CLASSIFICATIONS:
            result.add_error(
                f"{lp}: invalid classification {cls!r} (expected one of {_CLASSIFICATIONS})"
            )
            schema_errors += 1
        else:
            for req in ("reason", "owner", "replacement", "validation"):
                if not ent.get(req):
                    result.add_error(f"{lp}: missing {req} (required by manifest schema)")
                    schema_errors += 1

        if cls == "runtime":
            validation_text = ent.get("validation", "")
            if NO_CLEANUP_MARKER not in validation_text:
                result.add_error(
                    f"{lp}: runtime entry missing no-cleanup marker {NO_CLEANUP_MARKER}"
                )
                runtime_marker_errors += 1

    legacy_root = project_root / "legacy-system"
    if not legacy_root.is_dir():
        result.add_error("legacy-system/ directory missing")
        schema_errors += 1
    else:
        disk_files = [
            f"legacy-system/{rel}" for rel in _rel_paths_under(legacy_root)
        ]
        manifest_set = set(manifest_paths)
        for path in disk_files:
            if path not in manifest_set:
                result.add_error(f"File under legacy-system/ not listed in manifest: {path}")
                schema_errors += 1
        for path in manifest_set:
            if not path.startswith("legacy-system/"):
                result.add_error(f"Manifest path unexpected (not under legacy-system/): {path}")
                schema_errors += 1

    overview = (
        project_root / "docs" / "migration" / "Cursor-Rules-System-2026-Improvements-Overview.md"
    )
    phase1 = project_root / "docs" / "migration" / "Phase-1-Minimal-Runtime-Foundation-Plan.md"
    for label, path in (
        ("Governance overview", overview),
        ("Phase 1 plan", phase1),
    ):
        if path.is_file():
            result.add_pass(f"{label} present: {path.relative_to(project_root)}")
        else:
            result.add_error(f"Missing {label}: {path.relative_to(project_root)}")

    staging = project_root / "staging" / ".cursor"
    for sub in ("rules", "agents", "skills"):
        d = staging / sub
        if d.is_dir():
            result.add_pass(f"staging/.cursor/{sub}/ exists")
        else:
            result.add_error(f"staging/.cursor/{sub}/ missing (required skeleton)")

    lic = project_root / "LICENSE"
    if lic.is_file() and lic.stat().st_size > 0:
        result.add_pass("LICENSE present at repository root")
    else:
        result.add_error("LICENSE missing or empty at repository root (see section 5 register)")

    lic_txt = project_root / "LICENSE.txt"
    if lic_txt.is_file():
        result.add_warning(
            "LICENSE.txt found; canonical name is LICENSE per section 5 - remove LICENSE.txt if redundant"
        )

    root_cursor = project_root / ".cursor"
    if root_cursor.exists():
        result.add_warning(
            f"{root_cursor} exists at kit root - keep runtime under staging/.cursor/ during kit development unless intentional"
        )

    artifact_presence: Dict[str, bool] = {}
    for key, rel_path in PHASE1_REQUIRED_FILES.items():
        artifact_path = project_root / rel_path
        artifact_presence[key] = artifact_path.is_file()
        if artifact_presence[key]:
            result.add_pass(f"Phase 1 artifact present: {rel_path}")
        else:
            result.add_error(f"Missing required Phase 1 artifact: {rel_path}")

    signoff_accepted = False
    if artifact_presence.get("phase1_signoff", False):
        signoff_text = (project_root / PHASE1_REQUIRED_FILES["phase1_signoff"]).read_text(
            encoding="utf-8"
        )
        phase1_status = _extract_status_value(signoff_text, "Phase 1 Status")
        signoff_accepted = phase1_status == "ACCEPTED"
        if signoff_accepted:
            result.add_pass("Phase 1 signoff indicates ACCEPTED status")
        else:
            result.add_error(
                "Phase 1 signoff exists but does not declare 'Phase 1 Status: ACCEPTED'"
            )

    phase1_summary = {
        "criterion_root_classification": artifact_presence.get("inventory_baseline", False)
        and artifact_presence.get("classification_log", False),
        "criterion_no_cleanup_proof": runtime_marker_errors == 0,
        "criterion_manifest_rubric": schema_errors == 0
        and artifact_presence.get("manifest_rubric", False),
        "criterion_ambiguity_resolution": artifact_presence.get("classification_log", False),
        "criterion_release_gate_acceptance": signoff_accepted,
    }
    _print_phase1_summary(phase1_summary)

    phase2_artifact_presence: Dict[str, bool] = {}
    for key, rel_path in PHASE2_REQUIRED_FILES.items():
        artifact_path = project_root / rel_path
        phase2_artifact_presence[key] = artifact_path.is_file()
        if phase2_artifact_presence[key]:
            result.add_pass(f"Phase 2 artifact present: {rel_path}")
        else:
            result.add_warning(
                f"Phase 2 artifact missing (expected during Phase 2 rollout): {rel_path}"
            )

    phase2_signoff_accepted = False
    if phase2_artifact_presence.get("phase2_signoff", False):
        phase2_signoff_text = (
            project_root / PHASE2_REQUIRED_FILES["phase2_signoff"]
        ).read_text(encoding="utf-8")
        phase2_status = _extract_status_value(phase2_signoff_text, "Phase 2 Status")
        phase2_signoff_accepted = phase2_status == "ACCEPTED"
        if phase2_signoff_accepted:
            result.add_pass("Phase 2 signoff indicates ACCEPTED status")
        else:
            result.add_warning("Phase 2 signoff is present but not yet ACCEPTED")

    phase2_summary = {
        "criterion_inference_contract": phase2_artifact_presence.get("inference_contract", False),
        "criterion_review_gate": phase2_artifact_presence.get("review_gate", False),
        "criterion_continuity_baseline": phase2_artifact_presence.get("continuity_baseline", False),
        "criterion_install_hardening": phase2_artifact_presence.get("install_hardening", False),
        "criterion_validation_rubric": phase2_artifact_presence.get("validation_rubric", False),
        "criterion_phase2_signoff_accepted": phase2_signoff_accepted,
    }
    _print_phase2_summary(phase2_summary)

    phase3_artifact_presence: Dict[str, bool] = {}
    for key, rel_path in PHASE3_REQUIRED_FILES.items():
        artifact_path = project_root / rel_path
        phase3_artifact_presence[key] = artifact_path.is_file()
        if phase3_artifact_presence[key]:
            result.add_pass(f"Phase 3 artifact present: {rel_path}")
        else:
            result.add_warning(
                f"Phase 3 artifact missing (expected during Phase 3 rollout): {rel_path}"
            )

    phase3_signoff_accepted = False
    if phase3_artifact_presence.get("phase3_signoff", False):
        phase3_signoff_text = (
            project_root / PHASE3_REQUIRED_FILES["phase3_signoff"]
        ).read_text(encoding="utf-8")
        phase3_status = _extract_status_value(phase3_signoff_text, "Phase 3 Status")
        phase3_signoff_accepted = phase3_status == "ACCEPTED"
        if phase3_signoff_accepted:
            result.add_pass("Phase 3 signoff indicates ACCEPTED status")
        else:
            result.add_warning("Phase 3 signoff is present but not yet ACCEPTED")

    innovate_checkpoint_auditable = False
    topology_present = phase3_artifact_presence.get("topology_contract", False)
    handoff_present = phase3_artifact_presence.get("handoff_checklist", False)
    if topology_present and handoff_present:
        marker_missing: Dict[str, List[str]] = {}
        for artifact_key in ("topology_contract", "handoff_checklist"):
            rel_path = PHASE3_REQUIRED_FILES[artifact_key]
            artifact_text = (project_root / rel_path).read_text(encoding="utf-8").lower()
            missing = [
                marker
                for marker in PHASE3_INNOVATE_AUDIT_MARKERS[artifact_key]
                if marker not in artifact_text
            ]
            if missing:
                marker_missing[artifact_key] = missing
        innovate_checkpoint_auditable = not marker_missing
        if innovate_checkpoint_auditable:
            result.add_pass(
                "Phase 3 Innovate checkpoint markers present in topology and handoff artifacts"
            )
        else:
            details = "; ".join(
                f"{PHASE3_REQUIRED_FILES[key]} missing markers: {', '.join(missing)}"
                for key, missing in marker_missing.items()
            )
            result.add_warning(
                "Phase 3 Innovate checkpoint audit markers incomplete - " + details
            )
    else:
        result.add_warning(
            "Phase 3 Innovate checkpoint audit skipped: topology and handoff artifacts are required"
        )

    phase3_summary = {
        "criterion_topology_contract": phase3_artifact_presence.get("topology_contract", False),
        "criterion_handoff_checklist": phase3_artifact_presence.get("handoff_checklist", False),
        "criterion_innovate_checkpoint_auditable": innovate_checkpoint_auditable,
        "criterion_ownership_boundary": phase3_artifact_presence.get("ownership_matrix", False),
        "criterion_runtime_concision": phase3_artifact_presence.get("runtime_concision", False),
        "criterion_phase3_signoff_accepted": phase3_signoff_accepted,
    }
    _print_phase3_summary(phase3_summary)


# --- consumer install validation (legacy rules layout) -----------------------


class InstallRulesValidator:
    """Validates a classic install: .cursor/rules/*.mdc copied from the legacy kit."""

    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root
        self.rules_dir = project_root / ".cursor" / "rules"
        self.result = ValidationResult()
        self.required_files = {
            "010-cursor_general_rules.mdc": "Central coordination hub",
            "011-cursor_project_rules.mdc": "Technology stack templates",
            "012-learned_memories.mdc": "Project knowledge storage",
            "013-cursor_riper_rules.mdc": "RIPER methodology framework",
            "020-task_list.mdc": "Active task management",
            "021-cursor_environment_rules.mdc": "Environment detection",
            "022-cursor_git_rules.mdc": "Git workflow integration",
            "030-cursor_task_rules.mdc": "Task workflow rules",
            "031-cursor_memory_rules.mdc": "Memory management framework",
            "032-cursor_quality_rules.mdc": "Quality assurance gates",
            "040-cursor_organization_rules.mdc": "File organization standards",
            "090-completed_tasks.mdc": "Task completion archive",
            "091-learned_memories_archive.mdc": "Historical knowledge archive",
        }
        self.placeholders = [
            "[PROJECT_NAME]",
            "[PROJECT_COMMAND_QUALITY]",
            "[MAIN_LANGUAGE]",
            "[TECH_STACK]",
            "[FRAMEWORK]",
            "[MIN_VERSION]",
            "[PACKAGE_MANAGER]",
        ]
        self.cross_references = {
            "@010-cursor_general_rules": "010-cursor_general_rules.mdc",
            "@011-cursor_project_rules": "011-cursor_project_rules.mdc",
            "@012-learned_memories": "012-learned_memories.mdc",
            "@013-cursor_riper_rules": "013-cursor_riper_rules.mdc",
            "@020-task_list": "020-task_list.mdc",
            "@021-cursor_environment_rules": "021-cursor_environment_rules.mdc",
            "@022-cursor_git_rules": "022-cursor_git_rules.mdc",
            "@030-cursor_task_rules": "030-cursor_task_rules.mdc",
            "@031-cursor_memory_rules": "031-cursor_memory_rules.mdc",
            "@032-cursor_quality_rules": "032-cursor_quality_rules.mdc",
            "@040-cursor_organization_rules": "040-cursor_organization_rules.mdc",
            "@090-completed_tasks": "090-completed_tasks.mdc",
            "@091-learned_memories_archive": "091-learned_memories_archive.mdc",
        }

    def validate_directory_structure(self) -> None:
        print(f"{Colors.BOLD}Checking .cursor/rules structure...{Colors.END}")
        if not self.rules_dir.is_dir():
            self.result.add_error(f"Rules directory not found: {self.rules_dir}")
            return
        self.result.add_pass(f"Rules directory exists: {self.rules_dir}")
        for filename, desc in self.required_files.items():
            fp = self.rules_dir / filename
            if fp.is_file():
                self.result.add_pass(f"Found {filename} ({desc})")
            else:
                self.result.add_error(f"Missing {filename} ({desc})")

    def validate_file_content(self) -> None:
        print(f"\n{Colors.BOLD}Checking file content...{Colors.END}")
        for filename in self.required_files:
            fp = self.rules_dir / filename
            if not fp.is_file():
                continue
            try:
                content = fp.read_text(encoding="utf-8")
            except OSError as e:
                self.result.add_error(f"Could not read {filename}: {e}")
                continue
            unreplaced = [ph for ph in self.placeholders if ph in content]
            if unreplaced:
                self.result.add_warning(
                    f"{filename}: unreplaced placeholders: {', '.join(unreplaced)}"
                )
            else:
                self.result.add_pass(f"{filename}: no standard placeholders remain")

    def validate_cross_references(self) -> None:
        print(f"\n{Colors.BOLD}Checking cross-rule references...{Colors.END}")
        all_refs = set()
        for filename in self.required_files:
            fp = self.rules_dir / filename
            if not fp.is_file():
                continue
            try:
                content = fp.read_text(encoding="utf-8")
            except OSError:
                continue
            for ref in self.cross_references:
                if ref in content:
                    all_refs.add(ref)
        for ref_pattern, target_file in self.cross_references.items():
            if ref_pattern in all_refs:
                target_path = self.rules_dir / target_file
                if target_path.is_file():
                    self.result.add_pass(f"Cross-reference {ref_pattern} → {target_file}")
                else:
                    self.result.add_error(
                        f"Cross-reference {ref_pattern} → MISSING {target_file}"
                    )

    def run(self) -> bool:
        self.validate_directory_structure()
        if self.rules_dir.is_dir():
            self.validate_file_content()
            self.validate_cross_references()
        print(f"\n{Colors.BOLD}Detailed Results:{Colors.END}")
        for sym, msg in self.result.messages:
            print(f"  {sym} {msg}")
        self.result.print_summary()
        return self.result.errors == 0


def detect_mode(project_root: Path) -> str:
    if (project_root / "migration-manifest.yaml").is_file():
        return "kit"
    if (project_root / ".cursor" / "rules").is_dir():
        return "install"
    return "unknown"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate kit migration layout or consumer .cursor/rules install"
    )
    parser.add_argument("--project-root", default=".", help="Project or kit root directory")
    parser.add_argument(
        "--mode",
        choices=["kit", "install", "auto"],
        default="auto",
        help="kit = Tholem-Cursor-Kit repo; install = .cursor/rules consumer project",
    )
    args = parser.parse_args()
    project_root = Path(args.project_root).resolve()

    mode = args.mode
    if mode == "auto":
        mode = detect_mode(project_root)
        if mode == "unknown":
            print(
                f"{Colors.RED}Cannot auto-detect mode: "
                f"no migration-manifest.yaml and no .cursor/rules{Colors.END}",
                file=sys.stderr,
            )
            sys.exit(2)

    print(
        f"{Colors.BOLD}{Colors.CYAN}Tholem-Cursor-Kit - validate_setup{Colors.END} "
        f"({mode}, root={project_root})"
    )

    if mode == "kit":
        result = ValidationResult()
        validate_kit_repo(project_root, result)
        print(f"\n{Colors.BOLD}Detailed Results:{Colors.END}")
        for sym, msg in result.messages:
            print(f"  {sym} {msg}")
        result.print_summary()
        sys.exit(0 if result.errors == 0 else 1)

    validator = InstallRulesValidator(project_root)
    success = validator.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
