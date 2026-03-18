#!/bin/bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
MEMORY_DIR=~/.claude/projects/-Users-mahika-claude-code-test-repo/memory
SNAPSHOT_DIR="./snapshots"
mkdir -p "$SNAPSHOT_DIR"
cp "$MEMORY_DIR/MEMORY.md" "$SNAPSHOT_DIR/MEMORY_${TIMESTAMP}.md" 2>/dev/null
cp "$MEMORY_DIR/project_datapipeline.md" "$SNAPSHOT_DIR/project_datapipeline_${TIMESTAMP}.md" 2>/dev/null
echo "Snapshot saved at $TIMESTAMP"
