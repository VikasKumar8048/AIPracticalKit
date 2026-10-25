#!/usr/bin/env sh
set -eu
WHEEL="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/dist/ai_practical_kit-1.1.0-py3-none-any.whl"
if command -v python3 >/dev/null 2>&1; then
  python3 -m pip install --no-index --no-deps --upgrade "$WHEEL"
else
  python -m pip install --no-index --no-deps --upgrade "$WHEEL"
fi
printf '\nAIPracticalKit installed. Select this Python interpreter in VS Code.\n'
