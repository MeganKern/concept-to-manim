#!/usr/bin/env bash
# Ralph loop. The loop is dumb on purpose: it just re-invokes the agent.
# All intelligence + state lives in orchestrator.md and state/.
set -euo pipefail

MAX_ITERS="${1:-15}"

mkdir -p state out
[ -f state/PROGRESS.md ] || cp PROGRESS.template.md state/PROGRESS.md

# ---------------------------------------------------------------------------
# Adapt ONLY this function to your harness. It must run a single agent turn in
# THIS directory, with bash + file tools, using orchestrator.md as the system
# prompt, and EXTENDED THINKING OFF. Example shown for Claude Code:
# ---------------------------------------------------------------------------
run_agent_once() {
  claude -p "Advance the pipeline by exactly one phase, per your system prompt. Read state/PROGRESS.md first, do that one phase, update PROGRESS.md, and stop." \
    --append-system-prompt "$(cat orchestrator.md)" \
    --allowedTools "Bash Read Write Edit" \
    --permission-mode acceptEdits
  # (flag names vary by CLI version; the requirements are the four in the comment above.)
}
# ---------------------------------------------------------------------------

for i in $(seq 1 "$MAX_ITERS"); do
  echo "──────── iteration $i ────────"
  run_agent_once
  if grep -q '^STATUS: DONE' state/PROGRESS.md; then
    echo "✅ pipeline complete → out/lesson.mp4"
    exit 0
  fi
done

echo "⚠ hit MAX_ITERS=$MAX_ITERS without DONE."
echo "  Inspect state/PROGRESS.md to see where it's stuck."
exit 1
