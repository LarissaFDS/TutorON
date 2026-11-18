"""Acervo de Banco de Dados e conferência do SQL.

Cada bloco ```sql dos materiais roda no SQLite, sobre o banco de teste do cabeçalho (`banco_teste`, um arquivo de
tests_acervo/sql_bd/). Quando o bloco traz "Resultado:" com uma tabela, as linhas devolvidas têm de ser as da tabela.
Trechos de outro dialeto começam com `-- dialeto: ...`: os de PostgreSQL (ANY/ALL) rodam no DuckDB, se instalado;
os de MySQL e SQL Server não rodam aqui e o teste confirma que o SQLite os recusa.
"""
import json
import re
import shutil
import sqlite3
import subprocess
from decimal import Decimal

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search, tokens

BD = disciplinas.obter('bd')
FONTES = read_json(ROOT / 'disciplinas/bd/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {i['id']: i for i in read_json(BD.itens)}
SQL_BD = ROOT / 'tests_acervo/sql_bd'
OUTRAS = ('paa', 'sd', 'oac', 'calc3', 'fis2', 'ed')
BLOCOS = {m['id']: (m, corpo) for m, corpo, _ in map(disciplinas.ler, sorted(BD.materiais.glob('*.md')))}


def buscar(pergunta, d=BD):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return ITENS[ident]['texto']


# ---------------------------------------------------------------- cadastro e acervo

def test_bd_cadastrado_com_acervo_proprio():
    assert BD.nome == 'Banco de Dados' and BD.itens.exists() and BD.indice.exists() and not BD.livro_supabase
    assert BD.situacao == 'em validação' and BD.em_validacao
    ids = {c['id'] for c in read_json(BD.indice)['chunks']}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({BD.itens, BD.indice})
        assert ids.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    assert all(c['disciplina'] == 'bd' for c in read_json(BD.indice)['chunks'])


def test_assuntos_das_aulas_tem_bloco_na_busca():
    """Critério A7.4: todo assunto confirmado pelos slides tem ao menos um bloco aprovado (na busca)."""
    confirmados = {t for f in ('ufal-bd-slides', 'ufal-bd2-slides') for t in CATALOGO[f]['topicos']}
    na_busca = {ITENS[c['id']]['assunto'] for c in read_json(BD.indice)['chunks']}
    assert confirmados and confirmados <= na_busca
    assert {i['assunto'] for i in ITENS.values()} <= set(BD.assuntos)


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas bd --embeddings`."""
    gerados = disciplinas.registros(BD)
    assert gerados == read_json(BD.itens)
    assert {c['id'] for c in read_json(BD.indice)['chunks']} == {
        i['id'] for i in gerados if i['confiabilidade'] in ('media', 'alta')}


def test_blocos_cabem_no_trecho():
    for i in ITENS.values():
        assert len(i['texto']) <= 2200, i['id']  # backend/rag.py corta acima disso


def test_notas_da_ia_ficam_fora_da_busca():
    na_busca = {c['id'] for c in read_json(BD.indice)['chunks']}
    notas = {i for i, x in ITENS.items() if x['natureza'] == 'nota_da_equipe_ia'}
    assert notas == {'bd-nota-er-estendido', 'bd-nota-juncao-divisao', 'bd-nota-bcnf', 'bd-nota-ddl-restricoes',
                     'bd-nota-indices', 'bd-nota-transacoes'}
    assert na_busca.isdisjoint(notas)
    assert all(ITENS[i]['status_curadoria'] == 'candidato' and ITENS[i]['confiabilidade'] == 'nao_verificada'
               for i in notas)
    assert all(ITENS[i]['natureza'] == 'material_da_disciplina' for i in na_busca)


def test_nenhum_bloco_aprovado_pelo_professor_ou_revisado_por_humano():
    for p in BD.materiais.glob('*.md'):
        cab = p.read_text(encoding='utf-8').split('---')[1]
        assert 'revisao_humana: pendente' in cab and 'revisao_professor' not in cab, p.name


# ---------------------------------------------------------------- busca e isolamento

@pytest.mark.parametrize('pergunta, aceitos', [
    ('Qual a diferença entre LEFT JOIN e INNER JOIN?', {'bd2-aula-joins-inner-left'}),
    ('O que o RIGHT JOIN devolve quando o cargo não tem funcionário?', {'bd2-aula-joins-right-full-cross'}),
    ('Quantas linhas tem o CROSS JOIN de FUNCIONARIO e CARGO?', {'bd2-aula-joins-right-full-cross'}),
    ('Quando uso HAVING em vez de WHERE?', {'bd2-aula-group-by-having'}),
    ('Qual a diferença entre UNION e UNION ALL?', {'bd2-aula-union', 'bd-aula-algebra-conjuntos'}),
    ('Como mapear um relacionamento N:M do modelo ER para tabelas?', {'bd-aula-mapeamento-er-relacional'}),
    ('Como sei se uma tabela está na 2FN ou na 3FN?', {'bd-aula-formas-normais', 'bd-aula-exercicios-normalizacao'}),
    ('Como escrever a projeção e a seleção da álgebra relacional em SQL?', {'bd-aula-algebra-selecao-projecao'}),
    ('O que é dependência funcional transitiva?', {'bd-aula-dependencia-funcional', 'bd-aula-formas-normais'}),
    ('Como funciona uma subconsulta correlacionada?', {'bd-aula-subconsultas'}),
    ('Por que NOT IN com NULL não devolve nada?', {'bd2-aula-exists-any-all'}),
    ('Como criar uma view no SQLite?', {'bd2-aula-visoes'}),
    ('Como criar uma trigger BEFORE DELETE com OLD?', {'bd2-aula-triggers'}),
    ('Como passar parâmetro para uma stored procedure?', {'bd2-aula-procedures'}),
    ('Como usar CASE WHEN no SELECT?', {'bd2-aula-case'}),
    ('Qual a cardinalidade dos relacionamentos da floricultura?', {'bd-aula-exercicios-er'}),
    ('O que é a arquitetura de três esquemas e a independência de dados?', {'bd-aula-modelos-arquitetura'}),
    ('Quais as vantagens de usar um SGBD?', {'bd-aula-conceitos-sgbd'}),
])
def test_pergunta_de_bd_encontra_material_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


def test_simbolos_da_algebra_estao_por_extenso():
    """tokens() guarda só [a-z0-9]: σ, π, ρ e ⋈ somem. Os blocos escrevem sigma, pi e rho ao lado do símbolo."""
    assert tokens('σ π ρ ⋈ →') == []
    assert 'algebra' in buscar('seleção sigma e projeção pi')[0]


@pytest.mark.parametrize('pergunta', [
    'Qual o período de oscilação de um pêndulo?', 'O que é um flip-flop D?', 'Qual a capital da França?',
    'Qual a curvatura de uma hélice?',
])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


@pytest.mark.parametrize('pergunta', ['Como funciona uma tabela hash?', 'O que é uma árvore B?', 'Como funciona o merge sort?'])
def test_vocabulario_comum_fica_na_disciplina_escolhida(pergunta):
    """Sem filtro por palavra-chave: cada disciplina busca só no próprio índice."""
    assert all(i.startswith('bd') for i in buscar(pergunta))
    for d in OUTRAS:
        assert not any(i.startswith('bd') for i in buscar(pergunta, disciplinas.obter(d)))


# ---------------------------------------------------------------- resoluções e correções

def test_resolucoes_ficam_pendentes_do_professor_e_dizem_no_texto():
    resolvidas = [i for i in ITENS.values() if 'status_resolucao' in i]
    assert {i['id'] for i in resolvidas} == {
        'bd-aula-exercicios-er', 'bd-aula-exercicio-streaming', 'bd-aula-exercicios-algebra-selecao',
        'bd-aula-exercicios-algebra-projecao', 'bd-aula-exercicios-algebra-renomear', 'bd-aula-exercicios-normalizacao'}
    for i in resolvidas:
        assert i['status_resolucao'] == 'pendente_professor'
        assert 'Status da resolução: pendente de confirmação do professor' in i['texto'], i['id']
        assert 'gabarito oficial' not in i['texto'].lower()


@pytest.mark.parametrize('errado', [
    'Tuplas (colunas)', 'OUTER LEFT', 'OUTER FULL', 'RIGTH', r'\bBEFOR\b', 'nota >= 0 ou', 'empregradosSS',
    'Supplies', 'Total_marks', r"VALUES\s+'", 'CPF à', r'LIKE\s+\'\[', 'codigoCargo', r'\bMONEY\(',
])
def test_erros_dos_slides_nao_entram_no_acervo(errado):
    for i in ITENS.values():
        assert not re.search(errado, i['texto']), (i['id'], errado)


def test_correcoes_dos_slides_estao_registradas():
    for ident, trecho in [('bd-aula-conceitos-sgbd', 'nota >= 0 AND nota <= 10'),
                          ('bd2-aula-joins-right-full-cross', 'o produto tem 12'),
                          ('bd2-aula-exists-any-all', 'se nenhum item tivesse quantidade 10, sairiam todos'),
                          ('bd2-aula-triggers', 'Os eventos são INSERT, UPDATE e DELETE'),
                          ('bd2-aula-procedures', '`GO` não é comando SQL'),
                          ('bd-aula-subconsultas', 'aceitam ORDER BY na subconsulta'),
                          ('bd2-aula-group-by-having', 'Agrupe pela chave')]:
        assert 'Correções da equipe' in texto(ident) and trecho in texto(ident), ident


def test_dados_pessoais_dos_slides_nao_entram():
    arquivos = [p for p in (ROOT / 'disciplinas/bd').rglob('*') if p.is_file()] + list(SQL_BD.glob('*'))
    for p in arquivos:
        t = p.read_text(encoding='utf-8')
        assert not re.search(r'@\w+\.ufal\.br|t\.me/|\d{2}/\d{2}/2023', t), p.name


# ---------------------------------------------------------------- SQL: executar e comparar

def _trechos():
    for ident, (meta, corpo) in BLOCOS.items():
        partes = re.split(r'```sql\n', corpo)[1:]
        for n, parte in enumerate(partes):
            sql, depois = parte.split('```', 1)
            depois = re.split(r'```', depois)[0]
            esperado = None
            m = re.search(r'^Resultado[^\n]*\n', depois, re.M)
            if m:
                resto = depois[m.start():]
                if re.match(r'Resultado: nenhuma linha', resto):
                    esperado = []
                else:
                    linhas = [l for l in resto[m.end() - m.start():].strip().splitlines() if l.startswith('|')]
                    esperado = [[c.strip() for c in l.strip('|').split('|')] for l in linhas[2:]]
            dialeto = re.match(r'-- dialeto: (\w+)', sql)
            yield pytest.param(ident, meta.get('banco_teste'), sql, esperado, dialeto and dialeto.group(1),
                               id=f'{ident}-{n + 1}')


TRECHOS = list(_trechos())


def _comandos(sql):
    atual = ''
    for linha in sql.splitlines(keepends=True):
        atual += linha
        if sqlite3.complete_statement(atual):
            yield atual.strip()
            atual = ''
    assert not atual.strip(), atual


def _valor(v):
    if v is None:
        return 'NULL'
    if isinstance(v, (float, Decimal)) and v == int(v):
        return str(int(v))
    return str(v)


def _comparar(consulta, linhas, esperado):
    obtido = [[_valor(v) for v in linha] for linha in linhas]
    if 'ORDER BY' not in consulta.upper():  # sem ORDER BY a ordem das linhas não é garantida
        obtido, esperado = sorted(obtido), sorted(esperado)
    assert obtido == esperado


def _fixture(banco):
    return (SQL_BD / f'{banco}.sql').read_text(encoding='utf-8') if banco else ''


@pytest.mark.parametrize('ident, banco, sql, esperado, dialeto', TRECHOS)
def test_sql_dos_blocos_roda_e_devolve_o_resultado_mostrado(ident, banco, sql, esperado, dialeto):
    if dialeto in ('mysql', 'sqlserver'):
        assert ITENS[ident]['verificacao'] == 'parcial'
        con = sqlite3.connect(':memory:')
        con.executescript(_fixture(banco))
        with pytest.raises(sqlite3.Error):
            con.executescript(sql)
        return
    if dialeto == 'postgresql':
        duckdb = pytest.importorskip('duckdb', reason='DuckDB confere ANY/ALL: pip install -r requirements-acervo.txt')
        con = duckdb.connect()
        con.execute(_fixture(banco))
        with pytest.raises(sqlite3.Error):
            sqlite3.connect(':memory:').executescript(_fixture(banco) + sql)
        linhas, consulta = con.execute(sql).fetchall(), sql
    else:
        assert dialeto is None, dialeto
        con = sqlite3.connect(':memory:', isolation_level=None)  # como o sqlite3 de linha de comando: BEGIN e COMMIT explícitos
        con.executescript(_fixture(banco))
        linhas = consulta = None
        for comando in _comandos(sql):
            cur = con.execute(comando)
            if cur.description:
                linhas, consulta = cur.fetchall(), comando
    if esperado is not None:
        assert linhas is not None, ident
        _comparar(consulta, linhas, esperado)


def test_todo_sql_aprovado_foi_conferido():
    assert len(TRECHOS) >= 35
    com_resultado = [p for p in TRECHOS if p.values[3] is not None]
    assert len(com_resultado) >= 30
    for ident, item in ITENS.items():
        if '```sql' in item['texto'] and item['natureza'] == 'material_da_disciplina':
            assert item['verificacao'] in ('conferida_por_codigo', 'parcial'), ident


def test_bancos_de_teste_rodam():
    for p in SQL_BD.glob('*.sql'):
        sqlite3.connect(':memory:').executescript(p.read_text(encoding='utf-8'))


# ---------------------------------------------------------------- normalização: fecho de atributos

def fecho(atributos, dfs):
    resultado = set(atributos)
    mudou = True
    while mudou:
        mudou = False
        for esq, dir_ in dfs:
            if esq <= resultado and not dir_ <= resultado:
                resultado |= dir_
                mudou = True
    return resultado


def _chave_candidata(x, todos, dfs):
    return fecho(x, dfs) == todos and all(fecho(x - {a}, dfs) != todos for a in x)


def _df(esq, dir_):
    return set(esq.split()), set(dir_.split())


def test_produto_compra_2fn():
    todos = {'cod_cliente', 'cod_produto', 'nome_produto', 'preco', 'quantidade'}
    dfs = [_df('cod_produto', 'nome_produto preco'), _df('cod_cliente cod_produto', 'quantidade')]
    assert fecho({'cod_produto'}, dfs) == {'cod_produto', 'nome_produto', 'preco'}
    assert _chave_candidata({'cod_cliente', 'cod_produto'}, todos, dfs)
    assert '{cod_produto}⁺ = {cod_produto, nome_produto, preco}' in texto('bd-aula-dependencia-funcional')
    assert 'Produto(cod_produto, nome_produto, preco) e Compra(cod_cliente, cod_produto, quantidade)' in texto('bd-aula-formas-normais')


def test_carro_fabricante_3fn():
    todos = {'placa', 'modelo', 'km_rodados', 'cod_fabricante', 'nome_fabricante'}
    dfs = [_df('placa modelo', 'km_rodados cod_fabricante'), _df('cod_fabricante', 'nome_fabricante')]
    assert _chave_candidata({'placa', 'modelo'}, todos, dfs)
    assert fecho({'cod_fabricante'}, dfs) != todos  # cod_fabricante não é superchave: dependência transitiva
    assert 'Fabricante(cod_fabricante, nome_fabricante)' in texto('bd-aula-formas-normais')


def test_boletim_resolucao():
    todos = {'matricula_aluno', 'codigo_materia', 'numero_prova', 'nota', 'data_prova', 'nome_aluno',
             'endereco_aluno', 'nome_materia'}
    dfs = [_df('matricula_aluno', 'nome_aluno endereco_aluno'), _df('codigo_materia', 'nome_materia'),
           _df('codigo_materia numero_prova', 'data_prova'), _df('matricula_aluno codigo_materia numero_prova', 'nota')]
    chave = {'matricula_aluno', 'codigo_materia', 'numero_prova'}
    assert _chave_candidata(chave, todos, dfs)
    parciais = [d for d in dfs if d[0] < chave]
    assert len(parciais) == 3  # as três primeiras DFs dependem de parte da chave: não está na 2FN
    for nome, atributos in [('Aluno', 'matricula_aluno nome_aluno endereco_aluno'), ('Materia', 'codigo_materia nome_materia'),
                            ('Prova', 'codigo_materia numero_prova data_prova'),
                            ('Nota', 'matricula_aluno codigo_materia numero_prova nota')]:
        assert f'{nome}({", ".join(atributos.split())})' in texto('bd-aula-exercicios-normalizacao')
    decomposicao = ['matricula_aluno nome_aluno endereco_aluno', 'codigo_materia nome_materia',
                    'codigo_materia numero_prova data_prova', 'matricula_aluno codigo_materia numero_prova nota']
    assert set().union(*(set(d.split()) for d in decomposicao)) == todos


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


def test_rigor_cobre_as_armadilhas_de_sql():
    for trecho in ('HAVING filtra grupos', 'NOT IN', 'NOT EXISTS', 'IS NULL', 'LEFT JOIN', 'fecho',
                   'em validação', '**Verificação:**', 'Não execute nem prometa executar o SQL do aluno'):
        assert trecho in BD.rigor, trecho


def test_catalogo_completo_e_coerente():
    obrigatorios = {'id', 'nome', 'autoria', 'url', 'idioma', 'formato', 'isa', 'dialeto', 'notacao_er',
                    'sql_roda_no_sqlite', 'topicos', 'licenca', 'acesso', 'prioridade', 'uso', 'justificativa'}
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f['id']
        assert f['prioridade'] in ('alta', 'media', 'referencia')
        assert f['uso'] in ('acervo', 'citada', 'referencia', 'candidato', 'indisponivel')
        assert set(f['topicos']) <= set(BD.assuntos), f['id']
    assert {x for i in ITENS.values() for x in i['fontes_catalogo']} <= set(CATALOGO)
    usadas = {x for i in ITENS.values() if i['natureza'] == 'material_da_disciplina' for x in i['fontes_catalogo']}
    assert {i for i, f in CATALOGO.items() if f['uso'] == 'acervo'} == usadas & {'ufal-bd-slides', 'ufal-bd2-slides'}
    for f in ('ufal-bd-slides', 'ufal-bd2-slides'):
        assert all(re.fullmatch(r'[0-9a-f]{64}', s) for s in CATALOGO[f]['arquivo_local'].values())


def test_originais_fora_do_repositorio():
    arquivos = [p for p in (ROOT / 'disciplinas/bd').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.rar', '.pptx', '.db', '.sqlite')]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (ROOT / 'disciplinas/bd/CURADORIA.md').read_text(encoding='utf-8')
    assert [i for i in CATALOGO if f'`{i}`' not in curadoria] == []
    assert [i for i in ITENS if f'`{i}`' not in curadoria] == []
    assert '`bd`' in (ROOT / 'docs/DISCIPLINAS.md').read_text(encoding='utf-8')
