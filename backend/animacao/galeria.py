"""Exemplos didáticos controlados, separados de animações planejadas por IA."""
from __future__ import annotations

import asyncio
import hashlib
import json
import re
from pathlib import Path

from acervo.curate import searchable

from . import renderizar, roteiro_valido

PASTA = Path(__file__).resolve().parent
_travas: dict[tuple[str, str], asyncio.Lock] = {}


def exemplos() -> list[dict]:
    return json.loads((PASTA / 'exemplos.json').read_text(encoding='utf-8'))


def obter(ident: str) -> dict:
    for e in exemplos():
        if e['id'] == ident:
            return e
    raise KeyError(ident)


def sugerir(pergunta: str, disciplina: str) -> dict | None:
    """Escolhe apenas uma analogia do catálogo; não adapta dados nem afirma resolver a tarefa."""
    texto = searchable(pergunta)
    regras = {'sd': [(r'karnaugh', 'karnaugh-bordas'),
                     (r'circuito|tabela.?verdade|tabela de verdade|porta logica', 'circuito-tabela')],
              'paa': [(r'robo|grade', 'robo-dp'), (r'fluxo|residual|aumentante', 'fluxo-residual'),
                      (r'certificado|cobertura de vertices', 'certificado-np'),
                      (r'reducao|np.complet|np.dific', 'direcao-reducao'),
                      (r'\bbfs\b|busca em largura', 'grafo-bfs')]}
    for padrao, ident in regras.get(disciplina, []):
        if re.search(padrao, texto):
            return obter(ident)
    return None


def identidade(roteiro: dict) -> str:
    h = hashlib.sha256(json.dumps(roteiro, sort_keys=True, ensure_ascii=False).encode('utf-8'))
    # Alterar o desenho ou a validação invalida também os vídeos antigos do cache.
    for arquivo in ('cena.py', 'didatica.py', 'roteiro.py'):
        h.update((PASTA / arquivo).read_bytes())
    return 'visual_' + h.hexdigest()[:32]


def resumo(e: dict, pasta: Path) -> dict:
    roteiro = roteiro_valido(e['roteiro'])
    ident = identidade(roteiro)
    return {**{k: v for k, v in e.items() if k != 'roteiro'},
            'video': f'/api/animacoes/{ident}.mp4' if (pasta / f'{ident}.mp4').is_file() else None,
            'poster': f'/api/animacoes/{ident}.jpg' if (pasta / f'{ident}.jpg').is_file() else None,
            'pergunta_final': roteiro['pergunta_final']}


def gerar_poster(video: Path, destino: Path) -> None:
    import av
    with av.open(str(video)) as arquivo:
        for quadro in arquivo.decode(video=0):
            if quadro.time is not None and quadro.time >= 3.5:
                quadro.to_image().save(destino, quality=88)
                return


async def preparar(e: dict, pasta: Path) -> str:
    roteiro = roteiro_valido(e['roteiro'])
    ident = identidade(roteiro)
    trava = _travas.setdefault((str(pasta.resolve()), ident), asyncio.Lock())
    async with trava:
        destino = pasta / f'{ident}.mp4'
        if not destino.is_file():
            temporario = await renderizar(roteiro, pasta)
            (pasta / f'{temporario}.mp4').replace(destino)
        poster = pasta / f'{ident}.jpg'
        if not poster.is_file():
            await asyncio.to_thread(gerar_poster, destino, poster)
    return ident
