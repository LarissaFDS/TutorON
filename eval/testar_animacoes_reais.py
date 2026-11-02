"""Teste real dos roteiros personalizados: IA local -> revisão -> render Manim."""
from __future__ import annotations

import asyncio
import argparse
import dataclasses
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from acervo.common import write_json  # noqa: E402
from backend.config import load_settings  # noqa: E402
from backend.dados import Registro  # noqa: E402
from backend.llm import LLM  # noqa: E402
from backend.tarefas import Tarefas  # noqa: E402


async def executar(saida):
    settings = dataclasses.replace(load_settings(), gemini_api_key='', gemini_models=(), local_thinking=False,
                                   data_dir=ROOT / 'dados/teste-animacoes-personalizadas')
    llm = LLM(settings)
    tarefas = Tarefas(llm, settings, Registro(settings.data_dir))
    resultados = []
    casos = [
        ('robo', 'paa', 'Faça uma pista visual para um robô que só anda à direita e abaixo. '
         'Use uma grade 3x3 de custos [[1,3,2],[2,1,4],[3,2,1]], sem obstáculos. '
         'Mostre a tabela DP em branco e destaque só os predecessores da célula (1,1). Não calcule a rota.'),
        ('karnaugh', 'sd', 'Quero enxergar a adjacência entre bordas do Karnaugh. Use um exemplo 2x4 '
         'com valores [[1,0,0,1],[0,1,1,0]], ordem Gray fixa. Destaque apenas o par da linha 0 nas '
         'colunas 0 e 3. Deixe os outros uns sem grupo e não dê expressão final.'),
    ]
    try:
        for ident, disciplina, pergunta in casos:
            inicio = time.monotonic()
            t = tarefas.animar(pergunta, None, disciplina)
            while t.status not in ('pronta', 'erro'):
                if time.monotonic() - inicio > 300:
                    raise TimeoutError('animação não terminou em 300 s')
                await asyncio.sleep(.2)
            r = {'caso': ident, 'disciplina': disciplina, 'pergunta': pergunta, 'modelo': settings.local_model,
                 'segundos': round(time.monotonic() - inicio, 2), **t.publico()}
            arquivo = settings.data_dir / 'animacoes.jsonl'
            if arquivo.exists():
                r['registro'] = json.loads(arquivo.read_text(encoding='utf-8').splitlines()[-1])
            resultados.append(r)
            write_json(saida, resultados)
            print(json.dumps({k: v for k, v in r.items() if k != 'registro'}, ensure_ascii=False), flush=True)
    finally:
        await tarefas.encerrar()
        await llm.client.aclose()


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--saida', type=Path, default=ROOT / 'eval/results/visuais-20261102/personalizadas.json')
    asyncio.run(executar(p.parse_args().saida))
