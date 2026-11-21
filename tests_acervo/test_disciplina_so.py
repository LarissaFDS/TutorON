"""Acervo de Sistemas Operacionais (turma do Prof. André Aquino) e conferência das resoluções.

Os blocos parafraseiam slides, provas e listas da turma; cada número citado é recalculado pelos simuladores
de `tests_acervo/so_verif.py`, e os programas de `tests_acervo/c_so/` são compilados e passam pelo
ThreadSanitizer (via Docker, quando disponível).
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
from tests_acervo import so_verif as sv

SO = disciplinas.obter("so")
PASTA = ROOT / "disciplinas/so"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
TODOS = {i["id"]: i for i in read_json(SO.itens)}
ITENS = {i: x for i, x in TODOS.items() if x["natureza"] == "material_da_disciplina"}
NOTAS = {i: x for i, x in TODOS.items() if x["natureza"] == "nota_da_equipe_ia"}
FRONTEIRA = ("oac", "ed")
OUTRAS = tuple(d["id"] for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] != "so")
C_SO = ROOT / "tests_acervo/c_so"


def buscar(pergunta, d=SO):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def texto(ident):
    return TODOS[ident]["texto"]


def tem(ident, *trechos):
    t = texto(ident).replace("{,}", ",").replace("−", "-")
    faltam = [n for n in trechos if n not in t]
    assert not faltam, f"{ident}: {faltam}"


def br(x):
    return f"{x:g}".replace(".", ",")


# ---------------------------------------------------------------- cadastro e acervo


def test_so_cadastrada_com_acervo_proprio():
    assert SO.nome == "Sistemas Operacionais" and SO.itens.exists() and not SO.livro_supabase
    ids = {c["id"] for c in read_json(SO.indice)["chunks"]}
    for d in map(disciplinas.obter, OUTRAS):
        assert {d.itens, d.indice}.isdisjoint({SO.itens, SO.indice})
        assert ids.isdisjoint({c["id"] for c in read_json(d.indice)["chunks"]})
    assert all(c["disciplina"] == "so" for c in read_json(SO.indice)["chunks"])
    assert {i["assunto"] for i in ITENS.values()} == set(SO.assuntos)
    assert ids == set(ITENS)


def test_situacao_da_disciplina():
    assert SO.situacao == "em validação" and SO.em_validacao


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas so --embeddings`."""
    gerados = disciplinas.registros(SO)
    assert gerados == read_json(SO.itens)
    assert {c["id"] for c in read_json(SO.indice)["chunks"]} == {
        i["id"] for i in gerados if i["confiabilidade"] in ("media", "alta")
    }


def test_blocos_cabem_no_trecho_e_terminam_com_verificacao():
    for i in TODOS.values():
        assert len(i["texto"]) <= 2200, i["id"]
        assert "**Verificação:**" in i["texto"].strip().splitlines()[-1], i["id"]
        assert not re.search(r"[\x00-\x08\x0b-\x1f]", i["texto"]), i["id"]


def test_notas_da_ia_fora_da_busca_e_nada_revisado_sem_registro():
    indice = {c["id"] for c in read_json(SO.indice)["chunks"]}
    assert NOTAS and indice.isdisjoint(NOTAS)
    assert all(x["status_curadoria"] == "candidato" for x in NOTAS.values())
    for p in SO.materiais.glob("*.md"):
        cab = p.read_text(encoding="utf-8").split("---")[1]
        assert "revisao_humana: pendente" in cab and "revisao_professor" not in cab, p.name


def test_resolucoes_tem_status_e_dizem_no_texto():
    status = {i: x["status_resolucao"] for i, x in ITENS.items() if "status_resolucao" in x}
    assert {i for i, x in ITENS.items() if x["tipo"] == "prova"} <= set(status)
    assert {i for i, s in status.items() if s == "pendente_professor"} == {"so-paginacao-bits-endereco-traducao"}
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
        ("Como montar o Gantt do Round-Robin com quantum 2?", {"so-escalonamento-round-robin"}),
        ("Quantas faltas de página o LRU dá com 3 quadros?", {"so-substituicao-paginas-fifo-lru-otimo"}),
        ("O que é uma condição de disputa?", {"so-condicao-de-disputa-secao-critica"}),
        ("Quais são as quatro condições para um impasse?", {"so-impasses-quatro-condicoes"}),
        ("Qual a diferença entre processo e thread?", {"so-tarefas-processos-threads-estados"}),
        ("Como resolver o produtor-consumidor com semáforos?", {"so-semaforos-produtor-consumidor"}),
        ("Qual o tamanho máximo de arquivo no ext2?", {"so-fat-cluster-ext2-tamanho-maximo"}),
        (
            "Como calcular o deslocamento da cabeça no SCAN e no LOOK?",
            {"so-escalonamento-disco-subindo", "so-ab2-escalonamento-disco-descendo"},
        ),
    ],
)
def test_pergunta_de_so_encontra_bloco_pertinente(pergunta, aceitos):
    assert buscar(pergunta)[0] in aceitos


