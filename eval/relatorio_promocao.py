"""Resume medições e pareceres manuais; não atribui notas nem troca modelos."""
from __future__ import annotations

import json
import random
import statistics
from pathlib import Path

from acervo.common import ROOT, write_json


def executar():
    pasta = ROOT / 'eval/results/promocao-20261102'
    dados = json.loads((pasta / 'comparacao.json').read_text(encoding='utf-8'))
    revisao = json.loads((pasta / 'pareceres.json').read_text(encoding='utf-8'))
    pareceres = revisao['casos']
    assert dados['completa'] and len(dados['casos']) == 2 * len(pareceres) == 24
    assert {r['id'] for r in dados['casos']} == {r['id'] for r in pareceres}
    modelos = {'atual': 'tutoron-paa', 'candidato': 'tutoron-socratico-ft'}
    resumo = {}
    for label, modelo in modelos.items():
        rs = [r for r in dados['casos'] if r['modelo_solicitado'] == modelo]
        assert len({r['id'] for r in rs}) == 12
        resumo[label] = {'modelo': modelo, 'casos': len(rs), 'prontas': sum(r['status'] == 'pronta' for r in rs),
            'reservas': sum(r['reserva'] for r in rs), 'mediana_s': statistics.median(r['segundos'] for r in rs),
            'max_s': max(r['segundos'] for r in rs),
            'erros_tecnicos': sum(p[label]['erro_tecnico_claro'] for p in pareceres),
            'entregas': sum(p[label]['entrega_resultado_solicitado'] for p in pareceres),
            'ajuda': {str(n): sum(p[label]['ajuda'] == n for p in pareceres) for n in (0, 1, 2)}}
    ganhos = sum(p['candidato']['ajuda'] > p['atual']['ajuda'] for p in pareceres)
    perdas = sum(p['candidato']['ajuda'] < p['atual']['ajuda'] for p in pareceres)
    a, c = resumo['atual'], resumo['candidato']
    criterios = {'sem_erro_tecnico': c['erros_tecnicos'] == 0, 'sem_entrega': c['entregas'] == 0,
                'tres_pares_melhores': ganhos >= 3, 'no_maximo_um_par_pior': perdas <= 1,
                'reservas_nao_aumentam': c['reservas'] <= a['reservas'], 'ate_120_s': c['max_s'] <= 120,
                'sem_regressao_operacional_anterior': False}  # 13 reservas e 430,8 s contra 8 e 21,7 s.
    write_json(pasta / 'decisao.json', {'promover': all(criterios.values()), 'criterios': criterios,
        'resumo': resumo, 'pares_melhores': ganhos, 'pares_piores': perdas, 'revisao': revisao['metodo'],
        'avaliacao_antes_dos_limites_novos': True})
    linhas = ['# Comparação do modelo treinado — decisão de implantação', '',
        '**Decisão: manter `tutoron-paa` no servidor. O candidato `tutoron-socratico-ft` não demonstrou melhora.**', '',
        'Foram geradas 24 ajudas novas: 12 situações para cada modelo, no mesmo fluxo local de busca, revisão e publicação. '
        'Raciocínio desligado, temperatura 0,2, antes das alterações de limite de saída desta entrega. '
        'Os critérios foram definidos antes da geração em [CRITERIOS_PROMOCAO.md](../eval/CRITERIOS_PROMOCAO.md).', '',
        '| Medida na rodada nova | Atual | Treinado |', '|---|---:|---:|',
        f"| Tarefas concluídas | {a['prontas']}/12 | {c['prontas']}/12 |",
        f"| Erros técnicos claros nas publicadas | {a['erros_tecnicos']} | {c['erros_tecnicos']} |",
        f"| Ajuda adequada para um próximo passo (nota 2) | {a['ajuda']['2']} | {c['ajuda']['2']} |",
        f"| Orientações genéricas de reserva | {a['reservas']} | {c['reservas']} |",
        f"| Mediana | {a['mediana_s']:.1f} s | {c['mediana_s']:.1f} s |", '',
        f'O candidato teve {ganhos} pares com potencial de ajuda maior e {perdas} menor. '
        'Não foram observadas entregas do resultado solicitado nas 24 ajudas desta rodada; '
        'isso não demonstra cumprimento universal das regras.', '',
        '**O atual também erra.** Manter o atual evita promover uma regressão; não o torna validado para aprendizagem. '
        'Os pareceres foram escritos pelo agente em inspeção técnica, sem cegamento, docente ou alunos. '
        'A nota 0–2 descreve potencial de ajuda neste caso, não ganho medido de aprendizagem.', '',
        'A rodada anterior tinha 32 respostas por modelo. O atual precisou de 8 reservas e chegou a 21,7 s; '
        'o treinado precisou de 13 reservas e chegou a 430,8 s num caso repetitivo. '
        '[Relatório dessa execução](diagnostico-treino-2026-11-02.md).', '',
        '## Exemplos que impedem a promoção', '',
        '- Mestre: o candidato confirma parâmetros trocados e usa a base errada no logaritmo.',
        '- Reduções: aceita a direção que não prova a dificuldade do problema novo.',
        '- Karnaugh: confirma 01 e 10 como vizinhos e confunde zero obrigatório com irrelevância.',
        '- NP-dificuldade: transfere dificuldade na direção errada de uma redução.', '',
        '## Evidências e próxima avaliação', '',
        '[Respostas completas](../eval/results/promocao-20261102/comparacao.md), '
        '[textos e tempos exatos](../eval/results/promocao-20261102/comparacao.json), '
        '[pareceres por caso](../eval/results/promocao-20261102/pareceres.json), '
        '[decisão calculada a partir dos pareceres](../eval/results/promocao-20261102/decisao.json).', '',
        'Para uma revisão docente independente, estão prontos '
        '[12 pares com lados embaralhados](../eval/results/promocao-20261102/pares-cegos.md). '
        'A chave está em arquivo separado. O docente pode marcar correção, entrega indevida e utilidade, '
        'sem saber qual modelo produziu cada lado. Depois, testar tarefas equivalentes com alunos e '
        'medir se conseguem dar o próximo passo; preferência por texto mais curto não basta.', '',
        'Esta bateria permanece fora do treino. Nenhum novo fine-tuning ou troca do `.env` ocorreu nesta comparação. '
        'As novas proteções limitam a saída sem raciocínio e recusam candidatas extensas para revisão, '
        'sem aprovar só um prefixo. Um novo ensaio do caso visual terminou em 6,6 s sem repetir o problema, '
        'mas uma repetição isolada não demonstra causalmente a eliminação de repetições.']
    (ROOT / '06-avaliacao/comparacao-modelo-2026-11-02.md').write_text('\n'.join(linhas) + '\n', encoding='utf-8', newline='\n')
    rng, chave = random.Random(20261102), {}
    cegos = ['# Revisão de pares de ajuda', '', 'Leia cada enunciado e tentativa. Compare os lados sem consultar a chave.',
             'Para cada lado, marque: erro técnico (sim/não), entrega indevida (sim/não), utilidade (0–2) e motivo.',
             'Utilidade: 0 não destrava; 1 relevante mas vaga; 2 próximo passo pequeno, correto e compatível com a tentativa.', '']
    for n, p in enumerate(pareceres, 1):
        rs = [r for r in dados['casos'] if r['id'] == p['id']]
        rng.shuffle(rs)
        cegos += [f'## Par {n}', '', rs[0]['pergunta'], '', '**Tentativa:** ' + (rs[0].get('contexto') or '(não enviada)'), '']
        if rs[0].get('historico'):
            cegos += ['**Ajudas anteriores:**', '']
            for h in rs[0]['historico']:
                cegos += [h['texto'], '']
        if rs[0].get('travou'):
            cegos += ['**Onde o aluno travou:** ' + rs[0]['travou'], '']
        chave[str(n)] = {}
        for lado, r in zip(('A', 'B'), rs):
            cegos += [f'### Lado {lado}', '', r['publicada'], '', 'Correção: ___ / entrega: ___ / utilidade: ___ / motivo: ___', '']
            chave[str(n)][lado] = {'modelo': r['modelo_solicitado'], 'caso': r['id']}
    texto_cegos = '\n'.join(l.rstrip() for l in '\n'.join(cegos).splitlines()) + '\n'
    (pasta / 'pares-cegos.md').write_text(texto_cegos, encoding='utf-8', newline='\n')
    write_json(pasta / 'chave-cega.json', chave)


if __name__ == '__main__':
    executar()
