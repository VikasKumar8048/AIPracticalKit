@echo off
setlocal
set "WHEEL=%~dp0dist\ai_practical_kit-1.1.0-py3-none-any.whl"
if not exist "%WHEEL%" (
  echo ERROR: Wheel not found:
  echo %WHEEL%
  echo Please extract the complete AIPracticalKit offline ZIP first.
  pause
  exit /b 1
)
where py >nul 2>nul
if %errorlevel%==0 (
  py -m pip install --no-index --no-deps --upgrade "%WHEEL%"
) else (
  python -m pip install --no-index --no-deps --upgrade "%WHEEL%"
)
if %errorlevel% neq 0 (
  echo.
  echo Installation failed. Check that Python and pip are installed.
  pause
  exit /b 1
)
echo.
echo AIPracticalKit installed successfully into this Python environment.
echo For VS Code, select the same Python interpreter in the status bar.
echo Launch GUI with: ai-practical-kit-gui
pause
