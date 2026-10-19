"""Cadastro de disciplinas, acervo de Sistemas Digitais e catálogo de fontes.

As resoluções do acervo de SD afirmam resultados (expressões mínimas, equações de FSM);
aqui elas são conferidas por enumeração, como as verificações objetivas da triagem de PAA.
"""
from itertools import product

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

SD = disciplinas.obter('sd')
FONTES = read_json(ROOT / 'disciplinas/sd/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}


def buscar_sd(pergunta):
    return search(pergunta, semantic=False, itens=SD.itens, indice=SD.indice)


# ---------------------------------------------------------------- cadastro

def test_sem_disciplina_vale_paa_e_caminhos_de_paa_nao_mudam():
    paa = disciplinas.obter()
    assert paa.id == 'paa' and disciplinas.obter('PAA') == paa
    assert paa.itens == ROOT / '02-acervo/itens.json' and paa.indice == ROOT / '04-rag/indice.json'
    assert paa.livro_supabase and not SD.livro_supabase  # o livro do Supabase é só de PAA


def test_disciplina_desconhecida():
    with pytest.raises(KeyError):
        disciplinas.obter('quimica')


def test_acervo_de_sd_localizado_e_separado_do_de_paa():
    assert SD.nome == 'Sistemas Digitais' and SD.itens.exists() and SD.indice.exists()
    paa = disciplinas.obter('paa')
    assert {SD.itens, SD.indice}.isdisjoint({paa.itens, paa.indice})
    ids_sd = {c['id'] for c in read_json(SD.indice)['chunks']}
    ids_paa = {c['id'] for c in read_json(paa.indice)['chunks']}
    assert ids_sd and ids_paa and ids_sd.isdisjoint(ids_paa)
    assert all(c['disciplina'] == 'sd' for c in read_json(SD.indice)['chunks'])


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas sd` (docs/DISCIPLINAS.md)."""
    gerados = disciplinas.registros(SD)
    assert gerados == read_json(SD.itens)
    indexados = {c['id'] for c in read_json(SD.indice)['chunks']}
    assert indexados == {i['id'] for i in gerados if i['confiabilidade'] in ('media', 'alta')}


def test_cabecalho_obrigatorio_e_curadoria(tmp_path):
    (tmp_path / 'x.md').write_text('---\nid: x\ntitulo: t\n---\ntexto', encoding='utf-8')
    with pytest.raises(ValueError, match='falta'):
        disciplinas.ler(tmp_path / 'x.md')
    cabecalho = 'id: x\ntitulo: t\nassunto: a\ntipo: lista\nfonte: f\nautoria: a\nlicenca: l\n'
    (tmp_path / 'y.md').write_text(f'---\n{cabecalho}curadoria: talvez\n---\ntexto', encoding='utf-8')
    with pytest.raises(ValueError, match='curadoria'):
        disciplinas.ler(tmp_path / 'y.md')


def test_candidato_e_rejeitado_ficam_fora_da_busca(tmp_path):
    (tmp_path / 'materiais').mkdir()
    base = 'titulo: t\nassunto: a\ntipo: lista\nfonte: f\nautoria: a\nlicenca: l\n'
    for ident, status in (('ok', 'aprovado'), ('cand', 'candidato'), ('rej', 'rejeitado')):
        (tmp_path / 'materiais' / f'{ident}.md').write_text(
            f'---\nid: {ident}\n{base}curadoria: {status}\n---\nmultiplexador {ident}', encoding='utf-8')
    d = disciplinas.Disciplina('t', 'Teste', 'T', tmp_path / 'itens.json', tmp_path / 'indice.json', rigor='',
                               materiais=tmp_path / 'materiais')
    disciplinas.construir(d, root=tmp_path)
    assert [c['id'] for c in read_json(d.indice)['chunks']] == ['ok']


# ---------------------------------------------------------------- busca

@pytest.mark.parametrize('pergunta, esperado', [
    ('Como simplifico com mapa de Karnaugh usando irrelevâncias?', 'sd-nota-karnaugh'),
    ('Qual o complemento de 2 de 101010?', 'sd-av1-q01-07'),
    ('Como desenhar a saída Q do flip-flop D no diagrama de tempo?', 'sd-nota-latches-flip-flops'),
    ('Como separar bloco operacional e bloco de controle no Fibonacci?', 'sd-av2-q05-06-08'),
    ('Circuito das catracas do restaurante com prioridade', 'sd-reav-q1-q3'),
])
def test_pergunta_de_sd_encontra_material_pertinente(pergunta, esperado):
    ids = [r['id'] for r in buscar_sd(pergunta)]
    assert ids[0] == esperado


def test_pergunta_fora_do_acervo_nao_inventa_material():
    assert buscar_sd('Explique a heurística de Dijkstra para grafos esparsos') == []


# ---------------------------------------------------------------- catálogo

def test_catalogo_completo_e_coerente():
    obrigatorios = {'id', 'nome', 'autoria', 'url', 'idioma', 'formato', 'topicos', 'licenca', 'acesso',
                    'prioridade', 'uso', 'justificativa'}
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f['id']
        assert f['prioridade'] in ('alta', 'media', 'referencia')
        assert f['uso'] in ('acervo', 'citada', 'referencia', 'candidato', 'indisponivel')
        assert set(f['topicos']) <= set(SD.assuntos), f['id']
    itens = read_json(SD.itens)
    citadas = {x for i in itens for x in i['fontes_catalogo']}
    assert citadas <= set(CATALOGO)
    # Toda fonte marcada como "acervo" tem bloco no acervo, e vice-versa.
    assert {i for i, f in CATALOGO.items() if f['uso'] == 'acervo'} == {
        x for i in itens if not i['id'].startswith('sd-nota') for x in i['fontes_catalogo']}


def test_material_protegido_nao_entra_no_acervo():
    assert CATALOGO['vahid-sistemas-digitais']['uso'] == 'referencia'
    for f in FONTES:
        if 'direitos autorais' in f['licenca'] or 'Não declarada no PDF' in f['licenca']:
            assert f['uso'] in ('referencia', 'candidato'), f['id']
    # Nenhum original (PDF, DOCX, vídeo) de SD é versionado: só as transcrições.
    arquivos = [p for p in (ROOT / 'disciplinas').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.docx', '.mkv', '.mp4', '.vhd')]


def test_documentacao_lista_todas_as_fontes():
    curadoria = (ROOT / 'disciplinas/sd/CURADORIA.md').read_text(encoding='utf-8')
    assert [i for i in CATALOGO if f'`{i}`' not in curadoria] == []


# ---------------------------------------------------------------- resoluções afirmadas no acervo

def bits(n):
    return product((0, 1), repeat=n)


def test_resolucoes_da_lista_av1():
    s6 = lambda a, b, c, d: (a ^ b) & ((b & (a | c)) | (d & (a | b | c)))
    assert all(s6(*v) == (((v[0] ^ v[1]) & v[3]) | ((1 - v[0]) & v[1] & v[2])) for v in bits(4))
    t7a = [1, 1, 0, 1, 0, 1, 0, 1]
    assert all(t7a[i] == (c | ((1 - a) & (1 - b))) for i, (a, b, c) in enumerate(bits(3)))
    t7b = {0: 1, 2: 0, 3: 1, 5: 1}  # demais linhas irrelevantes
    assert all(t7b[i] == ((1 - b) | c) for i, (a, b, c) in enumerate(bits(3)) if i in t7b)
    assert (0b11001 + 0b1011, 0b10010 - 0b10001, 0b1100 * 0b011) == (0b100100, 1, 0b100100)
    assert (2 ** 6 - 0b101010) == 0b010110
    segmentos = {0: 'abcdef', 1: 'bc', 2: 'abdeg', 3: 'abcdg'}
    for x1, x0 in bits(2):
        acesos = {'a': x1 | (1 - x0), 'b': 1, 'c': (1 - x1) | x0, 'd': x1 | (1 - x0), 'e': 1 - x0,
                  'f': (1 - x1) & (1 - x0), 'g': x1}
        assert {s for s, v in acesos.items() if v} == set(segmentos[2 * x1 + x0])


def test_karnaugh_da_nota():
    mintermos = {0, 2, 5, 7, 8, 10, 13, 15}
    assert all((i in mintermos) == bool(((1 - b) & (1 - d)) | (b & d)) for i, (a, b, c, d) in enumerate(bits(4)))


def test_fsm_da_prova2():
    def figura(estado, a, b):
        return {'A': 'A' if a else ('B' if b else 'C'), 'B': 'C' if a else 'B', 'C': 'D' if b else 'C', 'D': 'A'}[estado]
    codigo = {'A': (0, 0), 'B': (0, 1), 'C': (1, 0), 'D': (1, 1)}
    estado_de = {v: k for k, v in codigo.items()}
    for estado, a, b in product('ABCD', (0, 1), (0, 1)):
        s1, s0 = codigo[estado]
        n = lambda x: 1 - x
        n1 = (n(s1) & n(s0) & n(a) & n(b)) | (n(s1) & s0 & a) | (s1 & n(s0))
        n0 = (n(s1) & n(s0) & n(a) & b) | (n(s1) & s0 & n(a)) | (s1 & n(s0) & b)
        assert estado_de[(n1, n0)] == figura(estado, a, b)
        assert (s1 ^ s0) == (estado in 'BC')


def test_catracas_da_reav():
    for a, b, c, d in bits(4):
        abertas, n = [], 0
        for fila in (a, b, c, d):
            abre = int(bool(fila) and n < 2)
            n += abre
            abertas.append(abre)
        nb = lambda x: 1 - x
        assert abertas == [a, b, c & nb(a & b), d & ((nb(a) & nb(b)) | (nb(a) & nb(c)) | (nb(b) & nb(c)))]


def test_contas_da_prova1_e_av2():
    assert 10 / 0b10100 * 0b11101 == 14.5  # conversor D/A
    assert all(((a + (~b & 0xF) + 1) & 0xF) == a - b for a in range(16) for b in range(a + 1))
    assert all(((a + b) >> 1) == (a + b) // 2 for a in range(16) for b in range(16))
    assert all(int(e and a >= b) == int(e and (a > b or a == b)) for e in (0, 1) for a in range(4) for b in range(4))
    for s0, s1, ligada in product((0, 1), repeat=3):  # bomba d'água com histerese: B+ = S0' + B·S1'
        if s1 and not s0:
            continue  # sensor de cima molhado com o de baixo seco é impossível
        proximo = (1 - s0) | (ligada & (1 - s1))
        assert proximo == (1 if not s0 else 0 if s1 else ligada)
    assert int('0001001111101000', 2) == 5096
