@echo off
cd /d "%~dp0"
if "%~1"=="--dry-run" (
  .venv-acervo\Scripts\python.exe scripts\treinar_lora.py %*
  exit /b
)
nvidia-smi --query-gpu=name --format=csv,noheader >nul 2>&1
if errorlevel 1 (
  echo Este perfil QLoRA exige GPU NVIDIA/CUDA. Use outra maquina Linux/Windows/WSL2.
  echo Nenhuma biblioteca de treino foi baixada. Use preparar_treino.bat para validar os dados.
  exit /b 2
)
py -3 -m venv .venv-treino
if errorlevel 1 exit /b 1
if not defined TUTORON_TORCH_INDEX_URL set "TUTORON_TORCH_INDEX_URL=https://download.pytorch.org/whl/cu126"
.venv-treino\Scripts\python.exe -m pip install torch==2.14.1 --index-url "%TUTORON_TORCH_INDEX_URL%"
if errorlevel 1 exit /b 1
.venv-treino\Scripts\python.exe -c "import torch; assert torch.cuda.is_available(), 'PyTorch nao reconheceu CUDA; confira driver e indice de wheels.'"
if errorlevel 1 exit /b 1
.venv-treino\Scripts\python.exe -m pip install -r 05-modelo\treino\requirements.txt
if errorlevel 1 exit /b 1
.venv-treino\Scripts\python.exe scripts\treinar_lora.py %*
