@echo off
rem Abre o modo de validacao A/B (liga o servidor se precisar) e o painel de resultados.
title TutorON - Validacao
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\tutoron.ps1" -Acao Validacao %*
set "TUTORON_EXIT=%errorlevel%"
pause
exit /b %TUTORON_EXIT%
