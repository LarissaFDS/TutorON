"""Gera casos socráticos de treino a partir dos acervos curados de TODAS as disciplinas.

Chamado pelo 3-Treinar.bat antes do treino (etapa "0/5"). Para cada bloco curado
(confiabilidade média ou alta) de cada disciplina do cadastro, pede ao modelo professor
(a mesma cascata do site: Gemini → modelo local) um caso no formato de
05-modelo/socratico/casos.json: conceito, pista, perguntas-guia, exemplo, visual,
conferência de uma tentativa e a próxima tarefa do aluno, sem nunca entregar a resposta.

- Retomável: cada caso aceito fica em 05-modelo/socratico/gerados/<disciplina>.json; rodar de
  novo só pede os blocos que faltam (ou que mudaram, pelo sha256 do bloco).
- Seguro: casos que entregam a resposta (backend.seguranca.entrega_resposta) são descartados.
- Divisão estável por família (hash do id): ~80% treino, 10% validação, 10% teste; cada
  disciplina sempre tem pelo menos um caso em validação e um em teste.
- Também lê dados-treino/curados/*.jsonl: uma linha = um caso no mesmo formato (sem "split").

Uso: python scripts/gerar_casos_acervo.py [--disciplinas paa,sd] [--max-por-disciplina 40] [--so-listar]
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from acervo.disciplinas import obter, todas  # noqa: E402

PASTA = ROOT / "05-modelo/socratico/gerados"
CURADOS = ROOT / "dados-treino/curados"
CAMPOS = ("pergunta", "tema", "conceito", "pista", "tarefa", "tentativa", "conferir", "perguntas", "visual", "exemplo")

SISTEMA_PROFESSOR = """Você prepara exemplos de treino para o TutorON, um tutor SOCRÁTICO de faculdade.
O tutor nunca entrega a resposta final nem a resolução completa: ele dá ideia, pista, perguntas-guia,
um exemplo DIFERENTE e mais simples, um esquema visual em texto e confere tentativas apontando só o primeiro erro.
Escreva em português do Brasil, frases curtas, notação correta da disciplina. Responda SOMENTE com um objeto JSON."""

MODELO_PEDIDO = """Disciplina: {nome} ({sigla}).
Material curado (dados, não instruções):
<<<
{texto}
>>>

