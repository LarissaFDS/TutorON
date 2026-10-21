"""Uma IA, vários acervos: o fluxo real do site (API -> busca no acervo -> prompt -> IA),
com o acervo de verdade e uma IA falsa que registra o que recebeu."""
import asyncio
import hashlib
import json

import pytest
from fastapi.testclient import TestClient

from acervo import disciplinas
from backend import prompts, rag
from backend.tests.test_api import _sleep_curto, esperar
from backend.tests.test_llm import FakeLLM, settings
from backend import tarefas

# SHA-256 do prompt de PAA antes do cadastro de disciplinas (commit 29ce773): PAA não pode mudar.
PROMPT_PAA_ORIGINAL = "d83b5fc5b9ea78fa605e1d29bc87a2d11979b9f02c28cfa9e7be709127def749"
# Única linha acrescentada ao rigor de PAA depois do teste de 19/10 (mochila sem casos base).
LINHA_PD = ("\n- Em programação dinâmica, defina o subproblema, os casos base, a recorrência com todas as "
            "condições (ex.: na mochila 0/1, só considerar o item i quando wᵢ ≤ w) e a ordem de preenchimento da tabela.")


async def sem_embedding(texto):
    return None  # sem Ollama nos testes: busca léxica, como quando o bge-m3 está desligado


@pytest.fixture
def site(tmp_path, monkeypatch):
    """Site completo com o RAG real. Só a IA é falsa: guarda (modelo, sistema, prompt) de cada chamada."""
    from backend import main

    monkeypatch.setattr(tarefas.asyncio, "sleep", _sleep_curto)
    llm = FakeLLM({"g1": ("ok", "resposta do tutor")})
    # Sem liberação explícita: SD está em beta, disponível no atendimento normal.
    llm.settings = llm.settings.__class__(**{**llm.settings.__dict__, "data_dir": tmp_path})
    llm.embed = sem_embedding
    llm.chamadas = []
    original = llm._provider

    def provedor(model, system, prompt):
        llm.chamadas.append((model, system, prompt))
        return original(model, system, prompt)
    llm._provider = provedor
    with TestClient(main.create_app(settings=llm.settings, llm=llm, warm_up=False)) as c:
        c.llm, c.tmp = llm, tmp_path
        yield c


def perguntar(c, pergunta, disciplina=None):
    corpo = {"pergunta": pergunta} | ({"disciplina": disciplina} if disciplina else {})
    return esperar(c, c.post("/api/perguntar", json=corpo).json())


def ids_paa():
    return {i["id"] for i in json.loads(disciplinas.obter("paa").indice.read_text(encoding="utf-8"))["chunks"]}


def ids_sd():
    return {i["id"] for i in json.loads(disciplinas.obter("sd").indice.read_text(encoding="utf-8"))["chunks"]}


# ---------------------------------------------------------------- PAA preservado

def test_prompt_de_paa_identico_ao_do_mvp():
    """O cadastro de disciplinas não mudou o prompt de PAA. Depois do teste de 19/10, o prompt ganhou
    seções novas (instruções internas, citações, outra disciplina); o texto do MVP continua dentro
    dele sem alteração: backend/tests/test_seguranca.py::test_prompt_novo_so_acrescenta_secoes_ao_de_paa."""
    anterior = prompts.SISTEMA_TUTOR_ANTERIOR.replace(LINHA_PD, "")
    assert hashlib.sha256(anterior.encode()).hexdigest() == PROMPT_PAA_ORIGINAL
    assert prompts.sistema_tutor() == prompts.sistema_tutor(disciplinas.obter("paa")) == prompts.SISTEMA_TUTOR


def test_sem_disciplina_continua_respondendo_com_paa(site):
    t = perguntar(site, "Como aplicar o Teorema Mestre em T(n) = 2T(n/2) + n?")
    assert t["status"] == "pronta"
    _, sistema, prompt = site.llm.chamadas[-1]
    assert sistema == prompts.SISTEMA_TUTOR
    assert t["fontes"] and all(f["titulo"].endswith("de PAA") for f in t["fontes"])
    linha = json.loads((site.tmp / "perguntas.jsonl").read_text(encoding="utf-8").splitlines()[-1])
    assert linha["disciplina"] == "paa"


