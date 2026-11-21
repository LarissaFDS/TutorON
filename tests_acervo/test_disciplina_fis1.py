"""Acervo de Física 1 (turma do Prof. Rosso) e conferência das resoluções.

As questões vêm das provas AB1, AB2 e reavaliações (fotos da turma) e são problemas do Halliday: os blocos
trazem enunciado parafraseado e resolução independente da equipe. Cada número citado num bloco é recalculado
em `tests_acervo/fis1_verif.py`, e as expressões finais passam por análise dimensional com SymPy.
"""

import hashlib
import json
import re
import shutil
import subprocess
import unicodedata

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search
from tests_acervo import fis1_verif as fv
from tests_acervo.fis1_verif import fmt

FIS = disciplinas.obter("fis1")
PASTA = ROOT / "disciplinas/fis1"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(FIS.itens)}
ITENS = {i: x for i, x in TODOS.items() if x["natureza"] == "material_da_disciplina"}
NOTAS = {i: x for i, x in TODOS.items() if x["natureza"] == "nota_da_equipe_ia"}
FRONTEIRA = ("fis2", "calc3", "ga")
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "fis1")


def buscar(pergunta, d=FIS):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return TODOS[ident]["texto"]


def tem(ident, *numeros):
    t = texto(ident).replace("{,}", ",").replace("−", "-")
    faltam = [n for n in numeros if n not in t]
    assert not faltam, f"{ident}: {faltam}"


# ---------------------------------------------------------------- cadastro e acervo


