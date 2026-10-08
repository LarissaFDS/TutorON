from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path, PureWindowsPath

ROOT = Path(__file__).resolve().parents[1]
TOPICS = [
    'b1-01-corretude-complexidade', 'b1-02-divisao-e-conquista',
    'b1-03-algoritmos-gulosos', 'b2-04-programacao-dinamica',
    'b2-05-transformacao-de-problemas', 'b2-06-np-completude',
    'b2-07-lidando-com-np-completude',
]
DIRECTORIES = ['00-originais', '01-extraido', '02-acervo', '03-triagem/pacote-revisao',
               '04-rag', '05-modelo', '06-avaliacao', '07-validacao-alunos']


# Os dados do acervo foram gerados no Windows e guardam caminhos com '\\'. O ID de
# cada documento é o hash desse caminho; gravar '/' no Linux mudaria os IDs e
# desvincularia caches, pareceres, aprovações e pares. Por isso a forma gravada
# é sempre a do Windows, e só a abertura de arquivos usa o separador local.
def caminho_guardado(path, root=ROOT):
    """Caminho relativo a ``root`` na forma gravada nos dados (separador do Windows)."""
    return str(PureWindowsPath(*Path(path).relative_to(root).parts))


def caminho_local(guardado, root=ROOT):
    """Caminho gravado com '\\' ou '/' convertido para o sistema atual."""
    return Path(root).joinpath(*PureWindowsPath(guardado).parts)


def ordenados(paths, base):
    """Ordem do Windows (sem diferenciar maiúsculas) em qualquer sistema."""
    return sorted(paths, key=lambda p: PureWindowsPath(*Path(p).relative_to(base).parts))


def init(root=ROOT):
    for name in DIRECTORIES:
        (root / name).mkdir(parents=True, exist_ok=True)
    for topic in TOPICS + ['assunto_incerto']:
        for kind in ['provas', 'listas', 'resolucoes', 'gabaritos', 'material_estudo']:
            (root / '02-acervo' / topic / kind).mkdir(parents=True, exist_ok=True)


def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text.lower())
                   if not unicodedata.combining(c))


def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', normalize(text)).strip('-')


def digest(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode('utf-8')).hexdigest()


def read_json(path, default=None):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8', newline='\n')
    temp.replace(path)


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8-sig') as f:
        # '\n' como nos demais arquivos gerados; o padrão do csv é '\r\n'.
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def progress(stage, message, root=ROOT):
    from datetime import datetime
    with (root / 'PROGRESSO.md').open('a', encoding='utf-8', newline='\n') as f:
        f.write(f'\n## {datetime.now().isoformat(timespec="seconds")} — {stage}\n\n{message}\n')
