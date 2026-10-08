#!/usr/bin/env bash
# Instala um lançador Linux sem mudar a associação global dos arquivos .sh.
set -euo pipefail
raiz="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 - "$raiz" <<'PY'
import os
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(sys.argv[1])
launcher = root / 'iniciar_validacao.sh'
if not launcher.is_file():
    raise SystemExit('iniciar_validacao.sh não encontrado.')
launcher.chmod(launcher.stat().st_mode | 0o111)
# O campo Exec possui escape próprio; % introduz códigos de campo.
command = str(launcher).replace('\\', '\\\\').replace('"', '\\"').replace('`', '\\`').replace('$', '\\$').replace('%', '%%')
if any(c in str(root) for c in '\r\n'):
    raise SystemExit('O caminho do projeto não pode conter quebra de linha.')
content = '\n'.join([
    '[Desktop Entry]', 'Version=1.0', 'Type=Application',
    'Name=TutorON — Validação',
    'Comment=Abre a demonstração local e a comparação cega de respostas',
    f'Exec="{command}"',
    'Terminal=true', 'Icon=applications-science',
    'Categories=Education;', 'StartupNotify=false', '',
])
applications = Path(os.environ.get('XDG_DATA_HOME') or Path.home() / '.local/share') / 'applications'
applications.mkdir(parents=True, exist_ok=True)
target = applications / 'tutoron-validacao.desktop'
target.write_text(content, encoding='utf-8')
target.chmod(0o755)
print(f'Atalho instalado no menu de aplicativos: {target}')
if shutil.which('desktop-file-validate'):
    subprocess.run(['desktop-file-validate', str(target)], check=True)
if shutil.which('xdg-user-dir'):
    result = subprocess.run(['xdg-user-dir', 'DESKTOP'], capture_output=True, text=True, check=True)
    desktop = Path(result.stdout.strip())
    if desktop.is_dir() and desktop != Path.home():
        copy = desktop / target.name
        copy.write_text(content, encoding='utf-8')
        copy.chmod(0o755)
        if shutil.which('gio'):
            trusted = subprocess.run(['gio', 'set', str(copy), 'metadata::trusted', 'true'], capture_output=True)
            if trusted.returncode:
                print('Na área de trabalho, clique com o botão direito no atalho e escolha Permitir execução.')
        print(f'Atalho na área de trabalho: {copy}')
print('Abra TutorON — Validação pelo menu de aplicativos ou pela área de trabalho.')
print('Acesso direto: http://127.0.0.1:8765')
PY
