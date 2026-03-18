#!/bin/bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
MEMORY_DIR=~/.claude/projects/-Users-mahika-datapipeline/memory
SNAPSHOT_DIR="./snapshots"
mkdir -p "$SNAPSHOT_DIR"
cp "$MEMORY_DIR/MEMORY.md" "$SNAPSHOT_DIR/MEMORY_${TIMESTAMP}.md" 2>/dev/null
for f in "$MEMORY_DIR"/*.md; do
  fname=$(basename "$f")
  cp "$f" "$SNAPSHOT_DIR/${fname%.md}_${TIMESTAMP}.md" 2>/dev/null
done
echo "Snapshot saved at $TIMESTAMP"
