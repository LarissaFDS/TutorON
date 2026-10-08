"""Seguimento 7B isolado: mesmas questões/condições, sem alterar a rodada principal."""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
os.environ['TUTORON_BASE_MODEL'] = 'qwen2.5:7b'
os.environ['TUTORON_MODEL'] = 'tutoron-paa-7b'

from acervo import models
from acervo.common import ROOT, digest, read_json, write_json
from acervo.evaluate import SCENARIOS, assess
from acervo.runtime import settings


def main():
    questions = read_json(ROOT / '06-avaliacao/questoes.json', [])
    baseline = {(r['questao'], r['cenario']): r for r in read_json(ROOT / '06-avaliacao/resultados.json', [])}
    path = ROOT / '06-avaliacao/seguimento-7b.json'
    previous = read_json(path, [])
    rows = []
    for q in questions:
        if q['id'] not in ('Q1', 'Q2'):
            continue
        for scenario in SCENARIOS:
            source = baseline[q['id'], scenario]
            ctx = source['contexto_texto']
            model = settings()['base_model'] if scenario in ('generico', 'controle_prompt') else settings()['tutor_model']
            question = q['pergunta'] + '\n\nResponda em português em até 220 palavras.'
            key = digest(json.dumps([question, ctx, models.SYSTEM, settings(), scenario], ensure_ascii=False))
            identity = models.model_digest(model)
            cached = next((r for r in previous if r.get('cache_key') == key and r.get('modelo_digest') == identity and r['status'] == 'ok'), None)
            row = {'questao': q['id'], 'cenario': scenario, 'cache_key': key,
                   'contexto_sha256': digest(ctx), 'contexto_texto': ctx, 'configuracao': settings(), 'modelo_digest': identity,
                   'fontes_sha256': source['fontes_sha256'],
                   'limite': 'Seguimento exploratório de duas questões; não prova superioridade nem treinamento.'}
            if cached:
                row = cached
                row['reutilizada_do_cache'] = True
            else:
                try:
                    response = models.generate(question, ctx, 'ollama', scenario != 'generico', model=model)
                    row.update(status='ok', resposta=response, avaliacao=assess(q, response['texto'], scenario != 'generico'))
                except Exception as exc:
                    row.update(status='falhou', erro=type(exc).__name__ + ': ' + str(exc)[:200])
            rows.append(row)
            write_json(path, rows)
            print(q['id'], scenario, row['status'], flush=True)


if __name__ == '__main__':
    main()
