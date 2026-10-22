"""Roteiro de animação: o JSON que a IA devolve, validado antes de chegar ao Manim.

Por que roteiro e não código: a IA nunca escreve Python. Ela escolhe um dos modelos de cena
(árvore de recursão, vetor, grafo, tabela) e preenche os dados; quem desenha é o código
confiável de backend/animacao/cena.py. Assim um texto malicioso na pergunta ou numa foto não
vira código executado no servidor, e a animação não quebra por erro de sintaxe da IA.
"""
from __future__ import annotations

import json
import re
from typing import Annotated, Literal, Union

from pydantic import BaseModel, Field, TypeAdapter, field_validator, model_validator

Texto = Annotated[str, Field(max_length=150)]
LIMITE = 140  # legenda e pergunta final: até duas linhas no vídeo
Curto = Annotated[str, Field(max_length=14)]


def _limpar(valor: str) -> str:
    # Sem LaTeX no Manim (Text/Pango): tira $ e barras que a IA às vezes deixa.
    return re.sub(r"\s+", " ", valor.replace("$", "").replace("\\", "")).strip()


class _Base(BaseModel):
    titulo: Texto = ""
    pergunta_final: Texto = ""

    @field_validator("titulo", "pergunta_final", mode="before")
    @classmethod
    def sem_latex(cls, v):
        return _limpar(str(v or ""))[:LIMITE]


class ArvoreRecursao(_Base):
    modelo: Literal["arvore_recursao"]
    a: int = Field(ge=1, le=4)
    b: int = Field(ge=2, le=4)
    f: Curto = "n"
    niveis: int = Field(default=3, ge=2, le=4)
    custos_nivel: list[Texto] = Field(default_factory=list, max_length=4)

    @model_validator(mode="after")
    def completar(self):
        self.f = _limpar(self.f)
        self.custos_nivel = [_limpar(c) for c in self.custos_nivel][: self.niveis]
        self.custos_nivel += ["?"] * (self.niveis - len(self.custos_nivel))
        return self


class PassoVetor(BaseModel):
    destacar: list[int] = Field(default_factory=list, max_length=12)
    trocar: list[int] | None = None
    ponteiros: dict[Curto, int] = Field(default_factory=dict)
    legenda: Texto = ""

    @field_validator("legenda", mode="before")
    @classmethod
    def sem_latex(cls, v):
        return _limpar(str(v or ""))[:LIMITE]


class Vetor(_Base):
    modelo: Literal["vetor"]
    valores: list[Curto] = Field(min_length=1, max_length=12)
    passos: list[PassoVetor] = Field(default_factory=list, max_length=8)

    @field_validator("valores", mode="before")
    @classmethod
    def textos(cls, v):
        return [_limpar(str(x)) for x in v] if isinstance(v, list) else v

    @model_validator(mode="after")
    def indices(self):
        n = len(self.valores)
        for p in self.passos:
            p.destacar = [i for i in p.destacar if 0 <= i < n]
            if p.trocar is not None and (len(p.trocar) != 2 or not all(0 <= i < n for i in p.trocar)):
                p.trocar = None
            p.ponteiros = {k: i for k, i in p.ponteiros.items() if 0 <= i < n}
        return self


class PassoGrafo(BaseModel):
    nos: list[Curto] = Field(default_factory=list)
    arestas: list[list[Curto]] = Field(default_factory=list)
    legenda: Texto = ""

    @field_validator("legenda", mode="before")
    @classmethod
    def sem_latex(cls, v):
        return _limpar(str(v or ""))[:LIMITE]


class Grafo(_Base):
    modelo: Literal["grafo"]
    dirigido: bool = False
    nos: list[Curto] = Field(min_length=1, max_length=10)
    arestas: list[list[Curto]] = Field(default_factory=list, max_length=24)
    passos: list[PassoGrafo] = Field(default_factory=list, max_length=8)

    @model_validator(mode="after")
    def coerente(self):
        if len(set(self.nos)) != len(self.nos):
            raise ValueError("nós repetidos")
        nos = set(self.nos)
        self.arestas = [[a[0], a[1], a[2] if len(a) > 2 else ""] for a in self.arestas
                        if len(a) >= 2 and a[0] in nos and a[1] in nos and a[0] != a[1]]
        for p in self.passos:
            p.nos = [n for n in p.nos if n in nos]
            p.arestas = [a[:2] for a in p.arestas if len(a) >= 2 and a[0] in nos and a[1] in nos]
        return self


class Grupo(BaseModel):
    celulas: list[list[int]] = Field(max_length=64)
    legenda: Texto = ""


class Tabela(_Base):
    modelo: Literal["tabela"]
    linhas: list[Curto] = Field(min_length=1, max_length=8)
    colunas: list[Curto] = Field(min_length=1, max_length=8)
    celulas: list[list[Curto]]
    ordem: list[list[int]] = Field(default_factory=list, max_length=64)
    grupos: list[Grupo] = Field(default_factory=list, max_length=6)

    @field_validator("linhas", "colunas", mode="before")
    @classmethod
    def textos(cls, v):
        return [_limpar(str(x)) for x in v] if isinstance(v, list) else v

    @field_validator("celulas", mode="before")
    @classmethod
    def celulas_texto(cls, v):
        return [[_limpar(str(x)) for x in linha] for linha in v] if isinstance(v, list) else v

    @model_validator(mode="after")
    def formato(self):
        nl, nc = len(self.linhas), len(self.colunas)
        self.celulas = [(list(l) + [""] * nc)[:nc] for l in self.celulas[:nl]]
        self.celulas += [[""] * nc for _ in range(nl - len(self.celulas))]
        dentro = lambda c: len(c) == 2 and 0 <= c[0] < nl and 0 <= c[1] < nc  # noqa: E731
        self.ordem = [c for c in self.ordem if dentro(c)] or [[i, j] for i in range(nl) for j in range(nc)]
        for g in self.grupos:
            g.celulas = [c for c in g.celulas if dentro(c)]
        self.grupos = [g for g in self.grupos if g.celulas]
        return self


Roteiro = Annotated[Union[ArvoreRecursao, Vetor, Grafo, Tabela], Field(discriminator="modelo")]
_ADAPTADOR = TypeAdapter(Roteiro)


def extrair_json(texto: str) -> dict:
    """O primeiro objeto JSON do texto (a IA às vezes cerca com ```json ou escreve antes)."""
    texto = re.sub(r"<think>.*?</think>", "", texto or "", flags=re.S)
    inicio = texto.find("{")
    if inicio < 0:
        raise ValueError("sem JSON")
    obj, _ = json.JSONDecoder().raw_decode(texto[inicio:])
    if not isinstance(obj, dict):
        raise ValueError("JSON não é objeto")
    return obj


def validar(dados: dict | str) -> ArvoreRecursao | Vetor | Grafo | Tabela:
    if isinstance(dados, str):
        dados = extrair_json(dados)
    return _ADAPTADOR.validate_python(dados)
