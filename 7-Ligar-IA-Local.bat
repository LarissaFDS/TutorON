@echo off
rem Liga o modelo local deste PC ao TutorON hospedado (deixe esta janela aberta durante os testes).
title TutorON - IA local ligada ao site
cd /d "%~dp0"
if not exist ".tools\ollama\ollama.exe" if not exist "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" echo Aviso: Ollama nao encontrado. Abra o 1-Iniciar-Servidor.bat uma vez antes.
".venv\Scripts\python.exe" scripts\worker_pc.py
pause
