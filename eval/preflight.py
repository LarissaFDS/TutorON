"""Pré-voo da matriz no servidor: confere tudo o que faria a rodada falhar no meio ou medir a coisa errada.

    python eval/preflight.py --rodada 1                      # baseline: só o #21 no checkout
    python eval/preflight.py --rodada 2                      # integração #21 + #23 + #24, antes de reindexar
    python eval/preflight.py --rodada 2 --pos-indexacao      # depois de reindexar: exige os 5 materiais da equipe

Não chama nenhum modelo de resposta e nunca imprime a chave: só diz se ela existe.
Sai com código 1 se algum item der FALHA. Roteiro completo em eval/rodar_servidor.md.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "eval"))

from backend.config import load_settings  # noqa: E402

# Estimativas grosseiras (segundos por chamada, sem contar o intervalo nem esperas por 429).
SEGUNDOS_GERACAO = 25
SEGUNDOS_JUIZ = 10
CONDICOES_POR_RODADA = {1: "generico,atual_sem_rag,atual_rag,novo_sem_rag,novo_rag", 2: "atual_rag,novo_rag"}
MATERIAIS_EQUIPE = 5


class Checagem:
    def __init__(self) -> None:
        self.falhas = 0

    def ok(self, msg: str) -> None:
        print(f"  OK     {msg}")

    def aviso(self, msg: str) -> None:
        print(f"  AVISO  {msg}")

    def falha(self, msg: str) -> None:
        self.falhas += 1
        print(f"  FALHA  {msg}")


def git(*args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def tem_pr23() -> bool:
    """#23 (corte de relevância): a busca aceita penalidade de hub."""
    import inspect

    from acervo import retrieval

    return "hub_penalty" in inspect.signature(retrieval.search).parameters


def tem_pr24() -> bool:
    """#24 (curadoria de PD): módulo e pasta dos materiais da equipe."""
    return (ROOT / "acervo" / "equipe.py").exists() and (ROOT / "materiais" / "Equipe").is_dir()


def estimar(n_perguntas: int, condicoes: list[str], juizes: int, intervalo: float) -> dict:
    geracoes = n_perguntas * 2 * len(condicoes)  # modelo forte e lite
    julgamentos = geracoes * juizes
    segundos = geracoes * (SEGUNDOS_GERACAO + intervalo) + julgamentos * (SEGUNDOS_JUIZ + intervalo)
    return {"geracoes": geracoes, "julgamentos": julgamentos, "chamadas": geracoes + julgamentos,
            "minutos": round(segundos / 60), "por_minuto": round(60 / (SEGUNDOS_JUIZ + intervalo), 1)}


def checar_chave(c: Checagem, settings) -> None:
    if settings.gemini_api_key:
        c.ok("GEMINI_API_KEY presente (valor não exibido)")
    else:
        c.falha("GEMINI_API_KEY ausente: coloque no .env da raiz (não cole a chave em nenhum outro lugar)")


def checar_ollama(c: Checagem, settings) -> None:
    modelo = settings.embed_model
    try:
        tags = httpx.get(settings.ollama_url + "/api/tags", timeout=5).json()
    except (httpx.HTTPError, ValueError) as exc:
        c.falha(f"Ollama fora do ar em {settings.ollama_url} ({type(exc).__name__}): a busca cairia para léxica")
        return
    nomes = [m.get("name", "") for m in tags.get("models", [])]
    if not any(n == modelo or n.startswith(modelo + ":") for n in nomes):
        c.falha(f"Ollama no ar, mas sem o {modelo} (instalados: {', '.join(nomes) or 'nenhum'})")
        return
    try:
        r = httpx.post(settings.ollama_url + "/api/embed", timeout=60,
                       json={"model": modelo, "input": ["teste"], "options": {"num_gpu": 0}})
        r.raise_for_status()
        dim = len(r.json()["embeddings"][0])
    except (httpx.HTTPError, ValueError, KeyError, IndexError) as exc:
        c.falha(f"{modelo} instalado, mas o embedding falhou ({type(exc).__name__})")
        return
    c.ok(f"Ollama no ar com {modelo} (embedding de teste com {dim} dimensões)")


