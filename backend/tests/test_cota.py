import time

from backend.cota import Cota, estimar_tokens


def test_cota_esgota_e_renova(tmp_path):
    c = Cota(tmp_path / "c.json", limite=100, janela_h=1)
    assert c.pode("a")
    c.cobrar("a", 120)
    assert not c.pode("a")
    assert c.pode("b")  # outro convidado não é afetado
    c._uso["a"]["inicio"] = time.time() - 3601  # passou a janela
    assert c.pode("a")


def test_dev_sem_limite(tmp_path):
    c = Cota(tmp_path / "c.json", limite=10, janela_h=1, chave_dev="segredo")
    assert c.eh_dev("segredo") and not c.eh_dev("errado") and not c.eh_dev(None)
    c.cobrar("d", 999, dev=True)
    assert c.pode("d", dev=True) and c.situacao("d")["usados"] == 0


def test_persistencia(tmp_path):
    Cota(tmp_path / "c.json", 100, 1).cobrar("a", 50)
    assert Cota(tmp_path / "c.json", 100, 1).situacao("a")["usados"] == 50


def test_estimativa():
    assert estimar_tokens("a" * 400, None) == 101


def test_relatorio_por_aluno(tmp_path):
    c = Cota(tmp_path / "c.json", limite=1000, janela_h=1)
    c.cobrar("a", 100, tipo="pergunta")
    c.cobrar("a", 50, tipo="resposta")
    c.cobrar("b", 1500, tipo="foto")
    c.cobrar("dev1", 10, dev=True, tipo="pergunta")
    r = {x["quem"]: x for x in c.relatorio()}
    assert r["a"]["tokens"] == 150 and r["a"]["perguntas"] == 1 and r["a"]["restantes_agora"] == 850
    assert r["b"]["fotos"] == 1 and r["dev1"]["dev"]
