"""Respostas esperadas da bateria de SD (relatório de 19/10/2026), conferidas por enumeração.

Isto confere o RESULTADO (expressão, entradas do MUX, contas, equações do contador). Não avalia o
texto de uma resposta do tutor: a explicação e as citações são avaliadas à parte, por pessoas.
O avaliador de expressões abaixo só serve para estes testes; não é um resolvedor de circuitos.
"""
import itertools
import re

import pytest


def avaliar(expr, valores):
    """Soma de produtos com ' para negação: "B'D' + BD"."""
    def termo(t):
        return all((not valores[v]) if neg else valores[v] for v, neg in re.findall(r"([A-Z])('?)", t))
    return any(termo(t) for t in expr.replace(" ", "").split("+"))


def confere(expr, variaveis, mintermos, irrelevantes=()):
    """1 em todo mintermo, 0 em todo o resto que não é irrelevância. Devolve as linhas erradas."""
    erradas = []
    for n, bits in enumerate(itertools.product((0, 1), repeat=len(variaveis))):
        if n in irrelevantes:
            continue
        if avaliar(expr, dict(zip(variaveis, bits))) != (n in mintermos):
            erradas.append(n)
    return erradas


# -------------------------------------------------------------------------- Karnaugh

def test_karnaugh_basico_do_teste_manual():
    """F(A,B,C,D) = Σm(0,2,5,7,8,10,13,15): gabarito B'D' + BD (Gemini e local acertaram)."""
    assert confere("B'D' + BD", "ABCD", {0, 2, 5, 7, 8, 10, 13, 15}) == []


def test_mintermo_m7_e_0111_nao_m15():
    """Deslize do modelo local: chamou de m15 a combinação 0111."""
    assert int("0111", 2) == 7 and int("1111", 2) == 15


def test_av1_q7b_com_irrelevancias():
    """Lista AV1 7b (m01): S = 1 em 000, 011, 101; x em 001, 100, 110, 111 → S = B' + C."""
    assert confere("B' + C", "ABC", {0, 3, 5}, irrelevantes={1, 4, 6, 7}) == []
    assert confere("B' + C", "ABC", {0, 3, 5}) == [1, 4, 7]  # sem usar os x, B' + C não serve


# Caso com irrelevâncias que reproduz a FORMA do erro do relatório (o enunciado original da
# conversa não foi guardado): F(A,B,C,D) = Σm(0,1,3,7,11,15) + d(2), mínima CD + A'B'.
KARNAUGH_X = dict(variaveis="ABCD", mintermos={0, 1, 3, 7, 11, 15}, irrelevantes={2})


def test_karnaugh_com_irrelevancia_resposta_certa():
    assert confere("CD + A'B'", **KARNAUGH_X) == []


@pytest.mark.parametrize("errada", ["BD + AC", "B'D + A'D + CD"])
def test_respostas_erradas_do_modelo_local_falham_na_tabela(errada):
    """As duas respostas do modelo local: a conferência linha a linha mostra o erro."""
    assert confere(errada, **KARNAUGH_X) != []


def test_sem_a_irrelevancia_a_forma_minima_muda():
    assert confere("CD + A'B'", **{**KARNAUGH_X, "irrelevantes": set()}) == [2]
    assert confere("CD + A'B'C'", **{**KARNAUGH_X, "irrelevantes": set()}) == []


# -------------------------------------------------------------------------- MUX 4x1

def test_mux_4x1_sigma_m_1_2_6_7():
    """F(A,B,C) = Σm(1,2,6,7) com seleção AB: I0 = C, I1 = C', I2 = 0, I3 = 1."""
    entradas = {0: lambda c: c, 1: lambda c: 1 - c, 2: lambda c: 0, 3: lambda c: 1}
    for n in range(8):
        a, b, c = (n >> 2) & 1, (n >> 1) & 1, n & 1
        assert entradas[2 * a + b](c) == (n in {1, 2, 6, 7})
    assert format(6, "03b") == "110"  # m6 = ABC' (o modelo escreveu AB'C, que é m5)


# -------------------------------------------------------------------------- complemento de 2

def compl2(x, bits):
    return (~x + 1) & ((1 << bits) - 1)


def test_complemento_de_dois():
    assert format(compl2(0b101010, 6), "06b") == "010110"


@pytest.mark.parametrize("a, b, overflow", [(0b0110, 0b0011, True), (0b0011, 0b0010, False),
                                            (0b1100, 0b1011, True), (0b1110, 0b0011, False)])
def test_overflow_e_xor_dos_dois_ultimos_carries(a, b, overflow):
    """V = Cₙ ⊕ Cₙ₋₁ (4 bits): confere com a definição (soma fora de -8..7)."""
    c3 = ((a & 0b0111) + (b & 0b0111)) >> 3  # carry que entra no bit de sinal
    c4 = (a + b) >> 4                          # carry que sai dele
    com_sinal = lambda x: x - 16 if x & 8 else x
    fora = not -8 <= com_sinal(a) + com_sinal(b) <= 7
    assert (c3 ^ c4) == fora == overflow


# -------------------------------------------------------------------------- contador mod 6 com JK

def test_contador_modulo_6_com_jk_pelo_metodo_da_disciplina():
    """Tabela de excitação JK, estados 110 e 111 como irrelevâncias:
    J0 = K0 = 1; J1 = Q2'Q0, K1 = Q0; J2 = Q1Q0, K2 = Q0. Simulado estado a estado."""
    def jk(q, j, k):
        return {(0, 0): q, (0, 1): 0, (1, 0): 1, (1, 1): 1 - q}[(j, k)]
    estado = 0
    visitados = []
    for _ in range(7):
        visitados.append(estado)
        q2, q1, q0 = (estado >> 2) & 1, (estado >> 1) & 1, estado & 1
        n0 = jk(q0, 1, 1)
        n1 = jk(q1, (1 - q2) & q0, q0)
        n2 = jk(q2, q1 & q0, q0)
        estado = n2 << 2 | n1 << 1 | n0
    assert visitados == [0, 1, 2, 3, 4, 5, 0]
