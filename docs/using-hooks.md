# Using Hooks Effectively

Hooks give you deterministic control over the agent loop. They are scripts that run at specific moments in the agent's lifecycle and can observe, block, or modify behavior.

## What Are Hooks?

Hooks are external scripts defined in `.cursor/hooks.json`. They communicate with Cursor via JSON over stdin/stdout.

They are the primary mechanism for deterministic lifecycle controls (for example, "keep running until tests pass", "block dangerous commands", or "auto-format after edits").

## Shipped State in This Kit

The staged runtime currently ships an empty template:

```json
{
  "version": 1,
  "hooks": {}
}
```

That means hook behavior is opt-in by design. You add hook entries and scripts only when your project needs them.

For current platform semantics and event behavior, use [Cursor Docs](https://cursor.com/docs).

## Common Hook Events

| Event                    | When It Fires                        | Typical Use Case                     |
|--------------------------|--------------------------------------|--------------------------------------|
| `stop`                   | When agent finishes a response       | Long-running loops, "grind until green" |
| `afterFileEdit`          | After the agent edits a file         | Auto-format, lint, git add           |
| `beforeShellExecution`   | Before running any terminal command  | Safety checks, block `rm -rf`        |
| `beforeSubmitPrompt`     | Before sending prompt to model       | Add timestamps, inject context       |
| `beforeReadFile`         | Before agent reads a file            | Logging, access control              |

## Example: Long-Running Test Loop (Most Popular)

**`.cursor/hooks.json`**
```json
{
  "version": 1,
  "hooks": {
    "stop": [
      { "command": ".cursor/hooks/grind.sh" }
    ]
  }
}
```

**`.cursor/hooks/grind.sh`**
```bash
#!/bin/bash
input="$(cat)"

if npm test; then
  echo '{"action": "stop"}'
else
  echo '{"followup_message": "Tests are still failing. Keep fixing and run tests again."}'
fi
```

This makes the agent keep working in a loop until all tests pass.

## Example: Safety Hook

**`.cursor/hooks/safety.sh`**
```bash
#!/bin/bash
input="$(cat)"
command=$(echo "$input" | jq -r '.command // empty')

if echo "$command" | grep -qE 'rm -rf /|sudo rm|curl.*\| sh'; then
  echo '{"action": "block", "reason": "Dangerous command blocked by safety hook"}'
else
  echo '{"action": "allow"}'
fi
```

## Example: Auto-Format After Edit

**`.cursor/hooks/format.sh`**
```bash
#!/bin/bash
input=$(cat)
file=$(echo "$input" | jq -r '.file // empty')

if [[ "$file" == *.ts || "$file" == *.tsx ]]; then
  npx prettier --write "$file"
  echo '{"action": "continue"}'
else
  echo '{"action": "continue"}'
fi
```

## Best Practices

1. **Keep hooks fast** — Long-running hooks can slow down the agent.
2. **Always return valid JSON** — The hook must output a JSON object with an `action` field.
3. **Prefer fail-closed behavior for safety checks** — Better to block than silently allow.
4. **Test hooks in isolation** — Run scripts manually with sample JSON input.
5. **Document ownership** — Note which team owns each hook and rollback path.
6. **Keep hook scope narrow** — Avoid one script handling unrelated responsibilities.

## Common Patterns

- **"Grind until green"** — Keep running tests/linting until everything passes
- **Safety gates** — Block dangerous commands or file operations
- **Auto-documentation** — Update docs after significant changes
- **Notification hooks** — Send Slack/Discord messages when long tasks complete

## Related

- [Using Subagents](using-subagents.md)
- [RIPER + Subagents Workflow](riper-with-subagents.md)
- [Cursor Docs](https://cursor.com/docs)