import json
import re
import time
from collections import Counter
from html.parser import HTMLParser

from .common import ROOT, TOPICS, digest, progress, read_json, write_csv, write_json
from .curate import searchable
from .retrieval import search, context
from . import models


def checkpoint(label, regex, kind='deve'):
    return {'rotulo': label, 'regex': regex, 'tipo': kind}


def make_questions(root=ROOT):
    items = read_json(root / '02-acervo/itens.json', [])
    original = read_json(root / 'questoes.json', [])
    questions = []
    for q in original:
        refs = [r['id'] for r in items if any(r['id'] == ref or r['id'].startswith(ref + '-q') for ref in q['contexto'])]
        questions.append({**q, 'assunto': TOPICS[1 if q['id'] == 'Q1' else 0 if q['id'] == 'Q2' else 5],
                          'contexto': refs, 'fontes_esperadas': refs,
                          'categoria': 'material_com_erro' if q['id'] == 'Q4' else 'poc',
                          'checklist_status': 'herdado_da_poc_revisao_professor_pendente'})
    extra = [
        ('Q5', 2, 4, '1', 'Se eu somar 1 ao peso de cada aresta de um grafo conexo, a árvore geradora mínima continua mínima? E os caminhos mínimos? Justifique com um contraexemplo numérico.',
         [checkpoint('Aumento n−1 por árvore', r'n\s*[-−]\s*1'), checkpoint('Caminho depende do número de arestas', r'numero de arestas|quantidade de arestas'), checkpoint('Dá contraexemplo', r'contraexemplo|exemplo')], 'material_com_erro'),
        ('Q6', 3, 5, '4', 'Como resolver a subsequência contígua de soma máxima em tempo linear, seguindo a convenção da Lista 5? Mostre a recorrência e os resultados para [5,15,-30,10,-5,40,10] e [-5,-2,-8].',
         [checkpoint('Permite subsequência vazia', r'vazi'), checkpoint('Exemplo positivo: 55', r'55'), checkpoint('Caso negativo retorna zero', r'zero|soma\s*0|=\s*0'), checkpoint('Tempo linear', r'o\(n\)|linear')], 'lista'),
        ('Q7', 4, 6, '1', 'Maria ouve n−1 números distintos de 1 a n. Como encontrar o número faltante usando O(1) de memória? Explique tempo e possíveis problemas de overflow.',
         [checkpoint('Soma ou XOR', r'soma|xor'), checkpoint('Espaço constante', r'o\(1\)|constante'), checkpoint('Tempo linear', r'o\(n\)|linear')], 'lista'),
        ('Q8', 6, 8, '1', 'Como usar backtracking para encontrar todos os quadrados mágicos de ordem 3 com os números distintos de 1 a 9? Explique os testes e as podas.',
         [checkpoint('Soma mágica 15', r'15'), checkpoint('Números não repetidos', r'distint|repet'), checkpoint('Verifica diagonais', r'diagona'), checkpoint('Retrocede e poda', r'backtrack|retroced')], 'lista'),
        ('Q9', 1, 3, '1', 'Como ordenar a pilha de panquecas de tamanhos distintos usando inversões de prefixo? Diferencie quantidade de inversões e custo total de movimentar elementos.',
         [checkpoint('Coloca a maior na base', r'maior'), checkpoint('Inversões lineares', r'2\s*\(?n|o\(n\)|linear'), checkpoint('Custo quadrático ao mover elementos', r'quadratic|n\^?2|n²')], 'lista'),
        ('Q10', 0, None, None, 'Me perdi nos asteriscos: por que não é só n vezes? Tem duas chamadas com n menos 1 e um laço que imprime n. Pode montar a conta e conferir n=3?',
         [checkpoint('Recorrência com duas chamadas', r'2\s*\*?\s*[at]\s*\(n\s*[-−]\s*1\)'), checkpoint('Onze asteriscos', r'11|onze')], 'linguagem_aluno'),
        ('Q11', 5, None, None, 'Se testar divisores faz só O(n) testes, por que o professor fala que COMPOSTO não ficou polinomial? O que muda quando a entrada está escrita em binário?',
         [checkpoint('Mede entrada em bits', r'bits|binari'), checkpoint('Exponencial no tamanho da entrada', r'exponencial'), checkpoint('Não afirma que COMPOSTO é NP-completo', r'composto (e|eh) np.completo', 'nao_deve')], 'linguagem_aluno'),
        ('Q12', 5, None, None, 'Qual será a data, a sala e o conteúdo exato da próxima prova de PAA em outubro de 2026?',
         [checkpoint('Admite ausência no acervo', r'nao (?:encontr|ha|tenho|possuo)|sem inform|nao consta|indisponivel'), checkpoint('Não inventa sala', r'sala\s+[0-9]+', 'nao_deve')], 'sem_resposta'),
    ]
    for qid, topic_idx, list_num, number, question, checks, category in extra:
        refs = [r['id'] for r in items if list_num and f'PAA_L{list_num}.pdf' in r['fonte_original'] and r['questao'] == number]
        if qid == 'Q10': refs = ['c04', 'c05']
        if qid == 'Q11': refs = ['c07', 'c08']
        questions.append({'id': qid, 'titulo': question[:80], 'pergunta': question, 'assunto': TOPICS[topic_idx],
                          'contexto': refs, 'fontes_esperadas': refs, 'checkpoints': checks,
                          'categoria': category, 'checklist_status': 'proposto_revisao_professor_pendente'})
    write_json(root / '06-avaliacao/questoes.json', questions)
    write_json(root / '06-avaliacao/cobertura.json', {'questoes': len(questions),
               'por_assunto': dict(Counter(q['assunto'] for q in questions)),
               'sem_fonte': [q['id'] for q in questions if not q['contexto'] and q['categoria'] != 'sem_resposta'],
               'revisao_professor': 'pendente'})
    return questions


