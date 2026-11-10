"""Controle de qualidade do material de PD da equipe: cada recorrência é implementada aqui e
precisa reproduzir o rastreio escrito no .md e os exemplos do conjunto dourado (eval/perguntas.json)."""
import json
import shutil
from pathlib import Path

import pytest

from acervo import equipe
from acervo.common import read_json, write_json
from backend.rag import MAX_CHARS_TRECHO

ROOT = Path(__file__).resolve().parents[1]
PASTA = ROOT / equipe.PASTA


def texto(nome):
    return (PASTA / nome).read_text(encoding="utf-8")


def linha(rotulo, valores):
    return f"{rotulo} | " + " ".join(str(v) for v in valores)


# ---------------------------------------------------------------------- recorrências
def mochila(itens, W):
    V = [[0] * (W + 1)]
    for i, (w, v) in enumerate(itens, 1):
        V.append([max(V[i - 1][c], v + V[i - 1][c - w]) if w <= c else V[i - 1][c] for c in range(W + 1)])
    return V


def subset_sum(a, t):
    S = [[s == 0 for s in range(t + 1)]]
    for i, ai in enumerate(a, 1):
        S.append([S[i - 1][s] or (ai <= s and S[i - 1][s - ai]) for s in range(t + 1)])
    return S


def substring_comum(x, y):
    L = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            L[i][j] = L[i - 1][j - 1] + 1 if x[i - 1] == y[j - 1] else 0  # x_i = y_j em base 0
    return L


def troco(moedas, V):
    C, ultima = [0] + [float("inf")] * V, [None] * (V + 1)
    for v in range(1, V + 1):
        for d in moedas:
            if d <= v and C[v - d] + 1 < C[v]:
                C[v], ultima[v] = C[v - d] + 1, d
    return C, ultima


def robo(m):
    r, c = len(m), len(m[0])
    F = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            vizinhos = [F[i - 1][j]] * (i > 0) + [F[i][j - 1]] * (j > 0)
            F[i][j] = m[i][j] + max(vizinhos, default=0)
    return F


# ---------------------------------------------------------------------- conferência dos rastreios
def test_mochila_rastreio_confere():
    V = mochila([(1, 1), (3, 4), (4, 5)], 7)
    md = texto("e01_pd_mochila_01.md")
    for i, valores in enumerate(V):
        assert linha(str(i), valores) in md
    assert V[3][7] == 9


def test_subset_sum_rastreio_e_exemplo_do_conjunto_dourado():
    a, t = [3, 34, 4, 12, 5, 2], 9
    S = subset_sum(a, t)
    md = texto("e02_pd_subset_sum.md")
    assert linha("0", [int(x) for x in S[0]]) in md
    for i, ai in enumerate(a, 1):
        assert linha(f"{i} ({ai})", [int(x) for x in S[i]]) in md
    assert S[-1][t] is True  # A2: {3,34,4,12,5,2}, t=9 -> sim (4+5)
    assert subset_sum([3, 5], 4)[-1][4] is False


def test_substring_comum_rastreio_e_exemplo_do_conjunto_dourado():
    x, y = "ABABC", "BABCA"
    L = substring_comum(x, y)
    md = texto("e03_pd_substring_comum.md")
    for i, letra in enumerate(x, 1):
        assert linha(letra, L[i][1:]) in md
    assert max(map(max, L)) == 4 and L[5][4] == 4  # A3: ABABC/BABCA -> 4 (BABC)
    assert "x[i-1] = y[j-1]" in md and "base 0" in md


def test_troco_rastreio_e_exemplo_do_conjunto_dourado():
    C, ultima = troco([1, 3, 4], 6)
    md = texto("e04_pd_troco.md")
    assert linha("C[v]", C) in md
    assert linha("ultima[v]", ["-"] + ultima[1:]) in md
    assert C == [0, 1, 2, 1, 1, 2, 2]  # P3: moedas {1,3,4}, V=6


def test_robo_rastreio_confere():
    m = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0]]
    F = robo(m)
    md = texto("e05_pd_robo_matriz.md")
    for i, valores in enumerate(F, 1):
        assert linha(str(i), valores) in md
    assert F[-1][-1] == 3


# ---------------------------------------------------------------------- forma e integração
@pytest.mark.parametrize("caminho", sorted(PASTA.glob("*.md")), ids=lambda p: p.name)
def test_cada_arquivo_segue_o_padrao(caminho):
    meta, corpo, _ = equipe.ler(caminho)
    assert meta["revisado"] == "false" and "não é material do professor" in meta["autoria"]
    assert len(corpo) <= MAX_CHARS_TRECHO, "o RAG cortaria o fim do arquivo"
    for parte in ("Tabela:", "Recorrência", "Por que", "Pseudocódigo:", "Rastreio:", "Complexidade:"):
        assert parte in corpo, f"falta '{parte}'"
    assert "def " not in corpo and "for (" not in corpo  # pseudocódigo em português, sem linguagem


def test_atribuir_ao_professor_e_recusado(tmp_path):
    arquivo = tmp_path / "x.md"
    arquivo.write_text("---\nid: x\ntitulo: t\nassunto: a\nautoria: Professor da disciplina\nrevisado: false\n---\ntexto")
    with pytest.raises(ValueError):
        equipe.ler(arquivo)


def test_sincronizar_e_idempotente_e_preserva_o_resto(tmp_path):
    (tmp_path / "02-acervo").mkdir()
    shutil.copytree(PASTA, tmp_path / equipe.PASTA)
    write_json(tmp_path / "02-acervo/itens.json", [{"id": "c01", "texto": "outro", "origem": None}])
    equipe.sincronizar(tmp_path)
    itens = equipe.sincronizar(tmp_path)
    assert [i["id"] for i in itens] == ["c01", "e01", "e02", "e03", "e04", "e05"]
    novos = [i for i in itens if i.get("origem") == "equipe"]
    assert all(i["revisado"] is False and i["confiabilidade"] == "media" and i["tipo"] == "material_equipe"
               for i in novos)
    assert read_json(tmp_path / "02-acervo/itens.json", []) == json.loads(json.dumps(itens))
