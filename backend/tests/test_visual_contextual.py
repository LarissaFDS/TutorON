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


def test_animacao_sem_disciplina_identificada_usa_conhecimento_geral(site, monkeypatch):  # noqa: F811
    # Desde 24/11/2026 qualquer assunto pode virar animação/imagem (blocos narrados), mesmo sem acervo.
    monkeypatch.setattr(animacao, 'disponivel', lambda: True)
    for disciplina in ('auto', 'geral'):
        r = site.post('/api/animar', json={'pergunta': 'Me explique esta tabela', 'disciplina': disciplina})
        assert r.status_code == 200 and r.json()['disciplina'] == 'geral'


def test_animacao_recebe_tentativa_e_foto_em_campos_separados(site, monkeypatch):  # noqa: F811
    roteiro = {'modelo': 'esquema', 'titulo': 'Dependências da célula',
        'blocos': [{'id': 'anterior', 'texto': 'Célula anterior permitida'},
                   {'id': 'atual', 'texto': 'Custo para chegar à célula', 'lacuna': True}],
        'ligacoes': [['anterior', 'atual']], 'pergunta_final': 'Que informação você usaria aqui?'}
    site.llm.roteiro['g1'] = ('ok', json.dumps(roteiro))

    async def renderizar(r, pasta, qualidade='low_quality', **_):
        assert r['modelo'] == 'esquema'
        return 'videoContextual123'

    monkeypatch.setattr(animacao, 'disponivel', lambda: True)
    monkeypatch.setattr(animacao, 'renderizar', renderizar)
    t = esperar(site, site.post('/api/animar', json={'pergunta': 'Como montar a tabela do robô?',
        'disciplina': 'auto', 'contexto': 'Tentei usar a diagonal', 'foto': 'Minha foto já conferida: ' + 'x' * 5000}).json())
    assert t['status'] == 'pronta' and t['disciplina'] == 'paa'
    p = site.llm.chamadas[0][2]
    assert 'Tentei usar a diagonal' in p and 'Minha foto já conferida' in p


def test_aba_visual_separada_tem_pergunta_livre_e_recomendacoes_opcionais(site):  # noqa: F811
    html = site.get('/').text
    assert 'Fase MVP' not in html and 'href="/visuais"' in html and 'Aprender com desenhos' in html
    assert 'id="temas-visuais"' not in html and 'id="sugestoes-visuais"' not in html
    assert 'Disciplina (opcional)' in html
    r = site.get('/visuais', follow_redirects=False)
    assert r.status_code == 200 and 'Temas recomendados' in r.text
    assert 'id="livre-pergunta"' in r.text and 'id="livre-form"' in r.text
    # mesmo layout do chat: barra lateral e caixa de mensagem, sem o cabeçalho antigo
    assert 'class="lateral"' in r.text and 'chat.css' in r.text and 'masthead' not in r.text
    assert 'masthead' not in site.get('/demo').text


def test_script_da_interface_e_revalidado_apos_atualizacao(site):  # noqa: F811
    r = site.get('/static/app.js?v=abas-visuais-2')
    assert r.status_code == 200 and r.headers['cache-control'] == 'no-cache'
    assert 'Só animação' in r.text and "'auto'" in r.text
    assert 'Identificar automaticamente' in site.get('/').text
    condicional = site.get('/static/app.js?v=abas-visuais-2', headers={'If-None-Match': r.headers['etag']})
    assert condicional.status_code == 304 and condicional.headers['cache-control'] == 'no-cache'
    assert site.get('/static/visuais.js?v=pergunta-livre-2').headers['cache-control'] == 'no-cache'


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

    async def renderizar(*args, **_):
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


def test_esquema_lacuna_com_pergunta_guia_e_texto_longo_cortado():
    r = {'modelo': 'esquema', 'blocos': [
        {'id': 'a', 'texto': 'Atuador: amplifica o comando Vc ' * 4, 'legenda': 'O comando é fraco.'},
        {'id': 'b', 'texto': 'Qual o papel do sensor?', 'lacuna': True},
        {'id': 'c', 'texto': 'K_a = 5', 'lacuna': True}], 'ligacoes': [['a', 'b'], ['b', 'a']]}
    v = animacao.roteiro_valido(r)
    assert len(v['blocos'][0]['texto']) <= 90 and v['blocos'][0]['texto'].endswith('…')
    assert v['blocos'][1]['texto'] == 'Qual o papel do sensor?'  # pergunta-guia fica
    assert v['blocos'][2]['texto'] == 'Você completa'  # valor pronto nunca aparece


def test_rota_de_imagem_recusa_nome_invalido_e_arquivo_ausente(site):
    assert site.get('/api/animacoes/x.png').status_code == 404
    assert site.get('/api/animacoes/abcdefghijkl.png').status_code == 404


def test_feedback_aceita_correcao_de_disciplina(site):
    r = site.post('/api/feedback', json={'id': 'abc-d', 'tipo': 'disciplina', 'util': False,
                                         'comentario': 'detectada=sd; correta=controle'})
    assert r.status_code == 200
