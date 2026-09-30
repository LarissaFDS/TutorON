import csv
import json
from concurrent.futures import ThreadPoolExecutor

import pytest

from acervo.common import init, read_json, write_json, digest, TOPICS
from acervo.extract import inventory, extract, snapshot, topic_for
from acervo.curate import rule_findings, split_questions, organize, triage, searchable
from acervo.retrieval import build, search, context
from acervo import models
from acervo.app import Study, summarize


@pytest.fixture
def workspace(tmp_path):
    init(tmp_path)
    (tmp_path / 'materiais').mkdir()
    return tmp_path


def test_snapshot_versioned_and_no_original_writes(workspace):
    source = workspace / 'materiais/original.txt'
    source.write_text('original', encoding='utf-8')
    dest, sha = snapshot(source, workspace)
    assert dest.read_text() == source.read_text()
    assert snapshot(source, workspace) == (dest, sha)
    source.write_text('nova versão', encoding='utf-8')
    second, _ = snapshot(source, workspace)
    assert second != dest and dest.read_text() == 'original'


def test_pdf_inventory_extract_idempotent_and_corrupt_input(workspace):
    import pymupdf
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((50, 70), 'Questao 1. Prove a corretude de um algoritmo por inducao.')
    doc.save(workspace / 'materiais/prova.pdf')
    doc.close()
    (workspace / 'materiais/quebrado.pdf').write_bytes(b'not pdf')
    rows = inventory(workspace)
    extract(workspace)
    files = list((workspace / '01-extraido').glob('*.md'))
    assert len(rows) == len(files) == 2
    valid = next(r for r in rows if 'prova.pdf' in r['arquivo'])
    output = workspace / '01-extraido' / (valid['id'] + '.md')
    mtime = output.stat().st_mtime_ns
    extract(workspace)
    assert output.stat().st_mtime_ns == mtime
    broken = next(r for r in rows if 'quebrado.pdf' in r['arquivo'])
    assert read_json(workspace / '01-extraido' / (broken['id'] + '.json'))['paginas_extraidas'][0]['qualidade'] == 'ilegivel'


def test_taxonomy_filename_overrides_wrong_internal_title():
    assert topic_for('PAA_L4.pdf\nLista de Exercícios 3') == TOPICS[2]


@pytest.mark.parametrize('text,rule', [
    ('NP inclui problemas que ninguém conseguiu até hoje comprovar se são polinomiais.', 'np-definicao'),
    ('NP inclui problemas que ningu´em conseguiu at´e hoje comprovar se s˜ao polinomiais.', 'np-definicao'),
    ('Aumenta-se o custo de cada árvore gerada também por uma unidade.', 'agm-incremento'),
    ('Aumenta-se o custo de cada ´arvore gerada tamb´em por uma unidade.', 'agm-incremento'),
])
def test_known_errors_even_with_pdf_diacritics(text, rule):
    assert rule in [f['regra'] for f in rule_findings(text)]


def test_split_keeps_question_across_pages():
    pages = [{'pagina': 1, 'qualidade': 'boa', 'texto': '1. Considere um grafo.\nSolução: primeira parte\n'},
             {'pagina': 2, 'qualidade': 'parcial', 'texto': 'continuação da solução\n2. Defina NP.\n'}]
    parts = split_questions(pages)
    assert len(parts) == 2
    assert 'continuação' in parts[0]['texto'] and parts[0]['paginas'] == [1, 2]


def test_segmentation_ignores_lower_numbered_solution_steps():
    p = {'pagina': 1, 'qualidade': 'boa', 'texto': '1. Questão inicial.\n2. Segunda questão.\n1. Etapa interna.\n3. Terceira questão.'}
    parts = split_questions([p])
    assert [r['numero'] for r in parts] == ['1', '2', '3']
    assert 'Etapa interna' in parts[1]['texto']


def test_question_number_on_separate_pdf_line_is_preserved():
    text = '3. Questão anterior.\n4.\nUma subsequência contígua.\n5. Próxima questão.'
    parts = split_questions([{'pagina':4,'qualidade':'parcial','texto':text}])
    assert [p['numero'] for p in parts] == ['3','4','5']
    assert parts[1]['texto'].startswith('4.\nUma')


def seed_item(identifier, text, confidence='nao_verificada'):
    return {'id': identifier, 'texto': text, 'sha256': digest(text), 'confiabilidade': confidence,
            'qualidade_ocr': 'boa', 'assunto': TOPICS[0], 'segmentacao': 'automatica',
            'fonte_original': 'lista.pdf | p1', 'tem_resposta': 's'}


def test_low_confidence_never_enters_search_and_revocation_is_immediate(workspace):
    good = seed_item('bom', 'ASTERISCO imprime uma recorrência.')
    bad = seed_item('ruim', 'ASTERISCO ASTERISCO ASTERISCO', 'baixa')
    write_json(workspace / '02-acervo/itens.json', [good, bad])
    index = build(workspace)
    assert [r['id'] for r in index['chunks']] == ['bom']
    assert search('ASTERISCO', workspace, semantic=False)[0]['id'] == 'bom'
    good['confiabilidade'] = 'baixa'
    write_json(workspace / '02-acervo/itens.json', [good, bad])
    assert search('ASTERISCO', workspace, semantic=False) == []


