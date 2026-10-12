@echo off
rem Desliga o site, o tunel publico e o modelo local (libera a GPU).
title TutorON - Desligar
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\tutoron.ps1" -Acao Parar
set "TUTORON_EXIT=%errorlevel%"
pause
exit /b %TUTORON_EXIT%
