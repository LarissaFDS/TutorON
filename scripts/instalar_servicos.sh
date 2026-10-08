#!/usr/bin/env bash
# Serviços da sessão do usuário Ubuntu; execute após preparar_modelos.sh.
set -euo pipefail
raiz="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
unidades="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
[ -x "$raiz/.tools/ollama/bin/ollama" ] || { echo 'Prepare o Ollama portátil primeiro.' >&2; exit 1; }
[ -x "$raiz/.venv-acervo/bin/python" ] || { echo 'Prepare o ambiente acervo primeiro.' >&2; exit 1; }
mkdir -p "$unidades"
cat > "$unidades/tutoron-ollama.service" <<EOF
[Unit]
Description=Ollama local para validação TutorON
After=network.target

[Service]
WorkingDirectory=$raiz
Environment="OLLAMA_MODELS=$raiz/.tools/models"
Environment=OLLAMA_HOST=127.0.0.1:11434
Environment=OLLAMA_NUM_PARALLEL=1
Environment=OLLAMA_MAX_LOADED_MODELS=1
ExecStart="$raiz/.tools/ollama/bin/ollama" serve
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
EOF
cat > "$unidades/tutoron-validacao.service" <<EOF
[Unit]
Description=Validação A/B local TutorON
After=tutoron-ollama.service
Wants=tutoron-ollama.service

[Service]
WorkingDirectory=$raiz
Environment=PYTHONUTF8=1
ExecStart="$raiz/.venv-acervo/bin/python" -m acervo servir
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
EOF
systemctl --user daemon-reload
systemctl --user enable tutoron-ollama.service tutoron-validacao.service
echo 'Serviços habilitados para sua sessão de usuário.'
echo 'Encerre instâncias manuais antes de: systemctl --user start tutoron-ollama tutoron-validacao'
echo 'Logs: journalctl --user -u tutoron-ollama -u tutoron-validacao'
echo 'Mantenha notebook ligado e sem suspensão; logout pode encerrar serviços da sessão.'
