@echo off
rem Treina o modelo local do TutorON na GPU (QLoRA), avalia e instala no Ollama.
title TutorON - Treinamento
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\tutoron.ps1" -Acao Treinar %*
set "TUTORON_EXIT=%errorlevel%"
pause
exit /b %TUTORON_EXIT%
