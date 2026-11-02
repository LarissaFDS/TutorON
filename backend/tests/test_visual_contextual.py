"""Dúvida aberta, acervo inferido e planejamento visual isolado por tarefa."""
import asyncio
import json

import httpx
import pytest

from backend import animacao, prompts
from backend.disciplina_auto import identificar
from backend.tests.test_api import esperar
from backend.tests.test_disciplinas import site  # noqa: F401


@pytest.mark.parametrize('texto,esperada', [
    ('Como preencher a tabela do robô numa grade com obstáculos?', 'paa'),
    ('Qual a direção da redução para provar NP-difícil?', 'paa'),
    ('T(n)=3T(n/4)+n, por onde começo?', 'paa'),
    ('Como agrupar no Karnaugh sem incluir um zero?', 'sd'),
    ('A porta E recebe um e zero', 'sd'),
    ('Como funciona o clock do flip-flop D?', 'sd'),
    ('Explique esta tabela', None),
    ('Um circuito implementa um algoritmo de fluxo máximo', None),
])
def test_identificacao_conservadora(texto, esperada):
    assert identificar(texto) == esperada


def test_contexto_ajuda_quando_enunciado_nao_tem_sinal_mas_nao_troca_tema_claro():
    assert identificar('Me ajude com a foto', 'Mapa de Karnaugh') == 'sd'
    assert identificar('Minha dúvida é sobre mochila 0/1', 'meu circuito') == 'paa'


def test_auto_resolve_acervo_e_permanece_nos_polls(site):  # noqa: F811
    t = esperar(site, site.post('/api/perguntar', json={'pergunta': 'Como começar o mapa de Karnaugh?',
                                                    'disciplina': 'auto'}).json())
    assert t['disciplina'] == 'sd' and t['status'] == 'pronta'
    assert 'Sistemas Digitais' in site.llm.chamadas[0][1]
    assert all('de PAA' not in f['titulo'] for f in t['fontes'])


def test_auto_ambiguo_pede_escolha_sem_chamar_modelo(site):  # noqa: F811
    r = site.post('/api/perguntar', json={'pergunta': 'Me explique esta tabela', 'disciplina': 'auto'})
    assert r.status_code == 409 and 'Escolha a disciplina' in r.json()['erro']
    assert not site.llm.chamadas


def test_animacao_recebe_tentativa_e_foto_em_campos_separados(site, monkeypatch):  # noqa: F811
    roteiro = {'modelo': 'esquema', 'titulo': 'Dependências da célula',
        'blocos': [{'id': 'anterior', 'texto': 'Célula anterior permitida'},
                   {'id': 'atual', 'texto': 'Custo para chegar à célula', 'lacuna': True}],
        'ligacoes': [['anterior', 'atual']], 'pergunta_final': 'Que informação você usaria aqui?'}
    site.llm.roteiro['g1'] = ('ok', json.dumps(roteiro))

    async def renderizar(r, pasta, qualidade='low_quality'):
        assert r['modelo'] == 'esquema'
        return 'videoContextual123'

    monkeypatch.setattr(animacao, 'disponivel', lambda: True)
    monkeypatch.setattr(animacao, 'renderizar', renderizar)
    t = esperar(site, site.post('/api/animar', json={'pergunta': 'Como montar a tabela do robô?',
        'disciplina': 'auto', 'contexto': 'Tentei usar a diagonal', 'foto': 'Minha foto já conferida: ' + 'x' * 5000}).json())
    assert t['status'] == 'pronta' and t['disciplina'] == 'paa'
    p = site.llm.chamadas[0][2]
    assert 'Tentei usar a diagonal' in p and 'Minha foto já conferida' in p


def test_navegacao_nao_tem_galeria_e_link_antigo_abre_compositor_visual(site):  # noqa: F811
    html = site.get('/').text
    assert 'Fase MVP' not in html and 'Aprender com desenhos' not in html
    assert 'Disciplina (opcional)' in html
    r = site.get('/visuais', follow_redirects=False)
    assert r.status_code == 307 and r.headers['location'] == '/?visual=1'


def test_script_da_interface_e_revalidado_apos_atualizacao(site):  # noqa: F811
    r = site.get('/static/app.js?v=conversa-visual-1')
    assert r.status_code == 200 and r.headers['cache-control'] == 'no-cache'
    assert 'Só animação' in r.text and 'Identificar automaticamente' in r.text
    condicional = site.get('/static/app.js?v=conversa-visual-1', headers={'If-None-Match': r.headers['etag']})
    assert condicional.status_code == 304 and condicional.headers['cache-control'] == 'no-cache'


