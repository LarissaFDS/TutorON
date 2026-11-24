"""Acervo de Variáveis Complexas e conferência das resoluções.

As provas (três versões da Prova 1 do Prof. Xu Yang) não têm gabarito. Cada valor afirmado num bloco é refeito
aqui com SymPy (aritmética exata, raízes, `residue`, integral da curva parametrizada) e numericamente com NumPy
(integral sobre a parametrização, com a orientação dada no enunciado).
"""

import json
import re
import shutil
import subprocess

import numpy as np
import pytest
import sympy as sp

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

VC = disciplinas.obter("varcomp")
FONTES = read_json(ROOT / "disciplinas/varcomp/fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
ITENS = {x["id"]: x for x in read_json(VC.itens)}
NA_BUSCA = {c["id"] for c in read_json(VC.indice)["chunks"]}
VETORES = json.loads((ROOT / "eval/relevancia-vetores.json").read_text(encoding="utf-8"))
I = sp.I
z, t = sp.symbols("z t")


def texto(ident):
    return ITENS[f"varcomp-{ident}"]["texto"]


def buscar(pergunta, d=VC):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def hibrida(pergunta, d=VC):
    return [
        r["id"]
        for r in search(
            pergunta,
            k=4,
            vector=VETORES[pergunta],
            min_similarity=0.45,
            hub_penalty=True,
            itens=d.itens,
            indice=d.indice,
        )
    ]


def numerica(f, gamma, dgamma, a=0.0, b=2 * np.pi, n=20001):
    """Integral de f ao longo de gamma(t), t de a até b, com dz = gamma'(t) dt (gamma' exata).

    Curva fechada (de 0 a 2π): soma sem repetir o ponto final, que é a regra do trapézio periódica (converge muito
    rápido); caminho aberto: regra do trapézio comum.
    """
    fechada = (a, b) == (0.0, 2 * np.pi)
    tt = np.linspace(a, b, n, endpoint=not fechada)
    integrando = f(gamma(tt)) * dgamma(tt)
    return integrando.sum() * (b - a) / n if fechada else np.trapezoid(integrando, tt)


def curva(gamma_sp):
    """Parametrização simbólica -> (gamma, gamma') para NumPy."""
    return sp.lambdify(t, gamma_sp, "numpy"), sp.lambdify(t, sp.diff(gamma_sp, t) + 0 * t, "numpy")


def exata(f, gamma):
    """Mesma integral com SymPy, sobre a parametrização simbólica (curva fechada, t de 0 a 2π)."""
    integrando = sp.simplify(f.subs(z, gamma) * sp.diff(gamma, t))
    return sp.simplify(sp.integrate(integrando, (t, 0, 2 * sp.pi)))


CIRC3 = curva(3 * sp.cos(t) + 3 * I * sp.sin(t))
G = sp.sin(sp.pi * z**2) + sp.cos(sp.pi * z**2)


def g_np(zz):
    return np.sin(np.pi * zz**2) + np.cos(np.pi * zz**2)


# ---------------------------------------------------------------- cadastro e acervo


def test_varcomp_cadastrada_com_acervo_proprio_e_a_mesma_ia():
    assert VC.nome == "Variáveis Complexas" and VC.itens.exists() and VC.indice.exists()
    assert (
        not VC.livro_supabase
        and VC.rigor.strip() == (ROOT / "disciplinas/varcomp/rigor.md").read_text(encoding="utf-8").strip()
    )
    assert all(c["disciplina"] == "varcomp" for c in read_json(VC.indice)["chunks"])
    for outra in (
        "paa",
        "sd",
        "oac",
        "calc3",
        "fis2",
        "ed",
        "bd",
        "prob",
        "circ",
        "sinais",
        "controle",
        "eletronica",
        "pcom",
    ):
        d = disciplinas.obter(outra)
        assert NA_BUSCA.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    bruto = [d for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] == "varcomp"][0]
    assert not {"modelo", "model", "provedor", "endpoint", "prompt", "chave"} & set(bruto)
    assert bruto["situacao"] == "MVP" and "aviso" not in bruto
    assert (
        read_json(VC.indice)["embedding_model"] == read_json(disciplinas.obter("eletronica").indice)["embedding_model"]
    )


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas varcomp --embeddings`."""
    gerados = disciplinas.registros(VC)
    assert gerados == read_json(VC.itens)
    assert NA_BUSCA == {x["id"] for x in gerados if x["confiabilidade"] in ("media", "alta")}
    assert read_json(VC.indice)["modo"] == "hibrido"


def test_blocos_cabem_no_trecho_e_formulas_fecham():
    for x in ITENS.values():
        assert len(x["texto"]) <= 2200, x["id"]
        sem_destaque = x["texto"].replace("$$", "")
        assert x["texto"].count("$$") % 2 == 0 and sem_destaque.count("$") % 2 == 0, x["id"]
        assert "**Verificação:**" in x["texto"], x["id"]


NOTAS_IA = {
    "varcomp-nota-ia-cauchy-riemann",
    "varcomp-nota-ia-funcoes-elementares",
    "varcomp-nota-ia-taylor-laurent",
    "varcomp-nota-ia-residuos",
    "varcomp-nota-ia-conformes",
    "varcomp-nota-ia-harmonicas",
    "varcomp-nota-ia-gamma-stirling",
}


def test_notas_de_ia_sem_revisao_ficam_fora_da_busca():
    notas = {x["id"] for x in ITENS.values() if x["natureza"] == "nota_da_equipe_ia"}
    assert notas == NOTAS_IA
    assert all(ITENS[n]["status_curadoria"] == "candidato" and ITENS[n]["revisao_humana"] == "pendente" for n in notas)
    assert notas.isdisjoint(NA_BUSCA)
    assert not any(x.get("revisao_humana") == "feita" or x.get("revisao_professor") for x in ITENS.values())


def test_topicos_das_provas_tem_bloco_na_busca():
    """Critério de liberação: os tópicos "Sim" (com evidência nas provas) têm bloco na busca; os outros, não."""
    sim = {
        "varcomp-01-numeros-complexos",
        "varcomp-04-integrais-de-contorno",
        "varcomp-05-cauchy-goursat-primitivas",
        "varcomp-06-formula-integral-cauchy",
    }
    lista1 = {"varcomp-02-funcoes-analiticas-cauchy-riemann", "varcomp-03-funcoes-elementares"}  # 4º período de EC
    assert {ITENS[x]["assunto"] for x in NA_BUSCA} == sim | lista1
    assert set(CATALOGO["ufal-varcomp-prova1-2021"]["topicos"]) == sim
    assert set(CATALOGO["ufal-varcomp-lista1"]["topicos"]) == lista1 | {"varcomp-01-numeros-complexos"}


def test_resolucoes_sao_pendentes_do_professor_e_dizem_no_texto():
    turma = [x for x in ITENS.values() if x["natureza"] == "material_da_disciplina"]
    assert len(turma) == 16 and {x["id"] for x in turma} == NA_BUSCA
    for x in turma:
        assert x["status_resolucao"] == "pendente_professor", x["id"]
        assert "Status da resolução: pendente de confirmação do professor" in x["texto"]
        assert x["verificacao"] == "conferida_por_codigo" and x["revisao_humana"] == "pendente"
        assert x["publicacao_transcricao"].startswith("não autorizada") and "Enunciado parafraseado" in x["texto"]


# ---------------------------------------------------------------- questão 1: aritmética e raízes


@pytest.mark.parametrize(
    "bloco, valores",
    [
        (
            "p1c-q1-operacoes",
            [
                ((2 - 3 * I) * (4 + 2 * I), 14 - 8 * I, "14 - 8i"),
                ((I**30 - I**19) / (2 * I - 1), (3 + I) / 5, r"\frac{3 + i}{5}"),
                ((3 + 2 * I) * sp.conjugate(7 + I), 23 + 11 * I, "23 + 11i"),
                ((3 + 2 * I) * (7 + I), 19 + 17 * I, "19 + 17i"),
            ],
        ),  # erro comum citado no bloco
        (
            "p1a-q1-operacoes-raizes",
            [
                ((1 + I) * (1 - 2 * I), 3 - I, "3 - i"),
                ((I**10 - I**9) / (2 * I + 1), (-3 + I) / 5, r"\frac{-3 + i}{5}"),
                ((3 + 2 * I) * sp.conjugate(3 - I), 7 + 9 * I, "7 + 9i"),
            ],
        ),
        (
            "p1b-q1-operacoes-raizes",
            [
                ((2 + I) * (2 - 5 * I), 9 - 8 * I, "9 - 8i"),
                ((I**12 - I**15) / (2 * I + 3), (5 + I) / 13, r"\frac{5 + i}{13}"),
                ((4 + I) * sp.conjugate(3 - 2 * I), 10 + 11 * I, "10 + 11i"),
            ],
        ),
    ],
)
def test_q1_operacoes(bloco, valores):
    for expr, esperado, escrito in valores:
        assert sp.simplify(expr - esperado) == 0, (bloco, escrito)
        assert escrito in texto(bloco), (bloco, escrito)


def test_q1b_versao_c_tres_raizes_cubicas_de_1_menos_i():
    w = 1 - I
    assert sp.arg(w) == -sp.pi / 4 and sp.Abs(w) == sp.sqrt(2)
    raizes = [2 ** sp.Rational(1, 6) * sp.exp(I * (-sp.pi / 4 + 2 * k * sp.pi) / 3) for k in range(3)]
    for r in raizes:
        assert sp.simplify(sp.expand_complex(r**3) - w) == 0
    assert sp.simplify(sp.expand_complex(sum(raizes))) == 0
    numericas = [complex(sp.N(r)) for r in raizes]
    for r in np.roots([1, 0, 0, -(1 - 1j)]):  # NumPy acha as mesmas três raízes
        assert min(abs(r - s) for s in numericas) < 1e-12
    x = texto("p1c-q1b-raizes-cubicas")
    for s in (
        "1{,}0842 - 0{,}2905i",
        "-0{,}2905 + 1{,}0842i",
        "-0{,}7937 - 0{,}7937i",
        "-3\\pi/4",
        "7\\pi/12",
        "-\\pi/12",
    ):
        assert s in x
    assert "**Dúvida de enunciado:**" in x and "2^{1/6} e^{2k\\pi i/3}" in x
    assert sp.nsimplify(sp.Abs(w) ** sp.Rational(1, 3)) == 2 ** sp.Rational(1, 6)


@pytest.mark.parametrize(
    "bloco, w, aprox, modulo",
    [
        ("p1a-q1-operacoes-raizes", -2 - I, "0{,}3436 - 1{,}4553i", "5^{1/4}"),
        ("p1b-q1-operacoes-raizes", 5 - 2 * I, "2{,}2787 - 0{,}4388i", "29^{1/4}"),
    ],
)
def test_q1b_versoes_a_b_raizes_quadradas(bloco, w, aprox, modulo):
    r = sp.sqrt(w)
    assert sp.simplify(sp.expand(r**2) - w) == 0
    re_, im_ = (float(v) for v in aprox.replace("{,}", ".").replace(" - ", " ").replace("i", "").split())
    assert abs(complex(sp.N(r)) - complex(re_, -im_)) < 1e-4 or abs(complex(sp.N(-r)) - complex(re_, -im_)) < 1e-4
    assert abs(float(sp.Abs(w)) ** 0.5 - float(sp.sympify(modulo.replace("{", "(").replace("}", ")")))) < 1e-12
    assert aprox in texto(bloco) and modulo in texto(bloco) and "**Dúvida de enunciado**" in texto(bloco)
    if w == -2 - I:  # 3º quadrante: Arg = -π + arctan(1/2)
        assert sp.simplify(sp.arg(w) - (-sp.pi + sp.atan(sp.Rational(1, 2)))) == 0


# ---------------------------------------------------------------- questão 2: fórmula integral de Cauchy


@pytest.mark.parametrize(
    "bloco, p1, p2, segunda, esperado1, esperado2",
    [
        ("p1c-q2-formula-cauchy", 1, 2, sp.exp(2 * z) / (z + 1) ** 4, 4 * sp.pi * I, 8 * sp.pi * I * sp.exp(-2) / 3),
        ("p1a-q2-formula-cauchy", -1, 2, sp.exp(z) / (z - 2) ** 4, 4 * sp.pi * I / 3, sp.pi * I * sp.exp(2) / 3),
        (
            "p1b-q2-formula-cauchy",
            sp.Rational(-1, 2),
            sp.Rational(3, 2),
            sp.exp(2 * z) / (z - sp.Rational(3, 2)) ** 4,
            0,
            8 * sp.pi * I * sp.exp(3) / 3,
        ),
    ],
)
def test_q2_residuos_e_integral_numerica(bloco, p1, p2, segunda, esperado1, esperado2):
    primeira = G / ((z - p1) * (z - p2))
    # Todas as singularidades estão dentro de |z| = 3 (anti-horária): teorema dos resíduos.
    assert abs(p1) < 3 and abs(p2) < 3
    soma1 = sp.residue(primeira, z, p1) + sp.residue(primeira, z, p2)
    polo = sp.solve(sp.denom(segunda), z)[0]
    assert abs(polo) < 3
    assert sp.simplify(2 * sp.pi * I * soma1 - esperado1) == 0
    assert sp.simplify(2 * sp.pi * I * sp.residue(segunda, z, polo) - esperado2) == 0
    f1 = sp.lambdify(z, primeira, "numpy")
    f2 = sp.lambdify(z, segunda, "numpy")
    assert abs(numerica(f1, *CIRC3) - complex(esperado1)) < 1e-3
    assert abs(numerica(f2, *CIRC3) - complex(sp.N(esperado2))) < 1e-6
    assert "3!" in texto(bloco) and "dentro" in texto(bloco)


def test_q2_erros_tipicos_dariam_outro_valor():
    """Sem o 3! ou com n = 4, o resultado da versão C muda: o bloco usa o fator certo."""
    certo = 2 * sp.pi * I / sp.factorial(3) * sp.diff(sp.exp(2 * z), z, 3).subs(z, -1)
    assert sp.simplify(certo - 8 * sp.pi * I * sp.exp(-2) / 3) == 0
    assert sp.simplify(2 * sp.pi * I * sp.diff(sp.exp(2 * z), z, 3).subs(z, -1) - certo) != 0
    # Versão B: g(-0,5) = g(1,5) = √2, por isso a primeira integral é zero (não por Cauchy-Goursat).
    assert sp.simplify(G.subs(z, sp.Rational(-1, 2)) - sp.sqrt(2)) == 0
    assert sp.simplify(G.subs(z, sp.Rational(3, 2)) - sp.sqrt(2)) == 0
    assert "não vem do teorema de Cauchy-Goursat" in texto("p1b-q2-formula-cauchy")


# ---------------------------------------------------------------- questão 3: 1/z e 1/z², orientação


@pytest.mark.parametrize(
    "bloco, gamma_sp, centro, esperado",
    [
        ("p1c-q3-1-sobre-z-elipse", sp.cos(t) + 2 * I * sp.sin(t), 0, 2 * sp.pi * I),
        ("p1a-q3-orientacao-horaria", 2 * sp.cos(t) - I * sp.sin(t), 0, -2 * sp.pi * I),
        ("p1b-q3-1-sobre-z-menos-1", 3 * sp.cos(t) + 3 * I * sp.sin(t), 1, 2 * sp.pi * I),
    ],
)
def test_q3_um_sobre_z_e_um_sobre_z2(bloco, gamma_sp, centro, esperado):
    assert abs(numerica(lambda zz: 1 / (zz - centro), *curva(gamma_sp)) - complex(esperado)) < 1e-8
    assert abs(numerica(lambda zz: 1 / (zz - centro) ** 2, *curva(gamma_sp))) < 1e-8
    if centro == 0 and bloco != "p1c-q3-1-sobre-z-elipse":
        assert sp.simplify(exata(1 / z**2, gamma_sp)) == 0
    # orientação: o sinal da parte imaginária de γ'(0)·conj(γ(0)) diz se gira no sentido anti-horário
    giro = complex(sp.N((sp.diff(gamma_sp, t) * sp.conjugate(gamma_sp - centro)).subs(t, 0))).imag
    assert (giro > 0) == (esperado == 2 * sp.pi * I)
    assert str(esperado).replace("*", "") in ("2Ipi", "-2Ipi")
    x = texto(bloco)
    assert ("-2\\pi i" in x) == (esperado == -2 * sp.pi * I)
    assert sp.residue(1 / z**2, z, 0) == 0


# ---------------------------------------------------------------- questão 4: z² no segmento


@pytest.mark.parametrize(
    "bloco, fim, esperado",
    [
        ("p1c-q4-z2-segmento", 2 + I, (2 + 11 * I) / 3),
        ("p1a-q4-z2-segmento", 1 - 2 * I, (-11 + 2 * I) / 3),
        ("p1b-q4-z2-segmento", 3 - 4 * I, -39 - 44 * I / 3),
    ],
)
def test_q4_primitiva_parametrizacao_e_numerica(bloco, fim, esperado):
    assert sp.expand(fim**3 / 3 - esperado) == 0
    assert sp.expand(sp.integrate((fim * t) ** 2 * fim, (t, 0, 1)) - esperado) == 0
    c = complex(fim)
    assert abs(numerica(lambda zz: zz**2, lambda tt: c * tt, lambda tt: c + 0 * tt, 0, 1) - complex(esperado)) < 1e-6
    # outro caminho (0 → Re → fim) dá o mesmo: independência do caminho
    re_ = complex(sp.re(fim))
    outro = numerica(lambda zz: zz**2, lambda tt: re_ * tt, lambda tt: re_ + 0 * tt, 0, 1) + numerica(
        lambda zz: zz**2, lambda tt: re_ + (c - re_) * tt, lambda tt: (c - re_) + 0 * tt, 0, 1
    )
    assert abs(outro - complex(esperado)) < 1e-6


# ---------------------------------------------------------------- notas da equipe (fora da busca, mas conferidas)


def test_notas_conferidas():
    x, y = sp.symbols("x y", real=True)
    u, v = sp.re(sp.expand((x + I * y) ** 2)), sp.im(sp.expand((x + I * y) ** 2))
    assert sp.diff(u, x) == sp.diff(v, y) and sp.diff(u, y) == -sp.diff(v, x)
    assert sp.diff(u, x, 2) + sp.diff(u, y, 2) == 0 and v == 2 * x * y
    assert sp.simplify(sp.exp(sp.log(-1)) + 1) == 0 and sp.log(-1) == I * sp.pi
    assert abs(complex(sp.N(I**I)) - np.exp(-np.pi / 2)) < 1e-12
    serie = sp.series(1 / (z * (z - 1)), z, 0, 3).removeO()
    assert sp.expand(serie - (-1 / z - 1 - z - z**2)) == 0
    assert sp.residue(1 / (1 + z**2), z, I) == 1 / (2 * I)
    assert sp.integrate(1 / (1 + sp.Symbol("x") ** 2), (sp.Symbol("x"), -sp.oo, sp.oo)) == sp.pi
    w = (z - I) / (z + I)
    assert [sp.simplify(w.subs(z, a)) for a in (0, 1, I)] == [-1, -I, 0]
    assert sp.gamma(sp.Rational(1, 2)) == sp.sqrt(sp.pi)
    q = float(sp.sqrt(20 * sp.pi) * (10 / sp.E) ** 10 / sp.factorial(10))
    assert round(q, 4) == 0.9917 and abs(float(sp.sqrt(20 * sp.pi) * (10 / sp.E) ** 10) - 3.5987e6) < 100


# ---------------------------------------------------------------- busca

EXEMPLOS = [
    ("Como calcular todas as raízes cúbicas de 1 − i?", {"varcomp-p1c-q1b-raizes-cubicas"}),
    ("Como usar a fórmula integral de Cauchy em ∮ e^{2z}/(z+1)⁴ dz?", {"varcomp-p1c-q2-formula-cauchy"}),
    (
        "Por que ∮ 1/z dz = 2πi e ∮ 1/z² dz = 0?",
        {"varcomp-p1c-q3-1-sobre-z-elipse", "varcomp-p1b-q3-1-sobre-z-menos-1"},
    ),
    ("Como calcular ∫ z² dz no segmento de 0 a 2+i?", {"varcomp-p1c-q4-z2-segmento"}),
    ("Por que o sentido da curva muda o sinal de ∮ 1/z dz?", {"varcomp-p1a-q3-orientacao-horaria"}),
]
VARIANTES = [
    (r"Raízes de $(1-i)^{1/3}$", "raiz cubica de 1 menos i", EXEMPLOS[0][1]),
    (
        r"Como calcular $\oint \frac{e^{2z}}{(z+1)^4}dz$ pela fórmula de Cauchy?",
        "integral de e elevado a 2z sobre z mais 1 à quarta na circunferência de raio 3",
        EXEMPLOS[1][1],
    ),
    (
        r"Por que $\oint \frac{1}{z^2}dz = 0$?",
        "integral de 1 sobre z ao quadrado numa curva fechada dá zero?",
        {"varcomp-p1c-q3-1-sobre-z-elipse"},
    ),
    (r"$\int_\gamma z^2 dz$ de 0 a $2+i$", "integral de z ao quadrado no segmento de 0 a 2 mais i", EXEMPLOS[3][1]),
]
FORA = [
    "Como simplificar uma função com mapa de Karnaugh?",
    "Como fazer um LEFT JOIN em SQL?",
    "Me conte uma piada",
    "Qual a transformada de Laplace de e^{-at}?",
    "O que é um fasor?",
]


def test_exemplos_do_cadastro_sao_os_testados():
    assert list(VC.exemplos) == [p for p, _ in EXEMPLOS]


@pytest.mark.parametrize("pergunta, aceitos", EXEMPLOS)
def test_perguntas_de_exemplo_trazem_o_bloco_certo(pergunta, aceitos):
    assert aceitos & set(hibrida(pergunta))


@pytest.mark.parametrize("latex, simples, aceitos", VARIANTES)
def test_latex_e_texto_simples_trazem_o_mesmo_bloco(latex, simples, aceitos):
    assert aceitos & set(hibrida(latex)) and aceitos & set(hibrida(simples))


@pytest.mark.parametrize("pergunta", FORA)
def test_pergunta_de_outra_area_nao_traz_material(pergunta):
    assert hibrida(pergunta) == []


def test_cauchy_riemann_so_teria_bloco_com_a_nota_aprovada(tmp_path):
    """Hoje Cauchy-Riemann só tem nota de IA fora da busca; aprovada, ela seria o primeiro bloco."""
    assert "varcomp-nota-ia-cauchy-riemann" not in buscar("O que são as equações de Cauchy-Riemann?")
    shutil.copytree(VC.materiais, tmp_path / "m")
    p = tmp_path / "m" / "n01-cauchy-riemann.md"
    p.write_text(p.read_text(encoding="utf-8").replace("curadoria: candidato", "curadoria: aprovado"), encoding="utf-8")
    import dataclasses

    d = dataclasses.replace(
        VC, materiais=tmp_path / "m", itens=tmp_path / "itens.json", indice=tmp_path / "indice.json"
    )
    disciplinas.construir(d, root=tmp_path)
    assert buscar("O que são as equações de Cauchy-Riemann?", d)[0] == "varcomp-nota-ia-cauchy-riemann"


def test_isolamento_com_calculo3_sinais_e_circuitos():
    """Nas duas direções: Cálculo 3, Sinais e Circuitos não trazem blocos de Variáveis Complexas, e vice-versa."""
    fronteira = [disciplinas.obter(i) for i in ("calc3", "sinais", "circ")]
    for p, _ in EXEMPLOS:
        for d in fronteira:
            assert not any(x.startswith("varcomp-") for x in buscar(p, d))
    for d in fronteira:
        for p in d.exemplos:
            assert all(x.startswith("varcomp-") for x in buscar(p))
            assert not any(x.startswith(("calc3-", "sinais-", "circ-")) for x in buscar(p))


# ---------------------------------------------------------------- KaTeX, catálogo e restrições

FORMULA = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


@pytest.mark.skipif(not shutil.which("node"), reason="node indisponível")
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for x in ITENS.values() for a, b in FORMULA.findall(x["texto"])]
    formulas += [a or b for a, b in FORMULA.findall(VC.rigor)]
    assert len(formulas) > 150
    katex = (ROOT / "backend/web/vendor/katex/katex.min.js").as_posix()
    script = (
        f"const k=require({json.dumps(katex)});const fs=require('fs');"
        "const erros=[];for(const f of JSON.parse(fs.readFileSync(0,'utf8'))){"
        "try{k.renderToString(f,{throwOnError:true})}catch(e){erros.push(f+' :: '+e.message)}}"
        "console.log(JSON.stringify(erros))"
    )
    r = subprocess.run(
        ["node", "-e", script], input=json.dumps(formulas), capture_output=True, text=True, encoding="utf-8", check=True
    )
    assert json.loads(r.stdout) == []


def test_catalogo_completo_e_coerente():
    obrigatorios = {
        "id",
        "nome",
        "autoria",
        "url",
        "idioma",
        "formato",
        "notacao",
        "topicos",
        "licenca",
        "acesso",
        "prioridade",
        "uso",
        "justificativa",
    }
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f["id"]
        assert f["prioridade"] in ("alta", "media", "referencia") and f["uso"] in ("acervo", "citada", "referencia")
        assert set(f["topicos"]) <= set(VC.assuntos), f["id"]
    assert {x for i_ in ITENS.values() for x in i_["fontes_catalogo"]} <= set(CATALOGO)
    assert {k for k, f in CATALOGO.items() if f["uso"] == "acervo"} == {"ufal-varcomp-prova1-2021", "ufal-varcomp-lista1"}
    for protegido in ("avila-variaveis-complexas", "churchill-variaveis-complexas"):
        assert CATALOGO[protegido]["uso"] == "referencia"


def test_provas_e_imagens_fora_do_repositorio():
    arquivos = [p for p in (ROOT / "disciplinas/varcomp").rglob("*") if p.is_file()]
    assert not [p for p in arquivos if p.suffix.lower() in (".pdf", ".png", ".jpg", ".jpeg", ".webp", ".docx", ".pptx")]
    rastreados = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
    assert not [
        l
        for l in rastreados.splitlines()
        if re.search(r"(prova ?variaveis|prova1[06])\.pdf$|WhatsApp Image 2021-04-03", l, re.I)
    ]


def test_documentacao_lista_fontes_e_blocos():
    curadoria = (ROOT / "disciplinas/varcomp/CURADORIA.md").read_text(encoding="utf-8")
    assert [k for k in CATALOGO if f"`{k}`" not in curadoria] == []
    assert [k for k in ITENS if f"`{k}`" not in curadoria] == []


# ---------------------------------------------------------------- lista 1 (4º período de EC, 24/11/2026)


def test_lista1_q2_partes_real_e_imaginaria():
    x, y = sp.symbols("x y", real=True)
    z, zc = x + I * y, x - I * y
    casos = [
        ((z - 4 * I) / (z + 3 * I), (x**2 + y**2 - y - 12) / (x**2 + (y + 3) ** 2), -7 * x / (x**2 + (y + 3) ** 2)),
        (
            (z - 3 * I * zc) / (z - I),
            (x**2 + y**2 - 6 * x * y + 3 * x - y) / (x**2 + (y - 1) ** 2),
            (-3 * x**2 + x + 3 * y**2 - 3 * y) / (x**2 + (y - 1) ** 2),
        ),
        (sp.exp(z) * (z - I), sp.exp(x) * (x * sp.cos(y) - (y - 1) * sp.sin(y)), sp.exp(x) * (x * sp.sin(y) + (y - 1) * sp.cos(y))),
    ]
    for w, u, v in casos:
        w = sp.expand_complex(w)
        assert sp.simplify(sp.re(w) - u) == 0 and sp.simplify(sp.im(w) - v) == 0
    assert "-7x" in ITENS["varcomp-lista1-q2-partes-u-v"]["texto"]


def test_lista1_q3_limites():
    z = sp.symbols("z")
    assert sp.limit((z**3 - 8 * I) / (z + 2 * I), z, -2 * I) == -12
    assert sp.limit(((1 + z) ** sp.Rational(1, 4) - 1) / z, z, 0) == sp.Rational(1, 4)
    assert sp.limit(((1 + z) ** sp.Rational(1, 3) - (1 - z) ** sp.Rational(1, 3)) / z, z, 0) == sp.Rational(2, 3)
    assert sp.expand((z + 2 * I) * (z**2 - 2 * I * z - 4)) == z**3 - 8 * I


def test_lista1_q6_q7_exponencial():
    assert sp.simplify(sp.exp(2 + 3 * sp.pi * I)) == sp.simplify(sp.exp(2 - 3 * sp.pi * I)) == -sp.exp(2)
    assert sp.simplify(sp.expand_complex(sp.exp((2 + sp.pi * I) / 4)) - sp.sqrt(sp.E) * sp.sqrt(2) / 2 * (1 + I)) == 0
    for k in range(-3, 4):
        assert sp.simplify(sp.exp(sp.log(2) + I * (sp.pi + 2 * k * sp.pi))) == -2
        assert sp.simplify(sp.expand_complex(sp.exp(sp.log(2) + I * (sp.pi / 3 + 2 * k * sp.pi))) - (1 + sp.sqrt(3) * I)) == 0
        assert sp.simplify(sp.exp(2 * (sp.Rational(1, 2) + k * sp.pi * I) - 1)) == 1
