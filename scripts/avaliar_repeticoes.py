"""Estabilidade exploratória de Q2/Q6 em duas sementes adicionais, isolada do agregado."""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from acervo import models
from acervo.common import ROOT, digest, read_json, write_json
from acervo.evaluate import assess
from acervo.runtime import settings


def main():
    questions = {q['id']: q for q in read_json(ROOT / '06-avaliacao/questoes.json', [])}
    baseline = {(r['questao'], r['cenario']): r for r in read_json(ROOT / '06-avaliacao/resultados.json', [])}
    path = ROOT / '06-avaliacao/repeticoes.json'
    previous = read_json(path, [])
    rows = []
    for seed in (7, 2026):
        os.environ['TUTORON_SEED'] = str(seed)
        for qid in ('Q2', 'Q6'):
            q = questions[qid]
            for scenario in ('generico', 'rag_automatica'):
                ctx = baseline[qid, scenario]['contexto_texto']
                question = q['pergunta'] + '\n\nResponda em português em até 220 palavras.'
                model = settings()['base_model' if scenario == 'generico' else 'tutor_model']
                key = digest(json.dumps([question, ctx, models.SYSTEM, settings(), scenario], ensure_ascii=False))
                identity = models.model_digest(model)
                cached = next((r for r in previous if r.get('cache_key') == key and r.get('modelo_digest') == identity and r['status'] == 'ok'), None)
                row = {'questao': qid, 'cenario': scenario, 'seed': seed, 'cache_key': key,
                       'contexto_sha256': digest(ctx), 'contexto_texto': ctx, 'modelo_digest': identity,
                       'fontes_sha256': baseline[qid, scenario]['fontes_sha256']}
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
                print(seed, qid, scenario, row['status'], flush=True)


if __name__ == '__main__':
    main()
