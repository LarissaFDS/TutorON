"""Acervo de Estrutura de Dados e conferência do código C.

Os blocos trazem código C revisado das anotações da turma. Cada trecho de código de um bloco é cópia exata
de uma função dos programas de tests_acervo/c_ed/, que aqui são compilados com -Wall -Wextra -pedantic -Werror
e rodados (com AddressSanitizer e UBSan quando houver um gcc que os tenha).
"""
import heapq
import itertools
import json
import re
import shutil
import subprocess

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search, tokens

ED = disciplinas.obter('ed')
FONTES = read_json(ROOT / 'disciplinas/ed/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {i['id']: i for i in read_json(ED.itens)}
C_ED = ROOT / 'tests_acervo/c_ed'
PROGRAMAS = sorted(C_ED.glob('*.c'))
FLAGS = ['-std=c99', '-Wall', '-Wextra', '-pedantic', '-Werror', '-g']
SANITIZADORES = ['-fsanitize=address,undefined', '-fno-sanitize-recover=all']
OUTRAS = ('paa', 'sd', 'oac', 'calc3', 'fis2')


def buscar(pergunta, d=ED):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return ITENS[ident]['texto']


# ---------------------------------------------------------------- cadastro e acervo

def test_ed_cadastrada_com_acervo_proprio():
    assert ED.nome == 'Estrutura de Dados' and ED.itens.exists() and ED.indice.exists() and not ED.livro_supabase
    assert ED.situacao == 'beta' and not ED.em_validacao and 'não foi validado pelo professor' in ED.aviso
    ids = {c['id'] for c in read_json(ED.indice)['chunks']}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({ED.itens, ED.indice})
        assert ids.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    assert all(c['disciplina'] == 'ed' for c in read_json(ED.indice)['chunks'])
    assert {i['assunto'] for i in ITENS.values()} == set(ED.assuntos)


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas ed --embeddings`."""
    gerados = disciplinas.registros(ED)
    assert gerados == read_json(ED.itens)
    assert {c['id'] for c in read_json(ED.indice)['chunks']} == {
        i['id'] for i in gerados if i['confiabilidade'] in ('media', 'alta')}


def test_blocos_cabem_no_trecho():
    for i in ITENS.values():
        assert len(i['texto']) <= 2200, i['id']  # backend/rag.py corta acima disso


def test_notas_da_ia_ficam_fora_da_busca():
    na_busca = {c['id'] for c in read_json(ED.indice)['chunks']}
    notas = {i for i, x in ITENS.items() if x['natureza'] == 'nota_da_equipe_ia'}
    assert notas == {'ed-nota-avl', 'ed-nota-depuracao-memoria'}
    assert na_busca.isdisjoint(notas)
    assert all(ITENS[i]['status_curadoria'] == 'candidato' and ITENS[i]['confiabilidade'] == 'nao_verificada'
               for i in notas)


def test_nenhum_bloco_aprovado_pelo_professor_ou_revisado_por_humano():
    for p in ED.materiais.glob('*.md'):
        cab = p.read_text(encoding='utf-8').split('---')[1]
        assert 'revisao_humana: pendente' in cab and 'revisao_professor' not in cab, p.name


# ---------------------------------------------------------------- busca, notação e isolamento

@pytest.mark.parametrize('pergunta, aceitos', [
    ('Como remover o último nó de uma lista encadeada?', {'ed-notion-ponteiros-lista', 'ed-notion-listas-genericas'}),
    ('Por que meu heap escreve fora do vetor quando fica cheio?', {'ed-notion-heap'}),
    ('Como tratar colisões numa tabela hash com endereçamento aberto?', {'ed-notion-hash'}),
    ('Quando a AVL faz rotação dupla?', {'ed-notion-abb'}),
    ('Qual a diferença entre BFS e DFS na implementação?', {'ed-notion-grafos'}),
    ('Como funciona o merge sort em C?', {'ed-notion-quick-merge'}),
    ('O quick sort tem pior caso n ao quadrado?', {'ed-notion-quick-merge', 'ed-notion-recorrencias'}),
    ('Big-O de dois laços aninhados', {'ed-notion-big-o'}),
    ('Como fazer a busca binária?', {'ed-notion-busca'}),
    ('Por que T(1) = 1 na recorrência?', {'ed-notion-recorrencias'}),
    ('pilha vazia pop retorna -1', {'ed-notion-pilha-fila'}),
    ('como usar void* numa lista genérica', {'ed-notion-listas-genericas'}),
    ('Como montar a árvore de Huffman?', {'ed-prof-huffman', 'ed-prof-projetos-ab2'}),
    ('Como ler um arquivo DIMACS no SAT solver?', {'ed-prof-sat', 'ed-prof-projetos-ab2'}),
])
def test_pergunta_de_ed_encontra_material_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize('variantes, bloco', [
    (('p->prox = NULL;', 'ponteiro para o próximo nó nulo no fim da lista'), 'ed-notion-ponteiros-lista'),
    (('sizeof(int*)', 'Qual o tamanho de um int com sizeof?', 'printf com %zu ou %lu para size_t'), 'ed-notion-sizeof-alocacao'),
])
def test_variantes_de_codigo_e_texto_chegam_ao_mesmo_bloco(variantes, bloco):
    assert {buscar(v)[0] for v in variantes} == {bloco}


def test_tokenizador_reduz_codigo_a_palavras():
    """Limitação conhecida: tokens() guarda só [a-z0-9]; `->`, `*` e `;` somem e a busca casa pelo nome."""
    assert tokens('p->prox = NULL;') == ['prox', 'null'] and tokens('sizeof(int*)') == ['sizeof', 'int']


@pytest.mark.parametrize('pergunta', [
    'Explique a heurística de Dijkstra para grafos esparsos', 'Qual o período de um pêndulo simples?',
    'O que é um flip-flop D?', 'Qual a capital da França?',
])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


@pytest.mark.parametrize('pergunta', [
    'Como funciona o merge sort?', 'Qual a complexidade do quick sort?', 'O que é Big-O?', 'Como funciona um heap?',
    'Como implementar BFS?', 'Como implementar DFS?', 'O que é SAT?',
])
def test_vocabulario_comum_com_paa_fica_na_disciplina_escolhida(pergunta):
    """Sem filtro por palavra-chave: cada disciplina busca só no próprio índice."""
    assert all(i.startswith('ed-') for i in buscar(pergunta))
    for d in OUTRAS:
        assert not any(i.startswith('ed-') for i in buscar(pergunta, disciplinas.obter(d)))


def test_prova_formal_com_ed_usa_material_de_ed_e_regra_de_paa():
    achados = buscar('Prove pelo Teorema Mestre que o merge sort é n log n')
    assert achados and all(i.startswith('ed-') for i in achados) and achados[0] == 'ed-notion-recorrencias'
    assert 'prova completa é de PAA' in ED.rigor and 'Teorema Mestre' in ED.rigor


def test_blocos_de_ed_nao_copiam_paa():
    paa = [i['texto'] for i in read_json(disciplinas.obter('paa').itens)]
    for i in ITENS.values():
        frases = [f.strip() for f in re.split(r'[.\n]', i['texto']) if len(f.strip()) > 60]
        assert not [f for f in frases if any(f in t for t in paa)], i['id']


# ---------------------------------------------------------------- resoluções e correções

def test_resolucoes_tem_status_e_dizem_no_texto():
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    resolvidas = [i for i in ITENS.values() if 'status_resolucao' in i]
    assert len(resolvidas) == 17
    for i in resolvidas:
        assert f"Status da resolução: {rotulo[i['status_resolucao']]}" in i['texto'], i['id']
        assert 'gabarito oficial' not in i['texto'].lower()
    for i in resolvidas:
        if i['status_resolucao'] == 'corrigida':
            assert 'Divergência' in i['texto'] and 'Correções da equipe' in i['texto'], i['id']
            assert 'não é gabarito do professor' in i['texto'], i['id']


def test_caso_base_vem_do_algoritmo_e_convencao_fica_pendente():
    t = texto('ed-notion-recorrencias')
    assert ITENS['ed-notion-recorrencias']['status_resolucao'] == 'pendente_professor'
    assert 'o caso-base não vem de elemento neutro' in t and 'vem do próprio algoritmo' in t
    assert 'vale como convenção, não como regra' in t
    assert 'T(n) = T(n − 1) + O(n) → O(n²)' in t  # pior caso do Quick sort, que faltava no quadro


def test_trechos_de_codigo_dos_blocos_sao_os_programas_testados():
    fonte = '\n'.join(p.read_text(encoding='utf-8') for p in PROGRAMAS)
    trechos = 0
    for i in ITENS.values():
        for bloco in re.findall(r'```c\n(.*?)```', i['texto'], re.S):
            for funcao in re.split(r'\n\n(?=\S)', bloco.strip()):
                if re.match(r'^[\w ]+\**\w+\(.*\)\n\{', funcao):  # definição completa de função
                    assert funcao in fonte, (i['id'], funcao.splitlines()[0])
                    trechos += 1
    assert trechos >= 20


def test_codigos_de_huffman_do_exemplo_da_aula():
    freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    fila = [(w, k, c) for k, (c, w) in enumerate(freq.items())]
    heapq.heapify(fila)
    contador = itertools.count(len(fila))
    while len(fila) > 1:
        a, b = heapq.heappop(fila), heapq.heappop(fila)
        heapq.heappush(fila, (a[0] + b[0], next(contador), (a[2], b[2])))
    codigos = {}

    def descer(no, prefixo):
        if isinstance(no, str):
            codigos[no] = prefixo
        else:
            descer(no[0], prefixo + '0')
            descer(no[1], prefixo + '1')

    descer(fila[0][2], '')
    assert codigos == {'f': '0', 'c': '100', 'd': '101', 'a': '1100', 'b': '1101', 'e': '111'}
    assert sum(freq[c] * len(v) for c, v in codigos.items()) == 224
    assert 'f 0, c 100, d 101, a 1100, b 1101, e 111' in texto('ed-prof-huffman') and '224 bits' in texto('ed-prof-huffman')


def test_exemplo_dimacs_da_aula_e_satisfativel():
    clausulas = [[-1, -2], [1, -2], [-1, -3]]
    ok = lambda v: all(any((l > 0) == v[abs(l)] for l in c) for c in clausulas)
    assert ok({1: True, 2: False, 3: False}) and ok({1: False, 2: False, 3: False})
    assert 'p cnf 3 3\n-1 -2 0\n1 -2 0\n-1 -3 0' in texto('ed-prof-sat')


def test_projetos_avaliativos_nao_tem_implementacao_completa():
    for i in ITENS.values():
        assert 'int main' not in i['texto'] and 'fopen' not in i['texto'], i['id']
    for p in PROGRAMAS:
        assert 'fopen' not in p.read_text(encoding='utf-8'), p.name  # nada de compactar arquivo ou ler DIMACS
    versionados = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    assert not re.search(r'(?i)(huff|sat_?solver|dimacs)[^/\n]*\.(c|h)$', versionados, re.M)
    assert 'Não escreva o projeto completo' in ED.rigor


# ---------------------------------------------------------------- código C: compilar e rodar

def _gcc():
    if not shutil.which('gcc'):
        pytest.skip('gcc não encontrado: instale o gcc para compilar os programas de tests_acervo/c_ed')
    return 'gcc'


@pytest.mark.parametrize('programa', PROGRAMAS, ids=lambda p: p.name)
def test_codigo_c_compila_sem_avisos_e_passa(programa, tmp_path):
    exe = tmp_path / 'prog.exe'
    r = subprocess.run([_gcc(), *FLAGS, str(programa), '-o', str(exe)], capture_output=True, text=True)
    assert r.returncode == 0 and not r.stderr, r.stderr
    r = subprocess.run([str(exe)], capture_output=True, text=True, timeout=60)
    assert r.returncode == 0 and r.stdout.strip() == 'OK', r.stderr


def _com_sanitizador_local(tmp_path):
    teste = tmp_path / 'vazio.c'
    teste.write_text('int main(void) { return 0; }\n', encoding='utf-8')
    r = subprocess.run(['gcc', *SANITIZADORES, str(teste), '-o', str(tmp_path / 'vazio.exe')], capture_output=True)
    return r.returncode == 0


def _docker_gcc():
    if not shutil.which('docker'):
        return False
    r = subprocess.run(['docker', 'image', 'inspect', 'gcc:14'], capture_output=True)
    return r.returncode == 0


def test_codigo_c_passa_no_address_sanitizer_e_ubsan(tmp_path):
    """ASan + UBSan (e LeakSanitizer no Linux). O MinGW não tem sanitizadores; aí usa a imagem gcc:14 do Docker."""
    if shutil.which('gcc') and _com_sanitizador_local(tmp_path):
        for p in PROGRAMAS:
            exe = tmp_path / (p.stem + '.exe')
            subprocess.run(['gcc', *FLAGS, *SANITIZADORES, str(p), '-o', str(exe)], check=True)
            r = subprocess.run([str(exe)], capture_output=True, text=True, timeout=120)
            assert r.returncode == 0 and r.stdout.strip() == 'OK', (p.name, r.stderr)
        return
    if not _docker_gcc():
        pytest.skip('sem sanitizadores: o gcc local não aceita -fsanitize e a imagem Docker gcc:14 não está disponível')
    script = ('for f in /src/*.c; do gcc ' + ' '.join(FLAGS + SANITIZADORES) +
              ' "$f" -o /tmp/p && [ "$(/tmp/p)" = OK ] || { echo "FALHOU $f"; exit 1; }; done')
    r = subprocess.run(['docker', 'run', '--rm', '-v', f'{C_ED}:/src:ro', 'gcc:14', 'sh', '-c', script],
                       capture_output=True, text=True, timeout=600)
    assert r.returncode == 0, r.stdout + r.stderr


@pytest.mark.parametrize('original, erro', [
    ('#include <stdlib.h>\ntypedef struct node { int item; struct node *prox; } Noe;\n'
     'int main(void) { Node *p = malloc(sizeof *p); free(p); return 0; }\n', 'Node'),
    ('int integers_equals(void item1, void item2) { return 0; }\nint main(void) { return 0; }\n', 'void'),
])
def test_erros_de_compilacao_das_anotacoes_se_confirmam(original, erro, tmp_path):
    """Reproduz, em versão mínima escrita pela equipe, os dois erros de compilação apontados nos blocos."""
    fonte = tmp_path / 'original.c'
    fonte.write_text(original, encoding='utf-8')
    r = subprocess.run([_gcc(), '-std=c99', '-c', str(fonte), '-o', str(tmp_path / 'o.o')], capture_output=True, text=True)
    assert r.returncode != 0 and erro in r.stderr


# ---------------------------------------------------------------- fórmulas, catálogo e restrições

FORMULA = re.compile(r'\$\$(.+?)\$\$|\$(.+?)\$', re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in ITENS.values():
        assert i['texto'].count('$') % 2 == 0, i['id']


@pytest.mark.skipif(not shutil.which('node'), reason='node indisponível')
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for i in ITENS.values() for a, b in FORMULA.findall(i['texto'])]
    assert len(formulas) >= 15
    katex = (ROOT / 'backend/web/vendor/katex/katex.min.js').as_posix()
    script = (f"const k=require({json.dumps(katex)});const fs=require('fs');"
              "const erros=[];for(const f of JSON.parse(fs.readFileSync(0,'utf8'))){"
              "try{k.renderToString(f,{throwOnError:true})}catch(e){erros.push(f+' :: '+e.message)}}"
              "console.log(JSON.stringify(erros))")
    r = subprocess.run(['node', '-e', script], input=json.dumps(formulas), capture_output=True, text=True,
                       encoding='utf-8', check=True)
    assert json.loads(r.stdout) == []


def test_catalogo_completo_e_coerente():
    obrigatorios = {'id', 'nome', 'autoria', 'url', 'idioma', 'formato', 'isa', 'topicos', 'licenca', 'acesso',
                    'prioridade', 'uso', 'justificativa'}
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f['id']
        assert f['prioridade'] in ('alta', 'media', 'referencia')
        assert f['uso'] in ('acervo', 'citada', 'referencia', 'candidato', 'indisponivel')
        assert set(f['topicos']) <= set(ED.assuntos), f['id']
    assert {x for i in ITENS.values() for x in i['fontes_catalogo']} <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f['uso'] == 'acervo'} == {
        x for i in ITENS.values() if i['natureza'] == 'material_da_disciplina' for x in i['fontes_catalogo']}


def test_originais_fora_do_repositorio():
    arquivos = [p for p in (ROOT / 'disciplinas/ed').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.docx', '.pptx', '.gif', '.c', '.h')]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (ROOT / 'disciplinas/ed/CURADORIA.md').read_text(encoding='utf-8')
    assert [i for i in CATALOGO if f'`{i}`' not in curadoria] == []
    assert [i for i in ITENS if f'`{i}`' not in curadoria] == []
    assert '`ed`' in (ROOT / 'docs/DISCIPLINAS.md').read_text(encoding='utf-8')
