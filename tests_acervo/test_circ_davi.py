"""Complemento de Circuitos Elétricos com o material do Prof. Davi (slides, provas de 2017 e reavaliação).

Cada circuito dos blocos `circ-davi-*` é remontado a partir da descrição em palavras e resolvido de novo:
MNA exata (`circ_mna`) com balanço de potências, e `dsolve` para primeira e segunda ordem. Os erros das
resoluções fotografadas são conferidos como erros. Também se confere que nada do material bruto
(fotos, slides, nomes de alunos, e-mail) foi versionado.
"""

import re
import subprocess

import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from tests_acervo.circ_mna import I, R, V, i, resolver, thevenin

CIRC = disciplinas.obter("circ")
ITENS = {x["id"]: x for x in read_json(CIRC.itens)}
NA_BUSCA = {c["id"] for c in read_json(CIRC.indice)["chunks"]}
DAVI = {k: x for k, x in ITENS.items() if k.startswith("circ-davi-")}
k = 1000
t = sp.Symbol("t", nonnegative=True)
f = sp.Function("f")
mA = sp.Rational(1, 1000)


def texto(ident):
    return ITENS[ident]["texto"]


def test_blocos_do_professor_entram_como_complemento():
    assert len(DAVI) == 10 and set(DAVI) <= NA_BUSCA
    assert CIRC.nome == "Circuitos Elétricos"
    bruto = [d for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] == "circ"][0]
    assert not {"modelo", "model", "provedor", "endpoint", "prompt"} & set(bruto)
    for x in DAVI.values():
        assert x["fontes_catalogo"] == ["ufal-circ-davi-2017"] and x["natureza"] == "material_da_disciplina"
        assert x["verificacao"] == "conferida_por_codigo" and x["revisao_humana"] == "pendente"
        assert x["publicacao_transcricao"].startswith("não declarada") and "parafrase" in x["publicacao_transcricao"]
        assert f"Status da resolução: {x['status_resolucao']}" in x["texto"]
    corrigidas = {k_ for k_, x in DAVI.items() if x["status_resolucao"] == "corrigida"}
    assert corrigidas == {
        "circ-davi-amp-op-media-ab2-q1",
        "circ-davi-nodal-thevenin-reav-q4-q5",
        "circ-davi-supermalha-ccvs-reav-q7",
        "circ-davi-primeira-ordem-ab2-q2-q3",
        "circ-davi-maxima-transferencia-ab1-q5",
    }
    assert all("**Correções:**" in texto(c) for c in corrigidas)


def test_rigor_tem_hipoteses_do_amp_op_e_primeira_ordem():
    assert "$i_p = i_n = 0$" in CIRC.rigor and "$v_p = v_n$" in CIRC.rigor and "$-R_f/R_s$" in CIRC.rigor
    assert "Fasores ainda não têm material" in CIRC.rigor


# ---------------------------------------------------------------- amp-op


def test_inversor_e_media_de_tres_sensores():
    vs, rs, rf, vo = sp.symbols("v_s R_s R_f v_o")
    assert sp.solve(sp.Eq(vs / rs + vo / rf, 0), vo)[0] == -rf * vs / rs
    assert (-rf * vs / rs).subs({rf: 4 * k, rs: k, vs: sp.Rational(1, 2)}) == -2
    v1, v2, v3, rb = sp.symbols("v1 v2 v3 R_B", positive=True)
    vx = -k * (v1 + v2 + v3) / (3 * k)
    vo = -rb / k * vx
    ganho = sp.solve(sp.Eq(vo.subs({v1: sp.Rational(1, 4), v2: sp.Rational(1, 4), v3: sp.Rational(1, 4)}), 1), rb)[0]
    assert ganho == 4 * k  # 0,25 V de média por 10 °C -> 1 V
    assert vo.subs({rb: 4 * k, v1: 1, v2: 1, v3: 1}) == 4
    assert vo.subs({rb: 12 * k, v1: 1, v2: 1, v3: 1}) == 12  # o 12 da foto dá 3 V por 10 °C
    assert "$R_B = 4$ kΩ" in texto("circ-davi-amp-op-media-ab2-q1")


# ---------------------------------------------------------------- divisores


