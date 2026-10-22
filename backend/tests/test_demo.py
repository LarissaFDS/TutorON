"""Página /demo: respostas reais gravadas do tutor socrático, sem IA. Garante que ela existe,
que todos os arquivos estão no lugar e que nenhuma resposta da vitrine entrega a solução."""
import json

import pytest

from backend import animacao, prompts, seguranca
from backend.main import WEB
from backend.tests.test_disciplinas import site  # noqa: F401

DEMO = json.loads((WEB / "demo" / "demo.json").read_text(encoding="utf-8"))
RESPOSTAS = [c["texto"] for c in DEMO["ajudas"]] + [r["texto"] for r in DEMO["ciclo"]["rodadas"]]


def test_demo_carrega_sem_chamar_ia(site):  # noqa: F811
    assert "não dá a resposta" in site.get("/demo").text
    assert site.get("/static/demo.js").status_code == 200
    assert site.get("/static/demo/demo.json").json() == DEMO
    for arquivo in [DEMO["ciclo"]["foto"]] + [v["arquivo"] for v in DEMO["animacoes"]]:
        r = site.get(f"/static/demo/{arquivo}")
        assert r.status_code == 200 and len(r.content) > 10_000
    assert site.llm.chamadas == []
    assert 'href="/demo"' in site.get("/").text


def test_demo_cobre_todos_os_tipos_de_ajuda_e_as_duas_disciplinas():
    tipos = {c["ajuda"] for c in DEMO["ajudas"]} | {r["ajuda"] for r in DEMO["ciclo"]["rodadas"]}
    assert set(prompts.AJUDAS) <= tipos
    assert {c["disciplina"] for c in DEMO["ajudas"]} == {"PAA", "SD"}
    assert len(DEMO["ciclo"]["rodadas"]) >= 3
    assert len({r["ajuda"] for r in DEMO["ciclo"]["rodadas"]}) == len(DEMO["ciclo"]["rodadas"])  # cada rodada muda a forma


@pytest.mark.parametrize("texto", RESPOSTAS)
def test_nenhuma_resposta_da_demo_entrega_a_solucao(texto):
    assert not seguranca.entrega_resposta(texto)
    assert "### Sua vez" in texto


def test_roteiros_das_animacoes_sao_validos_e_param_antes_da_resposta():
    for v in DEMO["animacoes"]:
        r = animacao.roteiro_valido(v["roteiro"])
        assert r["pergunta_final"] and r["pergunta_final"] == v["pergunta_final"]
    assert {v["modelo_cena"] for v in DEMO["animacoes"]} == {"arvore_recursao", "tabela", "grafo"}


def test_html_offline_esta_atualizado_e_nao_depende_de_servidor():
    """demo-offline/TutorON-demo.html: arquivo único para apresentar sem servidor nem internet.
    Se este teste falhar, gere de novo: python scripts/demo_offline.py"""
    import re
    from backend.main import WEB as web
    html = (web.parents[1] / "demo-offline" / "TutorON-demo.html").read_text(encoding="utf-8")
    embutido = json.loads(re.search(r"window\.TUTORON_DEMO = (\{.*?\});\n", html).group(1))
    assert embutido == DEMO
    assert 'src="/' not in html and 'href="/' not in html and "url(fonts/" not in html
    for v in DEMO["animacoes"]:
        for nome in (v["arquivo"], v["arquivo"].replace(".mp4", ".webm"), v["arquivo"].replace(".mp4", ".png")):
            assert f'"{nome}": "data:' in html
