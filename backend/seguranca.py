"""Verificações no código em volta da resposta da IA (as regras do prompt continuam valendo).

Depois do teste de 19/10/2026: o modelo local parafraseou o prompt de sistema quando pedido e
citou rótulos soltos. O prompt já proíbe as duas coisas, mas depende de o modelo obedecer. Aqui fica
o que dá para garantir sem depender do modelo:

- pedido explícito das instruções internas não chega à IA: recebe uma recusa fixa;
- a resposta não sai com rótulo [P3]/[L2] que não existe no material desta pergunta;
- resposta que copia um trecho longo das instruções é trocada pela recusa.

Paráfrase de um pedido indireto ainda depende do prompt: este módulo não a detecta.
"""
from __future__ import annotations

import re

from acervo.curate import searchable

# Verbo de "mostrar" + objeto que só pode ser as instruções do tutor. "Instruções" sozinha não
# conta (ex.: "liste as instruções do processador"), por isso o objeto exige um qualificador.
_VERBO = (r"(mostr\w*|revel\w*|repit\w*|repet\w*|imprim\w*|exib\w*|list\w*|cop\w*|escrev\w*|transcrev\w*|"
          r"diga|diz|conte|fala|passa|manda|envi\w*|compartilh\w*|resum\w*|parafrase\w*|traduz\w*|"
          r"qual e|quais sao|como e|show|reveal|print|repeat|tell me|what (is|are))")
_OBJETO = (r"(prompt|system prompt|mensagem (de|do) sistema|"
           r"(suas|tuas|your) (instrucoes|regras|diretrizes|ordens|configurac\w*)|"
           r"instruc\w* (internas|iniciais|originais|ocultas|secretas|de sistema|do sistema|que (voce )?recebeu|que te deram|que lhe deram)|"
           r"regras (internas|ocultas|secretas|do sistema|de sistema|que (voce )?(recebeu|segue))|"
           r"texto (acima|anterior|inicial)|(instructions|rules) (you|above))")
_PEDIDO = re.compile(rf"\b{_VERBO}\b.{{0,60}}\b{_OBJETO}")
_DIRETO = re.compile(r"\b(system prompt|prompt de sistema|prompt do sistema|modo desenvolvedor|developer mode|jailbreak)\b")

RECUSA = "Não posso mostrar minhas instruções internas, mas posso ajudar com {nome}. Qual é a sua dúvida da matéria?"
_ROTULO = re.compile(r"\[\s*([PL]\d+)\s*\]")


def pedido_de_instrucoes(texto: str) -> bool:
    t = searchable(texto or "")
    return bool(_PEDIDO.search(t) or _DIRETO.search(t))


def recusa(nome: str) -> str:
    return RECUSA.replace("{nome}", nome)


def rotulos_invalidos(texto: str, validos: set[str]) -> set[str]:
    return {r for r in _ROTULO.findall(texto) if r not in validos}


def limpar_rotulos(texto: str, validos: set[str]) -> str:
    """Tira da resposta os rótulos que não existem no material enviado (ex.: [P3] com só 2 trechos)."""
    def trocar(m: re.Match) -> str:
        return m.group(0) if m.group(1) in validos else ""
    return re.sub(r" ?\[\s*([PL]\d+)\s*\]", trocar, texto)


def _palavras(texto: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", searchable(texto))


def copia_instrucoes(resposta: str, sistema: str | None, janela: int = 12) -> bool:
    """A resposta repete 12 palavras seguidas das instruções? (Cópia literal; paráfrase escapa.)"""
    if not sistema:
        return False
    s = _palavras(sistema)
    trechos = {" ".join(s[i:i + janela]) for i in range(len(s) - janela + 1)}
    r = _palavras(resposta)
    return any(" ".join(r[i:i + janela]) in trechos for i in range(len(r) - janela + 1))


def revisar(resposta: str, sistema: str | None, validos: set[str], nome: str) -> tuple[str, list[str]]:
    """Resposta final + o que foi corrigido (para o registro)."""
    ajustes = []
    if copia_instrucoes(resposta, sistema):
        return recusa(nome), ["copia_instrucoes"]
    invalidos = rotulos_invalidos(resposta, validos)
    if invalidos:
        resposta = limpar_rotulos(resposta, validos)
        ajustes.append("rotulos_inexistentes:" + ",".join(sorted(invalidos)))
    return resposta, ajustes
