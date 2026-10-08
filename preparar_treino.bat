@echo off
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\tutoron.ps1 -Acao Preparar
if errorlevel 1 exit /b 1
.venv-acervo\Scripts\python.exe scripts\preparar_treino.py
if errorlevel 1 exit /b 1
.venv-acervo\Scripts\python.exe scripts\treinar_lora.py --dry-run
