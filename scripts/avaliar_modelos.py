"""Avaliação rápida do MVP: as mesmas perguntas em várias condições, com respostas reais.

Condições:
  tutoron_gemini   RAG + prompt TutorON, cascata Gemini (o que o aluno recebe no modo Tutor)
  generico_gemini  mesma pergunta crua, no mesmo modelo Gemini que respondeu acima
  tutoron_local    RAG + prompt TutorON no modelo local atual (qwen3:8b com raciocínio)
  tutoron_antigo   RAG + prompt TutorON no modelo local anterior (tutoron-paa-qwen25 = qwen2.5:7b), se existir
  generico_local   pergunta crua no qwen3:8b

Uso: python scripts/avaliar_modelos.py [--perguntas arquivo.json] [--saida dados/avaliacao/x.json]
O arquivo de perguntas é uma lista de {"id", "pergunta", "referencia"}.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from backend import prompts  # noqa: E402
from backend.config import load_settings  # noqa: E402
from backend.llm import LLM, AllUnavailable, Model  # noqa: E402
from backend.rag import contexto, recuperar  # noqa: E402


async def rodar(perguntas: list[dict], saida: Path, condicoes: list[str]) -> None:
    settings = load_settings()
    llm = LLM(settings)
    locais = {m["name"] for m in (await llm.client.get(settings.ollama_url + "/api/tags")).json()["models"]}
    resultados = json.loads(saida.read_text(encoding="utf-8")) if saida.exists() else []
    resultados = [r for r in resultados if r.get("texto")]  # falhas anteriores são refeitas
    feitos = {(r["id"], r["condicao"]) for r in resultados}
    gemini = [m for m in llm.cascade() if m.provider == "gemini"]

    for q in perguntas:
        trechos = await recuperar(q["pergunta"], llm, settings)
        prompt_tutor = prompts.prompt_tutor(q["pergunta"], contexto(trechos))
        prompt_gen = prompts.prompt_generico(q["pergunta"])
        planos = {
            "tutoron_gemini": (prompts.SISTEMA_TUTOR, prompt_tutor, gemini),
            "generico_gemini": (None, prompt_gen, None),  # definido depois do tutoron_gemini
            "tutoron_local": (prompts.SISTEMA_TUTOR, prompt_tutor, [Model("ollama", settings.local_model)]),
            "tutoron_antigo": (prompts.SISTEMA_TUTOR, prompt_tutor, [Model("ollama", "tutoron-paa-qwen25")]),
            "generico_local": (None, prompt_gen, [Model("ollama", settings.local_generic_model)]),
        }
        for condicao in condicoes:
            if (q["id"], condicao) in feitos:
                continue
            sistema, prompt, modelos = planos[condicao]
            if condicao == "generico_gemini":
                anterior = next((r for r in resultados if r["id"] == q["id"] and r["condicao"] == "tutoron_gemini"
                                 and r.get("provedor") == "gemini"), None)
                modelos = [Model("gemini", anterior["modelo"])] if anterior else gemini
            if condicao == "tutoron_antigo" and "tutoron-paa-qwen25:latest" not in locais:
                continue
            if not gemini and "gemini" in condicao:
                continue
            print(f"[{q['id']}] {condicao}…", flush=True)
            inicio = time.monotonic()
            try:
                for tentativa in range(3 if condicao == "generico_gemini" else 1):
                    try:
                        r = await llm.complete(sistema, prompt, models=modelos)
                        break
                    except AllUnavailable:
                        if tentativa == 2:
                            # O mesmo modelo segue fora: usa a cascata e registra o modelo usado.
                            r = await llm.complete(sistema, prompt, models=gemini)
                            break
                        llm.breaker.reset(modelos[0])
                        await asyncio.sleep(8)
                registro = {"texto": r.text, "provedor": r.model.provider, "modelo": r.model.name,
                            "segundos": round(r.seconds, 1), "tentativas": r.attempts}
            except AllUnavailable as exc:
                registro = {"texto": None, "erro": "nenhum modelo disponível", "tentativas": exc.attempts,
                            "segundos": round(time.monotonic() - inicio, 1)}
            resultados.append({"id": q["id"], "pergunta": q["pergunta"], "referencia": q["referencia"],
                               "condicao": condicao, "fontes": [t.publico() for t in trechos] if "tutoron" in condicao else [],
                               "data": datetime.now().isoformat(timespec="seconds"), **registro})
            saida.parent.mkdir(parents=True, exist_ok=True)
            saida.write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"    -> {registro.get('modelo', registro.get('erro'))} em {registro['segundos']} s", flush=True)
    await llm.client.aclose()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--perguntas", default=str(ROOT / "06-avaliacao/perguntas-mvp.json"))
    parser.add_argument("--saida", default=str(ROOT / "06-avaliacao/resultados-mvp.json"))
    parser.add_argument("--condicoes", default="tutoron_gemini,generico_gemini,tutoron_local,tutoron_antigo,generico_local")
    args = parser.parse_args()
    perguntas = json.loads(Path(args.perguntas).read_text(encoding="utf-8"))
    asyncio.run(rodar(perguntas, Path(args.saida), args.condicoes.split(",")))


if __name__ == "__main__":
    main()
