"""Acervo de Metodologia da Pesquisa e do Trabalho Científico e compilação de todo exemplo de LaTeX.

O material da turma são dois guias de LaTeX (Lopez e Silva, UFRJ, 2013, CC BY-SA 3.0; Wilkins, 1995, sem
licença aberta) e um modelo de artigo baseado na NBR 6022:2003 (Alves e Arruda, BU/UFSC, 2004, sem licença
aberta). Nenhum deles é versionado: os blocos parafraseiam e trazem exemplos próprios.

Cada bloco ```latex de disciplinas/metodologia/materiais é extraído e compilado aqui com pdflatex (e bibtex,
quando o documento cita), junto com o ```bibtex do bloco do arquivo .bib. A compilação usa o pdflatex local,
se houver, ou a imagem Docker `tutoron-latex-metodologia` (TeX Live + abnTeX2):

    docker build -t tutoron-latex-metodologia tests_acervo/latex_metodologia

Sem nenhum dos dois, os testes de compilação são pulados com o motivo.
"""

import base64
import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

from acervo import disciplinas
from acervo.common import ROOT, read_json
from acervo.retrieval import search

MET = disciplinas.obter("metodologia")
PASTA = ROOT / "disciplinas/metodologia"
FONTES = read_json(PASTA / "fontes.json")["fontes"]
CATALOGO = {f["id"]: f for f in FONTES}
ITENS = {x["id"]: x for x in read_json(MET.itens)}
NA_BUSCA = {c["id"] for c in read_json(MET.indice)["chunks"]}
VETORES = json.loads((ROOT / "eval/relevancia-vetores.json").read_text(encoding="utf-8"))
IMAGEM = "tutoron-latex-metodologia"
LATEX = re.compile(r"```latex\n(.*?)```", re.S)
BIBTEX = re.compile(r"```bibtex\n(.*?)```", re.S)
# PNG de 1x1 pixel: a imagem `grafico.png` que o exemplo de figura espera ao lado do .tex.
PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
)

# Tópicos da ementa sem material da turma: só notas da equipe com IA, fora da busca até revisão humana.
SO_NOTAS = {
    "metodologia-01-ciencia-conhecimento",
    "metodologia-02-tipos-metodos-pesquisa",
    "metodologia-03-problema-hipotese-projeto",
    "metodologia-10-etica-plagio",
}


def texto(ident):
    return ITENS[f"metodologia-{ident}"]["texto"]


def buscar(pergunta, d=MET):
    return [r["id"] for r in search(pergunta, semantic=False, itens=d.itens, indice=d.indice)]


def hibrida(pergunta, d=MET):
    return [
        r["id"]
        for r in search(
            pergunta,
            k=4,
            vector=VETORES[pergunta],
            min_similarity=0.45,
            hub_penalty=True,
            itens=d.itens,
            indice=d.indice,
        )
    ]


# ---------------------------------------------------------------- cadastro e acervo


def test_metodologia_cadastrada_com_acervo_proprio_e_a_mesma_ia():
    assert MET.nome == "Metodologia da Pesquisa e do Trabalho Científico" and MET.itens.exists() and MET.indice.exists()
    assert not MET.livro_supabase and MET.rigor.strip() == (PASTA / "rigor.md").read_text(encoding="utf-8").strip()
    assert all(c["disciplina"] == "metodologia" for c in read_json(MET.indice)["chunks"])
    for outra in disciplinas.todas():
        if outra.id != "metodologia":
            assert NA_BUSCA.isdisjoint({c["id"] for c in read_json(outra.indice)["chunks"]}), outra.id
    bruto = [d for d in read_json(ROOT / "disciplinas/disciplinas.json")["disciplinas"] if d["id"] == "metodologia"][0]
    assert not {"modelo", "model", "provedor", "endpoint", "prompt", "chave"} & set(bruto)
    assert bruto["situacao"] == "MVP" and "aviso" not in bruto
    assert read_json(MET.indice)["embedding_model"] == read_json(disciplinas.obter("ingles").indice)["embedding_model"]


