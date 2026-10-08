#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
./scripts/tutoron.sh Preparar
.venv-acervo/bin/python scripts/preparar_treino.py
.venv-acervo/bin/python scripts/treinar_lora.py --dry-run