def test_fis1_cadastrada_com_acervo_proprio():
    assert FIS.nome == "Física 1" and FIS.itens.exists() and not FIS.livro_supabase
    ids = {c["id"] for c in read_json(FIS.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({FIS.itens, FIS.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert all(c["disciplina"] == "fis1" for c in read_json(FIS.indice)["chunks"])
    # todo tópico da ementa tem bloco da turma na busca (notas da IA não contam)
    assert {i["assunto"] for i in ITENS.values()} == set(FIS.assuntos)
    assert ids == set(ITENS)


def test_situacao_da_disciplina():
    assert FIS.situacao == "em validação" and FIS.em_validacao


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas fis1 --embeddings`."""
    gerados = disciplinas.registros(FIS)
    assert gerados == read_json(FIS.itens)
    assert {c["id"] for c in read_json(FIS.indice)["chunks"]} == {
        i["id"] for i in gerados if i["confiabilidade"] in ("media", "alta")
    }


def test_blocos_cabem_no_trecho_e_terminam_com_verificacao():
    for i in TODOS.values():
        assert len(i["texto"]) <= 2200, i["id"]
        assert "**Verificação:**" in i["texto"].strip().splitlines()[-1], i["id"]
        assert not re.search(r"[\x00-\x08\x0b-\x1f]", i["texto"]), i["id"]


def test_notas_da_ia_fora_da_busca_e_nada_revisado_sem_registro():
    indice = {c["id"] for c in read_json(FIS.indice)["chunks"]}
    assert NOTAS and indice.isdisjoint(NOTAS)
    assert all(x["status_curadoria"] == "candidato" for x in NOTAS.values())
    for p in FIS.materiais.glob("*.md"):
        cab = p.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, p.name


def test_resolucoes_tem_status_e_dizem_no_texto():
    status = {i: x["status_resolucao"] for i, x in ITENS.items() if "status_resolucao" in x}
    assert set(status) == {i for i, x in ITENS.items() if x["tipo"] == "prova"}
    assert {i for i, s in status.items() if s == "pendente_professor"} == {
        "fis1-ab2-q4-bola-rampa-rolamento",
        "fis1-reav-ab2-q1-pendulo-balistico",
        "fis1-reav-ab2-q2-atwood-disco",
    }
    assert {i for i, s in status.items() if s == "corrigida"} == {
        "fis1-ab1-q2-projetil-rochedo",
        "fis1-ab2-q3-disco-bloco",
    }
    for i, s in status.items():
        t = texto(i)
        assert f"Status da resolução: {s}" in t and "não é gabarito do professor" in t, i
        if s == "corrigida":
            assert "**Correção:**" in t, i
        if s == "pendente_professor":
            assert "**Pendente:**" in t, i


# ---------------------------------------------------------------- busca e isolamento


@pytest.mark.parametrize(
    "pergunta, aceitos",
    [
        (
            "Como montar o diagrama de corpo livre de um bloco num plano inclinado com atrito?",
            {"fis1-reav-ab1-q4-plano-inclinado-polia"},
        ),
        ("Qual o alcance máximo de um projétil?", {"fis1-reav-ab1-q1-bola-parede"}),
        ("Quando a energia mecânica se conserva?", {"fis1-ab2-q1-pacote-mola-atrito"}),
        ("Como resolver uma colisão perfeitamente inelástica?", {"fis1-reav-ab2-q1-pendulo-balistico"}),
        (
            "Como achar a aceleração de um bloco pendurado num fio enrolado num disco?",
            {"fis1-ab2-q3-disco-bloco", "fis1-reav-ab2-q2-atwood-disco"},
        ),
        (
            "Como calcular a velocidade de uma bola que rola sem deslizar numa rampa?",
            {"fis1-ab2-q4-bola-rampa-rolamento"},
        ),
        ("Quais capítulos do Halliday caem na AB2?", {"fis1-mapa-provas-listas"}),
    ],
)
def test_pergunta_de_fis1_encontra_bloco_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize("pergunta", ["Qual a capital da França?", "Qual a receita de bolo de cenoura?"])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


@pytest.mark.parametrize(
    "pergunta",
    [
        "Quando a energia mecânica se conserva?",
        "Como decompor um vetor em componentes?",
        "Como montar o diagrama de corpo livre?",
        "Qual o momento de inércia de um disco?",
    ],
)
def test_vocabulario_comum_fica_na_disciplina_escolhida(pergunta):
    """Fronteira com Física 2, Cálculo 3 e GA: cada uma busca só no próprio índice."""
    assert all(i.startswith("fis1-") for i in buscar(pergunta))
    for d in FRONTEIRA:
        assert not any(i.startswith("fis1-") for i in buscar(pergunta, disciplinas.obter(d)))


def test_pergunta_de_fisica_2_nao_puxa_material_de_fisica_1_e_vice_versa():
    for d in map(disciplinas.obter, FRONTEIRA):
        assert all(not i.startswith("fis1-") for i in buscar("Qual o período de um pêndulo simples de 1 m?", d))
    assert all(i.startswith("fis1-") for i in buscar("Qual o período de um pêndulo simples de 1 m?"))


def test_rigor_tem_fronteiras_e_metodos():
    for termo in ("Física 2", "Cálculo", "Geometria Analítica", "diagrama de corpo livre", "atrito estático máximo",
                  "energia mecânica só se conserva", "½MR²", "(2/5)MR²", "sen 60° ≈ 0,866", "Halliday",
                  "**Verificação:**", "Não entregue a resolução completa"):  # fmt: skip
        assert termo in FIS.rigor, termo


# ---------------------------------------------------------------- conferência das resoluções


def test_ab1_q1_velocidade_vetorial():
    r = fv.ab1_q1_velocidade()
    assert r["a3"] == -18 and r["t_a0"] == 0.75 and len(r["t_rapidez10"]) == 1
    tem("fis1-ab1-q1-velocidade-vetorial", "-18", "0,75 s", fmt(r["t_rapidez10"][0], 1) + " s")


def test_ab1_q2_projetil_e_correcao_do_seno():
    r, r98 = fv.ab1_q2_projetil(), fv.ab1_q2_projetil(g=9.8)
    errado = fv.ab1_q2_projetil(sen=0.809, cos_=0.588)
    assert abs(fv.sin(fv.radians(54)) - 0.809) < 1e-3 and abs(fv.cos(fv.radians(54)) - 0.588) < 1e-3
    tem("fis1-ab1-q2-projetil-rochedo", fmt(r["h"], 1) + " m", fmt(r["v"], 1) + " m/s", fmt(-r["ang"], 1) + "°",
        fmt(r["H"], 1) + " m", fmt(r98["h"], 1), fmt(r98["v"], 1), fmt(r98["H"], 1), fmt(errado["h"], 1))  # fmt: skip
    assert r["t_topo"] < 5.5 and r["vy"] < 0 and r["H"] > r["h"]


def test_ab1_q3_atrito_com_g_98_e_g_10():
    esperado = {8: (6.0, False), 10: (3.625, True), 12: (3.125, True)}
    for P, (f, desliza) in esperado.items():
        assert fv.atrito_bloco(6.0, P) == pytest.approx((f, desliza))
    assert fv.atrito_bloco(6.0, 10, g=10) == (6.0, False)  # limiar exato com g = 10
    assert fv.atrito_bloco(6.0, 12, g=10)[0] == pytest.approx(3.25)
    tem("fis1-ab1-q3-atrito-estatico-cinetico", "6,6 N", "5,8 N", "3,6 N", "3,1 N", "3,3 N", "limiar")


def test_ab1_q4_tres_blocos():
    assert fv.ab1_q4_mu() == pytest.approx(0.375) and fv.ab1_q4_mu(g=9.8) == pytest.approx(0.3724, abs=1e-4)
    t1, t3 = fv.ab1_q4_tracoes_por_massa()
    assert t3 > t1
    tem("fis1-ab1-q4-tres-blocos", "0,375", "0,372", fmt(t1, 1), fmt(t3, 1), "g/5 = 2,0")


def test_reav_ab1_q1_parede_e_alcance():
    r = fv.projetil_parede()
    assert r["vy"] > 0 and r["t"] < r["t_topo"]
    tem("fis1-reav-ab1-q1-bola-parede", fmt(r["t"], 3), fmt(r["y"], 1) + " m", fmt(r["vx"], 1), fmt(r["vy"], 2),
        fmt(r["t_topo"], 2), fmt(r["alcance"], 1), "45^\\circ")  # fmt: skip
    assert fv.alcance(25, 30) == pytest.approx(fv.alcance(25, 60))
    assert max(range(1, 90), key=lambda th: fv.alcance(25, th)) == 45


def test_reav_ab1_q3_forca_inclinada():
    r, errado = fv.bloco_forca_inclinada(), fv.bloco_forca_inclinada(th=0)
    tem("fis1-reav-ab1-q3-bloco-forca-inclinada", fmt(r["N"], 1), "11 N", fmt(r["a"], 2) + " m/s²")
    sem_sen = {"fk": 0.25 * 3.5 * 9.8}
    sem_sen["a"] = (15 * fv.cos(fv.radians(40)) - sem_sen["fk"]) / 3.5
    tem("fis1-reav-ab1-q3-bloco-forca-inclinada", fmt(sem_sen["fk"], 1) + " N", fmt(sem_sen["a"], 2))
    assert errado["N"] == pytest.approx(3.5 * 9.8)
    assert fv.bloco_forca_inclinada(para_baixo=False)["a"] > r["a"]


def test_reav_ab1_q4_plano_inclinado():
    mB, mB_sobe = fv.plano_inclinado_polia(), fv.plano_inclinado_polia(A_desce=False)
    tem("fis1-reav-ab1-q4-plano-inclinado-polia", fmt(mB * 9.8, 1) + " N", fmt(mB, 1) + " kg", fmt(mB_sobe, 1) + " kg")
    assert mB < fv.plano_inclinado_polia(muk=0) == pytest.approx(5.0)


def test_ab2_q1_pacote_mola():
    r = fv.pacote_mola()
    assert r["U"] + r["termica"] == pytest.approx(r["K"]) and r["d"] < r["d_sem_atrito"]
    tem("fis1-ab2-q1-pacote-mola-atrito", "5000\\,d^2 + 15\\,d - 16 = 0", fmt(r["d"], 3) + " m", fmt(r["U"], 2),
        fmt(r["termica"], 2), fmt(r["d_sem_atrito"], 4))  # fmt: skip


def test_ab2_q2_colisao_elastica():
    r = fv.colisao_elastica()
    assert r["p_depois"] == pytest.approx(r["p_antes"]) and r["K_depois"] == pytest.approx(r["K_antes"])
    tem("fis1-ab2-q2-colisao-elastica", fmt(r["v1i"], 2), fmt(r["v1f"], 2), fmt(r["v2f"], 2) + " m/s",
        fmt(r["h2"], 3) + " m", fmt(r["p_antes"], 4), fmt(r["K_antes"] * 1000, 1) + " mJ")  # fmt: skip


def test_ab2_q3_disco_bloco():
    r = fv.disco_bloco()
    assert r["T"] == pytest.approx(r["T_bloco"])
    tem("fis1-ab2-q3-disco-bloco", fmt(r["a"], 1) + " m/s²", fmt(r["alpha"], 0) + " rad/s²", fmt(r["T"], 1) + " N")
    assert fv.disco_bloco(M=0)["a"] == pytest.approx(9.8)


def test_ab2_q4_rolamento_esfera_e_disco():
    esf, dis = fv.rolamento_rampa(2 / 5), fv.rolamento_rampa(1 / 2)
    tem("fis1-ab2-q4-bola-rampa-rolamento", fmt(esf["v"], 2), fmt(dis["v"], 2), fmt(esf["a"], 2), fmt(dis["a"], 2),
        fmt(esf["f"], 2) + " N", fmt(dis["f"], 2) + " N", fmt(esf["mu_min"], 2), fmt((2 * 9.8 * 1.2) ** 0.5, 2))  # fmt: skip
    assert esf["f"] > 0  # o atrito não é nulo (erro visto na turma)


def test_reav_ab2_q1_pendulo_balistico():
    cm, m = fv.pendulo_balistico(0.063), fv.pendulo_balistico(6.3)
    assert round(cm["v"], -1) == 630 and m["v"] == pytest.approx(10 * cm["v"])
    tem("fis1-reav-ab2-q1-pendulo-balistico", fmt(cm["V"], 2), "630 m/s", fmt(m["V"], 1), "6,3 × 10³", "99,8 %")


def test_reav_ab2_q2_atwood_disco():
    g, kg = fv.atwood_disco(0.5), fv.atwood_disco(500)
    assert g["torque"] == pytest.approx(g["I_alpha"])
    tem("fis1-reav-ab2-q2-atwood-disco", fmt(g["a"], 2), fmt(g["T1"], 2), fmt(g["T2"], 2), fmt(g["alpha"], 1),
        "7,8 × 10⁻³", fmt(kg["T1"], 2), fmt(kg["T2"], 2), fmt(g["torque"], 3))  # fmt: skip
    assert fv.atwood_disco(0)["a"] == pytest.approx(9.8 / 5)


def test_reav_ab2_q3_cilindro_telhado():
    r = fv.cilindro_telhado()
    tem("fis1-reav-ab2-q3-cilindro-telhado", fmt(r["v"], 2), fmt(r["omega"], 0) + " rad/s", fmt(r["vx"], 2),
        fmt(r["vy"], 2), fmt(r["t"], 3), fmt(r["x"], 1) + " m", fmt(r["t_largado"], 2))  # fmt: skip


def test_reav_ab2_q4_barata():
    r = fv.barata_disco()
    tem("fis1-reav-ab2-q4-barata-disco", "3,64", "1,37 rad/s", fmt(r["wf"], 3), fmt(r["K_razao"], 2))
    assert round(r["wf"], 3) == 1.365
    assert r["wf"] < 1.5 and r["K_razao"] < 1


def test_notas_da_equipe_conferidas():
    tem("fis1-nota-vetores-componentes", fmt((2**2 + 6**2) ** 0.5, 1), fmt(fv.degrees(fv.atan2(6, 2)), 1) + "°",
        fmt(fv.degrees(fv.atan2(2, 1)), 1) + "°")  # fmt: skip
    tem("fis1-nota-movimento-circular", "4500 N", "5880 N", fmt((0.6 * 9.8 * 50) ** 0.5, 1))
    tem("fis1-nota-trabalho-potencia", "30 J", fmt((2 * 30 / 5) ** 0.5, 1))


def test_analise_dimensional_das_expressoes():
    assert fv.dimensoes() == []


# ---------------------------------------------------------------- fórmulas, catálogo e restrições

FORMULA = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in TODOS.values():
        assert i["texto"].count("$") % 2 == 0, i["id"]


@pytest.mark.skipif(not shutil.which("node"), reason="node indisponível")
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for i in TODOS.values() for a, b in FORMULA.findall(i["texto"])]
    assert len(formulas) >= 100
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
    obrigatorios = {"id", "nome", "autoria", "url", "idioma", "formato", "isa", "topicos", "licenca", "acesso",
                    "prioridade", "uso", "justificativa"}  # fmt: skip
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f["id"]
        assert f["prioridade"] in ("alta", "media", "referencia")
        assert f["uso"] in ("acervo", "citada", "referencia", "candidato", "indisponivel")
        assert set(f["topicos"]) <= set(FIS.assuntos), f["id"]
    citadas = {x for i in TODOS.values() for x in i["fontes_catalogo"]}
    assert citadas <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f["uso"] == "acervo"} <= citadas
    for protegido in ("halliday-fundamentos-vol1", "halliday-resolucoes-10ed", "alonso-finn-solucoes"):
        f = CATALOGO[protegido]
        assert f["uso"] == "referencia" and f["acesso"].startswith("Não incluído") and not f["url"]


def _janelas(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    p = re.findall(r"[a-z]+", t)
    return {hashlib.sha256(f"{a} {b}".encode()).hexdigest()[:16] for a, b in zip(p, p[1:], strict=False)}


# Nomes de alunos que aparecem nas fotos das provas, guardados só como hash de pares de palavras.
NOMES_DE_ALUNOS = {"bb9b82482c35da1e", "81d1515ff454ee14", "f2a95f24517a47a3", "151cbb6cc2ecab55",
                   "7fd5a913029e24ff", "738321d4e7f9b965"}  # fmt: skip


def test_originais_e_dados_pessoais_fora_do_repositorio():
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()]
    assert not [
        p
        for p in arquivos
        if p.suffix.lower() in (".pdf", ".epub", ".png", ".jpg", ".jpeg", ".heic", ".webp", ".zip", ".txt")
    ]
    proibidos = re.compile(r"(?i)[\w.]+@[\w-]+\.\w+|groups\.google|dropbox|sites\.google|whatsapp|aluno:\s*\w")
    for p in [
        *FIS.materiais.glob("*.md"),
        FIS.itens,
        PASTA / "rigor.md",
        PASTA / "CURADORIA.md",
        PASTA / "fontes.json",
    ]:
        conteudo = p.read_text(encoding="utf-8")
        assert not proibidos.search(conteudo), p.name
        assert not _janelas(conteudo) & NOMES_DE_ALUNOS, p.name
    for i in TODOS.values():
        assert "http" not in i["texto"], i["id"]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert [i for i in CATALOGO if f"`{i}`" not in curadoria] == []
    assert [i for i in TODOS if f"`{i}`" not in curadoria] == []
    assert "`fis1`" in (ROOT / "docs/DISCIPLINAS.md").read_text(encoding="utf-8")