def test_itens_gerados_estao_atualizados():
    """Quem editar um .md precisa rodar `python -m acervo.disciplinas metodologia --embeddings`."""
    gerados = disciplinas.registros(MET)
    assert gerados == read_json(MET.itens)
    assert NA_BUSCA == {x["id"] for x in gerados if x["confiabilidade"] in ("media", "alta")}
    assert read_json(MET.indice)["modo"] == "hibrido"


def test_blocos_cabem_no_trecho_e_terminam_com_verificacao():
    for x in ITENS.values():
        assert len(x["texto"]) <= 2200, x["id"]  # backend/rag.py corta acima disso
        assert "**Verificação:**" in x["texto"], x["id"]
        assert not x["texto"].count("```") % 2, x["id"]  # nenhum bloco de código cortado no meio


def test_nenhuma_nota_de_ia_sem_revisao_na_busca():
    notas = {i for i, x in ITENS.items() if x["natureza"] == "nota_da_equipe_ia"}
    assert len(notas) == 6 and notas.isdisjoint(NA_BUSCA)
    assert all(ITENS[i]["status_curadoria"] == "candidato" for i in notas)
    assert not any(x.get("revisao_humana") == "feita" or x.get("revisao_professor") for x in ITENS.values())
    assert all(x["revisao_humana"] == "pendente" for x in ITENS.values())


def test_todo_topico_com_material_da_turma_tem_bloco_na_busca():
    com_bloco = {ITENS[i]["assunto"] for i in NA_BUSCA}
    assert com_bloco == set(MET.assuntos) - SO_NOTAS
    turma = {"alves-arruda-2004-artigo", "lopez-silva-2013-latex", "wilkins-1995-latex"}
    assert {t for f in turma for t in CATALOGO[f]["topicos"]} <= com_bloco
    assert {ITENS[i]["assunto"] for i in ITENS if i not in NA_BUSCA} >= SO_NOTAS


def test_status_dos_blocos_na_busca():
    for i in NA_BUSCA:
        x = ITENS[i]
        assert x["status_resolucao"] in ("validada", "corrigida", "pendente_professor"), i
        assert "Prof." not in x["texto"], i  # o professor da turma não foi identificado
        if x["status_resolucao"] == "pendente_professor":
            assert "Status da resolução: pendente de confirmação do professor" in x["texto"], i
        if x["status_resolucao"] == "corrigida":
            assert "Correção" in x["texto"] and "Status da resolução: corrigida" in x["texto"], i
        if LATEX.search(x["texto"]):
            assert x["verificacao"] == "conferida_por_codigo", i


# ---------------------------------------------------------------- compilação dos exemplos de LaTeX


def _compilador():
    if shutil.which("pdflatex") and shutil.which("bibtex"):
        return "local"
    if shutil.which("docker"):
        r = subprocess.run(["docker", "image", "inspect", IMAGEM], capture_output=True)
        if r.returncode == 0:
            return "docker"
    return None


ROTEIRO = (
    'set -u; for d in */; do cd "$BASE/$d"; '
    "pdflatex -interaction=nonstopmode -halt-on-error artigo >/dev/null 2>&1; "
    "if grep -q '\\\\citation' artigo.aux 2>/dev/null; then bibtex artigo >/dev/null 2>&1; fi; "
    "pdflatex -interaction=nonstopmode -halt-on-error artigo >/dev/null 2>&1; "
    "pdflatex -interaction=nonstopmode -halt-on-error artigo >/dev/null 2>&1; echo $? > status; done"
)


def compilar(pasta: Path):
    """Compila cada subpasta de `pasta` (artigo.tex + refs.bib + grafico.png)."""
    modo = _compilador()
    if modo is None:
        pytest.skip(f"sem pdflatex/bibtex e sem a imagem Docker {IMAGEM}: veja a docstring do módulo")
    if modo == "local":
        r = subprocess.run(["sh", "-c", ROTEIRO], cwd=pasta, env={**__import__("os").environ, "BASE": str(pasta)})
    else:
        r = subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "-v",
                f"{pasta.as_posix()}:/w",
                "-w",
                "/w",
                "-e",
                "BASE=/w",
                IMAGEM,
                "sh",
                "-c",
                ROTEIRO,
            ],
            capture_output=True,
            text=True,
            timeout=900,
        )
    assert r.returncode == 0, r