def test_divisor_de_corrente_e_delta_y():
    i1 = 6 * mA * 2 * k / (3 * k)
    assert i1 == 4 * mA and 6 * mA - i1 == 2 * mA
    els = [I("S", "0", "a", 6 * mA), R("R1", "a", "0", k), R("R2", "a", "0", 2 * k)]
    _, c, p = resolver(els)
    assert c["R1"] == 4 * mA and sum(p.values()) == 0
    assert 9 * 9 / sp.Integer(27) == 3


# ---------------------------------------------------------------- reavaliação


def reav_q4(carga=True):
    els = [
        V("E", "n1", "0", 12),
        I("S2", "n1", "n2", 2 * mA),
        R("Ra", "n1", "n3", 2 * k),
        R("Rb", "n2", "n3", k),
        I("S4", "0", "n3", 4 * mA),
    ]
    return els + ([R("Ro", "n2", "0", 2 * k)] if carga else [])


def test_reav_q4_nodal_e_potencias_das_fontes():
    tens, c, p = resolver(reav_q4())
    assert tens["n2"] == sp.Rational(52, 5) and tens["n3"] == sp.Rational(68, 5)
    assert c["Ro"] == sp.Rational(26, 5) * mA
    assert p["E"] == -sp.Rational(144, 10) * mA and p["S4"] == -sp.Rational(544, 10) * mA
    assert p["S2"] == sp.Rational(32, 10) * mA and sum(p.values()) == 0


def test_reav_q5_thevenin_e_potencia_maxima_em_watts():
    vth, rth = thevenin(reav_q4(carga=False), "n2", "0")
    assert (vth, rth) == (26, 3 * k)
    pmax = vth**2 / (4 * rth)
    assert abs(float(pmax) - 0.0563) < 1e-4
    assert "56{,}3$ mW" in texto("circ-davi-nodal-thevenin-reav-q4-q5") and "watts" in texto(
        "circ-davi-nodal-thevenin-reav-q4-q5"
    )


def test_reav_q6_thevenin_com_duas_fontes_de_corrente():
    els = [
        V("E", "T", "L", 18),
        R("R1", "L", "0", 6 * k),
        R("R2", "T", "N", 6 * k),
        R("R3", "N", "0", 6 * k),
        R("R4", "T", "A", 4 * k),
        R("R5", "T", "A", 4 * k),
        I("S2", "N", "0", 2 * mA),
        I("S1", "0", "A", mA),
    ]
    assert thevenin(els, "A", "0") == (14, 6 * k)
    tens, c, p = resolver(els + [R("Ro", "A", "0", 3 * k)])
    assert c["Ro"] == sp.Rational(14, 9) * mA and tens["A"] == sp.Rational(14, 3) and sum(p.values()) == 0


def test_reav_q7_supermalha_com_fonte_de_tensao_dependente():
    els = [
        V("E", "a", "0", 6),
        R("R6", "a", "b", 6 * k),
        R("Rx", "b", "0", 2 * k),
        V("H", "c", "b", 2000 * i("Rx")),
        I("S", "0", "c", 3 * mA),
        R("R4", "c", "d", 4 * k),
    ]
    assert thevenin(els, "d", "0") == (12, 7 * k)
    tens, c, p = resolver(els + [R("Ro", "d", "0", 4 * k)])
    assert tens["d"] == sp.Rational(48, 11) and sum(p.values()) == 0
    assert c["Ro"] == sp.Rational(12, 11) * mA  # I3; a foto usa 4,9 mA e chega a 19,6 V
    i1, i2 = sp.symbols("I1 I2")
    s = sp.solve([4 * i1 - i2 - 3, -4 * i1 + 12 * i2 + 24], [i1, i2])
    assert s[i2] == sp.Rational(-21, 11) and 3 + s[i2] == sp.Rational(12, 11)


def test_reav_q8_malhas_com_fonte_de_corrente_dependente():
    i3 = sp.Symbol("I3")
    i2 = sp.Rational(3, 4) * (1 - i3)
    sol = sp.solve(3 * (i3 - 1) + (i3 - i2) + 3 * i3, i3)[0]
    assert sol == sp.Rational(15, 31) and abs(float(3 * sol) - 1.45) < 0.01
    assert i2.subs(i3, sol) == 3 * (1 - sol) / 4


def test_reav_q3_supermalha_do_caderno():
    els = [
        R("Ra", "0", "L", 2 * k),
        V("E", "L", "P", 12),
        R("Ro", "P", "0", 2 * k),
        R("Rb", "P", "Q", 4 * k),
        I("S", "0", "Q", 4 * mA),
        R("Rc", "Q", "S", 2 * k),
        R("Rd", "S", "0", 4 * k),
    ]
    _, c, p = resolver(els)
    assert c["Ro"] == -sp.Rational(18, 11) * mA and sum(p.values()) == 0  # -1,64 mA do caderno


