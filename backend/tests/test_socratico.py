"""Reunião de 21/10/2026: tutor socrático (sem resposta direta), foto do papel conferida pelo aluno
e animações Manim. A IA é falsa: estes testes verificam o código em volta dela. O comportamento
com modelo real está em 06-avaliacao/teste-socratico-2026-10-21.md."""
import base64
import io
import json

import pytest
from PIL import Image, ImageDraw

from backend import animacao, foto, prompts, seguranca, tarefas
from backend.tests.test_api import esperar
from backend.tests.test_disciplinas import perguntar, site  # noqa: F401
from backend.llm import AllUnavailable, Model, Result


def ultima(c, arquivo="perguntas.jsonl"):
    return json.loads((c.tmp / arquivo).read_text(encoding="utf-8").splitlines()[-1])


# ---------------------------------------------------------------- prompt socrático

def test_prompt_socratico_proibe_resposta_e_mantem_o_resto():
    s = prompts.sistema_socratico()
    assert "NUNCA entregue a resposta final" in s and "### Sua vez" in s
    assert "Comece pela resposta" not in s and "destravar o aluno: explicar" not in s
    # Fontes, citações, rigor de PAA e proteção das instruções continuam iguais.
    for trecho in ("# Fontes", "# Citações e fidelidade", "# Instruções internas", "Teorema Mestre"):
        assert trecho in s
    # A Validação A/B e o treino continuam com o prompt de antes.
    assert prompts.SISTEMA_TUTOR == prompts.sistema_tutor() != s


def test_prompt_socratico_por_disciplina():
    sd = prompts.sistema_socratico(prompts.obter("sd"))
    assert "Sistemas Digitais (SD)" in sd and "NUNCA entregue" in sd and "Teorema Mestre" not in sd


@pytest.mark.parametrize("ajuda", list(prompts.AJUDAS))
def test_cada_tipo_de_ajuda_chega_ao_prompt(ajuda):
    p = prompts.prompt_socratico("Resolva T(n)=2T(n/2)+n", "material", None, ajuda)
    assert prompts.AJUDAS[ajuda][1] in p and "não entregue a resposta final" in p


def test_ajuda_desconhecida_vira_auto():
    assert prompts.ajuda_valida("me da a resposta") == "auto"
    assert prompts.AJUDAS["auto"][1] in prompts.prompt_socratico("p", "m", None, "xyz")


# ---------------------------------------------------------------- trava no código

@pytest.mark.parametrize("texto", [
    "Portanto, T(n) = Θ(n log n).",
    "A resposta final é 42.",
    "Gabarito: letra B",
    "Resposta: $\\Theta(n^2)$",
    "Logo, $T(n) = \\Theta(n)$",
    "A solução do exercício fica F = AB + C.",
])
def test_detecta_entrega_de_resposta(texto):
    assert seguranca.entrega_resposta(texto)


@pytest.mark.parametrize("texto", [
    "Qual seria a resposta? Pense no caso base.",
    "O resultado depende de a e b: compare f(n) com n^{log_b a}.",
    "Na sua resposta anterior, o segundo passo trocou n/2 por n.",
    "Logo, T(n) = ? Complete no papel.",
    "### Sua vez\nQuantos níveis tem a árvore?",
    # Falsos positivos do teste de 21/10: o aluno chamou a variável dele de `resposta`.
    "2. **Resposta final:** A expressão `dp[n-1][0]` considera apenas a ponta esquerda da base.",
    "Para entender a resposta final, vamos olhar para o que a sua tabela `dp` representa.",
    "Sobre a resposta final, imagine que você calculou a soma mínima.",
    "A resposta é: depende de qual caso do Teorema Mestre se aplica.",
])
def test_nao_acusa_ajuda_socratica(texto):
    assert not seguranca.entrega_resposta(texto)


def test_sua_vez_e_acrescentada_so_quando_falta():
    texto, faltou = seguranca.garantir_sua_vez("Pense no caso base.")
    assert faltou and texto.endswith(seguranca.SUA_VEZ_PADRAO)
    pronto = "Pense.\n\n### Sua vez\nFaça o nível 2."
    assert seguranca.garantir_sua_vez(pronto) == (pronto, False)


