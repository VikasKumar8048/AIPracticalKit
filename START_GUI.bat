@echo off
cd /d "%~dp0"
py app.py
if errorlevel 1 (
  echo.
  echo GUI could not start. Try running py run.py for the text menu.
  pause
)
