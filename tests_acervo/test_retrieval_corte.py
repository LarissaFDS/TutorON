"""Corte de relevância e penalidade de hub na busca do acervo, com vetores sintéticos (sem bge-m3)."""
import json
import math

import pytest

from acervo.retrieval import hub_scores, search


def _norm(v):
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v]


BLOCOS = {
    # id: (texto, vetor)
    "mochila": ("Mochila 0/1: tabela de valor por item e capacidade.", [1, 0, 0]),
    "robo": ("Robô na matriz coleta moedas; a mochila não aparece aqui.", [0, 1, 0]),  # palavra em comum, vetor longe
    "hub": ("Potência a^n por divisão e conquista.", [1, 1, 1]),  # perto de todos
    "grafo": ("Caminho em DAG por ordenação topológica.", [0, 0, 1]),
}


@pytest.fixture
def acervo(tmp_path):
    itens = [{"id": i, "sha256": i, "confiabilidade": "media", "texto": t, "fonte_original": f"{i}.pdf",
              "tipo": "lista", "assunto": "x"} for i, (t, _) in BLOCOS.items()]
    (tmp_path / "02-acervo").mkdir()
    (tmp_path / "04-rag").mkdir()
    (tmp_path / "02-acervo/itens.json").write_text(json.dumps(itens), encoding="utf-8")
    indice = {"modo": "hibrido", "embedding_model": "bge-m3", "chunks": itens,
              "vectors": [_norm(v) for _, v in BLOCOS.values()]}
    (tmp_path / "04-rag/indice.json").write_text(json.dumps(indice), encoding="utf-8")
    return tmp_path


PERGUNTA = "Como montar a mochila 0/1?"
VETOR = _norm([0.9, 0.1, 0.42])  # parecido com "mochila"; o hub também parece parecido (0,82)


def ids(itens):
    return [i["id"] for i in itens]


def test_hub_tem_vizinhanca_mais_alta_que_os_outros():
    hubs = hub_scores([_norm(v) for _, v in BLOCOS.values()])
    assert max(range(4), key=hubs.__getitem__) == 2 and hubs[2] > 0
    # Relatório de 19/10: penalidade negativa aumentava a nota de blocos isolados. Agora só penaliza.
    assert min(hubs) == 0


def test_comportamento_antigo_sem_corte(acervo):
    # Sem min_similarity: qualquer palavra em comum passa (o "robô" entra só por "mochila").
    assert set(ids(search(PERGUNTA, root=acervo, vector=VETOR))) >= {"mochila", "robo", "hub"}


def test_corte_absoluto_tira_quem_so_tem_palavra_em_comum(acervo):
    achados = search(PERGUNTA, root=acervo, vector=VETOR, min_similarity=0.6)
    assert "robo" not in ids(achados) and ids(achados)[0] == "mochila"
    assert achados[0]["similaridade"] == pytest.approx(0.902, abs=0.01)


def test_penalidade_de_hub_tira_o_bloco_que_parece_com_tudo(acervo, monkeypatch):
    from acervo import retrieval
    monkeypatch.setattr(retrieval, "DESTAQUE_COM_PALAVRA", 0)  # isola o efeito da penalidade
    monkeypatch.setattr(retrieval, "DESTAQUE_SO_SEMANTICO", 0)
    sem = search(PERGUNTA, root=acervo, vector=VETOR, min_similarity=0.6)
    com = search(PERGUNTA, root=acervo, vector=VETOR, min_similarity=0.6, hub_penalty=True)
    assert "hub" in ids(sem) and ids(com) == ["mochila"]
    assert com[0]["similaridade_ajustada"] == com[0]["similaridade"]  # bloco comum não ganha bônus


def test_penalidade_de_hub_nunca_aumenta_a_similaridade(acervo):
    for item in search(PERGUNTA, root=acervo, vector=VETOR, min_similarity=0.0, hub_penalty=True, k=10):
        assert item["similaridade_ajustada"] <= item["similaridade"]


def test_nada_relevante_devolve_lista_vazia(acervo):
    longe = _norm([-1, -1, -1])
    assert search("pergunta sem relação nenhuma", root=acervo, vector=longe, min_similarity=0.5, hub_penalty=True) == []


def test_correspondencia_exata_continua_entrando_mesmo_abaixo_do_corte(acervo):
    itens = json.loads((acervo / "02-acervo/itens.json").read_text(encoding="utf-8"))
    itens[3]["texto"] = "Quantos asteriscos ASTERISCO(n) imprime?"
    for nome in ("02-acervo/itens.json",):
        (acervo / nome).write_text(json.dumps(itens), encoding="utf-8")
    indice = json.loads((acervo / "04-rag/indice.json").read_text(encoding="utf-8"))
    indice["chunks"] = itens
    (acervo / "04-rag/indice.json").write_text(json.dumps(indice), encoding="utf-8")
    achados = search("Quantos asteriscos imprime ASTERISCO?", root=acervo, vector=_norm([1, 0, 0]),
                     min_similarity=0.95, hub_penalty=True)
    assert "grafo" in ids(achados)


def test_busca_so_lexica_ignora_o_corte(acervo):
    achados = search(PERGUNTA, root=acervo, semantic=False, min_similarity=0.99, hub_penalty=True)
    assert {"mochila", "robo"} <= set(ids(achados)) and achados[0]["similaridade"] is None


def test_backend_passa_o_corte_da_configuracao(monkeypatch):
    import dataclasses

    from acervo import retrieval
    from backend import rag
    from backend.config import Settings

    chamadas = []
    monkeypatch.setattr(retrieval, "search", lambda *a, **kw: chamadas.append(kw) or [])
    rag._acervo("p", [0.1], Settings(acervo_min_similarity=0.62))
    rag._acervo("p", [0.1], dataclasses.replace(Settings(), acervo_min_similarity=-1, acervo_hub_penalty=False))
    rag._acervo("p", [0.1], Settings(acervo_min_similarity=-1))  # penalidade ligada, mas corte desligado
    assert chamadas[0]["min_similarity"] == 0.62 and chamadas[0]["hub_penalty"] is True
    assert chamadas[1]["min_similarity"] is None and chamadas[1]["hub_penalty"] is False
    assert chamadas[2]["min_similarity"] is None and chamadas[2]["hub_penalty"] is False


def test_indice_refeito_com_o_mesmo_mtime_nao_reusa_hub_antigo(acervo):
    import os

    caminho = acervo / "04-rag/indice.json"
    search(PERGUNTA, root=acervo, vector=VETOR, min_similarity=0.0, hub_penalty=True)
    mtime = caminho.stat().st_mtime_ns
    novo = {"id": "lis", "sha256": "lis", "confiabilidade": "media", "texto": "Mochila e LIS.",
            "fonte_original": "lis.pdf", "tipo": "lista", "assunto": "x"}
    for nome in ("02-acervo/itens.json", "04-rag/indice.json"):
        dados = json.loads((acervo / nome).read_text(encoding="utf-8"))
        if nome.startswith("04"):
            dados["chunks"].append(novo)
            dados["vectors"].append(_norm([0.95, 0.05, 0.3]))
        else:
            dados.append(novo)
        (acervo / nome).write_text(json.dumps(dados), encoding="utf-8")
    os.utime(caminho, ns=(mtime, mtime))  # sistemas de arquivo com mtime grosso
    assert "lis" in ids(search(PERGUNTA, root=acervo, vector=VETOR, min_similarity=0.0, hub_penalty=True))
