"""Material da equipe com `revisado: false` não entra na busca de produção; a matriz pode ligá-lo."""
import shutil
from pathlib import Path

import pytest

from acervo import equipe, retrieval
from acervo.common import digest, read_json, write_json
from backend.config import load_settings

ROOT = Path(__file__).resolve().parents[1]
PERGUNTA = "mochila 0/1 tabela de programação dinâmica capacidade"


@pytest.fixture
def acervo(tmp_path, monkeypatch):
    monkeypatch.delenv("ACERVO_USAR_NAO_REVISADOS", raising=False)
    (tmp_path / "02-acervo").mkdir()
    shutil.copytree(ROOT / equipe.PASTA, tmp_path / equipe.PASTA)
    texto = "Prova: mochila 0/1 com capacidade W; preencha a tabela de programação dinâmica."
    professor = {"id": "p01", "texto": texto, "sha256": digest(texto), "confiabilidade": "alta", "qualidade_ocr": "boa",
                 "assunto": "b2-04-programacao-dinamica", "segmentacao": "automatica", "fonte_original": "prova.pdf",
                 "tipo": "prova"}
    write_json(tmp_path / "02-acervo/itens.json", [professor])
    equipe.sincronizar(tmp_path)
    retrieval.build(root=tmp_path, embed=False)
    return tmp_path


def ids(root):
    return {r["id"] for r in retrieval.search(PERGUNTA, root=root, k=10, semantic=False)}


def test_producao_ignora_material_nao_revisado(acervo):
    achados = ids(acervo)
    assert "p01" in achados
    assert not achados & {"e01", "e02", "e03", "e04", "e05"}


@pytest.mark.parametrize("valor", ["1", "true", "sim"])
def test_variavel_inclui_nao_revisados_so_quando_ligada(acervo, monkeypatch, valor):
    monkeypatch.setenv("ACERVO_USAR_NAO_REVISADOS", valor)
    assert "e01" in ids(acervo)
    monkeypatch.setenv("ACERVO_USAR_NAO_REVISADOS", "0")
    assert "e01" not in ids(acervo)


def test_marcar_revisado_libera_sem_reindexar(acervo):
    arquivo = acervo / equipe.PASTA / "e01_pd_mochila_01.md"
    arquivo.write_text(arquivo.read_text(encoding="utf-8").replace("revisado: false", "revisado: true"),
                       encoding="utf-8")
    equipe.sincronizar(acervo)  # `python -m acervo equipe`; o sha256 é do corpo, então o índice continua válido
    assert "e01" in ids(acervo)
    assert "e02" not in ids(acervo)
    assert {i["id"]: i.get("revisado") for i in read_json(acervo / "02-acervo/itens.json", [])}["e01"] is True


def test_config_padrao_nao_usa_nao_revisados(monkeypatch):
    monkeypatch.delenv("ACERVO_USAR_NAO_REVISADOS", raising=False)
    assert load_settings().acervo_usar_nao_revisados is False
    monkeypatch.setenv("ACERVO_USAR_NAO_REVISADOS", "1")
    assert load_settings().acervo_usar_nao_revisados is True
