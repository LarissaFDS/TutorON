"""Decisão da Fase 2 a partir do resumo.json das rodadas da matriz.

    python eval/decidir.py --rodada1 eval/results/rodada1/resumo.json --rodada2 eval/results/rodada2/resumo.json

Rodada 1 = baseline (só o #21). Rodada 2 = integração (#21 + #23 + #24, índice refeito), só atual_rag e
novo_rag. Imprime a decisão e grava eval/results/decisao.md.

Os limiares abaixo são HEURÍSTICOS: escolhidos pela equipe antes de ver os resultados, não derivados de
um teste estatístico. Com 3 perguntas, cada diferença tem n <= 3; a folha cega do aluno é a validação final.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

# ----------------------------------------------------------------- limiares (heurísticos)
NOTA_MINIMA_ORIGINAIS = 4      # (a) critérios a, b e d nas 3 perguntas originais do aluno
LIMIAR_ROTEAMENTO = 0.5        # (b) "modelo (forte - lite)" a partir do qual vale abrir o PR de roteamento
LIMIAR_H4 = -0.3               # (c) "RAG (com - sem), prompt atual" até o qual o RAG atual atrapalha
LIMIAR_CURADORIA = 0.3         # (d) |rodada 2 - rodada 1| abaixo disso conta como sem efeito
BRACOS_CURADORIA = ("atual_rag", "novo_rag")
ORIGINAIS = tuple(q["id"] for q in json.loads((Path(__file__).parent / "perguntas.json").read_text(encoding="utf-8"))
                  if q.get("original_aluno"))


def _media(valores) -> float | None:
    valores = [v for v in valores if v is not None]
    return round(statistics.fmean(valores), 2) if valores else None


def _dif(resumo: dict, chave: str) -> float | None:
    return (resumo.get("efeitos", {}).get(chave) or {}).get("dif")


def _papeis(resumo: dict) -> list[str]:
    return [p for p in ("forte", "lite") if p in resumo.get("modelos", {})]


def originais_ok(resumo: dict, papel: str) -> bool | None:
    """Critérios a, b e d >= NOTA_MINIMA_ORIGINAIS no novo_rag de cada pergunta original julgada."""
    notas = [v.get(c, 0) for k, v in (resumo.get("por_criterio") or {}).items()
             if k in {f"{i}|{papel}|novo_rag" for i in ORIGINAIS} for c in "abd"]
    return None if not notas else all(n >= NOTA_MINIMA_ORIGINAIS for n in notas)


def prompt_aprovado(resumo: dict) -> dict:
    """(a) #25 sai do rascunho se, em todos os modelos com dados, novo_rag >= genérico (pareado, do relatório)
    e a, b, d >= NOTA_MINIMA_ORIGINAIS nas perguntas originais do aluno."""
    por_papel = {}
    for p in _papeis(resumo):
        cs = resumo.get("criterio_sucesso", {}).get(p, {})
        originais = originais_ok(resumo, p)
        iguala = cs.get("iguala_ou_supera")
        por_papel[p] = {"novo_rag": cs.get("novo_rag"), "generico": cs.get("generico"), "iguala_ou_supera": iguala,
                        "originais_ok": originais,
                        "ok": None if iguala is None or originais is None else bool(iguala and originais)}
    valores = [v["ok"] for v in por_papel.values()]
    decisao = None if not valores or None in valores else all(valores)
    return {"aprovado": decisao, "por_papel": por_papel}


def prompt_aprovado_com_curadoria(r1: dict, r2: dict) -> dict:
    """(a') Mesmo critério, com novo_rag da rodada 2 contra o genérico da rodada 1 (o genérico não usa o acervo)."""
    juiz = juiz_comum(r1, r2)
    if juiz is None:
        return {"aprovado": None, "por_papel": {}, "juiz": None}
    n1, n2 = r1["notas"][juiz], r2["notas"][juiz]
    por_papel = {}
    for p in _papeis(r2):
        ids = sorted({k.split("|")[0] for k in n2 if k.endswith(f"|{p}|novo_rag")} &
                     {k.split("|")[0] for k in n1 if k.endswith(f"|{p}|generico")})
        novo = _media(n2[f"{i}|{p}|novo_rag"] for i in ids)
        gen = _media(n1[f"{i}|{p}|generico"] for i in ids)
        originais = originais_ok(r2, p)
        iguala = None if novo is None or gen is None else novo >= gen
        por_papel[p] = {"novo_rag": novo, "generico": gen, "perguntas": len(ids), "iguala_ou_supera": iguala,
                        "originais_ok": originais,
                        "ok": None if iguala is None or originais is None else bool(iguala and originais)}
    valores = [v["ok"] for v in por_papel.values()]
    return {"aprovado": None if not valores or None in valores else all(valores), "por_papel": por_papel, "juiz": juiz}


def roteamento(resumo: dict, braco: str) -> dict:
    """(b) PR de roteamento só se o modelo forte ganhar do lite por >= LIMIAR_ROTEAMENTO no braço que vai a produção."""
    dif = _dif(resumo, f"modelo (forte - lite): {braco}")
    return {"braco": braco, "dif": dif, "abrir_pr": None if dif is None else dif >= LIMIAR_ROTEAMENTO}


def h4(resumo: dict) -> dict:
    """(c) H4: o RAG atual atrapalha se "RAG (com - sem), prompt atual" <= LIMIAR_H4 em algum modelo."""
    difs = {p: _dif(resumo, f"{p}: RAG (com - sem), prompt atual") for p in _papeis(resumo)}
    conhecidos = [d for d in difs.values() if d is not None]
    return {"por_papel": difs, "confirmada": None if not conhecidos else any(d <= LIMIAR_H4 for d in conhecidos)}


def juiz_comum(r1: dict, r2: dict) -> str | None:
    """O juiz das tabelas da rodada 1, se também julgou a rodada 2; senão, qualquer juiz das duas."""
    n1, n2 = r1.get("notas") or {}, r2.get("notas") or {}
    comuns = [j for j in n1 if j in n2]
    if r1.get("juiz") in comuns:
        return r1["juiz"]
    return sorted(comuns)[0] if comuns else None


def curadoria(r1: dict, r2: dict) -> dict:
    """(d) Efeito da curadoria = rodada 2 - rodada 1, pareado por (pergunta, modelo), com o mesmo juiz."""
    juiz = juiz_comum(r1, r2)
    if juiz is None:
        return {"juiz": None, "bracos": {}}
    n1, n2 = r1["notas"][juiz], r2["notas"][juiz]
    bracos = {}
    for braco in BRACOS_CURADORIA:
        for p in sorted({k.split("|")[1] for k in n2 if k.endswith("|" + braco)}):
            chaves = [k for k in n2 if k.endswith(f"|{p}|{braco}") and k in n1]
            difs = [n2[k] - n1[k] for k in chaves]
            dif = _media(difs)
            efeito = None if dif is None else (
                "ajudou" if dif >= LIMIAR_CURADORIA else "piorou" if dif <= -LIMIAR_CURADORIA else "sem efeito claro")
            bracos[f"{p}|{braco}"] = {"dif": dif, "n": len(difs), "vence": sum(d > 0 for d in difs),
                                      "perde": sum(d < 0 for d in difs), "efeito": efeito}
    return {"juiz": juiz, "bracos": bracos}


def decidir(r1: dict, r2: dict | None = None) -> dict:
    a = prompt_aprovado(r1)
    a2 = prompt_aprovado_com_curadoria(r1, r2) if r2 else None
    braco = "novo_rag" if a["aprovado"] else "atual_rag"
    return {"a": a, "a_curadoria": a2, "b": roteamento(r1, braco), "c": h4(r1),
            "d": curadoria(r1, r2) if r2 else None}


def _fmt(x) -> str:
    return "–" if x is None else f"{x:+.2f}" if isinstance(x, float) else str(x)


def _sim(x, sim="sim", nao="não") -> str:
    return "sem dados" if x is None else sim if x else nao


def texto(d: dict) -> str:
    linhas = ["# Decisão da Fase 2", "",
              f"Limiares heurísticos: nota mínima {NOTA_MINIMA_ORIGINAIS}; roteamento >= {LIMIAR_ROTEAMENTO}; "
              f"H4 <= {LIMIAR_H4}; curadoria |dif| >= {LIMIAR_CURADORIA}. Com 3 perguntas, n <= 3 por comparação.", ""]
    a = d["a"]
    linhas.append(f"## (a) #25 prompt novo: {_sim(a['aprovado'], 'SAI DO RASCUNHO', 'continua rascunho')}")
    for p, v in a["por_papel"].items():
        linhas.append(f"- {p}: novo_rag {v['novo_rag']} x genérico {v['generico']} -> "
                      f"{_sim(v['iguala_ou_supera'], 'iguala ou supera', 'abaixo')}; "
                      f"a, b, d >= {NOTA_MINIMA_ORIGINAIS} nas originais: {_sim(v['originais_ok'])}")
    if d["a_curadoria"]:
        a2 = d["a_curadoria"]
        linhas += ["", f"Com a curadoria (novo_rag da rodada 2 x genérico da rodada 1, juiz {a2['juiz'] or '–'}): "
                       f"{_sim(a2['aprovado'], 'passa', 'não passa')}."]
        for p, v in a2["por_papel"].items():
            linhas.append(f"- {p}: novo_rag {v['novo_rag']} x genérico {v['generico']} ({v['perguntas']} perguntas); "
                          f"a, b, d >= {NOTA_MINIMA_ORIGINAIS}: {_sim(v['originais_ok'])}")
        if not a["aprovado"] and a2["aprovado"]:
            linhas.append("- O prompt novo só passa com o material da equipe: mesclar o #25 junto com o #24, "
                          "depois da revisão humana do conteúdo.")
    b = d["b"]
    linhas += ["", f"## (b) PR de roteamento: {_sim(b['abrir_pr'], 'ABRIR', 'não abrir')}",
               f"- modelo (forte - lite) em {b['braco']} (o braço que vai a produção): {_fmt(b['dif'])}"]
    c = d["c"]
    linhas += ["", f"## (c) H4, RAG atual atrapalha: {_sim(c['confirmada'], 'CONFIRMADA: #23 com limiar calibrado vira prioridade', 'não confirmada')}"]
    linhas += [f"- {p}: RAG (com - sem), prompt atual = {_fmt(v)}" for p, v in c["por_papel"].items()]
    if d["d"] is not None:
        cur = d["d"]
        linhas += ["", f"## (d) Efeito da curadoria (rodada 2 - rodada 1, juiz {cur['juiz'] or '–'})"]
        if not cur["bracos"]:
            linhas.append("- sem notas do mesmo juiz nas duas rodadas")
        for k, v in cur["bracos"].items():
            linhas.append(f"- {k.replace('|', ' ')}: {_fmt(v['dif'])} (n={v['n']}, vence {v['vence']}, perde {v['perde']}) "
                          f"-> {v['efeito']}")
    linhas += ["", "A folha cega do aluno confirma ou derruba estas decisões; o juiz Gemini é triagem."]
    return "\n".join(linhas) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rodada1", default="eval/results/rodada1/resumo.json")
    parser.add_argument("--rodada2", help="resumo.json da rodada 2 (opcional)")
    parser.add_argument("--saida", default="eval/results/decisao.md")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    r1 = json.loads(Path(args.rodada1).read_text(encoding="utf-8"))
    r2 = json.loads(Path(args.rodada2).read_text(encoding="utf-8")) if args.rodada2 else None
    if "notas" not in r1 or (r2 is not None and "notas" not in r2):
        raise SystemExit("resumo.json antigo, sem notas por pergunta: rode `matriz.py relatorio --saida ...` de novo.")
    saida = texto(decidir(r1, r2))
    Path(args.saida).parent.mkdir(parents=True, exist_ok=True)
    Path(args.saida).write_text(saida, encoding="utf-8")
    print(saida)


if __name__ == "__main__":
    main()
