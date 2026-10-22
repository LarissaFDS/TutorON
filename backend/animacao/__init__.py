"""Animações Manim no modo Tutor (protótipo): a IA escreve um roteiro JSON e o servidor desenha.

Cada render roda num processo Python separado (backend/animacao/cena.py), um de cada vez,
com tempo limite. O vídeo fica em dados/animacoes/<id>.mp4 e é servido por /api/animacoes/<id>.mp4.
"""
from __future__ import annotations

import asyncio
import importlib.util
import json
import secrets
import shutil
import sys
from pathlib import Path

from pydantic import ValidationError

from .roteiro import validar

TEMPO_LIMITE_S = 90
_fila = asyncio.Semaphore(1)  # o render usa a CPU toda por alguns segundos


class FalhaAnimacao(Exception):
    pass


def disponivel() -> bool:
    return importlib.util.find_spec("manim") is not None


def roteiro_valido(texto_ou_dados) -> dict:
    """Valida o roteiro da IA e devolve a versão limpa (a que vai para o Manim)."""
    try:
        return validar(texto_ou_dados).model_dump()
    except (ValueError, ValidationError) as exc:
        raise FalhaAnimacao(f"roteiro inválido: {str(exc)[:200]}") from exc


async def renderizar(roteiro: dict, pasta: Path, qualidade: str = "low_quality") -> str:
    """Desenha o roteiro e devolve o id do vídeo (dados/animacoes/<id>.mp4)."""
    ident = secrets.token_urlsafe(12)
    trabalho = pasta / "tmp" / ident
    trabalho.mkdir(parents=True, exist_ok=True)
    arquivo = trabalho / "roteiro.json"
    arquivo.write_text(json.dumps(roteiro, ensure_ascii=False), encoding="utf-8")
    raiz = Path(__file__).resolve().parents[2]
    try:
        async with _fila:
            proc = await asyncio.create_subprocess_exec(
                sys.executable, "-W", "ignore", "-m", "backend.animacao.cena", str(arquivo), str(trabalho), qualidade,
                cwd=str(raiz), stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            try:
                saida, erro = await asyncio.wait_for(proc.communicate(), TEMPO_LIMITE_S)
            except asyncio.TimeoutError:
                proc.kill()
                await proc.wait()
                raise FalhaAnimacao("tempo esgotado no render") from None
        if proc.returncode != 0:
            raise FalhaAnimacao("render falhou: " + erro.decode("utf-8", "replace").strip().splitlines()[-1:][0][:200]
                                if erro.strip() else "render falhou")
        video = Path(json.loads(saida.decode("utf-8").strip().splitlines()[-1])["video"])
        destino = pasta / f"{ident}.mp4"
        shutil.move(str(video), destino)
        return ident
    finally:
        shutil.rmtree(trabalho, ignore_errors=True)
