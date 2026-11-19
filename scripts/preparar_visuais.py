"""Prepara os vídeos Manim e os quadros de conferência antes da apresentação.

python scripts/preparar_visuais.py [--ids robo-dp fluxo-residual] [--quadros tmp/qa-visuais]
Não chama IA nem altera o modelo de atendimento.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from acervo.common import write_json  # noqa: E402
from backend.animacao import galeria  # noqa: E402
from backend.config import load_settings  # noqa: E402


def conferir(video: Path, quadros: Path, ident: str) -> dict:
    import av
    quadros.mkdir(parents=True, exist_ok=True)
    with av.open(str(video)) as arquivo:
        stream = arquivo.streams.video[0]
        duracao = float(stream.duration * stream.time_base)
        ultimo = None
        intermediario = False
        for quadro in arquivo.decode(video=0):
            ultimo = quadro
            if not intermediario and quadro.time >= duracao * .55:
                quadro.to_image().save(quadros / f'{ident}-meio.png')
                intermediario = True
        if ultimo is None:
            raise RuntimeError('vídeo sem quadros')
        ultimo.to_image().save(quadros / f'{ident}-final.png')
        return {'segundos_video': round(duracao, 2), 'largura': stream.width, 'altura': stream.height,
                'bytes': video.stat().st_size, 'quadros_decodificados': stream.frames}


async def executar(args):
    pasta = load_settings().data_dir / 'animacoes'
    registros = []
    exemplos = galeria.exemplos()
    if args.ids:
        exemplos = [galeria.obter(i) for i in args.ids]
    for exemplo in exemplos:
        inicio = time.monotonic()
        ident = await galeria.preparar(exemplo, pasta)
        dados = conferir(pasta / f'{ident}.mp4', args.quadros, exemplo['id'])
        registros.append({'id': exemplo['id'], 'video': ident, 'preparo_s': round(time.monotonic() - inicio, 2), **dados})
        print(json.dumps(registros[-1], ensure_ascii=False), flush=True)
        write_json(args.quadros / 'verificacao.json', {'completa': False, 'exemplos': registros})
    write_json(args.quadros / 'verificacao.json', {'completa': True, 'exemplos': registros})


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ids', nargs='+')
    p.add_argument('--quadros', type=Path, default=ROOT / 'tmp/qa-visuais')
    asyncio.run(executar(p.parse_args()))
