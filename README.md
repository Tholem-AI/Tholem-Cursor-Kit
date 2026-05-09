# Tholem Cursor Kit

Tholem Cursor Kit is a safety-first runtime framework for Cursor-based project execution.

The maintained runtime lives under `staging/.cursor/` and is intended to be copied into active project paths.

## What This Provides

The staged framework includes:

- `staging/.cursor/rules` for governance, execution flow, safety, quality, and constraints
- `staging/.cursor/agents` for role-specific agent contracts
- `staging/.cursor/skills` for guided workflows (bootstrap, orchestration, roadmap, docs)
- `staging/.cursor/hooks.json` as an opt-in hooks template

## Core Philosophy

- **Safety first**: changes should be review-gated and evidence-backed
- **Low-friction adoption**: copy runtime surfaces and start immediately
- **Operational clarity**: role boundaries and artifacts stay explicit
- **Documentation continuity**: behavior changes should stay aligned with docs

## Quickstart

1. Follow [INSTALL.md](INSTALL.md) to copy runtime surfaces into your active `.cursor/` path.
2. Optionally run bootstrap for requirements-driven initialization.
3. Use role-focused subagents and RIPER checkpoints for non-trivial work.

## Documentation Map

- [Installation Guide](INSTALL.md)
- [Contributing](CONTRIBUTING.md)
- [Docs Index](docs/README.md)
- [Using Subagents](docs/using-subagents.md)
- [Using Hooks Effectively](docs/using-hooks.md)
- [RIPER + Subagents Workflow](docs/riper-with-subagents.md)
- [Bootstrap Flow Deep Dive](docs/bootstrap-flow.md)

## Official Cursor Docs

For the latest platform behavior and feature semantics, see [Cursor Docs](https://cursor.com/docs).

## Testing-Phase Disclaimer

This framework intentionally changes default Cursor behavior through custom rules, agents, skills, and optional hooks. Outputs can be unsuitable without review. You are responsible for validating generated changes before applying them in your project. See [LICENSE](LICENSE) for legal terms and limitations.
