"""Validade técnica, parcialidade e integração dos desenhos didáticos."""
import asyncio
from copy import deepcopy

import pytest

from backend import animacao
from backend.animacao import galeria
from backend.tests.test_api import esperar
from backend.tests.test_disciplinas import site  # noqa: F401


def exemplo(ident):
    return deepcopy(galeria.obter(ident)['roteiro'])


def test_catalogo_cobre_temas_e_roteiros_parciais():
    es = galeria.exemplos()
    assert len({e['id'] for e in es}) == len(es) == 7
    assert {e['disciplina'] for e in es} == {'paa', 'sd'}
    for e in es:
        r = animacao.roteiro_valido(e['roteiro'])
        assert r['pergunta_final'] and e['tarefa'] and e['pergunta']
    # Nem rota calculada, nem tabela de estados, nem saídas do circuito ou expressão simplificada.
    for ident, campo in [('robo-dp', 'caminho'), ('circuito-tabela', 'saidas'), ('karnaugh-bordas', 'expressao')]:
        r = exemplo(ident)
        r[campo] = 'resposta pronta'
        with pytest.raises(animacao.FalhaAnimacao):
            animacao.roteiro_valido(r)


@pytest.mark.parametrize('grupo', [
    [[0, 0], [0, 1]],  # inclui zero obrigatório
    [[0, 0], [0, 3], [1, 3]],  # três células e forma de L
    [[0, 0], [2, 0]],  # linhas não adjacentes
    [[0, 0], [0, 0]],  # repetição
])
def test_karnaugh_recusa_grupo_invalido(grupo):
    r = exemplo('karnaugh-bordas')
    r['grupo'] = grupo
    with pytest.raises(animacao.FalhaAnimacao):
        animacao.roteiro_valido(r)


def test_karnaugh_aceita_bordas_e_x_mas_nao_cobre_todos_os_uns():
    r = exemplo('karnaugh-bordas')
    assert animacao.roteiro_valido(r)['grupo'] == [[0, 0], [0, 3]]
    r['celulas'][0][3] = 'X'
    animacao.roteiro_valido(r)
    r['celulas'] = [['1', '0', '0', 'X'], ['0', '0', '0', '0']]
    with pytest.raises(animacao.FalhaAnimacao, match='parcial'):
        animacao.roteiro_valido(r)


@pytest.mark.parametrize('alteracao', ['capacidade', 'conservacao', 'caminho_completo'])
def test_fluxo_preserva_capacidade_conservacao_e_passo_parcial(alteracao):
    r = exemplo('fluxo-residual')
    if alteracao == 'capacidade':
        r['arestas'][0]['fluxo'] = 8
    elif alteracao == 'conservacao':
        r['arestas'][0]['fluxo'] = 4
    else:
        r['primeiro_passo'] = ['s', 't']
    with pytest.raises(animacao.FalhaAnimacao):
        animacao.roteiro_valido(r)


def test_circuito_recusa_ciclo_e_robot_nao_pisa_em_bloqueio():
    r = exemplo('circuito-tabela')
    r['portas'][0]['entradas'] = ['Y', 'B']
    with pytest.raises(animacao.FalhaAnimacao):
        animacao.roteiro_valido(r)
    r = exemplo('robo-dp')
    r['foco'] = [1, 2]
    with pytest.raises(animacao.FalhaAnimacao):
        animacao.roteiro_valido(r)


def test_grafo_recusa_posicoes_ausentes_ou_nao_finitas():
    r = exemplo('grafo-bfs')
    r['posicoes']['A'] = [float('nan'), 0]
    with pytest.raises(animacao.FalhaAnimacao):
        animacao.roteiro_valido(r)