@pytest.mark.parametrize("pergunta", ["Qual a capital da França?", "Qual a receita de bolo de cenoura?"])
def test_pergunta_fora_do_acervo_nao_inventa_material(pergunta):
    assert buscar(pergunta) == []


@pytest.mark.parametrize(
    "pergunta",
    ["Como funciona a memória virtual com paginação?", "O que é uma fila de prontos?", "O que é DMA?"],
)
def test_vocabulario_comum_fica_na_disciplina_escolhida(pergunta):
    """Fronteira com OAC e ED: cada disciplina busca só no próprio índice."""
    assert all(i.startswith("so-") for i in buscar(pergunta))
    for d in FRONTEIRA:
        assert not any(i.startswith("so-") for i in buscar(pergunta, disciplinas.obter(d)))


def test_rigor_tem_fronteiras_e_metodos():
    for termo in ("tarefa", "Gantt", "passo a passo", "entrelaçamento", "quatro condições", "Organização e Arquitetura",
                  "Estrutura de Dados", "Tanenbaum", "**Verificação:**", "Não entregue a resolução completa"):  # fmt: skip
        assert termo in SO.rigor, termo


# ---------------------------------------------------------------- conferência das resoluções


def test_escalonamento_do_caderno():
    esperado = {"fcfs": (11.4, 6.6), "sjf": (10.6, 5.8), "srtf": (10.6, 5.8), "prio": (11.2, 6.4),
                "prio_p": (14.4, 9.6), "rr": (15, 10.2)}  # fmt: skip
    for pol, (tt, tw) in esperado.items():
        assert sv.medias(sv.TAREFAS_CADERNO_17, pol) == pytest.approx((tt, tw)), pol
    tem("so-escalonamento-fcfs-sjf", br(11.4), br(6.6), br(10.6), br(5.8))
    tem("so-escalonamento-srtf-prioridades", br(11.2), br(6.4), br(14.4), br(9.6))
    tem("so-escalonamento-round-robin", br(15), br(10.2))


def test_lote_de_jobs_da_ab1():
    assert sv.medias(sv.JOBS_AB1_Q7, "fcfs") == pytest.approx((256, 154))
    assert sv.medias(sv.JOBS_AB1_Q7, "sjf") == pytest.approx((200, 98))
    tem("so-ab1-lote-jobs-fcfs-sjf", "154", "98", "510")


def test_substituicao_de_paginas_e_belady():
    assert [sv.faltas(sv.REFS_EXEMPLO, 3, a)[0] for a in ("fifo", "lru", "otimo")] == [10, 9, 7]
    assert sv.faltas(sv.BELADY, 3, "fifo")[0] == 9 and sv.faltas(sv.BELADY, 4, "fifo")[0] == 10
    assert sv.faltas(sv.BELADY, 3, "lru")[0] == 10 and sv.faltas(sv.BELADY, 4, "lru")[0] == 8
    assert sv.envelhecimento(sv.LEITURAS_AGING) == [1, 14, 15, 10]


def test_alocacao_contigua_e_paginacao():
    assert sv.alocar(sv.BURACOS, sv.PEDIDOS, "first") == [3, 4, 7, 20, 12, 20]
    assert sv.alocar(sv.BURACOS, sv.PEDIDOS, "best") == [0, 4, 0, 30, 12, 20]
    assert sv.alocar(sv.BURACOS, sv.PEDIDOS, "worst") == [10, 4, 7, 15, 12, 18]
    assert sv.bits_endereco(8, 4096, 64) == (15, 18)
    tem("so-paginacao-bits-endereco-traducao", "2^{15}", "2^{18}")


def test_escalonamento_de_disco_nos_dois_sentidos():
    subindo = {"fcfs": 423, "sstf": 180, "scan": 331, "cscan": 384, "look": 261, "clook": 280}
    descendo = {"scan": 214, "cscan": 380, "look": 180, "clook": 276}
    for pol, total in subindo.items():
        assert sv.disco(sv.PEDIDOS_DISCO, 50, pol)[1] == total, pol
    for pol, total in descendo.items():
        assert sv.disco(sv.PEDIDOS_DISCO, 50, pol, subindo=False)[1] == total, pol
    tem("so-escalonamento-disco-subindo", *(f"**{v}**" for v in subindo.values()))
    tem("so-ab2-escalonamento-disco-descendo", "**214**", "**180**", "**423**", "276", "363")


def test_arquivos_ext2_e_cluster():
    assert sv.ext2_maximo() == 2_164_404_224
    assert sv.clusters(1024, 2048) == 1
    tem("so-fat-cluster-ext2-tamanho-maximo", "2\\,164\\,404\\,224", "270 550 528")


def test_impasse_pior_caso():
    assert sv.pior_caso_sem_impasse(4, 3, 2)


# ---------------------------------------------------------------- código C