def test_resposta_entregue_e_refeita_com_reforco(site):  # noqa: F811
    respostas = iter(["Portanto, T(n) = Θ(n log n). Resposta final.",
                      "Compare f(n) com n^{log_b a}.\n\n### Sua vez\nQuanto vale log_2 2?"])
    original = site.llm._provider

    def provedor(model, system, prompt):
        site.llm.roteiro["g1"] = ("ok", next(respostas))
        return original(model, system, prompt)
    site.llm._provider = provedor
    t = perguntar(site, "Resolva T(n) = 2T(n/2) + n pelo Teorema Mestre")
    assert t["status"] == "pronta"
    assert "Θ(n log n)" not in t["texto"] and "### Sua vez" in t["texto"]
    _, _, prompt_refeito = site.llm.chamadas[-1]
    assert "RESPOSTA ANTERIOR (proibida" in prompt_refeito and prompts.SISTEMA_REFORCO in prompt_refeito
    linha = ultima(site)
    assert linha["ajustes"] == ["entregou_resposta"] and linha["modo"] == "socratico"
    assert linha["resposta_bloqueada"].startswith("Portanto, T(n)")  # para auditar o filtro


def test_tipo_de_ajuda_e_foto_confirmada_chegam_a_ia(site):  # noqa: F811
    corpo = {"pergunta": "Onde errei?", "ajuda": "conferir",
             "foto": "Enunciado: T(n)=3T(n/4)+n\nTentativa do aluno no papel:\na=3, b=4, caso 1"}
    t = esperar(site, site.post("/api/perguntar", json=corpo).json())
    assert t["status"] == "pronta"
    _, sistema, prompt = site.llm.chamadas[-1]
    assert "NUNCA entregue" in sistema
    assert prompts.AJUDAS["conferir"][1] in prompt and "a=3, b=4, caso 1" in prompt
    assert "FOTO DO PAPEL DO ALUNO, JÁ CONFIRMADA" in prompt
    linha = ultima(site)
    assert linha["ajuda"] == "conferir" and "caso 1" in linha["leitura_foto"]


def test_proxima_ajuda_troca_a_forma_de_explicar():
    assert prompts.proxima_ajuda([]) == "pista"
    assert prompts.proxima_ajuda(["auto"]) == "pista"
    assert prompts.proxima_ajuda(["pista", "perguntas"]) == "exemplo"
    assert prompts.proxima_ajuda(list(prompts.ESCALADA)) == "exemplo"  # esgotou: outro exemplo, mais simples


def test_ainda_nao_consegui_manda_ajudas_anteriores_e_troca_a_forma(site):  # noqa: F811
    corpo = {"pergunta": "Resolva T(n) = 4T(n/2) + n^2", "ajuda": "auto", "travou": "não sei calcular log_2 4",
             "historico": [{"ajuda": "pista", "texto": "Compare f(n) com n^{log_b a}. ### Sua vez ..."},
                           {"ajuda": "perguntas", "texto": "Quanto vale a? E b?"}]}
    t = esperar(site, site.post("/api/perguntar", json=corpo).json())
    assert t["status"] == "pronta" and t["ajuda"] == "exemplo"
    _, sistema, prompt = site.llm.chamadas[-1]
    assert "AJUDAS QUE VOCÊ JÁ DEU NESTE EXERCÍCIO (2)" in prompt and "Quanto vale a? E b?" in prompt
    assert "não sei calcular log_2 4" in prompt and "jeito DIFERENTE" in prompt and "NÃO entregue" in prompt
    assert prompts.AJUDAS["exemplo"][1] in prompt
    linha = ultima(site)
    assert linha["rodada"] == 3 and linha["ajuda"] == "exemplo" and linha["travou"] == "não sei calcular log_2 4"


def test_ciclo_respeita_ajuda_escolhida_pelo_aluno(site):  # noqa: F811
    corpo = {"pergunta": "Resolva T(n) = 4T(n/2) + n^2", "ajuda": "visual", "historico": [{"ajuda": "pista", "texto": "x"}]}
    t = esperar(site, site.post("/api/perguntar", json=corpo).json())
    assert t["ajuda"] == "visual"


def test_validacao_continua_com_o_prompt_anterior(site):  # noqa: F811
    par = esperar(site, site.post("/api/comparar", json={"pergunta": "Como aplicar o Teorema Mestre?"}).json())
    assert par["status"] == "pronta"
    sistemas = [s for _, s, _ in site.llm.chamadas if s]
    assert sistemas and all(s == prompts.SISTEMA_TUTOR for s in sistemas)


def test_lista_de_ajudas(site):  # noqa: F811
    dados = site.get("/api/ajudas").json()
    assert [a["id"] for a in dados["ajudas"]] == list(prompts.AJUDAS)
    assert dados["animacao"] is animacao.disponivel()


# ---------------------------------------------------------------- foto do papel