# ---------------------------------------------------------------- primeira e segunda ordem


def test_ab2_q2_rc_e_q3_rl():
    tens, _, _ = resolver(
        [
            V("E", "P", "0", 6),
            R("R12", "P", "Q", 12 * k),
            R("R8", "Q", "0", 8 * k),
            V("F", "x", "0", 12),
            R("R4", "x", "P", 4 * k),
        ]
    )
    vc0 = tens["P"] - tens["Q"]
    assert vc0 == sp.Rational(18, 5)
    depois = [V("F", "x", "0", 12), R("R4", "x", "P", 4 * k), R("R12", "P", "Q", 12 * k), R("R8", "Q", "0", 8 * k)]
    tens, _, _ = resolver(depois)
    vcinf = tens["P"] - tens["Q"]
    vth, rth = thevenin(depois, "P", "Q")
    assert vcinf == 6 and rth == 6 * k and rth * 100e-6 == 0.6
    vc = vcinf + (vc0 - vcinf) * sp.exp(-t / sp.Rational(3, 5))
    vo = sp.Rational(2, 3) * (12 - vc)
    assert sp.simplify(vo - (4 + sp.Rational(8, 5) * sp.exp(-sp.Rational(5, 3) * t))) == 0
    r = 1 / (1 / sp.Integer(k) + 1 / (sp.Integer(k) * 2 * 2 / 4 + 2 * k))
    assert r == 750 and sp.Rational(1, 1000) / r == sp.Rational(4, 3) * sp.Rational(1, 10**6)


def test_ab2_q4_q5_q6_segunda_ordem():
    s = sp.dsolve(
        f(t).diff(t, 2) + f(t).diff(t) / (8 * sp.Rational(4, 100)) + f(t) / sp.Rational(4, 100),
        f(t),
        ics={f(0): 8, f(t).diff(t).subs(t, 0): 0},
    ).rhs
    alfa, wd = sp.Rational(25, 16), 5 * sp.sqrt(231) / 16
    assert sp.simplify(s - sp.exp(-alfa * t) * (8 * sp.cos(wd * t) + 8 * alfa / wd * sp.sin(wd * t))) == 0
    assert abs(float(8 * alfa / wd) - 2.63) < 0.01 and abs(float(wd) - 4.75) < 0.01
    s = sp.dsolve(
        f(t).diff(t, 2) + 10**4 * f(t).diff(t) + 10**7 * (f(t) - 12), f(t), ics={f(0): 0, f(t).diff(t).subs(t, 0): 0}
    ).rhs
    assert (
        abs(float(s.subs(t, sp.Rational(1, 1000))) - (12 - 13.746 * 2.718281828**-1.127 + 1.746 * 2.718281828**-8.873))
        < 1e-2
    )
    s = sp.dsolve(
        f(t).diff(t, 2) + 10 * f(t).diff(t) + 25 * f(t), f(t), ics={f(0): 3, f(t).diff(t).subs(t, 0): 10 + 5 - 30}
    ).rhs
    assert sp.simplify(s - 3 * sp.exp(-5 * t)) == 0


def test_ab1_q5_potencia_maxima_e_6_4_mw():
    assert sp.Integer(8) ** 2 / (4 * 2500) == sp.Rational(64, 10000)
    assert "6{,}4\\ \\text{mW}" in texto("circ-davi-maxima-transferencia-ab1-q5")


# ---------------------------------------------------------------- nada de material bruto nem dados pessoais


def test_sem_fotos_slides_nomes_nem_email_no_repositorio():
    rastreados = subprocess.run(
        ["git", "ls-files", "disciplinas", "tests_acervo"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    ).stdout.splitlines()
    assert not [p for p in rastreados if re.search(r"\.(jpe?g|png|pptx|zip|heic)$", p, re.I)]
    assert not [p for p in rastreados if re.search(r"IMG[-_]\d", p)]
    pasta = ROOT / "disciplinas/circ"
    todo = "\n".join(p.read_text(encoding="utf-8") for p in pasta.rglob("*") if p.suffix in (".md", ".json"))
    for proibido in ("Bruno", "Barbosa", "@ic.ufal.br", "chat.whatsapp", "WA00"):
        assert proibido not in todo, proibido