def _docker():
    if not shutil.which("docker"):
        return False
    return subprocess.run(["docker", "info"], capture_output=True).returncode == 0


@pytest.mark.skipif(not _docker(), reason="Docker indisponível: gcc com pthread e TSan rodam na imagem gcc:14")
def test_codigo_c_compila_e_so_a_disputa_acusa_tsan():
    script = (
        "set -e; cd /src; for f in disputa mutex_contador produtor_consumidor ordem_travas; do "
        "gcc -std=c11 -Wall -Wextra -pedantic -Werror -pthread -o /tmp/$f $f.c; "
        "gcc -std=c11 -g -fsanitize=thread -pthread -o /tmp/$f.t $f.c; "
        "if setarch $(uname -m) -R /tmp/$f.t >/dev/null 2>/tmp/$f.log; then :; fi; "
        "if grep -q 'data race' /tmp/$f.log; then echo $f:race; else echo $f:ok; fi; done"
    )
    r = subprocess.run(
        ["docker", "run", "--rm", "--security-opt", "seccomp=unconfined", "-v", f"{C_SO.as_posix()}:/src:ro",
         "gcc:14", "bash", "-c", script],
        capture_output=True, text=True, timeout=600,
    )  # fmt: skip
    assert r.returncode == 0, r.stderr
    assert r.stdout.split() == ["disputa:race", "mutex_contador:ok", "produtor_consumidor:ok", "ordem_travas:ok"]


def test_trechos_de_c_nos_blocos_vem_dos_programas_testados():
    fonte = "".join(p.read_text(encoding="utf-8") for p in C_SO.glob("*.c"))
    for ident in ("so-condicao-de-disputa-secao-critica", "so-semaforos-produtor-consumidor"):
        for linha in re.findall(r"```c\n(.*?)```", texto(ident), re.S)[0].splitlines():
            codigo = re.sub(r"/\*.*?\*/|//.*", "", linha).strip()
            if codigo:
                assert codigo in fonte, (ident, linha)


# ---------------------------------------------------------------- fórmulas, catálogo e restrições

FORMULA = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def test_formulas_tem_delimitadores_fechados():
    for i in TODOS.values():
        assert i["texto"].count("$") % 2 == 0, i["id"]


@pytest.mark.skipif(not shutil.which("node"), reason="node indisponível")
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for i in TODOS.values() for a, b in FORMULA.findall(i["texto"])]
    assert len(formulas) >= 10
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
        assert set(f["topicos"]) <= set(SO.assuntos), f["id"]
    citadas = {x for i in TODOS.values() for x in i["fontes_catalogo"]}
    assert citadas <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f["uso"] == "acervo"} <= citadas
    for protegido in ("tanenbaum", "silberschatz", "deitel"):
        f = CATALOGO[protegido]
        assert f["uso"] == "referencia" and f["acesso"].startswith("Não incluído") and not f["url"]
    assert "Aquino" in CATALOGO["ufal-aquino-slides-so"]["autoria"]


def _janelas(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    p = re.findall(r"[a-z]+", t)
    return {hashlib.sha256(f"{a} {b}".encode()).hexdigest()[:16] for a, b in zip(p, p[1:], strict=False)}


# Nomes de alunos que aparecem nos comprovantes, listas e resumos, guardados só como hash de pares de palavras.
NOMES_DE_ALUNOS = {"92c69da92a84c812", "bafdc57fb1c0b4e9", "3c12c638cc541582", "1afbbdb18399e925",
                   "971ebb67a3af2a29"}  # fmt: skip
MATRICULAS = re.compile(r"\b(15112025|123228)\b")


def test_originais_e_dados_pessoais_fora_do_repositorio():
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()] + [p for p in C_SO.rglob("*") if p.is_file()]
    assert not [
        p
        for p in arquivos
        if p.suffix.lower() in (".pdf", ".epub", ".png", ".jpg", ".jpeg", ".heic", ".webp", ".zip", ".txt")
    ]
    proibidos = re.compile(r"(?i)[\w.]+@[\w-]+\.\w+|groups\.google|dropbox|sites\.google|whatsapp|aluno:\s*\w|\biago\b")
    for p in [*SO.materiais.glob("*.md"), SO.itens, PASTA / "rigor.md", PASTA / "CURADORIA.md", PASTA / "fontes.json"]:
        conteudo = p.read_text(encoding="utf-8")
        assert not proibidos.search(conteudo), p.name
        assert not MATRICULAS.search(conteudo), p.name
        assert not _janelas(conteudo) & NOMES_DE_ALUNOS, p.name
    for i in TODOS.values():
        assert "http" not in i["texto"], i["id"]


def test_documentacao_lista_todas_as_fontes_e_blocos():
    curadoria = (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert [i for i in CATALOGO if f"`{i}`" not in curadoria] == []
    assert [i for i in TODOS if f"`{i}`" not in curadoria] == []
    assert "`so`" in (ROOT / "docs/DISCIPLINAS.md").read_text(encoding="utf-8")