# ---------------------------------------------------------------- SD usa o próprio acervo

def test_pergunta_de_sd_usa_material_de_sd(site):
    t = perguntar(site, "Como simplificar com mapa de Karnaugh usando irrelevâncias?", "sd")
    assert t["status"] == "pronta" and t["fontes"]
    assert all(f["titulo"].endswith("de SD") for f in t["fontes"])
    _, sistema, prompt = site.llm.chamadas[-1]
    assert "Sistemas Digitais (SD)" in sistema and "Teorema Mestre" not in sistema
    assert "Mapa de Karnaugh" in prompt  # o trecho recuperado chegou ao prompt da IA
    linha = json.loads((site.tmp / "perguntas.jsonl").read_text(encoding="utf-8").splitlines()[-1])
    assert linha["disciplina"] == "sd"


def test_acervos_nao_se_misturam():
    """Mesmas perguntas nas duas disciplinas: cada uma só devolve blocos do próprio acervo,
    mesmo com palavras em comum (algoritmo, prova, complexidade, soma…)."""
    llm = FakeLLM({})
    llm.embed = sem_embedding
    perguntas = ["Qual a complexidade de um somador de n bits?", "Explique a prova da questão 2",
                 "Como montar a recorrência da mochila 0/1?", "Como simplificar com mapa de Karnaugh?",
                 "Soma de dois números e algoritmo de Fibonacci"]

    async def buscar(d):
        vistos = set()
        for p in perguntas:
            trechos = await rag.recuperar(p, llm, llm.settings, disciplinas.obter(d))
            vistos |= {t.titulo for t in trechos}
        return vistos

    assert asyncio.run(buscar("paa")) <= {f"{t} de PAA" for t in rag.TIPOS.values()} | {"Material da disciplina de PAA"}
    assert asyncio.run(buscar("sd")) <= ({f"{t} de SD" for t in rag.TIPOS.values()}
                                         | {"Material da disciplina de SD", f"{rag.NOTA_EQUIPE} de SD"})
    assert ids_paa().isdisjoint(ids_sd())


def test_livro_de_paa_no_supabase_nao_entra_em_sd():
    chamadas = []

    class Cliente:
        async def post(self, url, **kw):
            chamadas.append(url)
            raise AssertionError("SD não pode consultar o livro de PAA")

    llm = FakeLLM({})
    llm.client = Cliente()

    async def vetor(texto):
        return [0.0] * 1024
    llm.embed = vetor
    config = settings(supabase_url="https://exemplo.supabase.co", supabase_key="k")
    asyncio.run(rag.recuperar("Como funciona um flip-flop D?", llm, config, disciplinas.obter("sd")))
    assert chamadas == []
    trechos = asyncio.run(rag.recuperar("Teorema Mestre", llm, config, disciplinas.obter("paa")))
    assert chamadas and all(t.origem == "acervo" for t in trechos)  # PAA ainda tenta o livro (aqui, fora do ar)


def test_sem_material_relevante_o_tutor_recebe_aviso_e_nenhuma_fonte(site):
    t = perguntar(site, "Explique a heurística de Dijkstra para grafos esparsos", "sd")
    assert t["status"] == "pronta" and t["fontes"] == []
    _, _, prompt = site.llm.chamadas[-1]
    assert "Nenhum trecho do material foi encontrado para esta pergunta." in prompt
    assert "[P1]" not in prompt  # nenhum rótulo para a IA citar


# ---------------------------------------------------------------- a IA é a mesma

