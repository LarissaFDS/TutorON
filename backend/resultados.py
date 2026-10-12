"""Resumo das avaliações A/B e do uso do modo Tutor, a partir de ``dados/``."""
from __future__ import annotations

from collections import Counter, defaultdict
from statistics import mean

CRITERIOS = ("clareza", "confianca", "utilidade")


def _media(valores: list[float]) -> float | None:
    return round(mean(valores), 2) if valores else None


def resumo(registro) -> dict:
    avaliacoes = registro.ler("validacao/avaliacoes.jsonl")
    perguntas = registro.ler("perguntas.jsonl")
    feedback = registro.ler("feedback.jsonl")

    preferencia = Counter(a.get("preferida_condicao") for a in avaliacoes)
    por_condicao: dict[str, dict] = {}
    for condicao in ("tutoron", "generico"):
        notas = [a["notas"][condicao] for a in avaliacoes if condicao in a.get("notas", {})]
        por_condicao[condicao] = {
            **{c: _media([n[c] for n in notas]) for c in CRITERIOS},
            "erro_matematico_pct": round(100 * sum(n.get("erro_matematico", False) for n in notas) / len(notas), 1) if notas else None,
        }

    por_modelo: dict[str, Counter] = defaultdict(Counter)
    for a in avaliacoes:
        modelo = a.get("respostas", {}).get("tutoron", {}).get("modelo", "?")
        por_modelo[modelo][a.get("preferida_condicao")] += 1

    respondidas = [p for p in perguntas if "resposta" in p]
    total = len(avaliacoes)
    return {
        "validacao": {
            "avaliacoes": total,
            "preferencia_pct": {k: round(100 * preferencia.get(k, 0) / total, 1) if total else None
                                for k in ("tutoron", "generico", "empate")},
            "notas": por_condicao,
            "por_modelo_tutoron": {m: dict(c) for m, c in por_modelo.items()},
            "ultimas": [{"data": a["data"], "pergunta": a["pergunta"][:140], "preferida": a["preferida_condicao"],
                         "comentario": a.get("comentario", "")} for a in avaliacoes[-15:]][::-1],
        },
        "tutor": {
            "perguntas": len(perguntas),
            "respondidas": len(respondidas),
            "sem_modelo": len(perguntas) - len(respondidas),
            "por_modelo": dict(Counter(p.get("modelo") for p in respondidas)),
            "tempo_medio_s": _media([p["segundos"] for p in respondidas if p.get("segundos")]),
            "feedback": {"util": sum(f.get("util") is True for f in feedback),
                         "nao_util": sum(f.get("util") is False for f in feedback),
                         "erro_matematico": sum(bool(f.get("erro_matematico")) for f in feedback)},
        },
    }
