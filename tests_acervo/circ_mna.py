"""Análise nodal modificada (MNA) exata com SymPy, para conferir os circuitos do acervo de Circuitos Elétricos.

Cada circuito é descrito por nós (nomes) e elementos. O nó '0' é a referência.
- R(nome, a, b, ohms): corrente i = (v_a - v_b)/R, de a para b.
- V(nome, a, b, volts): fonte de tensão com + em a; sua corrente é incógnita, medida de a para b por dentro
  da fonte (entra pelo +). Negativa = a fonte fornece.
- I(nome, a, b, amperes): fonte de corrente que empurra a corrente de a para b *por dentro da fonte*
  (a seta aponta para b): retira corrente do nó a e injeta no nó b.
O valor de V e I pode ser expressão SymPy em `v('n')` (tensão de nó) e `i('X')` (corrente de um elemento), o que
cobre as fontes dependentes. `resolver` devolve tensões de nó, correntes e potências absorvidas por elemento
(positiva = absorve, negativa = fornece); a soma das potências tem de dar zero.
"""
from dataclasses import dataclass

import sympy as sp


def v(no):
    return sp.Symbol(f'v_{no}') if no != '0' else sp.Integer(0)


def i(nome):
    return sp.Symbol(f'i_{nome}')


@dataclass
class El:
    tipo: str
    nome: str
    a: str
    b: str
    valor: object


def R(nome, a, b, val):
    return El('R', nome, a, b, sp.nsimplify(val))


def V(nome, a, b, val):
    return El('V', nome, a, b, sp.nsimplify(val) if not isinstance(val, sp.Basic) else val)


def I(nome, a, b, val):
    return El('I', nome, a, b, sp.nsimplify(val) if not isinstance(val, sp.Basic) else val)


def resolver(elementos):
    nos = sorted({n for e in elementos for n in (e.a, e.b)} - {'0'})
    # corrente de cada elemento de a para b, pelo próprio elemento
    corr = {}
    eqs = []
    for e in elementos:
        if e.tipo == 'R':
            corr[e.nome] = (v(e.a) - v(e.b)) / e.valor
        elif e.tipo == 'I':
            corr[e.nome] = e.valor
        else:
            corr[e.nome] = i(e.nome)
            eqs.append(sp.Eq(v(e.a) - v(e.b), e.valor))
    # i('X') pode aparecer em expressões: liga o símbolo à corrente do elemento
    for nome, expr in corr.items():
        if expr != i(nome):
            eqs.append(sp.Eq(i(nome), expr))
    for n in nos:
        # KCL: soma das correntes que saem do nó n pelos elementos = 0
        saida = 0
        for e in elementos:
            if e.tipo == 'I':
                if e.a == n:
                    saida += e.valor
                if e.b == n:
                    saida -= e.valor
            else:
                if e.a == n:
                    saida += i(e.nome)
                if e.b == n:
                    saida -= i(e.nome)
        eqs.append(sp.Eq(saida, 0))
    incog = [v(n) for n in nos] + [i(e.nome) for e in elementos]
    sol = sp.solve(eqs, incog, dict=True)
    assert len(sol) == 1, 'circuito sem solução única'
    s = sol[0]
    tens = {n: sp.nsimplify(v(n).subs(s)) for n in nos} | {'0': sp.Integer(0)}
    ic = {e.nome: sp.nsimplify(i(e.nome).subs(s)) for e in elementos}
    # Convenção passiva para todos os elementos: ic é a corrente que entra pelo terminal a e atravessa o
    # elemento até b, então a potência absorvida é (v_a - v_b) * ic.
    pot = {e.nome: sp.nsimplify((tens[e.a] - tens[e.b]) * ic[e.nome]) for e in elementos}
    return tens, ic, pot


def thevenin(elementos, a, b):
    """(Vth, Rth) entre a e b: tensão em aberto e, com fonte de teste de 1 A injetada em a, Rth = v_ab/1."""
    t, _, _ = resolver(elementos)
    vth = t[a] - t[b]
    zerados = []
    for e in elementos:
        if e.valor.free_symbols:  # dependente: fica
            zerados.append(e)
        elif e.tipo == 'V':
            zerados.append(V(e.nome, e.a, e.b, 0))
        elif e.tipo == 'I':
            continue  # fonte de corrente independente zerada = aberta
        else:
            zerados.append(e)
    zerados.append(I('TESTE', b, a, 1))
    t2, _, _ = resolver(zerados)
    return sp.nsimplify(vth), sp.nsimplify(t2[a] - t2[b])
