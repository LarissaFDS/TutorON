"""Acervo de Computação Gráfica (Ciência da Computação) e conferência das contas com NumPy.

Os blocos parafraseiam as aulas, os exercícios e as provas do Prof. Marcelo Costa Oliveira (IC-UFAL).
Matrizes, rasterização, recorte, cores, iluminação e textura são refeitos aqui.
"""

import colorsys
import math
import re

import numpy as np
import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

CG = disciplinas.obter("cg")
PASTA = ROOT / "disciplinas/cg"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(CG.itens)}
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "cg")
FRONTEIRA = ("ga", "sinais", "ia")
TEXTO = " ".join(i["texto"] for i in TODOS.values())


def buscar(pergunta, d=CG):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def bloco(prefixo):
    return next(i["texto"] for k, i in TODOS.items() if k.startswith(prefixo))


# ---------------------------------------------------------------- cadastro e acervo


def test_cg_cadastrada_com_acervo_proprio():
    assert CG.nome == "Computação Gráfica" and CG.itens.exists()
    ids = {c["id"] for c in read_json(CG.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({CG.itens, CG.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert {i["assunto"] for i in TODOS.values()} == set(CG.assuntos)
    assert ids == set(TODOS)


def test_situacao_da_disciplina():
    assert CG.situacao == "MVP" and not CG.em_validacao and not CG.aviso


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas cg --embeddings`."""
    assert disciplinas.registros(CG) == read_json(CG.itens)


def test_blocos_sao_material_revisavel_com_fonte_e_teste():
    for i in TODOS.values():
        t = i["texto"]
        assert i["natureza"] == "material_da_disciplina", i["id"]
        assert i["status_curadoria"] == "aprovado", i["id"]
        assert len(t) <= 2800, i["id"]
        ultima = t.strip().splitlines()[-1]
        assert "**Verificação:**" in ultima, i["id"]
        assert "não é gabarito do professor" in t and "Status da resolução:" in t, i["id"]
        nomes = re.findall(r"`(test_\w+)`", ultima)
        assert nomes, i["id"]
        for nome in nomes:
            assert nome in globals(), (i["id"], nome)
    for arq in (PASTA / "materiais").glob("*.md"):
        cab = arq.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, arq.name
        for f in re.search(r"fontes_catalogo: (.+)", cab).group(1).split(","):
            assert f.strip() in CATALOGO, (arq.name, f)


def test_sem_dados_pessoais_livro_nem_binarios():
    textos = TEXTO + (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+", textos)
    assert not re.search(r"matr[ií]cula:? *\d", textos, re.I)
    for nome in ("Luiz Felipe", "Harnon", "Luciano"):  # alunos e autores citados nas cópias
        assert nome not in textos
    for f in FONTES:
        assert f["arquivo_local"] is None, f["id"]
        if f["licenca"].startswith("Protegido"):
            assert f["uso"] == "referencia", f["id"]
    soltos = [p for p in PASTA.rglob("*") if p.suffix.lower() in (".pdf", ".docx", ".ppt", ".pptx", ".png", ".jpg", ".jpeg")]
    assert not soltos
    for livro in ("*Azevedo*Conci*", "*Hearn*Baker*", "*SuperBible*", "*creative-3-d*"):
        assert not list(ROOT.rglob(livro)), livro


PERGUNTAS = [
    ("Qual o espaço em memória ocupado pelo frame buffer?", "cg-fundamentos"),
    ("Quantas posições tem a tabela de cores LUT?", "cg-fundamentos"),
    ("Como funciona o algoritmo de Bresenham para retas?", "cg-rasterizacao-de-retas"),
    ("O que é aliasing e quais os métodos de antialiasing?", "cg-aliasing"),
    ("Como compor matrizes de translação e rotação em coordenadas homogêneas?", "cg-transformacoes-2d"),
    ("Rotação em torno de um ponto qualquer", "cg-transformacoes-2d"),
    ("Qual a diferença entre projeção ortográfica e perspectiva?", "cg-transformacoes-3d"),
    ("O que são pontos de fuga e anomalias perspectivas?", "cg-transformacoes-3d"),
    ("Como funciona o recorte de Cohen-Sutherland com códigos de 4 bits?", "cg-recorte-de-retas"),
    ("Recorte de polígonos pelo algoritmo de Sutherland-Hodgman", "cg-recorte-de-poligonos"),
    ("Compare os sistemas de cores RGB e HSV", "cg-cores"),
    ("O que é quantização de níveis de cinza?", "cg-cores"),
    ("Como funciona a octree e a quadtree?", "cg-modelagem"),
    ("Qual a diferença entre reflexão difusa e especular?", "cg-iluminacao-local"),
    ("Vantagens do sombreamento de Gouraud em relação ao flat", "cg-sombreamento"),
    ("O que é ray tracing e a árvore de raios?", "cg-iluminacao-global"),
    ("Como se calcula o fator de forma na radiosidade?", "cg-iluminacao-global"),
    ("Quais os passos do mapeamento de textura?", "cg-mapeamento-de-textura"),
    ("O que é bump mapping?", "cg-mapeamento-de-textura"),
]


@pytest.mark.parametrize(("pergunta", "esperado"), PERGUNTAS)
def test_perguntas_acham_o_bloco_certo(pergunta, esperado):
    achados = buscar(pergunta)[:3]
    assert any(a.startswith(esperado) for a in achados), achados


def test_fronteiras_nos_dois_sentidos():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert {c["id"] for c in read_json(d.indice)["chunks"]}.isdisjoint(TODOS)
        assert set(buscar("Como funciona o algoritmo de Bresenham para retas?", d)).isdisjoint(TODOS)
    assert not buscar("Como calcular a impedância de um indutor?")
    assert not buscar("Me conte uma piada")


# ---------------------------------------------------------------- conferências


def test_frame_buffer_e_lut():
    bits = 20 * 20 * 8
    assert bits == 3200 and bits // 8 == 400
    assert 2**8 == 256 and math.ceil(math.log2(64)) == 6
    lado = 512 / 256
    assert lado == 2 and 13 * lado * lado == 52
    assert (100 / 400, 300 / 500) == (0.25, 0.6)
    t = bloco("cg-fundamentos")
    assert "3200" in t and "400" in t and "52 mm²" in t


def bresenham(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    p, pts, y = 2 * dy - dx, [], y1
    for x in range(x1, x2 + 1):
        pts.append((x, y))
        if p < 0:
            p += 2 * dy
        else:
            y, p = y + 1, p + 2 * (dy - dx)
    return pts


def test_bresenham():
    pts = bresenham(1, 1, 8, 5)
    assert pts == [(1, 1), (2, 2), (3, 2), (4, 3), (5, 3), (6, 4), (7, 4), (8, 5)]
    for x, y in pts:
        ideal = 1 + 4 / 7 * (x - 1)
        assert abs(y - ideal) <= 0.5 + 1e-9
    t = bloco("cg-rasterizacao")
    assert "(1,1), (2,2), (3,2), (4,3), (5,3), (6,4), (7,4), (8,5)" in t


def test_supersampling():
    # reta y = x/2 passando por um pixel dividido em 3 x 3 subpixels; conta os subpixels cortados
    cortados = sum(1 for i in range(3) for j in range(3) if j / 3 <= (i + 0.5) / 3 / 2 < (j + 1) / 3)
    assert 1 <= cortados <= 3
    mascara = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    assert mascara.sum() == 16
    cobertura = np.array([[0, 0, 0], [1, 1, 0], [1, 1, 1]])
    assert 0 < (mascara * cobertura).sum() / 16 < 1
    assert "soma 16" in bloco("cg-aliasing")


def T(dx, dy):
    return np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]], float)


def R(graus):
    c, s = math.cos(math.radians(graus)), math.sin(math.radians(graus))
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def S(sx, sy):
    return np.diag([sx, sy, 1.0])


def test_composicao_2d():
    ponto = np.array([1, 0, 1.0])
    ma = R(45) @ T(4, -2)
    assert np.allclose(ma @ ponto, R(45) @ (T(4, -2) @ ponto))
    assert not np.allclose(R(45) @ T(4, -2), T(4, -2) @ R(45))  # ordem importa
    mb = S(2, 4) @ T(4, 5) @ R(30) @ T(-4, -5)
    assert np.allclose(mb @ [4, 5, 1], [8, 20, 1])  # P é fixo pela rotação e só sofre a escala
    mc = S(3, 3) @ T(1, 0) @ S(-1, 1) @ T(-1, 0)
    assert np.allclose(mc @ [1, 3, 1], [3, 9, 1])
    for x, y in ((0, 0), (5, 2)):
        assert np.allclose(mc @ [x, y, 1], [3 * (2 - x), 3 * y, 1])
    t = bloco("cg-transformacoes-2d")
    assert "$M = R(45°)\\,T(4,-2)$" in t and "$(3, 9)$" in t


def _rot3(eixo, graus):
    c, s = math.cos(math.radians(graus)), math.sin(math.radians(graus))
    m = {
        "x": [[1, 0, 0], [0, c, -s], [0, s, c]],
        "y": [[c, 0, s], [0, 1, 0], [-s, 0, c]],
        "z": [[c, -s, 0], [s, c, 0], [0, 0, 1]],
    }[eixo]
    return np.array(m)


def test_rotacoes_e_perspectiva():
    for e in "xyz":
        r = _rot3(e, 37)
        assert np.allclose(r @ r.T, np.eye(3)) and math.isclose(np.linalg.det(r), 1)
    assert np.allclose(_rot3("x", 90) @ [0, 1, 0], [0, 0, 1])
    assert np.allclose(_rot3("y", 90) @ [0, 0, 1], [1, 0, 0])  # regra da mão direita
    d = 1.0

    def proj(x, y, z):
        return d * x / z, d * y / z

    assert proj(2, 2, 4) == tuple(v / 2 for v in proj(2, 2, 2))


DENTRO, ESQ, DIR, BAIXO, CIMA = 0, 1, 2, 4, 8


def _codigo(x, y, xmin, ymin, xmax, ymax):
    c = DENTRO
    c |= ESQ if x < xmin else DIR if x > xmax else 0
    c |= BAIXO if y < ymin else CIMA if y > ymax else 0
    return c


def _bits(c):
    """Ordem do material: acima, abaixo, direita, esquerda."""
    return "".join("1" if c & b else "0" for b in (CIMA, BAIXO, DIR, ESQ))


def cohen_sutherland(x1, y1, x2, y2, xmin=0, ymin=0, xmax=20, ymax=20):
    c1, c2 = _codigo(x1, y1, xmin, ymin, xmax, ymax), _codigo(x2, y2, xmin, ymin, xmax, ymax)
    while True:
        if not (c1 | c2):
            return (x1, y1, x2, y2)
        if c1 & c2:
            return None
        c = c1 or c2
        if c & CIMA:
            x, y = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1), ymax
        elif c & BAIXO:
            x, y = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1), ymin
        elif c & DIR:
            x, y = xmax, y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
        else:
            x, y = xmin, y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
        if c == c1:
            x1, y1, c1 = x, y, _codigo(x, y, xmin, ymin, xmax, ymax)
        else:
            x2, y2, c2 = x, y, _codigo(x, y, xmin, ymin, xmax, ymax)


def test_cohen_sutherland():
    assert _bits(_codigo(30, 50, 0, 0, 20, 20)) == "1010" and _bits(_codigo(10, 10, 0, 0, 20, 20)) == "0000"
    assert cohen_sutherland(30, 50, 10, 10) == (15, 20, 10, 10)
    assert cohen_sutherland(25, 25, 30, 30) is None
    t = bloco("cg-recorte-de-retas")
    assert "$C = (15, 20)$" in t and "1010" in t


def sutherland_hodgman(poligono, xmin, ymin, xmax, ymax):
    bordas = [
        (lambda p: p[0] >= xmin, lambda s, e: (xmin, s[1] + (e[1] - s[1]) * (xmin - s[0]) / (e[0] - s[0]))),
        (lambda p: p[0] <= xmax, lambda s, e: (xmax, s[1] + (e[1] - s[1]) * (xmax - s[0]) / (e[0] - s[0]))),
        (lambda p: p[1] >= ymin, lambda s, e: (s[0] + (e[0] - s[0]) * (ymin - s[1]) / (e[1] - s[1]), ymin)),
        (lambda p: p[1] <= ymax, lambda s, e: (s[0] + (e[0] - s[0]) * (ymax - s[1]) / (e[1] - s[1]), ymax)),
    ]
    saida = list(poligono)
    for dentro, corte in bordas:
        entrada, saida = saida, []
        for k, p in enumerate(entrada):
            s = entrada[k - 1]  # lista circular: (vn, v1), (v1, v2), ...
            if dentro(p):
                if not dentro(s):
                    saida.append(corte(s, p))
                saida.append(p)
            elif dentro(s):
                saida.append(corte(s, p))
    return saida


def test_sutherland_hodgman():
    res = sutherland_hodgman([(-5, 5), (15, 5), (5, 15)], 0, 0, 10, 10)
    assert {tuple(map(float, v)) for v in res} == {(0.0, 5.0), (10.0, 5.0), (10.0, 10.0), (0.0, 10.0)}
    assert all(0 <= x <= 10 and 0 <= y <= 10 for x, y in res)
    t = bloco("cg-recorte-de-poligonos")
    assert "$(0,5)$, $(10,5)$, $(10,10)$, $(0,10)$" in t and "$\\{3,1\\}$" in t


def test_cores():
    assert colorsys.rgb_to_hsv(1, 0, 0) == (0.0, 1.0, 1)
    assert math.isclose(colorsys.rgb_to_hsv(0, 1, 0)[0] * 360, 120)
    assert math.isclose(colorsys.rgb_to_hsv(0, 0, 1)[0] * 360, 240)
    assert colorsys.rgb_to_hsv(0.5, 0.5, 0.5)[1] == 0  # cinza não tem saturação
    rgb = np.array([0.2, 0.6, 1.0])
    assert np.allclose(1 - rgb, [0.8, 0.4, 0.0])
    assert math.log2(256) == 8 and math.log2(4) == 2
    t = bloco("cg-cores")
    assert "**quantização**" in t and "alternativa (b)" in t


def _quadtree(img, x=0, y=0, n=None, prof=0, folhas=None):
    n = n or len(img)
    folhas = [] if folhas is None else folhas
    bloco_ = [img[i][j] for i in range(y, y + n) for j in range(x, x + n)]
    if all(bloco_):
        folhas.append(("cheio", prof))
    elif not any(bloco_):
        folhas.append(("vazio", prof))
    else:
        h = n // 2
        for dy, dx in ((0, 0), (0, h), (h, 0), (h, h)):
            _quadtree(img, x + dx, y + dy, h, prof + 1, folhas)
    return folhas


def test_quadtree():
    img = [[1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1]]
    folhas = _quadtree(img)
    assert ("cheio", 1) in folhas and ("vazio", 1) in folhas
    assert max(p for _, p in folhas) == 2 == int(math.log2(len(img)))
    assert "**parcial**" in bloco("cg-modelagem")


def _unit(v):
    v = np.asarray(v, float)
    return v / np.linalg.norm(v)


def _phong(n, l, v, ka=0.1, ia=1.0, kd=0.7, ks=0.5, il=1.0, expo=10):
    n, l, v = map(_unit, (n, l, v))
    r = 2 * n.dot(l) * n - l
    return ka * ia, il * kd * max(n.dot(l), 0), il * ks * max(r.dot(v), 0) ** expo


def test_phong():
    n, luz = [0, 0, 1], [0, 1, 1]
    a1, d1, s1 = _phong(n, luz, [0, -1, 1])
    a2, d2, s2 = _phong(n, luz, [1, 0, 1])
    assert d1 == d2 and s1 != s2  # difusa não depende do observador; especular depende
    assert math.isclose(d1, 0.7 * math.cos(math.radians(45)))
    assert _phong(n, luz, [0, -0.9, 1], expo=50)[2] < _phong(n, luz, [0, -0.9, 1], expo=5)[2]
    t = bloco("cg-iluminacao-local")
    assert "**não depende do observador**" in t and "**depende da posição do observador**" in t


def test_gouraud_phong():
    luz, obs = _unit([0, 0, 1]), _unit([0, 0, 1])
    n0, n1 = _unit([-1, 0, 1]), _unit([1, 0, 1])

    def especular(n):
        n = _unit(n)
        r = 2 * n.dot(luz) * n - luz
        return max(r.dot(obs), 0) ** 20

    ts = np.linspace(0, 1, 11)
    gouraud = [(1 - t) * especular(n0) + t * especular(n1) for t in ts]
    phong = [especular((1 - t) * n0 + t * n1) for t in ts]
    assert max(gouraud) < 0.01 and math.isclose(max(phong), 1.0)
    t = bloco("cg-sombreamento")
    assert "**I e III**" in t and "(B)" in t


def test_radiosidade_e_reflexao():
    a1, a2, f12 = 2.0, 1.0, 0.25
    f21 = a1 * f12 / a2
    assert math.isclose(a1 * f12, a2 * f21)
    e, rho = np.array([1.0, 0.0]), np.array([0.5, 0.8])
    f = np.array([[0, f12], [f21, 0]])
    b = np.linalg.solve(np.eye(2) - rho[:, None] * f, e)
    assert np.allclose(b, e + rho * (f @ b)) and b[1] > 0
    d, n = _unit([1, -1, 0]), np.array([0, 1.0, 0])
    assert np.allclose(d - 2 * d.dot(n) * n, _unit([1, 1, 0]))
    t = bloco("cg-iluminacao-global")
    assert "$A_i F_{ij} = A_j F_{ji}$" in t


def test_textura():
    tex = np.array([[0.0, 1.0], [1.0, 0.0]])

    def bilinear(s, t):
        x, y = s * (tex.shape[1] - 1), t * (tex.shape[0] - 1)
        x0, y0 = int(x), int(y)
        x1, y1 = min(x0 + 1, 1), min(y0 + 1, 1)
        fx, fy = x - x0, y - y0
        topo = (1 - fx) * tex[y0, x0] + fx * tex[y0, x1]
        base = (1 - fx) * tex[y1, x0] + fx * tex[y1, x1]
        return (1 - fy) * topo + fy * base

    assert bilinear(0.5, 0.5) == 0.5 and bilinear(0, 0) == 0.0 and bilinear(1, 0) == 1.0
    t = bloco("cg-mapeamento")
    assert "**bump mapping:**" in t and "(C)" in t
