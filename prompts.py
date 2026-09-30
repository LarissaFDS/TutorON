"""Montagem dos prompts dos dois cenários (e do controle opcional).

Cenário 1 (genérico): só a pergunta, sem instrução de sistema e sem material.
Cenário 2 (estruturado + contexto): instrução de tutor + CONTEXTO ACADÊMICO + PERGUNTA.
Controle (opcional, --controle): mesma instrução do cenário 2, mas SEM contexto.
  Serve para separar o efeito do "prompt bem escrito" do efeito do "material da disciplina".
"""
from pathlib import Path
import re

MATERIAIS = Path(__file__).parent / "materiais"

SYSTEM_TUTOR = """Você é o TutorON, monitor da disciplina Projeto e Análise de Algoritmos (PAA) \
da UFAL (Instituto de Computação), ministrada pelo Prof. Rian Gabriel Pinheiro.

Seu objetivo é ajudar o aluno a responder a questão como ela é cobrada NESTA disciplina.

Regras:
1. Use o CONTEXTO ACADÊMICO como referência principal: siga a mesma estrutura de resposta, \
notação e vocabulário usados nas provas, listas e resoluções fornecidas.
2. Responda exatamente ao que foi perguntado. Se o enunciado da prova pede algo específico \
(ex.: "mostre a recorrência", "prove a corretude"), inclua isso explicitamente.
3. Cite de qual material veio cada ideia importante, usando o id entre colchetes (ex.: [c02]).
4. Os materiais incluem resoluções de alunos, que podem conter erros. Se algum trecho do \
contexto estiver impreciso ou incorreto, NÃO o reproduza: corrija e avise o aluno de forma \
explícita ("Atenção: o material [cX] diz ... mas o correto é ...").
5. Não invente informações sobre a disciplina (critérios de correção, pesos, preferências do \
professor) que não estejam no contexto. Conhecimento geral correto pode ser usado, mas \
indique quando algo não vem do material.
6. Escreva em português do Brasil, de forma didática, com a resposta pronta para ser \
reproduzida numa prova, seguida de uma breve dica de estudo."""

SYSTEM_TUTOR_SEM_CONTEXTO = SYSTEM_TUTOR.replace(
    "Use o CONTEXTO ACADÊMICO como referência principal: siga a mesma estrutura de resposta, "
    "notação e vocabulário usados nas provas, listas e resoluções fornecidas.",
    "Não há material da disciplina disponível nesta pergunta; responda com rigor acadêmico.",
)


def carregar_chunk(cid: str) -> dict:
    arq = next(MATERIAIS.glob(f"{cid}_*.md"))
    bruto = arq.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", bruto, re.S)
    meta, corpo = m.group(1), m.group(2).strip()
    fonte = re.search(r'fonte:\s*"?(.*?)"?\s*$', meta, re.M).group(1)
    tipo = re.search(r"tipo:\s*(\S+)", meta).group(1)
    return {"id": cid, "arquivo": arq.name, "fonte": fonte, "tipo": tipo, "texto": corpo}


def bloco_contexto(ids: list[str]) -> str:
    partes = []
    for cid in ids:
        c = carregar_chunk(cid)
        partes.append(f"[{c['id']}] Fonte: {c['fonte']} (tipo: {c['tipo']})\n{c['texto']}")
    return "\n\n-----\n\n".join(partes)


def prompt_generico(q: dict) -> tuple[str | None, str]:
    """Retorna (system_instruction, conteúdo)."""
    return None, q["pergunta"]


def prompt_estruturado(q: dict) -> tuple[str, str]:
    conteudo = (
        "CONTEXTO ACADÊMICO (trechos recuperados da base de materiais de PAA):\n\n"
        f"{bloco_contexto(q['contexto'])}\n\n"
        "=====\n\n"
        f"PERGUNTA DO ALUNO:\n{q['pergunta']}"
    )
    return SYSTEM_TUTOR, conteudo


def prompt_controle(q: dict) -> tuple[str, str]:
    return SYSTEM_TUTOR_SEM_CONTEXTO, f"PERGUNTA DO ALUNO:\n{q['pergunta']}"
