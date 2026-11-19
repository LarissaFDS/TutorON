"""Reserva local da GPU durante treino/mescla; o SO libera a trava se o processo cair."""
from __future__ import annotations

import os
from contextlib import contextmanager
from pathlib import Path

TRAVA_GPU = Path(__file__).resolve().parents[1] / '.tools/treino-gpu.lock'


def _travar(arquivo, liberar=False):
    arquivo.seek(0)
    if os.name == 'nt':
        import msvcrt
        msvcrt.locking(arquivo.fileno(), msvcrt.LK_UNLCK if liberar else msvcrt.LK_NBLCK, 1)
    else:
        import fcntl
        fcntl.flock(arquivo.fileno(), fcntl.LOCK_UN if liberar else fcntl.LOCK_EX | fcntl.LOCK_NB)


@contextmanager
def reservar_gpu(caminho: Path = TRAVA_GPU):
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open('a+b') as arquivo:
        if caminho.stat().st_size == 0:
            arquivo.write(b'0')
            arquivo.flush()
        try:
            _travar(arquivo)
        except OSError as exc:
            raise RuntimeError('Já existe um treino usando a GPU. Aguarde essa execução terminar.') from exc
        try:
            yield
        finally:
            _travar(arquivo, liberar=True)


def gpu_reservada(caminho: Path = TRAVA_GPU) -> bool:
    if not caminho.exists():
        return False
    try:
        with caminho.open('r+b') as arquivo:
            _travar(arquivo)
            _travar(arquivo, liberar=True)
        return False
    except OSError:
        return True