def test_esquema_aberto_exige_lacuna_e_conexoes_validas():
    r = {'modelo': 'esquema', 'blocos': [{'id': 'a', 'texto': 'Conceito'},
        {'id': 'b', 'texto': 'Aplicação', 'lacuna': True}], 'ligacoes': [['a', 'b']]}
    assert animacao.roteiro_valido(r)['blocos'][1]['lacuna']
    assert animacao.roteiro_valido(r)['blocos'][1]['texto'] == 'Você completa'
    r['ligacoes'] = [['a', 'z']]
    with pytest.raises(animacao.FalhaAnimacao):
        animacao.roteiro_valido(r)


def test_planejamento_json_nao_usa_orcamento_curto_da_revisao():
    from backend.llm import LLM, Model, PLANEJAMENTO_JSON, SEM_RACIOCINIO
    from backend.config import Settings
    corpos = []

    def responder(req):
        if req.url.path.endswith('/show'):
            return httpx.Response(200, json={'capabilities': ['thinking']})
        corpos.append(json.loads(req.content))
        return httpx.Response(200, text='{"message":{"content":"{}"},"done":true}\n')

    async def executar():
        async with httpx.AsyncClient(transport=httpx.MockTransport(responder)) as c:
            llm = LLM(Settings(), client=c)
            j, s = PLANEJAMENTO_JSON.set(True), SEM_RACIOCINIO.set(True)
            try:
                assert [x async for x in llm._ollama(Model('ollama', 'teste'), prompts.SISTEMA_ANIMACAO, 'dúvida')]
            finally:
                PLANEJAMENTO_JSON.reset(j)
                SEM_RACIOCINIO.reset(s)
    asyncio.run(executar())
    assert corpos[0]['format'] == 'json' and corpos[0]['options']['num_predict'] == 2048
    assert not PLANEJAMENTO_JSON.get()


def test_revisao_visual_recebe_roteiro_normalizado_sem_mudar_revisao_textual():
    from types import SimpleNamespace
    from backend import tutoria
    from backend.llm import Model, Result
    recebidos = []

    async def complete(sistema, dados):
        recebidos.append((sistema, json.loads(dados)))
        return Result('{"aprovada":true,"motivo":"conceito correto, sem cálculo"}', Model('ollama', 'teste'), 0, [])

    async def revisar(p, c, r):
        return await tutoria.revisar_com_modelo(llm, p, c, r)

    llm = SimpleNamespace(complete=complete, revisar_ajuda=revisar)
    r = {'modelo': 'esquema', 'blocos': [{'id': 'a', 'texto': 'Entrada'},
        {'id': 'b', 'texto': 'Um resultado que não deve ficar visível', 'lacuna': True}]}
    normalizado = animacao.roteiro_valido(r)
    assert asyncio.run(tutoria.avaliar_roteiro(llm, 'p', 'c', normalizado))['aprovada']
    assert recebidos[0][0] == tutoria.SISTEMA_REVISOR_VISUAL
    assert 'Um resultado' not in recebidos[0][1]['ajuda_candidata']
    assert not tutoria.REVISAO_VISUAL.get()


def test_reformulacao_visual_retoma_enunciado_sem_perder_contexto_na_revisao(site, monkeypatch):  # noqa: F811
    from backend import tutoria
    roteiro = {'modelo': 'esquema', 'blocos': [{'id': 'a', 'texto': 'Subproblema menor'},
        {'id': 'b', 'texto': 'Estado?', 'lacuna': True}], 'pergunta_final': 'O que você precisa guardar?'}
    site.llm.roteiro['g1'] = ('ok', json.dumps(roteiro))
    contextos = []

    async def revisar(p, c, r):
        contextos.append(c)
        return {'aprovada': len(contextos) == 2, 'motivo': 'teste'}

    async def renderizar(*args):
        return 'videoRetomado123'

    monkeypatch.setattr(site.llm, 'revisar_ajuda', revisar)
    monkeypatch.setattr(animacao, 'renderizar', renderizar)
    monkeypatch.setattr(animacao, 'disponivel', lambda: True)
    t = esperar(site, site.post('/api/animar', json={'pergunta': 'Como definir o estado na programação dinâmica?',
        'resposta': 'AJUDA ANTERIOR INCONSISTENTE', 'disciplina': 'auto'}).json())
    assert t['status'] == 'pronta'
    assert 'AJUDA ANTERIOR INCONSISTENTE' in site.llm.chamadas[0][2]
    assert 'AJUDA ANTERIOR INCONSISTENTE' not in site.llm.chamadas[1][2]
    assert all('AJUDA ANTERIOR INCONSISTENTE' in c for c in contextos)