def _preparar(pasta: Path, documentos: dict[str, str]):
    bib = [b for x in ITENS.values() for b in BIBTEX.findall(x["texto"])]
    assert len(bib) == 1
    for nome, tex in documentos.items():
        d = pasta / nome
        d.mkdir()
        (d / "artigo.tex").write_text(tex, encoding="utf-8", newline="\n")
        (d / "refs.bib").write_text(bib[0], encoding="utf-8", newline="\n")
        (d / "grafico.png").write_bytes(PNG)


def _exemplos():
    return {i: tex for i, x in ITENS.items() for tex in LATEX.findall(x["texto"])}


@pytest.fixture(scope="module")
def compilados(tmp_path_factory):
    pasta = tmp_path_factory.mktemp("latex_metodologia")
    docs = dict(_exemplos())
    # Contraprovas das correções: a ordem do guia (\label antes de \caption, numa figura da seção 2)
    # e o tipo @Online com BibTeX clássico.
    fig = docs["metodologia-latex-figura-legenda"]
    errado = fig.replace("\\section{Resultados}", "\\section{Introdução}\n\\section{Resultados}")
    errado = errado.replace(
        "  \\caption{Tempo de compilação por número de páginas}\n  \\label{fig:grafico}\n",
        "  \\label{fig:grafico}\n  \\caption{Tempo de compilação por número de páginas}\n",
    )
    assert errado.index("\\label{fig") < errado.index("\\caption")
    docs["contraprova-label-antes"] = errado
    docs["contraprova-online"] = docs["metodologia-bibtex-arquivo-bib"].replace("wilkins1995", "wilkins1995online")
    for n, (erro, _, _) in enumerate(ERROS):
        docs[f"erro-{n}"] = erro
    _preparar(pasta, docs)
    bib_online = pasta / "contraprova-online/refs.bib"
    bib_online.write_text(
        bib_online.read_text(encoding="utf-8")
        + "@Online{wilkins1995online,\n  author = {Wilkins, David R.},\n  title = {Getting started},\n"
        "  url = {https://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/},\n  year = {1995}\n}\n",
        encoding="utf-8",
    )
    compilar(pasta)
    return pasta


def _ler(pasta, nome, ext):
    p = pasta / nome / f"artigo.{ext}"
    return p.read_text(encoding="latin-1") if p.exists() else ""


def _pdf(pasta, nome):
    from pypdf import PdfReader

    r = PdfReader(str(pasta / nome / "artigo.pdf"))
    return r, re.sub(r"\s+", " ", " ".join(p.extract_text() or "" for p in r.pages))


def test_ha_exemplos_de_latex_suficientes():
    assert len(_exemplos()) == 9


@pytest.mark.parametrize("bloco", sorted(_exemplos()))
def test_exemplo_de_latex_compila_sem_erro_nem_referencia_pendente(compilados, bloco):
    log = _ler(compilados, bloco, "log")
    assert (compilados / bloco / "status").read_text().strip() == "0", log[-3000:]
    assert (compilados / bloco / "artigo.pdf").exists()
    assert not re.search(r"^! ", log, re.M), log[-3000:]
    assert "undefined" not in log.replace("Undefined", ""), [x for x in log.splitlines() if "undefined" in x]
    assert "There were undefined references" not in log and "Rerun to get" not in log
    if bloco != "metodologia-monografia-abntex2":  # a própria classe abntex2 ainda pede 'brazil' ao babel
        assert "is deprecated" not in "\n".join(x for x in log.splitlines() if "babel" in x)
    blg = _ler(compilados, bloco, "blg")
    assert "Warning" not in blg and "error message" not in blg, blg


def test_figura_e_tabela_numeradas_e_contraprova_do_label(compilados):
    assert "\\newlabel{fig:grafico}{{1}" in _ler(compilados, "metodologia-latex-figura-legenda", "aux")
    assert "\\newlabel{tab:tempo}{{1}" in _ler(compilados, "metodologia-latex-tabela", "aux")
    # Com o \label antes do \caption (como no guia), o rótulo guarda o número da seção (2), não o da figura.
    assert "\\newlabel{fig:grafico}{{2}" in _ler(compilados, "contraprova-label-antes", "aux")
    _, t = _pdf(compilados, "metodologia-latex-figura-legenda")
    assert "Figura 1" in t and "Figura 1 mostra" in t and "Fonte: elaborado pelo autor" in t


