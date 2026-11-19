@echo off
rem Liga (ou desliga, se ja estiver ligado) o inicio automatico do TutorON ao entrar no Windows.
title TutorON - Iniciar com o Windows
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\tutoron.ps1" -Acao AutoIniciar %*
pause
