#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if [ "${1:-}" = --dry-run ]; then
    exec .venv-acervo/bin/python scripts/treinar_lora.py "$@"
fi
if ! command -v nvidia-smi >/dev/null 2>&1 || ! nvidia-smi --query-gpu=name --format=csv,noheader >/dev/null 2>&1; then
    echo 'Este perfil QLoRA exige GPU NVIDIA/CUDA. Use outra máquina Linux/Windows/WSL2.' >&2
    echo 'Nenhuma biblioteca de treino foi baixada. Use ./preparar_treino.sh para validar os dados.' >&2
    exit 2
fi
python3 -m venv .venv-treino
.venv-treino/bin/python -m pip install 'torch==2.14.1' --index-url "${TUTORON_TORCH_INDEX_URL:-https://download.pytorch.org/whl/cu126}"
.venv-treino/bin/python -c 'import torch; assert torch.cuda.is_available(), "PyTorch não reconheceu CUDA; confira driver e índice de wheels."'
.venv-treino/bin/python -m pip install -r 05-modelo/treino/requirements.txt
.venv-treino/bin/python scripts/treinar_lora.py "$@"