def test_matematica_numera_as_equacoes(compilados):
    aux = _ler(compilados, "metodologia-latex-matematica", "aux")
    assert "\\newlabel{eq:media}{{1}" in aux
    _, t = _pdf(compilados, "metodologia-latex-matematica")
    assert "A média (1)" in t and "(2)" in t and "(3)" in t


def test_documento_minimo_tem_resumo_e_secao_1(compilados):
    _, t = _pdf(compilados, "metodologia-latex-documento-minimo")
    assert "Resumo" in t and "Seção 1" in t and "??" not in t


def test_bibtex_lista_tres_referencias_e_online_e_do_biblatex(compilados):
    assert _ler(compilados, "metodologia-bibtex-arquivo-bib", "bbl").count("\\bibitem") == 3
    blg = _ler(compilados, "contraprova-online", "blg")
    assert 'entry type for "wilkins1995online" isn\'t style-file defined' in blg


def test_abntex2cite_gera_as_duas_formas_de_citacao(compilados):
    _, t = _pdf(compilados, "metodologia-bibtex-abntex2cite")
    assert "Lopez e Silva (2013)" in t and "(LOPEZ; SILVA, 2013, p. 68)" in t and "Referências" in t
    bloco = texto("bibtex-abntex2cite")
    assert "*Lopez e Silva (2013)*" in bloco and "*(LOPEZ; SILVA, 2013, p. 68)*" in bloco


def test_monografia_abntex2_tem_capa_sumario_e_apendice(compilados):
    _, t = _pdf(compilados, "metodologia-monografia-abntex2")
    for trecho in ("Universidade Federal de Alagoas", "Maceió", "Sumário", "1 INTRODUÇÃO", "APÊNDICE A", "Referências"):
        assert trecho in t, trecho


def test_monografia_sem_linha_em_branco_apos_folha_de_rosto_quebra(tmp_path):
    """O bloco avisa: sem a linha em branco, \\imprimirfolhaderosto engole o \\begin{resumo} seguinte."""
    tex = _exemplos()["metodologia-monografia-abntex2"]
    assert "\\imprimirfolhaderosto\n\n\\begin{resumo}" in tex
    _preparar(tmp_path, {"sem-linha": tex.replace("\\imprimirfolhaderosto\n\n", "\\imprimirfolhaderosto\n")})
    compilar(tmp_path)
    assert "Argument of \\begin has an extra }" in _ler(tmp_path, "sem-linha", "log")


def test_beamer_tem_quatro_paginas(compilados):
    r, t = _pdf(compilados, "metodologia-apresentacao-beamer")
    assert len(r.pages) == 4 and "Roteiro" in t


def test_listas_compilam_com_tres_itens_numerados(compilados):
    _, t = _pdf(compilados, "metodologia-latex-listas-citacao-longa")
    assert all(f"{n}. rodar" in t for n in (1, 2, 3)) and "Apêndicetexto do próprio autor" in t.replace(
        "Apêndice texto", "Apêndicetexto"
    )


# Cada mensagem da tabela do bloco de compilação, reproduzida com um documento mínimo:
# (documento, trecho no .log, como o bloco escreve a mensagem).
CABECALHO = r"\documentclass{article}" "\n" r"\begin{document}" "\n"
FIM = "\n" r"\end{document}" "\n"
ERROS = [
    (CABECALHO + r"\textbff{x}" + FIM, "Undefined control sequence", "Undefined control sequence"),
    (CABECALHO + "x_1" + FIM, "Missing $ inserted", "Missing $ inserted"),
    (
        CABECALHO + r"\begin{itemize}\item a" + FIM,
        r"\begin{itemize} on input line 3 ended by \end{document}",
        r"\begin{itemize} … ended by \end{document}",
    ),
    (CABECALHO + r"\textbf{a" "\n\nb}" + FIM, "Runaway argument?", "Paragraph ended before … was complete"),
    (
        CABECALHO + r"\begin{tabular}{ll}a&b&c\\ \end{tabular}" + FIM,
        r"Extra alignment tab has been changed to \cr",
        r"Extra alignment tab has been changed to \cr",
    ),
]


