"""Acervo de Programação 1 e conferência do código C.

Os blocos parafraseiam os slides do Prof. Rodrigo de Barros Paes e duas seções do livro de Jaime Evaristo.
Cada função C que aparece num bloco é cópia exata de uma função dos programas de tests_acervo/c_prog1/,
compilados aqui com -Wall -Wextra -pedantic -Werror e rodados (com AddressSanitizer e UBSan quando houver
um gcc que os tenha). As questões do The Huxley entram só com número e tema, sem solução.
"""
import json
import math
import re
import shutil
import subprocess

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

P1 = disciplinas.obter('prog1')
PASTA = ROOT / 'disciplinas/prog1'
FONTES = read_json(PASTA / 'fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {i['id']: i for i in read_json(P1.itens)}
C_P1 = ROOT / 'tests_acervo/c_prog1'
PROGRAMAS = sorted(C_P1.glob('*.c'))
FLAGS = ['-std=c99', '-Wall', '-Wextra', '-pedantic', '-Werror', '-g']
SANITIZADORES = ['-fsanitize=address,undefined', '-fno-sanitize-recover=all']
OUTRAS = ('paa', 'sd', 'oac', 'calc3', 'fis2', 'ed', 'bd')


def buscar(pergunta, d=P1):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return ITENS[ident]['texto']


# ---------------------------------------------------------------- cadastro e acervo

def test_prog1_cadastrada_com_acervo_proprio():
    assert P1.nome == 'Programação 1' and P1.itens.exists() and P1.indice.exists() and not P1.livro_supabase
    ids = {c['id'] for c in read_json(P1.indice)['chunks']}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({P1.itens, P1.indice})
        assert ids.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    assert all(c['disciplina'] == 'prog1' for c in read_json(P1.indice)['chunks'])
    assert {i['assunto'] for i in ITENS.values()} == set(P1.assuntos)  # nenhum tópico sem bloco na busca
    assert ids == set(ITENS)


def test_situacao_da_disciplina():
    # Fica em validação até os sanitizers rodarem em Linux e a equipe revisar (veja CURADORIA.md).
    assert P1.situacao == 'em validação' and P1.em_validacao and P1.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas prog1 --embeddings`."""
    gerados = disciplinas.registros(P1)
    assert gerados == read_json(P1.itens)
    assert {c['id'] for c in read_json(P1.indice)['chunks']} == {
        i['id'] for i in gerados if i['confiabilidade'] in ('media', 'alta')}


def test_blocos_cabem_no_trecho():
    for i in ITENS.values():
        assert len(i['texto']) <= 2200, i['id']  # backend/rag.py corta acima disso


def test_nenhuma_nota_da_ia_e_nada_revisado_sem_registro():
    assert not [i for i, x in ITENS.items() if x['natureza'] == 'nota_da_equipe_ia']
    for p in P1.materiais.glob('*.md'):
        cab = p.read_text(encoding='utf-8').split('---')[1]
        assert 'revisao_humana: pendente' in cab and 'revisao_professor' not in cab, p.name


# ---------------------------------------------------------------- busca e isolamento

@pytest.mark.parametrize('pergunta, aceitos', [
    ('Por que meu scanf não lê o número?', {'prog1-erros-scanf'}),
    ('Qual a diferença entre while e do-while?', {'prog1-livro-do-while'}),
    ('Como passar um vetor para uma função em C?', {'prog1-aula11-vetores'}),
    ('Como inverter uma string em C?', {'prog1-aula13-strings'}),
    ('Por que minha função troca não troca os valores?', {'prog1-aula14-ponteiros'}),
    ('Como funciona o fatorial recursivo?', {'prog1-aula16-recursao'}),
    ('Como declarar uma struct com nome e data de nascimento?', {'prog1-aula15-structs'}),
    ('Como fazer a transposta de uma matriz?', {'prog1-aula12-matrizes'}),
    ('Qual a diferença entre = e == no if?', {'prog1-aula06-07-decisao'}),
    ('Por que a divisão de dois inteiros perde a parte fracionária?', {'prog1-divisao-inteira-resto', 'prog1-aula05-resolucao-problemas'}),
    ('Como compilar com gcc?', {'prog1-aula03-compilacao'}),
    ('O Huxley diz resposta errada mas o exemplo passa', {'prog1-huxley-juiz-online'}),
    ('Como ler uma frase com espaços usando fgets?', {'prog1-aula13-strings'}),
])
def test_pergunta_de_prog1_encontra_bloco_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize('pergunta', [
    'O que é um flip-flop D?', 'Qual a capital da França?', 'Qual a transformada de Laplace de um degrau?',
])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    """Só léxico: perguntas sem palavra em comum. As que têm ("pêndulo simples") ficam em eval/relevancia.py."""
    assert buscar(pergunta) == []


@pytest.mark.parametrize('pergunta', [
    'Como passar um ponteiro para uma função em C?', 'Como funciona uma struct em C?',
    'Como fazer uma função recursiva?', 'Como percorrer um vetor em C?',
])
def test_vocabulario_comum_com_ed_fica_na_disciplina_escolhida(pergunta):
    """Fronteira com ED: sem filtro por palavra-chave, cada disciplina busca só no próprio índice."""
    assert all(i.startswith('prog1-') for i in buscar(pergunta))
    for d in OUTRAS:
        assert not any(i.startswith('prog1-') for i in buscar(pergunta, disciplinas.obter(d)))
    assert not any(i.startswith('ed-') for i in buscar(pergunta))


def test_assunto_de_ed_com_prog1_selecionada_usa_regra_de_fronteira():
    assert 'Estrutura de Dados' in P1.rigor and 'Alocação dinâmica' in P1.rigor
    assert all(i.startswith('prog1-') for i in buscar('Como remover o último nó de uma lista encadeada?'))


# ---------------------------------------------------------------- resoluções e correções

def test_resolucoes_tem_status_e_dizem_no_texto():
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    resolvidas = [i for i in ITENS.values() if 'status_resolucao' in i]
    assert len(resolvidas) == 15
    for i in resolvidas:
        assert f"Status da resolução: {rotulo[i['status_resolucao']]}" in i['texto'], i['id']
        assert 'gabarito oficial' not in i['texto'].lower()
        if i['status_resolucao'] == 'corrigida':
            assert 'Divergência' in i['texto'] and 'Correções da equipe' in i['texto'], i['id']
            assert 'não é gabarito do professor' in i['texto'], i['id']


def test_contas_dos_blocos():
    notas = [8, 6, 7, 8, 7, 6, 6, 10]
    m = sum(notas) / len(notas)
    var = sum((x - m) ** 2 for x in notas) / len(notas)
    assert (m, var, round(math.sqrt(var), 6)) == (7.25, 1.6875, 1.299038)
    assert '1,6875' in texto('prog1-aula11-vetores') and '1{,}299038' in texto('prog1-aula11-vetores')
    assert [h * 60 + mi for h, mi in ((10, 15), (11, 20), (22, 40))] == [615, 680, 1360]
    assert round(77 / 1.81 ** 2, 1) == 23.5 and round(950 * 1.15 * 1.10, 2) == 1201.75
    assert (820 - 500) * 0.5 == 160 and [x * 60 for x in (0, 30, 100, 2000)] == [0, 1800, 6000, 120000]
    assert math.factorial(12) < 2 ** 31 <= math.factorial(13) and math.factorial(20) < 2 ** 63 <= math.factorial(21)


def test_trechos_de_codigo_dos_blocos_sao_os_programas_testados():
    fonte = '\n'.join(p.read_text(encoding='utf-8') for p in PROGRAMAS)
    trechos = 0
    for i in ITENS.values():
        for bloco in re.findall(r'```c\n(.*?)```', i['texto'], re.S):
            for funcao in re.split(r'\n\n(?=\S)', bloco.strip()):
                if re.match(r'^[\w ]+\**\w+\(.*\)\n\{', funcao):  # definição completa de função
                    if funcao.startswith('int main'):
                        continue
                    assert funcao in fonte, (i['id'], funcao.splitlines()[0])
                    trechos += 1
                elif funcao.startswith('struct cliente {'):
                    assert funcao in fonte
    assert trechos >= 25


def test_huxley_so_numero_e_tema_sem_solucao():
    lista = texto('prog1-huxley-juiz-online')
    for n in ('166', '247', '161', '352', '24 fatorial', '410', '240'):
        assert n in lista
    assert '```' not in lista
    for i in ITENS.values():  # o único programa completo é o "primeiro programa" da aula 3
        tem_main = bool(re.search(r'int main\(void\)\n\{', i['texto']))
        assert tem_main == (i['id'] == 'prog1-aula03-compilacao'), i['id']
    assert 'Nunca escreva a solução completa' in P1.rigor
    for i in ('prog1-aula13-strings', 'prog1-aula16-recursao', 'prog1-aula09-repeticao'):
        assert 'não entrega o programa' in texto(i)
    fonte = '\n'.join(p.read_text(encoding='utf-8') for p in PROGRAMAS)
    assert not re.search(r'(?i)\b(inverte|palindromo|mdc|primo)\w*\s*\(', fonte)


# ---------------------------------------------------------------- código C: compilar e rodar

def _gcc():
    if not shutil.which('gcc'):
        pytest.skip('gcc não encontrado: instale o gcc para compilar os programas de tests_acervo/c_prog1')
    return 'gcc'


@pytest.mark.parametrize('programa', PROGRAMAS, ids=lambda p: p.name)
def test_codigo_c_compila_sem_avisos_e_passa(programa, tmp_path):
    exe = tmp_path / 'prog.exe'
    r = subprocess.run([_gcc(), *FLAGS, str(programa), '-o', str(exe), '-lm'], capture_output=True, text=True)
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
    return subprocess.run(['docker', 'image', 'inspect', 'gcc:14'], capture_output=True).returncode == 0


def test_codigo_c_passa_no_address_sanitizer_e_ubsan(tmp_path):
    """ASan + UBSan. O MinGW não tem sanitizadores; aí usa a imagem gcc:14 do Docker, se houver."""
    if shutil.which('gcc') and _com_sanitizador_local(tmp_path):
        for p in PROGRAMAS:
            exe = tmp_path / (p.stem + '.exe')
            subprocess.run(['gcc', *FLAGS, *SANITIZADORES, str(p), '-o', str(exe), '-lm'], check=True)
            r = subprocess.run([str(exe)], capture_output=True, text=True, timeout=120)
            assert r.returncode == 0 and r.stdout.strip() == 'OK', (p.name, r.stderr)
        return
    if not _docker_gcc():
        pytest.skip('sem sanitizadores: o gcc local não aceita -fsanitize e a imagem Docker gcc:14 não está disponível')
    script = ('for f in /src/*.c; do gcc ' + ' '.join(FLAGS + SANITIZADORES) +
              ' "$f" -o /tmp/p -lm && [ "$(/tmp/p)" = OK ] || { echo "FALHOU $f"; exit 1; }; done')
    r = subprocess.run(['docker', 'run', '--rm', '-v', f'{C_P1}:/src:ro', 'gcc:14', 'sh', '-c', script],
                       capture_output=True, text=True, timeout=600)
    assert r.returncode == 0, r.stdout + r.stderr


@pytest.mark.parametrize('original, aviso', [
    ('#include <stdio.h>\nint imprimir(int q) { while (q) { puts("x"); --q; } }\n'
     'int main(void) { imprimir(1); return 0; }\n', 'return'),
    ('int main(void) { int x = 0; if (x = 5) { return 1; } return 0; }\n', 'parentheses'),
    ('#include <stdio.h>\nint main(void) { int n; scanf("%d", n); return n; }\n', 'format'),
])
def test_erros_dos_slides_e_de_iniciante_dao_aviso(original, aviso, tmp_path):
    """Versões mínimas, escritas pela equipe, dos erros apontados nos blocos: o -Wall os denuncia."""
    fonte = tmp_path / 'original.c'
    fonte.write_text(original, encoding='utf-8')
    r = subprocess.run([_gcc(), '-std=c99', '-Wall', '-Wextra', '-c', str(fonte), '-o', str(tmp_path / 'o.o')],
                       capture_output=True, text=True)
    assert 'warning' in r.stderr and aviso in r.stderr, r.stderr


def test_troca_sem_auxiliar_perde_o_valor():
    a, b = 5, 3
    a = b
    b = a
    assert (a, b) == (3, 3)


# ---------------------------------------------------------------- fórmulas, catálogo e restrições

FORMULA = re.compile(r'\$\$(.+?)\$\$|\$(.+?)\$', re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in ITENS.values():
        assert i['texto'].count('$') % 2 == 0, i['id']


@pytest.mark.skipif(not shutil.which('node'), reason='node indisponível')
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for i in ITENS.values() for a, b in FORMULA.findall(i['texto'])]
    assert len(formulas) >= 3
    katex = (ROOT / 'backend/web/vendor/katex/katex.min.js').as_posix()
    script = (f"const k=require({json.dumps(katex)});const fs=require('fs');"
              "const erros=[];for(const f of JSON.parse(fs.readFileSync(0,'utf8'))){"
              "try{k.renderToString(f,{throwOnError:true})}catch(e){erros.push(f+' :: '+e.message)}}"
              "console.log(JSON.stringify(erros))")
    r = subprocess.run(['node', '-e', script], input=json.dumps(formulas), capture_output=True, text=True,
                       encoding='utf-8', check=True)
    assert json.loads(r.stdout) == []


def test_blocos_de_codigo_indicam_a_linguagem():
    for i in ITENS.values():
        aberturas = re.findall(r'^```(\w*)$', i['texto'], re.M)
        assert all(a in ('c', 'bash', '') for a in aberturas), i['id']
        assert aberturas[::2] == [a for a in aberturas[::2] if a], i['id']  # toda abertura tem linguagem


def test_catalogo_completo_e_coerente():
    obrigatorios = {'id', 'nome', 'autoria', 'url', 'idioma', 'formato', 'isa', 'topicos', 'licenca', 'acesso',
                    'prioridade', 'uso', 'justificativa'}
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f['id']
        assert f['prioridade'] in ('alta', 'media', 'referencia')
        assert f['uso'] in ('acervo', 'citada', 'referencia', 'candidato', 'indisponivel')
        assert set(f['topicos']) <= set(P1.assuntos), f['id']
    assert {x for i in ITENS.values() for x in i['fontes_catalogo']} <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f['uso'] == 'acervo'} == {
        x for i in ITENS.values() if i['natureza'] == 'material_da_disciplina' for x in i['fontes_catalogo']}
    assert CATALOGO['schildt-c-completo-total']['uso'] == 'referencia'


def test_originais_e_dados_pessoais_fora_do_repositorio():
    arquivos = [p for p in PASTA.rglob('*') if p.is_file()] + PROGRAMAS
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.docx', '.pptx', '.gif', '.h')]
    assert not [p for p in PASTA.rglob('*.c')]
    proibidos = re.compile(r'(?i)[\w.]+@[\w-]+\.\w+|groups\.google|dropbox|bsenhab|usu[aá]rio: programador|sites\.google')
    for p in [*P1.materiais.glob('*.md'), P1.itens, PASTA / 'rigor.md', *PROGRAMAS]:
        assert not proibidos.search(p.read_text(encoding='utf-8')), p.name
    versionados = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    assert not re.search(r'(?im)(huxley|slides do paes|aprendendo a programar|c completo)[^\n]*\.(txt|pdf|pptx)$', versionados)


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (PASTA / 'CURADORIA.md').read_text(encoding='utf-8')
    assert [i for i in CATALOGO if f'`{i}`' not in curadoria] == []
    assert [i for i in ITENS if f'`{i}`' not in curadoria] == []
    assert '`prog1`' in (ROOT / 'docs/DISCIPLINAS.md').read_text(encoding='utf-8')