def checar_indice(c: Checagem, settings, rodada: int, pos_indexacao: bool) -> None:
    caminho = ROOT / "04-rag" / "indice.json"
    try:
        indice = json.loads(caminho.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        c.falha(f"não consegui ler {caminho.relative_to(ROOT)} ({type(exc).__name__})")
        return
    chunks, vetores = indice.get("chunks", []), indice.get("vectors", [])
    equipe = [i for i, ch in enumerate(chunks) if ch.get("tipo") == "material_equipe"]
    if not chunks:
        c.falha("índice vazio")
    elif len(vetores) != len(chunks) or indice.get("modo") != "hibrido":
        c.falha(f"índice sem vetores ({len(vetores)} vetores para {len(chunks)} blocos, modo {indice.get('modo')}); "
                "a busca seria só léxica")
    elif indice.get("embedding_model") != settings.embed_model:
        c.falha(f"índice feito com {indice.get('embedding_model')}, mas a busca usa {settings.embed_model}")
    else:
        c.ok(f"índice com {len(chunks)} blocos e {len(vetores)} vetores ({indice.get('embedding_model')})")
    if rodada == 1 and equipe:
        c.falha(f"o índice já tem {len(equipe)} materiais da equipe: a rodada 1 precisa do índice do #21 "
                "(restaure o backup ou `git checkout -- 04-rag/indice.json`)")
    if rodada == 2:
        if len(equipe) >= MATERIAIS_EQUIPE:
            c.ok(f"{len(equipe)} materiais da equipe no índice")
        elif pos_indexacao:
            c.falha(f"só {len(equipe)} de {MATERIAIS_EQUIPE} materiais da equipe no índice: reindexe com --embeddings")
        else:
            c.aviso(f"{len(equipe)} materiais da equipe no índice; normal antes de reindexar "
                    "(rode de novo com --pos-indexacao depois)")
    if git("status", "--porcelain", "--", "04-rag/indice.json"):
        msg = "04-rag/indice.json difere do commit"
        if rodada == 1:
            c.falha(msg + ": a rodada 1 mede o índice versionado; restaure-o antes")
        else:
            c.aviso(msg + " (esperado depois de reindexar; não faça commit dele sem decidir)")


def checar_checkout(c: Checagem, rodada: int) -> None:
    ramo = git("rev-parse", "--abbrev-ref", "HEAD") or "?"
    commit = git("rev-parse", "--short", "HEAD") or "?"
    print(f"  INFO   checkout: {ramo} @ {commit}")
    if git("status", "--porcelain", "--untracked-files=no", "--", "backend", "acervo", "eval"):
        c.aviso("há mudanças não commitadas em backend/, acervo/ ou eval/: o resultado não corresponde ao commit")
    if not (ROOT / "eval" / "matriz.py").exists():
        c.falha("eval/matriz.py ausente: o #21 não está no checkout")
    pr23, pr24 = tem_pr23(), tem_pr24()
    print(f"  INFO   #23 (corte de relevância) no checkout: {'sim' if pr23 else 'não'}; "
          f"#24 (curadoria de PD): {'sim' if pr24 else 'não'}")
    if rodada == 1:
        if pr23 or pr24:
            c.falha("a rodada 1 (baseline) precisa rodar SEM os #23 e #24; faça checkout só do #21")
        else:
            c.ok("baseline: sem #23 e #24")
    else:
        if pr23 and pr24:
            c.ok("integração: #23 e #24 presentes")
        else:
            c.falha("a rodada 2 precisa do #21 + #23 + #24 mesclados no checkout")
        settings = load_settings()
        if not hasattr(settings, "acervo_usar_nao_revisados"):
            c.falha("o #24 deste checkout não tem o filtro de material não revisado; atualize a branch")
        elif settings.acervo_usar_nao_revisados:
            c.aviso("ACERVO_USAR_NAO_REVISADOS ligado no ambiente/.env: o SITE também passaria a usar material "
                    "não revisado. Para a matriz basta `gerar --incluir-nao-revisados`")
        if hasattr(settings, "acervo_min_similarity"):
            print(f"  INFO   corte de similaridade do acervo: {settings.acervo_min_similarity} "
                  "(ajuste ACERVO_SIMILARIDADE_MINIMA depois do `diagnostico.py calibrar`)")


def checar_saida(pasta: Path) -> None:
    respostas = pasta / "respostas.jsonl"
    if respostas.exists():
        n = sum(1 for linha in respostas.read_text(encoding="utf-8").splitlines() if linha.strip())
        print(f"  INFO   {pasta.relative_to(ROOT)} já tem {n} respostas: o `gerar` retoma de onde parou")
    else:
        print(f"  INFO   saída nova: {pasta.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rodada", type=int, choices=(1, 2), required=True)
    parser.add_argument("--perguntas", default="A1,A2,A3")
    parser.add_argument("--condicoes", help="padrão: as 5 na rodada 1; atual_rag,novo_rag na rodada 2")
    parser.add_argument("--juizes", type=int, default=2, help="quantos juízes vão julgar (2 mede autopreferência)")
    parser.add_argument("--intervalo", type=float, default=4.0, help="o mesmo --intervalo do gerar/julgar")
    parser.add_argument("--pos-indexacao", action="store_true", help="rodada 2 depois de reindexar")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    settings = load_settings()
    c = Checagem()
    print(f"Pré-voo da rodada {args.rodada}\n")
    print("Checkout")
    checar_checkout(c, args.rodada)
    print("Chave e modelos")
    checar_chave(c, settings)
    checar_ollama(c, settings)
    print("Índice do acervo")
    checar_indice(c, settings, args.rodada, args.pos_indexacao)
    print("Saída")
    checar_saida(ROOT / "eval" / "results" / f"rodada{args.rodada}")

    import matriz

    n = len(matriz.perguntas(args.perguntas))
    condicoes = (args.condicoes or CONDICOES_POR_RODADA[args.rodada]).split(",")
    e = estimar(n, condicoes, args.juizes, args.intervalo)
    print("\nCusto estimado (sem novas tentativas por 429)")
    print(f"  {n} perguntas x 2 modelos x {len(condicoes)} braços = {e['geracoes']} gerações; "
          f"x {args.juizes} juízes = {e['julgamentos']} julgamentos; {e['chamadas']} chamadas Gemini no total")
    print(f"  ~{e['minutos']} min com --intervalo {args.intervalo:g} (ritmo de ~{e['por_minuto']} chamadas/min no julgamento)")
    print("  ATENÇÃO: se a chave do .env é a mesma do site, essas chamadas saem da MESMA cota dos alunos.\n"
          "  Rode fora do horário de uso ou com outra chave; um 429 aqui pode derrubar o site para o modelo lite.")
    print("\nResultado: " + ("pronto para rodar." if not c.falhas else f"{c.falhas} falha(s); corrija antes de rodar."))
    return 1 if c.falhas else 0


if __name__ == "__main__":
    raise SystemExit(main())
