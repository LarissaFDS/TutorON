"""Recuperação de contexto para o TutorON.

Duas fontes, consultadas com o mesmo embedding bge-m3 da pergunta:

1. Acervo curado local (provas, listas e resoluções de PAA em ``04-rag/indice.json``),
   busca híbrida léxica + semântica. Só entram blocos de confiança média/alta.
   É a FONTE PRINCIPAL: mostra como o professor cobra e é o material mais confiável.
2. Livro-texto de PAA no Supabase/pgvector (``match_chunks``), indexado por
   ``backend/ingest.py``. Complementar: entra depois do acervo, com menos trechos
   e só quando bem parecido com a pergunta. Sem SUPABASE_URL/KEY ou fora do ar,
   a resposta segue só com o acervo local.

Cada trecho recebe um rótulo curto ([P1], [L1]…) que o modelo usa para citar.
"""
from __future__ import annotations

import asyncio
import logging
import re
from dataclasses import dataclass

import httpx

from .config import Settings

logger = logging.getLogger("tutoron.rag")

ACERVO_K = 4  # fonte principal
LIVRO_K = 2   # complemento
MAX_CHARS_TRECHO = 2200
TIPOS = {
    "prova": "Prova", "lista": "Lista de exercícios", "resolucao_aluno": "Resolução de aluno",
    "gabarito": "Gabarito", "material_estudo": "Material de estudo", "resolucao": "Resolução",
}


@dataclass
class Trecho:
    rotulo: str
    origem: str  # "acervo" | "livro"
    titulo: str
    texto: str
    referencia: str

    @property
    def nome(self) -> str:
        return nome_legivel(self.referencia, self.origem)

    def para_prompt(self) -> str:
        # O modelo cita pelo nome entre colchetes ("(Lista 5, p. 7-8)"), o mesmo que o site mostra.
        return f"[{self.nome}] ({self.titulo})\n{self.texto}"

    def publico(self) -> dict:
        return {"rotulo": self.rotulo, "nome": self.nome, "origem": self.origem, "titulo": self.titulo,
                "referencia": self.referencia}


def nome_legivel(referencia: str, origem: str) -> str:
    """'PAA_L5.pdf | página(s): 7, 8' -> 'Lista 5, p. 7-8'; 'página 48' (livro) -> 'Livro, p. 48'."""
    if origem == "livro":
        pagina = re.search(r"\d+", referencia)
        return f"Livro, p. {pagina.group()}" if pagina else "Livro"
    arquivo, _, resto = referencia.partition("|")
    arquivo = arquivo.strip()
    paginas = re.findall(r"\d+", resto)
    lista = re.match(r"PAA_L(\d+)", arquivo)
    if lista:
        nome = f"Lista {lista.group(1)}"
    elif re.match(r"c\d+_prova", arquivo):
        nome = "Prova"
    elif re.match(r"e\d+_", arquivo):
        nome = "Material da equipe"
    else:
        nome = "Material da disciplina"
    if paginas:
        nome += f", p. {paginas[0]}" + (f"-{paginas[-1]}" if len(paginas) > 1 else "")
    return nome


def _cortar(texto: str) -> str:
    texto = texto.strip()
    return texto if len(texto) <= MAX_CHARS_TRECHO else texto[:MAX_CHARS_TRECHO].rsplit("\n", 1)[0] + "\n[…]"


def _acervo(pergunta: str, vetor: list[float] | None) -> list[Trecho]:
    from acervo.retrieval import search

    itens = search(pergunta, k=ACERVO_K, semantic=vetor is not None, vector=vetor)
    trechos = []
    for n, item in enumerate(itens, 1):
        fonte = item["fonte_original"].replace("\\", "/").split("/")[-1]
        tipo = TIPOS.get(item.get("tipo", ""), "Material da disciplina")
        trechos.append(Trecho(rotulo=f"P{n}", origem="acervo", titulo=f"{tipo} de PAA",
                              texto=_cortar(item["texto"]), referencia=fonte))
    return trechos


async def _livro(client: httpx.AsyncClient, settings: Settings, vetor: list[float]) -> list[Trecho]:
    if not settings.supabase_enabled:
        return []
    headers = {"apikey": settings.supabase_key, "Authorization": f"Bearer {settings.supabase_key}"}
    try:
        response = await client.post(f"{settings.supabase_url}/rest/v1/rpc/match_chunks", headers=headers,
                                     json={"query_embedding": vetor, "match_count": LIVRO_K}, timeout=8)
        response.raise_for_status()
        linhas = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        logger.warning("Supabase indisponível: %s", type(exc).__name__)
        return []
    trechos = []
    for linha in linhas if isinstance(linhas, list) else []:
        if not isinstance(linha, dict) or not str(linha.get("content", "")).strip():
            continue
        if float(linha.get("similarity") or 0) < settings.supabase_min_similarity:
            continue
        nome = str(linha.get("document_name") or "Livro de PAA").removesuffix(".pdf")
        pagina = linha.get("page_number")
        trechos.append(Trecho(rotulo=f"L{len(trechos) + 1}", origem="livro", titulo=nome[:90],
                              texto=_cortar(str(linha["content"])),
                              referencia=f"página {pagina}" if pagina else "livro-texto"))
    return trechos


async def recuperar(pergunta: str, llm, settings: Settings) -> list[Trecho]:
    """Busca acervo e livro em paralelo. Nunca lança: sem contexto, a lista vem vazia."""
    vetor = await llm.embed(pergunta)
    tarefa_acervo = asyncio.to_thread(_acervo, pergunta, vetor)
    tarefa_livro = _livro(llm.client, settings, vetor) if vetor else asyncio.sleep(0, result=[])
    acervo, livro = await asyncio.gather(tarefa_acervo, tarefa_livro, return_exceptions=True)
    trechos: list[Trecho] = []
    for parte, nome in ((acervo, "acervo"), (livro, "livro")):
        if isinstance(parte, BaseException):
            logger.warning("Falha na busca do %s: %s", nome, type(parte).__name__)
        else:
            trechos.extend(parte)
    return trechos


# Orçamento de caracteres para pergunta + código do aluno + material. O modelo local tem janela
# de 8192 tokens, compartilhada entre prompt, raciocínio e resposta; acima disso o Ollama cortaria o
# início do prompt (as instruções do tutor). ~9000 caracteres deixam ~4000 tokens para responder.
ORCAMENTO_CARACTERES = 9000
MATERIAL_MINIMO = 2500


def contexto(trechos: list[Trecho], ocupado: int = 0) -> str:
    """Material na ordem de prioridade (acervo antes do livro), sem passar do orçamento."""
    limite = max(MATERIAL_MINIMO, ORCAMENTO_CARACTERES - ocupado)
    blocos, usado = [], 0
    for t in trechos:
        bloco = t.para_prompt()
        if usado + len(bloco) > limite:
            continue  # pula o trecho inteiro em vez de cortar uma fórmula no meio
        blocos.append(bloco)
        usado += len(bloco)
    return "\n\n".join(blocos)  # vazio: o prompt omite o bloco de material
