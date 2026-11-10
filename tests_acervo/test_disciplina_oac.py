"""Acervo de Organização e Arquitetura de Computadores (OAC) e conferência das resoluções.

As resoluções do acervo de OAC afirmam números (CPI, tempos, speedups), codificações em binário e o
resultado de trechos de código RISC-V. Aqui as contas são refeitas e o código é executado num
interpretador mínimo do subconjunto RV32I usado nos blocos.
"""
import re

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

OAC = disciplinas.obter('oac')
FONTES = read_json(ROOT / 'disciplinas/oac/fontes.json')['fontes']
CATALOGO = {f['id']: f for f in FONTES}
ITENS = {i['id']: i for i in read_json(OAC.itens)}


def buscar(pergunta, d=OAC):
    return [r['id'] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


# ---------------------------------------------------------------- cadastro e acervo

def test_oac_cadastrada_com_acervo_proprio():
    assert OAC.nome == 'Organização e Arquitetura de Computadores' and OAC.sigla == 'OAC'
    assert OAC.itens.exists() and OAC.indice.exists() and not OAC.livro_supabase
    assert OAC.situacao == 'beta' and not OAC.em_validacao and 'não foi validado pelo professor' in OAC.aviso
    outros = [disciplinas.obter(i) for i in ('paa', 'sd')]
    assert {OAC.itens, OAC.indice}.isdisjoint({p for d in outros for p in (d.itens, d.indice)})
    ids = {c['id'] for c in read_json(OAC.indice)['chunks']}
    for d in outros:
        assert ids.isdisjoint({c['id'] for c in read_json(d.indice)['chunks']})
    assert all(c['disciplina'] == 'oac' for c in read_json(OAC.indice)['chunks'])


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas oac --embeddings`."""
    gerados = disciplinas.registros(OAC)
    assert gerados == read_json(OAC.itens)
    assert {c['id'] for c in read_json(OAC.indice)['chunks']} == {
        i['id'] for i in gerados if i['confiabilidade'] in ('media', 'alta')}


def test_blocos_cabem_no_trecho_e_nao_quebram_codigo():
    for i in ITENS.values():
        assert len(i['texto']) <= 2200, i['id']  # backend/rag.py corta acima disso
        assert i['texto'].count('```') % 2 == 0, i['id']  # blocos de código inteiros


def test_status_de_resolucao_invalido(tmp_path):
    base = 'id: x\ntitulo: t\nassunto: a\ntipo: lista\nfonte: f\nautoria: a\nlicenca: l\ncuradoria: aprovado\n'
    (tmp_path / 'x.md').write_text(f'---\n{base}status_resolucao: oficial\n---\ntexto', encoding='utf-8')
    with pytest.raises(ValueError, match='status_resolucao'):
        disciplinas.ler(tmp_path / 'x.md')


# ---------------------------------------------------------------- busca: OAC só recebe OAC

@pytest.mark.parametrize('pergunta, esperado', [
    ('Por que lw x9, 32(x22) acessa A[8]?', 'oac-aula-operando-memoria'),
    ('Como calculo o CPI médio de um programa com 50% de instruções tipo A, 30% tipo B e 20% tipo C?', None),
    ('Qual a diferença entre blt e bltu?', 'oac-notion-cap2-instrucoes'),
    ('Como escrever a sub-rotina swap em RISC-V?', 'oac-prova1-q4-swap'),
    ('Por que o PCSrc do monociclo precisa de OR Jump para o jal no SystemVerilog?', 'oac-notion-projeto1-monociclo'),
    ('Qual a diferença entre SIMD, MIMD e multithreading SMT?', 'oac-notion-cap6-paralelismo'),
])
def test_pergunta_de_oac_encontra_material_pertinente(pergunta, esperado):
    ids = buscar(pergunta)
    if esperado is None:  # CPI médio: qualquer bloco de desempenho com CPI médio por classe serve
        assert ids[0] in {'oac-prova1-a-q2-enade', 'oac-prova1-b-q2-enade', 'oac-nota-desempenho', 'oac-lista-ex2'}
    else:
        assert ids[0] == esperado


def test_sinais_de_controle_do_sw_vem_dos_projetos_revisados():
    # A tabela de sinais por instrução está numa nota de IA sem revisão humana, fora da busca.
    assert buscar('Quais sinais de controle ficam ativos numa instrução sw?')[0] in {
        'oac-notion-projeto2-pipeline', 'oac-notion-projeto1-monociclo'}


def test_notas_de_ia_sem_revisao_ficam_fora_da_busca_de_oac():
    # Lacuna registrada: custo de CI (yield, die) só tinha a nota n02, que saiu da busca.
    ids = buscar('Como calcular o yield e o custo por die de um wafer?')
    assert not any(i.startswith('oac-nota-') for i in ids)
    assert not any(i.startswith('oac-nota-') for i in (c['id'] for c in read_json(OAC.indice)['chunks']))


def test_vocabulario_comum_fica_na_disciplina_escolhida():
    sd = disciplinas.obter('sd')
    for pergunta in ('Como funciona um somador completo?', 'O que são registradores?',
                     'Como detectar overflow em complemento de 2?'):
        assert all(i.startswith('oac-') for i in buscar(pergunta))
        assert all(i.startswith('sd-') for i in buscar(pergunta, sd))


def test_pergunta_fora_do_acervo_nao_inventa_material():
    assert buscar('Explique a heurística de Dijkstra para grafos esparsos') == []


# ---------------------------------------------------------------- resoluções da turma: status explícito

def test_resolucoes_da_turma_tem_status_e_dizem_no_texto():
    turma = [i for i in ITENS.values() if i['natureza'] == 'material_da_disciplina']
    assert len(turma) == 18  # 11 da prova, lista e aula + 7 das anotações do Notion
    rotulo = {'validada': 'validada', 'corrigida': 'corrigida', 'pendente_professor': 'pendente de confirmação do professor'}
    for i in turma:
        assert i.get('status_resolucao') in rotulo, i['id']
        assert f"Status da resolução: {rotulo[i['status_resolucao']]}" in i['texto'] or \
            f"Status: {rotulo[i['status_resolucao']]}" in i['texto'], i['id']
    corrigidas = {i['id'] for i in turma if i['status_resolucao'] == 'corrigida'}
    assert {'oac-prova1-a-q2-enade', 'oac-prova1-b-q2-enade', 'oac-compiladores', 'oac-prova1-q4-swap'} <= corrigidas
    for ident in corrigidas:  # diz o que diverge do gabarito ou das anotações da turma
        texto = ITENS[ident]['texto'].lower()
        assert ('gabarito' if ident.startswith('oac-prova') or ident == 'oac-compiladores' else 'correç') in texto, ident
    assert {'oac-notion-cap2-instrucoes', 'oac-notion-projeto1-monociclo', 'oac-notion-projeto2-pipeline',
     'oac-notion-cap6-paralelismo'} <= corrigidas
    assert all(i['natureza'] == 'nota_da_equipe_ia' and 'status_resolucao' not in i
               for i in ITENS.values() if i['id'].startswith('oac-nota'))


def test_duas_versoes_da_prova_sao_itens_distintos():
    a, b = ITENS['oac-prova1-a-q2-enade'], ITENS['oac-prova1-b-q2-enade']
    assert '500 MHz' in a['texto'] and 'Alternativa (E)' in a['texto']
    assert '250 MHz' in b['texto'] and 'Alternativa (A)' in b['texto']
    assert 'bne  x28, x29, skip' in ITENS['oac-prova1-a-q5']['texto']
    assert 'beq  x28, x29, skip' in ITENS['oac-prova1-b-q5']['texto']


# ---------------------------------------------------------------- contas de desempenho

def cpi_medio(freq, cpis):
    return sum(f * c for f, c in zip(freq, cpis))


def test_enade_2005_nas_duas_versoes():
    m1, m2 = cpi_medio((.5, .3, .2), (5, 2, 10)), cpi_medio((.5, .3, .2), (3, 1, 4))
    assert m1 == pytest.approx(5.1) and m2 == pytest.approx(2.6)
    t1 = m1 / 1e9
    assert m2 / 500e6 / t1 == pytest.approx(1.02, abs=0.01)  # versão A: mesmo tempo (E)
    assert m2 / 250e6 / t1 == pytest.approx(2.04, abs=0.01)  # versão B: M1 2x mais rápida (A)


def test_lista_ex1_e_ex2():
    assert max({'P1': 3e9 / 1.5, 'P2': 2.5e9 / 1.0, 'P3': 4e9 / 2.2}.items(), key=lambda x: x[1])[0] == 'P2'
    assert 10 * 3e9 / 1.5 == pytest.approx(2e10) and 10 * 4e9 / 2.2 == pytest.approx(1.82e10, rel=1e-3)
    assert [round(1.2 / 0.7 * f / 1e9, 2) for f in (3e9, 2.5e9, 4e9)] == [5.14, 4.29, 6.86]
    p1, p2 = cpi_medio((.1, .2, .5, .2), (1, 2, 3, 2)), 2.0
    assert p1 == pytest.approx(2.4)
    assert (1e6 * p1 / 2.5e9) / (1e6 * p2 / 3e9) == pytest.approx(1.44, abs=0.01)


def test_compiladores_e_divergencia_do_gabarito():
    cpi_a, cpi_b = 1.1 / (1e9 * 1e-9), 1.5 / (1.2e9 * 1e-9)
    assert (cpi_a, cpi_b) == (pytest.approx(1.1), pytest.approx(1.25))
    razao = (1.2e9 * cpi_b) / (1e9 * cpi_a)
    assert round(razao, 2) == 1.36 and round(razao, 2) != 1.37  # o gabarito escreve 1,37
    novo = 6e8 * 1.1 * 1e-9
    assert (round(1.1 / novo, 2), round(1.5 / novo, 2)) == (1.67, 2.27)


def test_exemplos_das_notas():
    assert 1 / ((1 - .8) + .8 / 4) == pytest.approx(2.5)  # Amdahl
    y1, y2 = 1 / (1 + .02 * 1 / 2) ** 2, 1 / (1 + .02 * 2 / 2) ** 2
    assert round(y1, 3) == 0.980 and round(5000 / (700 * y1), 2) == 7.29
    assert round(5000 / (350 * y2), 2) == 14.86
    assert 1 + .05 * 100 == 6  # AMAT
    assert (16 * 1024 // 16, 32 - 10 - 4) == (1024, 18)  # cache de 16 KiB, blocos de 16 B
    import struct
    assert struct.pack('>f', -0.75).hex() == 'bf400000'
    assert (0x2 << 12) - 2048 == 0x1800 and (0x12345 << 12) + 0x678 == 0x12345678


# ---------------------------------------------------------------- codificação

OP = {'add': (0x33, 0, 0), 'sub': (0x33, 0, 0x20), 'addi': (0x13, 0, None), 'lw': (0x03, 2, None), 'sw': (0x23, 2, None)}


def codificar(instr):
    nome, resto = instr.split(None, 1)
    nums = [int(n) for n in re.findall(r'-?\d+', resto.replace('x', ' '))]
    op, f3, f7 = OP[nome]
    if f7 is not None:
        rd, rs1, rs2 = nums
        return f7 << 25 | rs2 << 20 | rs1 << 15 | f3 << 12 | rd << 7 | op
    if nome == 'sw':
        rs2, imm, rs1 = nums
        return (imm >> 5 & 0x7f) << 25 | rs2 << 20 | rs1 << 15 | f3 << 12 | (imm & 0x1f) << 7 | op
    if nome == 'lw':
        rd, imm, rs1 = nums
    else:
        rd, rs1, imm = nums
    return (imm & 0xfff) << 20 | rs1 << 15 | f3 << 12 | rd << 7 | op


def test_codificacoes_da_nota_de_formatos():
    texto = ITENS['oac-nota-formatos-codificacao']['texto']
    exemplos = re.findall(r'^- (\w+ [^→:]+?)(?: →|:).*= (0x[0-9A-F]{8})$', texto, re.M)
    assert len(exemplos) == 5
    for instr, hexa in exemplos:
        assert f'0x{codificar(instr):08X}' == hexa, instr


# ---------------------------------------------------------------- código RISC-V executado

def executar(asm, regs=None, mem=None, limite=200000):
    """Interpretador mínimo do RV32I usado nos blocos (palavras alinhadas, sem pseudoinstruções)."""
    linhas, rotulos = [], {}
    for linha in asm.splitlines():
        linha = linha.split('#')[0].strip()
        if ':' in linha:
            rotulo, linha = linha.split(':', 1)
            rotulos[rotulo.strip()] = len(linhas)
            linha = linha.strip()
        if linha:
            linhas.append(linha)
    x, mem = [0] * 32, dict(mem or {})
    x[1], x[2] = -1, 1 << 20  # retorno para fora do programa; pilha no alto da memória
    for r, v in (regs or {}).items():
        x[r] = v
    pc, passos = 0, 0
    while 0 <= pc < len(linhas) and passos < limite:
        nome, resto = linhas[pc].split(None, 1)
        a = [t.strip() for t in resto.split(',')]
        reg = lambda t: 2 if t == 'sp' else int(t.lstrip('x'))
        pc, passos = pc + 1, passos + 1
        if nome in ('lw', 'sw'):
            imm, base = re.fullmatch(r'(-?\d+)\((x\d+|sp)\)', a[1]).groups()
            ender = x[reg(base)] + int(imm)
            if nome == 'lw':
                x[reg(a[0])] = mem.get(ender, 0)
            else:
                mem[ender] = x[reg(a[0])]
        elif nome in ('add', 'sub'):
            x[reg(a[0])] = x[reg(a[1])] + (1 if nome == 'add' else -1) * x[reg(a[2])]
        elif nome == 'addi':
            x[reg(a[0])] = x[reg(a[1])] + int(a[2])
        elif nome == 'slli':
            x[reg(a[0])] = x[reg(a[1])] << int(a[2])
        elif nome == 'mul':
            x[reg(a[0])] = x[reg(a[1])] * x[reg(a[2])]
        elif nome in ('beq', 'bne'):
            if (x[reg(a[0])] == x[reg(a[1])]) == (nome == 'beq'):
                pc = rotulos[a[2]]
        elif nome == 'bge':
            if x[reg(a[0])] >= x[reg(a[1])]:
                pc = rotulos[a[2]]
        elif nome == 'jal':  # endereços de retorno são índices de linha
            x[reg(a[0])], pc = pc, rotulos[a[1]]
        elif nome == 'jalr':
            imm, base = re.fullmatch(r'(-?\d+)\((x\d+)\)', a[1]).groups()
            pc = x[reg(base)] + int(imm)  # x1 = -1 encerra no retorno ao chamador externo
        else:
            raise ValueError(nome)
        x[0] = 0
    return x, mem


def codigo(ident, n=-1):
    return re.findall(r'```asm\n(.*?)```', ITENS[ident]['texto'], re.S)[n]


def vetor(base, valores):
    return {base + 4 * i: v for i, v in enumerate(valores)}


def test_swap_da_prova():
    _, mem = executar(codigo('oac-prova1-q4-swap'), {10: 100, 11: 1}, vetor(100, [10, 20, 30]))
    assert [mem[100 + 4 * i] for i in range(3)] == [10, 30, 20]


@pytest.mark.parametrize('ident, esperado', [('oac-prova1-a-q5', 3), ('oac-prova1-b-q5', 6)])
def test_lacos_aninhados_das_duas_versoes(ident, esperado):
    a1, a2 = [1, 2, 3], [3, 1, 1]
    x, _ = executar(codigo(ident), {12: 0, 13: 1000, 14: 3, 15: 3}, vetor(0, a1) | vetor(1000, a2))
    assert x[10] == esperado == sum((u == v) == (ident.endswith('a-q5')) for u in a1 for v in a2)
    if ident.endswith('a-q5'):  # com repetição, é contagem de pares, não de "números iguais"
        x, _ = executar(codigo(ident), {12: 0, 13: 1000, 14: 2, 15: 1}, vetor(0, [1, 1]) | vetor(1000, [1]))
        assert x[10] == 2


def test_operando_em_memoria_da_aula():
    a = list(range(100, 116))
    x, mem = executar(codigo('oac-aula-operando-memoria'), {21: 7, 22: 4}, vetor(4, a))
    assert mem[4 + 48] == 7 + a[8]  # A[12] = h + A[8]
    assert 4 + 32 == 36


def test_fatorial_e_laco_das_anotacoes_da_turma():
    laco, fact = re.findall(r'```asm\n(.*?)```', ITENS['oac-notion-cap2-procedimentos']['texto'], re.S)
    for n, esperado in ((0, 1), (1, 1), (5, 120), (7, 5040)):
        x, _ = executar(fact, {10: n})
        assert x[10] == esperado and x[2] == 1 << 20  # pilha volta ao topo
    x, _ = executar(laco, {10: 0, 11: 7}, vetor(0, [7, 7, 3]))
    assert x[10] == 8  # parou no primeiro elemento diferente de k


def test_contas_das_anotacoes_da_turma():
    assert round(1.2 / 0.7, 3) == 1.714  # cap. 1: aumento de clock, não "proporcional"
    linhas = 8 * 1024 // 32
    assert (linhas, linhas // 2, 32 - 7 - 5) == (256, 128, 20)  # cap. 5: tag/índice/offset
    for p, f_min in ((10, .988), (100, .9989)):  # cap. 6: eficiência >= 0,9
        f = (p - 1 / .9) / (p - 1)
        assert round(f, len(str(f_min)) - 2) == f_min and 1 / ((1 - f) + f / p) / p == pytest.approx(.9)
    assert (110 / (10 + 100 / 10), 110 / (10 + 100 / 100)) == (5.5, 10)  # Ex. 1 do livro, não 9 somas
    texto = ITENS['oac-notion-cap2-instrucoes']['texto']
    assert 'A[12] = x9' in texto and 'lli' in texto and '12 bits' in texto
    assert 'ALUOp = 11 no addi está certo' in ITENS['oac-notion-projeto1-monociclo']['texto']
    assert 'x0' in ITENS['oac-notion-projeto2-pipeline']['texto']  # forwarding sem teste de x0
    assert 'linguagem de programação do domínio' in ITENS['oac-notion-cap6-paralelismo']['texto']


def test_if_else_e_while_da_nota():
    if_else, laco = re.findall(r'```asm\n(.*?)```', ITENS['oac-nota-desvios-lacos']['texto'], re.S)
    for i, j, f in ((5, 5, 2 + 3), (5, 6, 2 - 3)):
        assert executar(if_else.replace('...', ''), {20: 2, 21: 3, 22: i, 23: j})[0][19] == f
    x, _ = executar(laco.replace('...', ''), {22: 0, 24: 7, 25: 0}, vetor(0, [7, 7, 7, 2]))
    assert x[22] == 3


# ---------------------------------------------------------------- catálogo e restrições

def test_catalogo_completo_e_coerente():
    obrigatorios = {'id', 'nome', 'autoria', 'url', 'idioma', 'formato', 'isa', 'topicos', 'licenca', 'acesso',
                    'prioridade', 'uso', 'justificativa'}
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f['id']
        assert f['prioridade'] in ('alta', 'media', 'referencia')
        assert f['uso'] in ('acervo', 'citada', 'referencia', 'candidato', 'indisponivel')
        assert set(f['topicos']) <= set(OAC.assuntos), f['id']
    citadas = {x for i in ITENS.values() for x in i['fontes_catalogo']}
    assert citadas <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f['uso'] == 'acervo'} == {
        x for i in ITENS.values() if i['natureza'] == 'material_da_disciplina' for x in i['fontes_catalogo']}


def test_material_protegido_e_fotos_fora_do_repositorio():
    for ident in ('pattersonhennessy-cod-riscv', 'ufal-oac-slides-editora', 'borin-riscv-book'):
        assert CATALOGO[ident]['uso'] == 'referencia'
    arquivos = [p for p in (ROOT / 'disciplinas/oac').rglob('*') if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in ('.pdf', '.png', '.jpg', '.jpeg', '.docx', '.pptx')]


def test_documentacao_lista_todas_as_fontes():
    curadoria = (ROOT / 'disciplinas/oac/CURADORIA.md').read_text(encoding='utf-8')
    assert [i for i in CATALOGO if f'`{i}`' not in curadoria] == []
    assert [i for i in ITENS if f'`{i}`' not in curadoria] == []
