@echo off
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\tutoron.ps1" -Acao Dataset
set "TUTORON_EXIT=%errorlevel%"
pause
exit /b %TUTORON_EXIT%
