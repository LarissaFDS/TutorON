"""Preparação do treino com todas as disciplinas (scripts/gerar_casos_acervo.py), sem chamar modelo."""
import asyncio
import json

from scripts import gerar_casos_acervo as g

CASO = {"pergunta": "Me dá a resposta do exercício 2?", "tema": "pipeline e hazards",
        "conceito": "Um hazard de dados aparece quando uma instrução precisa de um valor ainda não escrito.",
        "pista": "Marque, ciclo a ciclo, em que estágio cada instrução escreve e lê o registrador.",
        "perguntas": "Em que estágio o valor fica pronto? Em que estágio a próxima instrução precisa dele?",
        "exemplo": "Com duas instruções independentes, nenhuma espera: compare com o caso em que a segunda lê x5.",
        "visual": "Desenhe uma tabela com os ciclos nas colunas e as instruções nas linhas, deixando as bolhas em branco.",
        "tentativa": "Coloquei a segunda instrução logo no ciclo seguinte, sem bolhas.",
        "conferir": "A ordem dos estágios está certa. Revise em que ciclo o valor de x5 fica disponível.",
        "tarefa": "Em que ciclo a segunda instrução pode ler x5?"}


def test_caso_valido_e_resposta_entregue_e_recusada():
    assert g.valido(CASO) is None
    assert g.valido({**CASO, "pista": ""}) == "campo pista ausente ou curto"
    assert g.extrair_json("<think>x</think> ok ```json\n" + json.dumps(CASO) + "\n```") == CASO


def test_divisao_estavel_cobre_validacao_e_teste_por_disciplina():
    casos = [{"id": f"oac-acervo-{i}", "disciplina": "oac", "split": "treino"} for i in range(5)]
    g.equilibrar(casos)
    assert {c["split"] for c in casos} == {"treino", "validacao", "teste"}
    assert g.split_de("x") == g.split_de("x")


def test_geracao_retomavel_com_professor_falso(tmp_path, monkeypatch):
    monkeypatch.setattr(g, "PASTA", tmp_path)
    chamadas = []

    class Resultado:
        def __init__(self):
            self.text = json.dumps(CASO)
            self.model = type("M", (), {"key": "falso"})()

    class Professor:
        def __init__(self, *_):
            pass

        async def complete(self, sistema, pedido):
            chamadas.append(pedido)
            return Resultado()

    import backend.llm
    monkeypatch.setattr(backend.llm, "LLM", Professor)
    resumo = asyncio.run(g.gerar(["oac"], maximo=3))
    assert resumo["oac"]["novos"] == 3 and len(chamadas) == 3
    assert asyncio.run(g.gerar(["oac"], maximo=3))["oac"]["novos"] == 3  # só os blocos que faltam
    assert len(g.carregar("oac")) == 6
    casos = [c for c in g.todos_os_casos() if c["disciplina"] == "oac"]
    assert len(casos) == 6 and all("origem" not in c for c in casos)
