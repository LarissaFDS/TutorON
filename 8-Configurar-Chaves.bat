@echo off
rem Grava as chaves do Supabase e do Groq no .env sem mostrar na tela.
title TutorON - Configurar chaves
cd /d "%~dp0"
".venv\Scripts\python.exe" scripts\configurar_chaves.py
pause