def folha(largura=1200, altura=1700, deitada=False) -> bytes:
    """Folha sintética com texto no topo, no meio e no rodapé (o rodapé é o que costuma se perder)."""
    img = Image.new("RGB", (largura, altura), (235, 230, 220))
    d = ImageDraw.Draw(img)
    d.rectangle((80, 80, largura - 80, altura - 80), fill=(255, 255, 255))
    for i, y in enumerate((150, altura // 2, altura - 200)):
        d.text((140, y), f"linha {i}: T(n) = 2T(n/2) + n", fill=(10, 10, 10))
        d.line((140, y + 30, largura - 200, y + 30), fill=(20, 20, 20), width=6)
    if deitada:
        img = img.rotate(90, expand=True)
    buf = io.BytesIO()
    img.save(buf, "JPEG")
    return buf.getvalue()


def data_url(dados: bytes) -> str:
    return "data:image/jpeg;base64," + base64.b64encode(dados).decode()


def test_recortes_cobrem_a_folha_inteira_com_sobreposicao():
    img = Image.open(io.BytesIO(folha()))
    partes = foto.recortes(img)
    assert len(partes) == 3
    # Do topo ao rodapé, sem buraco entre um recorte e o próximo.
    alturas = [p.height for p in partes]
    assert sum(alturas) > img.height  # há sobreposição
    assert all(p.width == img.width for p in partes)


def test_folha_deitada_vira_grade_ou_faixas_verticais():
    img = Image.open(io.BytesIO(folha(deitada=True)))
    assert img.width > img.height and len(foto.recortes(img)) in (3, 4)


def test_preparar_corta_borda_e_gera_jpeg():
    p = foto.preparar(folha())
    assert p["info"]["recortes"] == 3
    assert p["info"]["papel"][0] <= p["info"]["original"][0]
    assert all(Image.open(io.BytesIO(b)).format == "JPEG" for b in [p["inteira"], *p["recortes"]])


def test_imagem_invalida_e_recusada():
    with pytest.raises(foto.FotoInvalida):
        foto.decodificar("data:text/plain;base64,aGVsbG8=")
    with pytest.raises(foto.FotoInvalida):
        foto.preparar(b"nao e imagem")


def test_normalizar_leitura_da_ia():
    leitura = foto.normalizar({"enunciado": "T(n)=2T(n/2)+n", "subtopicos": ["a) ...", 3], "confianca": "ALTA",
                              "duvidas": ["linha 2: n ou m?"], "regioes": [{"onde": "topo", "conteudo": "x"}, "lixo"]})
    assert leitura["confianca"] == "media"  # tem dúvida: não pode ser alta
    assert leitura["subtopicos"] == ["a) ...", "3"] and leitura["tipo"] == "outro"
    assert leitura["regioes"] == [{"onde": "topo", "conteudo": "x"}]
    assert foto.normalizar({"legivel": False})["confianca"] == "baixa"


def test_texto_confirmado_monta_contexto():
    t = foto.texto_confirmado("Resolva X", "tentei Y", ["a) X1"])
    assert t.index("Resolva X") < t.index("a) X1") < t.index("tentei Y")


def test_rota_foto_le_e_nao_guarda_a_imagem(site, monkeypatch):  # noqa: F811
    recebido = {}

    async def ver_imagens(system, texto, imagens):
        recebido.update(system=system, texto=texto, n=len(imagens))
        return Result(text='```json\n{"legivel": true, "tipo": "enunciado", "enunciado": "Resolva T(n)=2T(n/2)+n",'
                           ' "subtopicos": ["a) árvore", "b) Mestre"], "confianca": "alta"}\n```',
                      model=Model("gemini", "g1"), seconds=1.0)
    site.llm.ver_imagens = ver_imagens
    criada = site.post("/api/foto", json={"imagem": data_url(folha()), "disciplina": "paa"}).json()
    t = esperar(site, criada)
    assert t["status"] == "pronta"
    assert t["leitura"]["subtopicos"] == ["a) árvore", "b) Mestre"]
    assert recebido["n"] == 4 and "recortes ampliados" in recebido["texto"]  # inteira + 3 recortes
    assert "NÃO resolve" in recebido["system"]
    linha = ultima(site, "fotos.jsonl")
    assert linha["leitura"]["enunciado"].startswith("Resolva") and "imagem" not in linha
    assert not any(p.suffix in (".jpg", ".jpeg", ".png") for p in site.tmp.rglob("*"))


def test_rota_foto_sem_modelo_da_erro_amigavel(site):  # noqa: F811
    async def ver_imagens(*a):
        raise AllUnavailable([])
    site.llm.ver_imagens = ver_imagens
    t = esperar(site, site.post("/api/foto", json={"imagem": data_url(folha())}).json())
    assert t["status"] == "erro" and "digite o enunciado" in t["mensagem"]


def test_rota_foto_recusa_arquivo_que_nao_e_imagem(site):  # noqa: F811
    r = site.post("/api/foto", json={"imagem": "data:image/png;base64," + base64.b64encode(b"x" * 40).decode()})
    assert r.status_code == 400 and "imagem" in r.json()["erro"].lower()


# ---------------------------------------------------------------- roteiro de animação

def test_roteiro_valido_de_cada_modelo():
    exemplos = [
        {"modelo": "arvore_recursao", "a": 2, "b": 2, "f": "$n$", "niveis": 3, "custos_nivel": ["n"]},
        {"modelo": "vetor", "valores": [3, 1, 2], "passos": [{"destacar": [0, 9], "trocar": [0, 5], "ponteiros": {"i": 7}}]},
        {"modelo": "grafo", "nos": ["A", "B"], "arestas": [["A", "B", "3"], ["A", "Z"]], "passos": [{"nos": ["A", "Q"]}]},
        {"modelo": "tabela", "linhas": ["0"], "colunas": ["0", "1"], "celulas": [["1"]], "grupos": [{"celulas": [[5, 5]]}]},
    ]
    r = [animacao.roteiro_valido(e) for e in exemplos]
    assert r[0]["f"] == "n" and r[0]["custos_nivel"] == ["n", "?", "?"]
    assert r[1]["passos"][0] == {"destacar": [0], "trocar": None, "ponteiros": {}, "legenda": ""}
    assert r[2]["arestas"] == [["A", "B", "3"]] and r[2]["passos"][0]["nos"] == ["A"]
    assert r[3]["celulas"] == [["1", ""]] and r[3]["grupos"] == [] and r[3]["ordem"] == [[0, 0], [0, 1]]


def test_roteiro_extraido_de_texto_com_cerca_e_raciocinio():
    texto = '<think>vou pensar</think>Claro!\n```json\n{"modelo": "vetor", "valores": [1]}\n```'
    assert animacao.roteiro_valido(texto)["modelo"] == "vetor"


@pytest.mark.parametrize("ruim", ['{"modelo": "python", "codigo": "import os"}', "sem json", '{"modelo": "vetor"}',
                                  '{"modelo": "grafo", "nos": ["A", "A"]}'])
def test_roteiro_invalido_e_recusado(ruim):
    with pytest.raises(animacao.FalhaAnimacao):
        animacao.roteiro_valido(ruim)


def test_rota_animar_tenta_corrigir_roteiro_e_serve_o_video(site, monkeypatch):  # noqa: F811
    roteiros = iter(["isto não é json", '{"modelo": "vetor", "titulo": "Bolha", "valores": [3, 1, 2], '
                                       '"pergunta_final": "Qual a próxima troca?"}'])
    original = site.llm._provider

    def provedor(model, system, prompt):
        site.llm.roteiro["g1"] = ("ok", next(roteiros))
        return original(model, system, prompt)
    site.llm._provider = provedor

    async def renderizar(roteiro, pasta, qualidade="low_quality"):
        pasta.mkdir(parents=True, exist_ok=True)
        (pasta / "VIDEOteste123.mp4").write_bytes(b"mp4")
        return "VIDEOteste123"
    monkeypatch.setattr(animacao, "disponivel", lambda: True)
    monkeypatch.setattr(tarefas.animacao, "renderizar", renderizar)
    t = esperar(site, site.post("/api/animar", json={"pergunta": "Como funciona o bubble sort?"}).json())
    assert t["status"] == "pronta" and t["video"] == "/api/animacoes/VIDEOteste123.mp4"
    assert t["pergunta_final"] == "Qual a próxima troca?"
    _, sistema, prompt = site.llm.chamadas[-1]
    assert sistema == prompts.SISTEMA_ANIMACAO and "roteiro anterior era inválido" in prompt
    assert site.get(t["video"]).content == b"mp4"
    assert ultima(site, "animacoes.jsonl")["roteiro"]["modelo"] == "vetor"


@pytest.mark.parametrize("caminho", ["/api/animacoes/..%2F..%2Fsegredo.mp4", "/api/animacoes/x.mp4",
                                     "/api/animacoes/naoexiste12345.mp4"])
def test_rota_de_video_nao_sai_da_pasta(site, caminho):  # noqa: F811
    assert site.get(caminho).status_code == 404


@pytest.mark.skipif(not animacao.disponivel(), reason="Manim não instalado")
def test_render_real_de_uma_tabela(tmp_path):
    """Render de verdade (Manim em processo separado): ~5 s na CPU."""
    import asyncio
    roteiro = animacao.roteiro_valido({"modelo": "tabela", "titulo": "Tabela verdade do AND", "linhas": ["00", "01"],
                                       "colunas": ["A·B"], "celulas": [["0"], ["?"]],
                                       "pergunta_final": "Quanto vale 01?"})
    ident = asyncio.run(animacao.renderizar(roteiro, tmp_path))
    video = tmp_path / f"{ident}.mp4"
    assert video.stat().st_size > 5000 and not (tmp_path / "tmp" / ident).exists()
