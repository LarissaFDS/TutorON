"""Dúvidas sem escolha de tema -> planejamento local -> revisão -> Manim."""
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
from backend.disciplina_auto import identificar  # noqa: E402
from backend.llm import LLM  # noqa: E402
from backend.tarefas import Tarefas  # noqa: E402


async def executar(saida):
    settings = dataclasses.replace(load_settings(), gemini_api_key='', gemini_models=(),
        local_thinking=False, data_dir=ROOT / 'dados/teste-visual-contextual')
    llm = LLM(settings)
    tarefas = Tarefas(llm, settings, Registro(settings.data_dir))
    resultados = []
    casos = [
        ('robo', 'Um robô anda numa grade só para direita ou para baixo, com custos e obstáculos. '
         'Já defini dp[i][j] como o custo mínimo para chegar à célula. Quero enxergar de quais vizinhos '
         'ela depende e o que muda se um deles está bloqueado. Não tenho valores para preencher uma tabela.'),
        ('pilha', 'Estou estudando recursão e pilha de chamadas. Entendi a ideia de empilhar, mas '
         'não visualizo como uma chamada espera a outra e retoma depois do retorno. Faça uma pista visual '
         'sem escrever código nem simular um programa inteiro.'),
        ('estado', 'Para que serve o registrador de estado numa máquina de estados e como ele se relaciona '
         'com a entrada? Quero identificar visualmente quais informações chegam ao próximo estado, '
         'sem projetar uma máquina completa.'),
    ]
    try:
        for ident, pergunta in casos:
            disciplina = identificar(pergunta)
            assert disciplina, ident
            inicio = time.monotonic()
            t = tarefas.animar(pergunta, None, disciplina)
            while t.status not in ('pronta', 'erro'):
                if time.monotonic() - inicio > 300:
                    raise TimeoutError(ident)
                await asyncio.sleep(.2)
            r = {'caso': ident, 'pergunta': pergunta, 'segundos': round(time.monotonic() - inicio, 2), **t.publico()}
            logs = settings.data_dir / 'animacoes.jsonl'
            if logs.exists():
                r['registro'] = json.loads(logs.read_text(encoding='utf-8').splitlines()[-1])
            resultados.append(r)
            write_json(saida, resultados)
            print(json.dumps({k: v for k, v in r.items() if k != 'registro'}, ensure_ascii=False), flush=True)
    finally:
        await tarefas.encerrar()
        await llm.client.aclose()


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--saida', type=Path, default=ROOT / 'eval/results/visual-contextual-v1/reais.json')
    asyncio.run(executar(p.parse_args().saida))
