@echo off
rem Gera casos de todas as disciplinas, treina o tutor socratico na GPU (QLoRA), avalia e instala no Ollama.
rem Nao troca o modelo em uso: depois de ler o relatorio, ative pelo .env (TUTORON_MODELO_LOCAL).
title TutorON - Treinamento
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\tutoron.ps1" -Acao Treinar %*
set "TUTORON_EXIT=%errorlevel%"
pause
exit /b %TUTORON_EXIT%
