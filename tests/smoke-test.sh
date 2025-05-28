#!/bin/bash
set -euo pipefail

echo "🧪 Running Jericho smoke test (Python-level)..."
echo "---------------------------------------------"

if [ ! -f tests/smoke_test.py ]; then
  echo "❌ Could not find tests/smoke_test.py"
  exit 1
fi

python tests/smoke_test.py

echo "✅ Python smoke test passed!"