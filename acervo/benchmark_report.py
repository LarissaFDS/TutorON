"""Relatório comparável de cobertura lexical; não declara acurácia matemática."""
from collections import Counter
from statistics import mean
from .common import ROOT, digest, read_json, write_json
from .evaluate import SCENARIOS


def report(root=ROOT):
    results = read_json(root / '06-avaliacao/resultados.json', [])
    grouped = {}
    for row in results:
        grouped.setdefault(row['questao'], {})[row['cenario']] = row
    comparison = []
    for qid, rows in grouped.items():
        complete = {s: r for s, r in rows.items() if r['status'] == 'ok'}
        labels = [set(c['rotulo'] for c in r['avaliacao']['checks'] if c['ok'] is not None and c['tipo'] != 'info') for r in complete.values()]
        common = set.intersection(*labels) if labels else set()
        scores = {s: sum(c['ok'] is True for c in r['avaliacao']['checks'] if c['rotulo'] in common) for s, r in complete.items()}
        comparison.append({'questao': qid, 'completa_quatro_condicoes': len(complete) == 4,
                           'criterios_comuns': sorted(common), 'acertos_comuns': scores})
    summaries = {}
    review = read_json(root / '06-avaliacao/revisao-tecnica.json', {})
    verdicts = {(r['questao'], r['cenario'], r['resposta_sha256']): r['parecer'] for r in review.get('revisoes', [])}
    full = [q for q in comparison if q['completa_quatro_condicoes']]
    for scenario in SCENARIOS:
        rows = [r for r in results if r['cenario'] == scenario and r['status'] == 'ok']
        summaries[scenario] = {'respostas_ok': len(rows),
            'falhas': sum(r['cenario'] == scenario and r['status'] != 'ok' for r in results),
            'criterios_lexicais_encontrados': sum(r['avaliacao']['acertos'] for r in rows),
            'criterios_lexicais_aplicaveis': sum(r['avaliacao']['total'] for r in rows),
            'criterios_comuns_encontrados': sum(q['acertos_comuns'][scenario] for q in full),
            'criterios_comuns_aplicaveis': sum(len(q['criterios_comuns']) for q in full),
            'tempo_medio_segundos': mean(r['resposta']['segundos'] for r in rows) if rows else None,
            'citacoes_invalidas': sum(len(r.get('citacoes_ids_invalidos', [])) for r in rows),
            'respostas_com_citacao_valida': sum(bool(set(r.get('citacoes_ids', [])) & set(r['fontes'])) for r in rows),
            'revisao_agente': dict(Counter(verdicts.get((r['questao'], scenario, digest(r['resposta']['texto'])), 'pendente') for r in rows))}
    differences = {}
    for baseline in ('generico', 'controle_prompt'):
        deltas = [q['acertos_comuns']['rag_automatica']-q['acertos_comuns'][baseline] for q in full]
        differences[baseline] = {'rag_maior': sum(d>0 for d in deltas), 'empate': sum(d==0 for d in deltas), 'rag_menor': sum(d<0 for d in deltas)}
    automatic = [r for r in results if r['cenario'] == 'rag_automatica']
    found = [r['top_k_acertou'] for r in automatic if r['top_k_acertou'] is not None]
    summary = {'condicoes': summaries, 'comparacao_por_questao': comparison, 'diferencas_checklist_comum': differences,
               'recuperacao_fontes_esperadas': {'encontradas': sum(found), 'avaliaveis': len(found)},
               'status': dict(Counter(r['status'] for r in results)),
               'limitacoes': ['Cobertura lexical não é acurácia.', 'Questões incluem variantes da mesma família.',
                              'Uma semente na rodada principal; sem inferência estatística de superioridade.',
                              'Material no RAG é permitido no protocolo aberto; não é teste de conhecimento memorizado.',
                              'Revisão técnica por agente e validação cega com alunos/professor são evidências separadas.']}
    write_json(root / '06-avaliacao/comparacao-atual.json', summary)
    lines = ['# Comparação local atual', '', 'Mesmos pesos Qwen2.5 3B, temperatura 0,2, seed 42, contexto de 4096 tokens. '
             'Todos recebem a mesma orientação de até 220 palavras. TutorON adiciona contexto acadêmico curado. '
             'O controle usa as mesmas instruções sem dados. Nenhum fine-tuning foi executado.', '',
             '| Condição | Respostas | Checklist comum | Tempo médio (s) | Com citação de ID válida | IDs inválidos |', '|---|---:|---:|---:|---:|---:|---:|']
    for scenario, s in summaries.items():
        seconds = f'{s["tempo_medio_segundos"]:.1f}' if s['tempo_medio_segundos'] is not None else '—'
        lines.append(f'| {scenario} | {s["respostas_ok"]} | {s["criterios_comuns_encontrados"]}/{s["criterios_comuns_aplicaveis"]} | {seconds} | {s["respostas_com_citacao_valida"]} | {s["citacoes_invalidas"]} |')
    lines += ['', 'A métrica de citações verifica somente IDs explícitos do acervo. Marcadores como [1] não são fontes verificadas. Ausência de IDs inválidos não demonstra fundamentação.']
    lines += ['', '## Comparação por questão (mesmos critérios aplicáveis)', '', '| Questão | Genérico | Controle | Manual | Automática | Total |', '|---|---:|---:|---:|---:|---:|']
    for q in comparison:
        values = [str(q['acertos_comuns'].get(s, 'falha')) for s in SCENARIOS]
        lines.append('| ' + q['questao'] + ' | ' + ' | '.join(values) + f' | {len(q["criterios_comuns"])} |')
    lines += ['', '## Revisão matemática por agente', '',
              'Somente pareceres vinculados ao hash exato da resposta são contabilizados. Não são votos humanos nem avaliação independente.', '',
              '| Condição | Adequadas | Parciais | Erro material | Pendentes |', '|---|---:|---:|---:|---:|']
    for scenario, s in summaries.items():
        counts = s['revisao_agente']
        lines.append(f'| {scenario} | {counts.get("adequada",0)} | {counts.get("parcial",0)} | {counts.get("erro_material",0)} | {counts.get("pendente",0)} |')
    lines += ['', '## Limites da conclusão', '', *['- '+s for s in summary['limitacoes']], '',
              'Respostas integrais, fontes, hashes e latência: resultados.json. Avaliação por agente: revisao-tecnica.json. '
              'Votos humanos reais são coletados em http://127.0.0.1:8765; nenhum voto é fabricado.']
    (root / '06-avaliacao/COMPARACAO_ATUAL.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(summary['status'], differences)
    return summary


if __name__ == '__main__':
    report()
