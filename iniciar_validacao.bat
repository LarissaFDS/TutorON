@echo off
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\tutoron.ps1" -Acao Validar
set "TUTORON_EXIT=%errorlevel%"
if not "%TUTORON_EXIT%"=="0" pause
exit /b %TUTORON_EXIT%
