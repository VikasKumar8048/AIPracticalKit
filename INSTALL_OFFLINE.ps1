$ErrorActionPreference = 'Stop'
$wheel = Join-Path $PSScriptRoot 'dist\ai_practical_kit-1.1.0-py3-none-any.whl'
if (-not (Test-Path $wheel)) {
    throw "Wheel not found: $wheel. Extract the complete offline ZIP first."
}
$py = Get-Command py -ErrorAction SilentlyContinue
if ($py) {
    & py -m pip install --no-index --no-deps --upgrade $wheel
} else {
    & python -m pip install --no-index --no-deps --upgrade $wheel
}
Write-Host 'AIPracticalKit installed. Select this Python interpreter in VS Code.'