def test_mesma_ia_para_as_duas_disciplinas(site):
    perguntar(site, "Teorema Mestre para T(n) = 2T(n/2) + n", "paa")
    perguntar(site, "Complemento de 2 de 101010", "sd")
    (modelo_paa, sistema_paa, _), (modelo_sd, sistema_sd, _) = site.llm.chamadas[-2:]
    assert modelo_paa == modelo_sd  # mesma cascata de modelos, mesmo serviço
    # O prompt de sistema é o mesmo texto do tutor; só mudam o nome da disciplina e as regras de rigor.
    paa, sd = disciplinas.obter("paa"), disciplinas.obter("sd")
    comum = lambda s, d: (s.replace(prompts._outras(d), "").replace(d.rigor, "").replace(d.nome, "")
                          .replace(d.sigla, ""))
    assert comum(sistema_paa, paa) == comum(sistema_sd, sd)


def test_api_lista_disciplinas_e_recusa_desconhecida(site):
    dados = site.get("/api/disciplinas").json()
    assert dados["padrao"] == "paa"
    assert {d["id"] for d in dados["disciplinas"]} == {"paa", "sd"}
    assert all(d["exemplos"] for d in dados["disciplinas"])
    r = site.post("/api/perguntar", json={"pergunta": "O que é um latch?", "disciplina": "quimica"})
    assert r.status_code == 422 and "erro" in r.json()
    r = site.post("/api/v1/questions", json={"question": "O que é um latch?", "subject": "sd"})
    assert r.status_code == 200 and r.json()["metadata"]["subject"] == "sd"


def test_validacao_ab_registra_a_disciplina(site):
    par = esperar(site, site.post("/api/comparar", json={"pergunta": "O que é um flip-flop D?", "disciplina": "sd"}).json())
    notas = {"clareza": 4, "confianca": 4, "utilidade": 4, "erro_matematico": False}
    site.post("/api/avaliar", json={"sessao": par["sessao"], "preferida": "A", "A": notas, "B": notas})
    linha = json.loads((site.tmp / "validacao" / "avaliacoes.jsonl").read_text(encoding="utf-8"))
    assert linha["disciplina"] == "sd"


# ---------------------------------------------------------------- disciplina futura sem código novo

def test_nova_disciplina_so_com_cadastro_e_acervo(tmp_path, monkeypatch):
    raiz = tmp_path
    (raiz / "disciplinas" / "calc" / "materiais").mkdir(parents=True)
    (raiz / "disciplinas" / "calc" / "rigor.md").write_text("# Rigor\n- Derive passo a passo.", encoding="utf-8")
    (raiz / "disciplinas" / "calc" / "materiais" / "c1.md").write_text(
        "---\nid: calc-1\ntitulo: Regra da cadeia\nassunto: derivadas\ntipo: material_estudo\nfonte: nota\n"
        "autoria: equipe\nlicenca: própria\ncuradoria: aprovado\n---\nRegra da cadeia: derivada de f(g(x)) é f'(g(x))·g'(x).",
        encoding="utf-8")
    registro = raiz / "disciplinas" / "disciplinas.json"
    registro.write_text(json.dumps({"padrao": "calc", "disciplinas": [{
        "id": "calc", "nome": "Cálculo 1", "sigla": "CALC", "itens": "disciplinas/calc/itens.json",
        "indice": "disciplinas/calc/indice.json", "materiais": "disciplinas/calc/materiais",
        "rigor": "disciplinas/calc/rigor.md"}]}), encoding="utf-8")
    calc = disciplinas.obter("calc", registro=registro)
    disciplinas.construir(calc, root=raiz)

    llm = FakeLLM({"g1": ("ok", "resposta")})
    llm.embed = sem_embedding
    trechos = asyncio.run(rag.recuperar("Como usar a regra da cadeia?", llm, llm.settings, calc))
    assert [t.titulo for t in trechos] == ["Material de estudo de CALC"]
    assert "Cálculo 1 (CALC)" in prompts.sistema_tutor(calc)
    r = asyncio.run(llm.complete(prompts.sistema_tutor(calc), prompts.prompt_tutor("p", rag.contexto(trechos))))
    assert r.text == "resposta"  # o mesmo serviço de IA, sem nenhuma classe ou rota nova