def test_embedding_failure_degrades_to_lexical_without_fake_vectors(workspace, monkeypatch):
    write_json(workspace / '02-acervo/itens.json', [seed_item('a', 'ASTERISCO')])
    monkeypatch.setattr(models, 'embeddings', lambda *a, **k: (_ for _ in ()).throw(TimeoutError()))
    index = build(workspace, embed=True)
    assert index['modo'] == 'lexical' and not index['vectors']
    assert search('ASTERISCO', workspace)[0]['id'] == 'a'


@pytest.mark.parametrize('failure', [TimeoutError, ValueError, ConnectionError])
def test_gemini_failure_uses_local_and_records_provider(monkeypatch, failure):
    monkeypatch.setenv('GEMINI_API_KEY', 'fake-test-key')
    monkeypatch.setattr(models, 'post', lambda *a, **k: (_ for _ in ()).throw(failure()))
    monkeypatch.setattr(models, 'local', lambda *a, **k: 'resposta local de teste')
    result = models.generate('pergunta', provider='auto')
    assert result['provedor'] == 'ollama' and result['fallback'] == failure.__name__


@pytest.mark.parametrize('second_truncated', [False, True])
def test_generation_retries_truncation_once_without_serving_partial(monkeypatch, second_truncated):
    budgets = []

    def fake_post(url, payload, timeout):
        budgets.append(payload['options']['num_predict'])
        truncated = len(budgets) == 1 or second_truncated
        return {'response': 'incompleta' if truncated else 'concluída',
                'done_reason': 'length' if truncated else 'stop'}

    monkeypatch.setattr(models, 'post', fake_post)
    if second_truncated:
        with pytest.raises(models.TruncatedResponse):
            models.generate('pergunta', provider='ollama')
    else:
        result = models.generate('pergunta', provider='ollama')
        assert result['texto'] == 'concluída'
        assert result['repetida_por_truncamento'] is True
        assert result['limite_saida_tokens'] == 3600
    assert budgets == [1800, 3600]


def test_blind_vote_maps_scores_prevents_duplicate_and_csv_injection(workspace):
    folder = workspace / '07-validacao-alunos'
    write_json(folder / 'pares.json', [{'id': 'q1', 'pergunta': 'Pergunta?', 'origem': 'teste',
                                       'generico': {'texto': 'gen'}, 'tutoron': {'texto': 'rag'}}])
    study = Study(workspace)
    response = study.start('q1')
    assert set(response) == {'sessao', 'pergunta', 'A', 'B'}
    order = study.sessions[response['sessao']]['ordem']
    data = {'sessao': response['sessao'], 'preferida': 'A', 'comentario': '=HYPERLINK("x")',
            **{key+'_'+side: 4 if side == 'a' else 2 for side in ['a', 'b'] for key in ['clareza', 'confianca', 'utilidade']}}
    assert study.vote(data) == {'salvo': True}
    with pytest.raises(ValueError):
        study.vote(data)
    summary = summarize(workspace)
    assert summary['total'] == 1
    assert summary['por_questao'][0]['preferencia_' + order[0]] == 100
    with (folder / 'respostas.csv').open(encoding='utf-8-sig') as f:
        saved = list(csv.DictReader(f))[0]
    assert saved['comentario'].startswith("'=")


def test_concurrent_double_submit_is_single_vote(workspace):
    write_json(workspace / '07-validacao-alunos/pares.json', [{'id':'q','pergunta':'q','origem':'teste','generico':{'texto':'a'},'tutoron':{'texto':'b'}}])
    study = Study(workspace)
    pair = study.start('q')
    data = {'sessao': pair['sessao'], 'preferida':'empate', **{key+'_'+s: 3 for s in ['a','b'] for key in ['clareza','confianca','utilidade']}}
    def submit():
        try: return study.vote(data)
        except ValueError: return None
    with ThreadPoolExecutor(2) as pool:
        outcomes = list(pool.map(lambda _: submit(), range(2)))
    assert sum(o is not None for o in outcomes) == 1
    assert summarize(workspace)['total'] == 1


def test_invalid_rating_does_not_save(workspace):
    write_json(workspace / '07-validacao-alunos/pares.json', [{'id':'q','pergunta':'q','origem':'teste','generico':{'texto':'a'},'tutoron':{'texto':'b'}}])
    study = Study(workspace)
    pair = study.start('q')
    with pytest.raises(ValueError):
        study.vote({'sessao':pair['sessao'], 'preferida':'A','clareza_a':True})
    assert not (workspace / '07-validacao-alunos/respostas.csv').exists()


def test_cached_ai_suspicion_survives_non_ai_rerun(workspace):
    item = seed_item('a', 'Solução de ASTERISCO a revisar.')
    write_json(workspace / '02-acervo/itens.json', [item])
    write_json(workspace / '03-triagem/pareceres-ia/a.json',
               {'sha256': item['sha256'], 'status': 'executado', 'decisao': 'suspeita', 'parecer': 'Conta inconsistente.'})
    assert triage(workspace, use_ai=False)[0]['confiabilidade'] == 'baixa'


def test_human_approval_expires_when_source_changes(workspace):
    item = seed_item('a', 'Solução inicial.')
    write_json(workspace / '03-triagem/revisoes.json', {'a': {'sha256': item['sha256'], 'revisor': 'Revisor de teste',
                                                          'justificativa':'Conferido.', 'confiabilidade':'alta'}})
    write_json(workspace / '02-acervo/itens.json', [item])
    assert triage(workspace)[0]['confiabilidade'] == 'alta'
    item['texto'] = 'Solução alterada.'
    item['sha256'] = digest(item['texto'])
    write_json(workspace / '02-acervo/itens.json', [item])
    assert triage(workspace)[0]['confiabilidade'] == 'nao_verificada'