def test_mensagens_de_erro_do_bloco_se_reproduzem(compilados):
    bloco = texto("latex-compilacao-erros")
    for n, (_, no_log, no_bloco) in enumerate(ERROS):
        assert no_log in _ler(compilados, f"erro-{n}", "log"), no_log
        assert no_bloco in bloco, no_bloco


# ---------------------------------------------------------------- normas: conferências por código


def test_resumo_revisado_cabe_e_nao_tem_citacao_nem_primeira_pessoa():
    t = texto("resumo-palavras-chave")
    revisado = t.split("**Versão revisada:**")[1].split("Palavras-chave:")[0]
    palavras = re.findall(r"\w+", revisado)
    assert 30 < len(palavras) < 250
    assert not re.search(r"\(\w+.*?\d{4}\)", revisado) and not re.search(r"\b\w+(amos|emos|aremos)\b", revisado)
    rascunho = t.split("**Rascunho com problemas:**")[1].split("Problemas:")[0]
    assert "falaremos" in rascunho and "(2013)" in rascunho  # os defeitos apontados estão no rascunho
    assert "Palavras-chave: LaTeX. BibTeX. Referências." in t


def test_referencias_em_ordem_alfabetica_e_sem_sinais_de_endereco():
    t = texto("abnt-referencias")
    refs = re.findall(r"^> ([A-ZÀ-Ú]+),", t, re.M)
    assert refs == ["LOPEZ", "WILSON", "WILKINS"]  # na ordem em que o bloco ensina os tipos
    assert sorted(refs) == ["LOPEZ", "WILKINS", "WILSON"] and "(LOPEZ, WILKINS, WILSON)" in t
    linhas = [x for x in t.splitlines() if x.startswith("> ")]
    assert not any("<http" in x or "http" in x and ">" in x.replace("> ", "", 1) for x in linhas)
    assert "DOI: 10.1371/journal.pbio.1001745" in t and "v. 12, n. 1, e1001745, 2014" in t


def test_citacoes_tem_as_duas_grafias_e_secoes_sem_ponto():
    t = texto("abnt-citacoes")
    assert "(FRANÇA et al., 2003, p. 59)" in t and "(França et al., 2003, p. 59)" in t and "(Lopez; Silva, 2013)" in t
    s = texto("abnt-ilustracoes-tabelas-secoes")
    assert re.search(r"Certo: \*\d+(\.\d+)* [A-Z]", s) and "Errado: *2.1. " in s


def test_dados_das_obras_batem_com_o_bib():
    bib = BIBTEX.findall(texto("bibtex-arquivo-bib"))[0]
    assert "volume  = {12}" in bib and "pages   = {e1001745}" in bib and "year    = {2014}" in bib
    assert "year      = {2013}" in bib and "year         = {1995}" in bib
    assert "@Online" not in bib and "@misc{wilkins1995" in bib


# ---------------------------------------------------------------- fórmulas no site


FORMULA = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def _sem_codigo(t):
    return re.sub(r"`[^`\n]*`", "", re.sub(r"```.*?```", "", t, flags=re.S))


def test_formulas_fora_do_codigo_tem_delimitadores_fechados():
    for x in ITENS.values():
        assert _sem_codigo(x["texto"]).count("$") % 2 == 0, x["id"]


@pytest.mark.skipif(not shutil.which("node"), reason="node indisponível")
def test_formulas_renderizam_no_katex_do_site():
    formulas = [a or b for x in ITENS.values() for a, b in FORMULA.findall(_sem_codigo(x["texto"]))]
    assert len(formulas) >= 3
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


# ---------------------------------------------------------------- busca e isolamento