def assess(q, answer, structured):
    # Reutiliza o avaliador e as exceções da PoC (inclusive citações de erros corrigidos).
    from run_demo import avaliar_checkpoints, cobertura
    checks = avaliar_checkpoints(q, answer, 'estruturado' if structured else 'generico')
    ok, total = cobertura(checks)
    return {'checks': checks, 'acertos': ok, 'total': total,
            'aviso': 'Cobertura lexical de checklist; não equivale a correção matemática.'}


def evaluate(root=ROOT, provider='ollama', generate=False, selected=None):
    questions = read_json(root / '06-avaliacao/questoes.json', []) or make_questions(root)
    items = {r['id']: r for r in read_json(root / '02-acervo/itens.json', [])}
    results = []
    output_name = 'resultados.json' if generate else 'recuperacao.json'
    for q in questions:
        if selected and q['id'] not in selected:
            continue
        begin = time.monotonic()
        hits = search(q['pergunta'], root)
        duration = time.monotonic() - begin
        expected = set(q['fontes_esperadas'])
        excluded = [i for i in expected if i in items and items[i]['confiabilidade'] == 'baixa']
        for scenario in ['generico', 'rag_manual', 'rag_automatica']:
            chosen = [] if scenario == 'generico' else ([items[i] for i in q['contexto'] if i in items] if scenario == 'rag_manual' else hits)
            ctx = context(chosen)
            actual_ids = re.findall(r'^\[([^\]]+)\] Fonte:', ctx, re.M)
            row = {'questao': q['id'], 'cenario': scenario, 'fontes': actual_ids,
                   'esperadas': sorted(expected), 'excluidas_baixa': excluded,
                   'top_k_acertou': bool(expected.intersection(actual_ids)) if expected else None,
                   'segundos_busca': duration if scenario == 'rag_automatica' else 0,
                   'ausencia_contexto': not actual_ids, 'modo_busca': hits[0]['busca'] if hits else 'sem_resultados',
                   'status': 'somente_recuperacao', 'manual_adversarial': bool(excluded) and scenario == 'rag_manual'}
            # Cache inclui prompt, contexto, modelo e provedor para não reciclar resultados incompatíveis.
            key = digest(json.dumps([q, ctx, provider, models.SYSTEM,
                                    __import__('os').environ.get('TUTORON_MODEL', 'qwen2.5:7b')], ensure_ascii=False))
            cache = root / '06-avaliacao/execucoes' / f'{q["id"]}-{scenario}-{key[:16]}.json'
            if generate:
                previous = read_json(cache, {})
                if previous.get('status') == 'ok':
                    row.update({'status': 'ok', 'resposta': previous['resposta'], 'reutilizada_do_cache': True})
                    row['avaliacao'] = assess(q, row['resposta']['texto'], scenario != 'generico')
                else:
                    try:
                        response = models.generate(q['pergunta'], ctx, provider, scenario != 'generico')
                        prose = re.sub(r'```.*?```|`[^`]*`', '', response['texto'], flags=re.S)
                        cited = re.findall(r'\[(c\d+(?:-q[\w-]+)?|[a-f0-9]{12}(?:-q[\w-]+)?)\]', prose)
                        row.update({'status': 'ok', 'resposta': response,
                                    'avaliacao': assess(q, response['texto'], scenario != 'generico'),
                                    'citacoes_ids': cited, 'citacoes_ids_invalidos': [c for c in cited if c not in actual_ids]})
                    except Exception as exc:
                        row.update({'status': 'falhou', 'erro': type(exc).__name__ + ': ' + str(exc)[:160]})
                    write_json(cache, row)
                if row['status'] == 'ok':
                    prose = re.sub(r'```.*?```|`[^`]*`', '', row['resposta']['texto'], flags=re.S)
                    cited = re.findall(r'\[(c\d+(?:-q[\w-]+)?|[a-f0-9]{12}(?:-q[\w-]+)?)\]', prose)
                    row['citacoes_ids'] = cited
                    row['citacoes_ids_invalidos'] = [c for c in cited if c not in actual_ids]
            results.append(row)
            write_json(root / '06-avaliacao' / output_name, results)
            print(q['id'], scenario, row['status'], flush=True)
    lines = ['# Avaliação de PAA', '', 'Checklists ainda dependem do professor. Percentuais são cobertura lexical, não acurácia.', '',
             '| Condição | Respostas concluídas | Critérios encontrados | Critérios aplicáveis |', '|---|---:|---:|---:|']
    for scenario in ['generico', 'rag_manual', 'rag_automatica']:
        complete = [r for r in results if r['cenario'] == scenario and r['status'] == 'ok']
        lines.append(f'| {scenario} | {len(complete)} | {sum(r["avaliacao"]["acertos"] for r in complete)} | {sum(r["avaliacao"]["total"] for r in complete)} |')
    lines += ['', 'RAG manual usa os contextos previstos, inclusive material de baixa confiabilidade nos casos adversariais. RAG automática os exclui. Esses casos avaliam também abstenção/filtragem, não só top-k.', '',
              '| Questão | Top-k automático | Fontes excluídas por baixa confiança | Segundos de busca |', '|---|---|---|---:|']
    for r in results:
        if r['cenario'] == 'rag_automatica':
            lines.append(f'| {r["questao"]} | {r["top_k_acertou"]} | {", ".join(r["excluidas_baixa"])} | {r["segundos_busca"]:.3f} |')
    (root / '06-avaliacao' / ('relatorio.md' if generate else 'relatorio-recuperacao.md')).write_text('\n'.join(lines), encoding='utf-8')
    progress('6. Avaliação', f'{len(questions)} questões definidas; {sum(r["status"] == "ok" for r in results)} respostas reais nesta execução. Resultados de recuperação e geração separados. Revisão com professor pendente.', root)
    return results


class HistoricalParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pre = None
        self.blocks = []
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'pre':
            self.pre = []

    def handle_data(self, data):
        if self.pre is not None:
            self.pre.append(data)

    def handle_endtag(self, tag):
        if tag == 'pre' and self.pre is not None:
            self.blocks.append(''.join(self.pre))
            self.pre = None


def offline(root=ROOT):
    results = read_json(root / '06-avaliacao/resultados.json', [])
    questions = {q['id']: q for q in read_json(root / '06-avaliacao/questoes.json', [])}
    pairs = []
    for qid, q in questions.items():
        answers = {r['cenario']: r for r in results if r['questao'] == qid and r['status'] == 'ok'}
        if 'generico' in answers and 'rag_automatica' in answers:
            pairs.append({'id': qid, 'pergunta': q['pergunta'], 'origem': 'avaliacao_local_rag_automatica',
                          'generico': answers['generico']['resposta'], 'tutoron': answers['rag_automatica']['resposta']})
    if not pairs:
        # Transcrições reais do relatório fornecido, nunca respostas inventadas/mock.
        source = root / '00-originais/referencias/TutorON_PoC_Gemini_PAA.html'
        if source.exists():
            parser = HistoricalParser()
            parser.feed(source.read_text(encoding='utf-8'))
            blocks = parser.blocks
            prompts = [(i, b) for i, b in enumerate(blocks) if ('Como resolver em tempo linear o problema da subsequência' in b or 'Considere um grafo não direcionado conexo' in b) and not b.lstrip().startswith('- main:') and len(b) < 6000]
            candidates = {'soma': [], 'grafos': []}
            for i, prompt in prompts:
                if i+1 >= len(blocks): continue
                answer = blocks[i+1]
                if answer.lstrip().startswith('- main:') or len(answer.strip()) < 200: continue
                if 'CONTEXTO ACADÊMICO:' in prompt:
                    kind = 'tutoron'
                elif 'Você é uma IA' not in prompt and len(prompt) < 600:
                    kind = 'generico'
                else:
                    continue
                group = 'soma' if 'subsequência' in prompt else 'grafos'
                candidates[group].append((kind, prompt.split('PERGUNTA DO ALUNO:')[-1].strip(), answer))
            for name, candidates_for_q in candidates.items():
                choices = {kind: (prompt, answer) for kind, prompt, answer in candidates_for_q}
                if set(choices) == {'generico', 'tutoron'}:
                    pairs.append({'id': 'historico-' + name, 'pergunta': choices['generico'][0],
                                  'origem': 'poc_historica_gemini_contexto_manual',
                                  **{kind: {'texto': choices[kind][1], 'modelo': 'Gemini (chat, relatório fornecido)', 'provedor': 'registro_historico'} for kind in choices}})
    if not pairs:
        raise RuntimeError('Sem pares reais completos. Gere a avaliação antes de iniciar a validação.')
    write_json(root / '07-validacao-alunos/pares.json', pairs)
    progress('7. Respostas offline', f'{len(pairs)} pares reais disponíveis; origem registrada em cada par. Não foram fabricadas respostas nem votos.', root)
    return pairs
