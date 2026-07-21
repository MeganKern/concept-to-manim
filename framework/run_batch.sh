#!/usr/bin/env bash
# Run the Ralph loop once per standard. Each standard gets a self-contained run
# directory so nothing collides. Point inputs/ at a whole grade's standards.
set -euo pipefail

MAX_ITERS="${1:-15}"
mkdir -p runs

shopt -s nullglob
inputs=(inputs/*.md)
# skip the format template if present
filtered=()
for f in "${inputs[@]}"; do
  [ "$(basename "$f")" = "template.md" ] && continue
  filtered+=("$f")
done

for f in "${filtered[@]}"; do
  name="$(basename "$f" .md)"
  d="runs/$name"
  echo "════════════════════ $name ════════════════════"
  rm -rf "$d"
  mkdir -p "$d/state" "$d/out"
  cp orchestrator.md primitives.md loop.sh PROGRESS.template.md "$d/"
  cp PROGRESS.template.md "$d/state/PROGRESS.md"
  cp "$f" "$d/input.md"
  ( cd "$d" && ./loop.sh "$MAX_ITERS" ) || echo "⚠ $name did not finish; see $d/state/"
done

echo
echo "Done. Videos: runs/*/out/lesson.mp4"
