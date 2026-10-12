@echo off
rem Religa os modelos e o site, sem mudar o endereco publico (use se algo travar).
title TutorON - Reiniciar
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\tutoron.ps1" -Acao Reiniciar
set "TUTORON_EXIT=%errorlevel%"
pause
exit /b %TUTORON_EXIT%