def test_cache_coalesce_pedidos_iguais_sem_chamar_ia(tmp_path, monkeypatch):
    chamadas = []

    async def renderizar(roteiro, pasta):
        chamadas.append(roteiro)
        await asyncio.sleep(.01)
        pasta.mkdir(exist_ok=True)
        (pasta / 'temporario123.mp4').write_bytes(b'video')
        return 'temporario123'

    monkeypatch.setattr(galeria, 'renderizar', renderizar)
    monkeypatch.setattr(galeria, 'gerar_poster', lambda video, destino: destino.write_bytes(b'jpg'))

    async def concorrentes():
        return await asyncio.gather(*(galeria.preparar(galeria.obter('robo-dp'), tmp_path) for _ in range(3)))

    ids = asyncio.run(concorrentes())
    assert len(set(ids)) == 1 and len(chamadas) == 1
    assert (tmp_path / f'{ids[0]}.mp4').read_bytes() == b'video'
    assert (tmp_path / f'{ids[0]}.jpg').read_bytes() == b'jpg'


def test_fluxo_da_galeria_serve_video_e_poster_sem_modelo(site, monkeypatch):  # noqa: F811
    async def renderizar(roteiro, pasta):
        pasta.mkdir(exist_ok=True)
        (pasta / 'video12345.mp4').write_bytes(b'video mp4 de teste')
        return 'video12345'

    monkeypatch.setattr(animacao, 'disponivel', lambda: True)
    monkeypatch.setattr(galeria, 'renderizar', renderizar)
    monkeypatch.setattr(galeria, 'gerar_poster', lambda video, destino: destino.write_bytes(b'poster'))
    lista = site.get('/api/visuais').json()
    assert len(lista['exemplos']) == 7 and all(e['video'] is None for e in lista['exemplos'])
    assert 'roteiro' not in lista['exemplos'][0]
    r = esperar(site, site.post('/api/visuais/robo-dp', json={'roteiro': {'codigo': 'ignorado'}}).json())
    assert r['status'] == 'pronta' and site.get(r['video']).content == b'video mp4 de teste'
    assert site.get(r['poster']).headers['content-type'] == 'image/jpeg'
    assert not site.llm.chamadas
    assert site.get('/api/visuais').json()['exemplos'][0]['video'] == r['video']
    assert site.post('/api/visuais/desconhecido').status_code == 404
    assert site.get('/api/animacoes/visual_invalido.jpg').status_code == 404
    assert site.get('/visuais').status_code == 200
    assert site.get('/static/visuais.js').status_code == 200


def test_galeria_indisponivel_retorna_erro_claro(site, monkeypatch):  # noqa: F811
    monkeypatch.setattr(animacao, 'disponivel', lambda: False)
    assert site.post('/api/visuais/robo-dp').status_code == 503


@pytest.mark.parametrize('pergunta,disciplina,ident', [
    ('Como desenhar a grade de um robô?', 'paa', 'robo-dp'),
    ('Como enxergar adjacência no Karnaugh?', 'sd', 'karnaugh-bordas'),
])
def test_roteiro_invalido_nao_substitui_duvida_por_tema_fixo(site, monkeypatch, pergunta, disciplina, ident):  # noqa: F811
    site.llm.roteiro['g1'] = ('ok', 'roteiro inválido')

    async def preparar(e, pasta):
        pytest.fail('A animação contextual não pode ser substituída pelo catálogo')

    monkeypatch.setattr(animacao, 'disponivel', lambda: True)
    monkeypatch.setattr(galeria, 'preparar', preparar)
    t = esperar(site, site.post('/api/animar', json={'pergunta': pergunta, 'disciplina': disciplina}).json())
    assert t['status'] == 'erro' and 'video' not in t
    assert 'Diga qual relação' in t['mensagem']


def test_sugestao_visual_nao_cruza_disciplinas_nem_inventa_cobertura():
    assert galeria.sugerir('Karnaugh', 'paa') is None
    assert galeria.sugerir('Mochila 0/1', 'paa') is None
    assert galeria.sugerir('Rede de fluxo residual', 'paa')['id'] == 'fluxo-residual'