EXEMPLOS = [
    (
        "Como fazer uma referência bibliográfica no LaTeX com BibTeX?",
        {"metodologia-bibtex-arquivo-bib", "metodologia-bibtex-abntex2cite"},
    ),
    (
        "Quais as seções de um artigo científico?",
        {"metodologia-artigo-estrutura", "metodologia-artigo-secoes-textuais"},
    ),
    ("Como citar um artigo segundo a ABNT?", {"metodologia-abnt-citacoes", "metodologia-abnt-referencias"}),
    ("Como inserir uma figura com legenda no LaTeX?", {"metodologia-latex-figura-legenda"}),
    ("Como escrever o resumo de um artigo científico?", {"metodologia-resumo-palavras-chave"}),
]
FORA = [
    "Como simplificar uma função com mapa de Karnaugh?",
    "Como fazer um LEFT JOIN em SQL?",
    "Me conte uma piada",
    "Qual a transformada de Laplace de e^{-at}?",
]


def test_exemplos_do_cadastro_sao_os_testados():
    assert list(MET.exemplos) == [p for p, _ in EXEMPLOS]


@pytest.mark.parametrize("pergunta, aceitos", EXEMPLOS)
def test_perguntas_de_exemplo_trazem_o_bloco_certo(pergunta, aceitos):
    assert aceitos & set(hibrida(pergunta))
    assert aceitos & set(buscar(pergunta)[:3])


@pytest.mark.parametrize("pergunta", FORA)
def test_pergunta_de_outra_area_nao_traz_material(pergunta):
    assert hibrida(pergunta) == []


def test_isolamento_com_ingles_instrumental_nos_dois_sentidos():
    ing = disciplinas.obter("ingles")
    for p, _ in EXEMPLOS:
        assert all(x.startswith("ingles-") for x in buscar(p, ing))
    for p in ing.exemplos:
        assert all(x.startswith("metodologia-") for x in buscar(p))


# ---------------------------------------------------------------- catálogo, autoria e o que não é versionado


def test_catalogo_completo_e_coerente():
    obrigatorios = {
        "id",
        "nome",
        "autoria",
        "url",
        "idioma",
        "formato",
        "topicos",
        "licenca",
        "acesso",
        "qualidade",
        "prioridade",
        "uso",
        "origem",
        "justificativa",
    }
    assert len(CATALOGO) == len(FONTES)
    for f in FONTES:
        assert obrigatorios <= set(f), f["id"]
        assert f["prioridade"] in ("alta", "media", "referencia")
        assert f["uso"] in ("acervo", "citada", "referencia")
        assert set(f["topicos"]) <= set(MET.assuntos), f["id"]
    assert {x for i in ITENS.values() for x in i["fontes_catalogo"]} <= set(CATALOGO)
    assert {i for i, f in CATALOGO.items() if f["uso"] == "acervo"} == {
        x for i in ITENS.values() if i["natureza"] == "material_da_disciplina" for x in i["fontes_catalogo"]
    }


def test_blocos_que_adaptam_obra_cc_by_sa_herdam_a_licenca():
    for x in ITENS.values():
        if x["natureza"] == "material_da_disciplina" and "lopez-silva-2013-latex" in x["fontes_catalogo"]:
            if "adapta" in x["licenca"] or LATEX.search(x["texto"]):
                assert x["licenca"].startswith("CC BY-SA 3.0"), x["id"]


def test_originais_binarios_e_dados_pessoais_fora_do_repositorio():
    arquivos = [p for p in PASTA.rglob("*") if p.is_file()]
    arquivos += [p for p in (ROOT / "tests_acervo/latex_metodologia").rglob("*") if p.is_file()]
    proibidos = (".pdf", ".png", ".jpg", ".jpeg", ".webp", ".docx", ".doc", ".jar", ".zip", ".aux", ".log")
    assert not [p for p in arquivos if p.suffix.lower() in proibidos]
    email = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")
    for p in arquivos:
        assert not email.search(p.read_text(encoding="utf-8")), p  # o modelo da turma traz e-mails das autoras
    assert not (ROOT / "JabRef-2.10.jar").exists()


def test_documentacao_lista_fontes_e_blocos():
    curadoria = (PASTA / "CURADORIA.md").read_text(encoding="utf-8")
    assert [i for i in CATALOGO if f"`{i}`" not in curadoria] == []
    assert [i for i in ITENS if f"`{i}`" not in curadoria] == []
    assert "ECOM018" in curadoria and "em validação" in curadoria