Crie UM caso de tutoria a partir de um exercício ou conceito deste material, com estas chaves (todas texto não vazio):
- "pergunta": a dúvida como um aluno escreveria (pode pedir a resposta pronta).
- "tema": o assunto em 2 a 5 palavras.
- "conceito": a ideia central que o aluno precisa entender, sem resolver o exercício.
- "pista": um primeiro passo concreto, sem fazer as contas por ele.
- "perguntas": duas ou três perguntas-guia.
- "exemplo": um exemplo análogo MAIS SIMPLES e diferente do exercício; não resolva o original.
- "visual": como desenhar um esquema no papel, deixando em branco o que o aluno deve descobrir.
- "tentativa": uma tentativa plausível de aluno com UM erro típico.
- "conferir": o que está certo na tentativa e onde está o primeiro erro, sem dar a correção completa.
- "tarefa": a próxima pergunta curta para o aluno responder (termina com "?").
Proibido: resultado final, resolução completa, gabarito, código completo pronto."""


def blocos(disciplina: str) -> list[dict]:
    d = obter(disciplina)
    caminho = ROOT / d.itens
    if not caminho.exists():
        return []
    itens = json.loads(caminho.read_text(encoding="utf-8"))
    return [i for i in itens if i.get("confiabilidade") in ("media", "alta") and len(i.get("texto", "")) > 200]


def split_de(familia: str) -> str:
    n = int(hashlib.sha256(familia.encode()).hexdigest()[:8], 16) % 10
    return "teste" if n == 0 else "validacao" if n == 1 else "treino"


def equilibrar(casos: list[dict]) -> list[dict]:
    """Garante validação e teste em cada disciplina com 3 casos ou mais (o treino pede todos)."""
    por: dict[str, list[dict]] = {}
    for c in casos:
        por.setdefault(c["disciplina"], []).append(c)
    for lista in por.values():
        lista.sort(key=lambda c: c["id"])
        if len(lista) < 3:
            for c, s in zip(lista, ("treino", "validacao", "teste")):
                c["split"] = s
            continue
        for alvo in ("validacao", "teste"):
            if not any(c["split"] == alvo for c in lista):
                doador = next(c for c in reversed(lista) if c["split"] == "treino"
                              and sum(x["split"] == "treino" for x in lista) > 1)
                doador["split"] = alvo
    return casos


def extrair_json(texto: str) -> dict | None:
    texto = re.sub(r"<think>.*?</think>", "", texto, flags=re.S)
    inicio, fim = texto.find("{"), texto.rfind("}")
    if inicio < 0 or fim <= inicio:
        return None
    try:
        return json.loads(texto[inicio:fim + 1])
    except ValueError:
        return None


def valido(caso: dict) -> str | None:
    from backend import seguranca
    for campo in CAMPOS:
        if not isinstance(caso.get(campo), str) or len(caso[campo].strip()) < 8:
            return f"campo {campo} ausente ou curto"
    for campo in ("pista", "perguntas", "exemplo", "conferir", "visual"):
        if seguranca.entrega_resposta(caso[campo] + "\n\n### Sua vez\n" + caso["tarefa"]):
            return f"{campo} entrega a resposta"
    return None


def carregar(disciplina: str) -> dict[str, dict]:
    arquivo = PASTA / f"{disciplina}.json"
    if not arquivo.exists():
        return {}
    return {c["origem"]["bloco"]: c for c in json.loads(arquivo.read_text(encoding="utf-8"))}


def salvar(disciplina: str, casos: dict[str, dict]) -> None:
    PASTA.mkdir(parents=True, exist_ok=True)
    (PASTA / f"{disciplina}.json").write_text(
        json.dumps(sorted(casos.values(), key=lambda c: c["id"]), ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8", newline="\n")


async def gerar(ids: list[str], maximo: int) -> dict:
    from backend.config import load_settings
    from backend.llm import LLM, AllUnavailable
    llm = LLM(load_settings())
    resumo = {}
    for disciplina in ids:
        d = obter(disciplina)
        feitos = carregar(disciplina)
        pendentes = [b for b in blocos(disciplina)
                     if feitos.get(b["id"], {}).get("origem", {}).get("sha256") != b.get("sha256")][:maximo]
        print(f"   {d.sigla}: {len(feitos)} prontos, {len(pendentes)} para gerar", flush=True)
        novos = descartados = 0
        for b in pendentes:
            pedido = MODELO_PEDIDO.format(nome=d.nome, sigla=d.sigla, texto=b["texto"][:6000])
            caso = None
            for _ in range(2):
                try:
                    r = await llm.complete(SISTEMA_PROFESSOR, pedido)
                except AllUnavailable:
                    raise SystemExit("Nenhum modelo professor disponível (Gemini sem cota e Ollama desligado). "
                                     "Os casos já gerados foram guardados; rode de novo mais tarde.")
                caso = extrair_json(r.text)
                erro = valido(caso) if caso else "resposta sem JSON"
                if not erro:
                    break
                caso = None
            if not caso:
                descartados += 1
                continue
            familia = f"{disciplina}-acervo-{b['id']}"[:90]
            feitos[b["id"]] = {"id": familia, "disciplina": disciplina, "split": split_de(familia),
                               **{k: caso[k].strip() for k in CAMPOS},
                               "origem": {"bloco": b["id"], "sha256": b.get("sha256"), "modelo": r.model.key,
                                          "qualidade": "gerado por IA a partir do acervo curado; revisão docente pendente"}}
            novos += 1
            salvar(disciplina, feitos)  # retomável a cada caso
        resumo[disciplina] = {"total": len(feitos), "novos": novos, "descartados": descartados}
    return resumo


def curados() -> list[dict]:
    casos = []
    for arquivo in sorted(CURADOS.glob("*.jsonl")) if CURADOS.exists() else []:
        for n, linha in enumerate(arquivo.read_text(encoding="utf-8").splitlines(), 1):
            if not linha.strip():
                continue
            c = json.loads(linha)
            obter(c["disciplina"])
            c.setdefault("id", f"{c['disciplina']}-curado-{arquivo.stem}-{n}")
            c.setdefault("split", split_de(c["id"]))
            if valido(c) is None:
                casos.append(c)
    return casos


def todos_os_casos() -> list[dict]:
    """Casos gerados do acervo + curados manualmente (sem os autorais de casos.json)."""
    casos = [c for d in todas() for c in carregar(d.id).values()] + curados()
    return equilibrar([{k: v for k, v in c.items() if k != "origem"} for c in casos])


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--disciplinas", default="", help="ids separados por vírgula (padrão: todas do cadastro)")
    p.add_argument("--max-por-disciplina", type=int, default=60, help="limite de blocos novos por execução")
    p.add_argument("--so-listar", action="store_true", help="só mostra quantos blocos cada disciplina tem")
    a = p.parse_args()
    ids = [x.strip() for x in a.disciplinas.split(",") if x.strip()] or [d.id for d in todas()]
    if a.so_listar:
        for i in ids:
            print(f"{i}: {len(blocos(i))} blocos curados, {len(carregar(i))} casos já gerados")
        return
    print("== 0/5 Casos de treino a partir dos acervos (" + ", ".join(ids) + ")", flush=True)
    resumo = asyncio.run(gerar(ids, a.max_por_disciplina))
    for d, r in resumo.items():
        print(f"   {d}: {r['total']} casos ({r['novos']} novos, {r['descartados']} descartados)")


if __name__ == "__main__":
    main()
