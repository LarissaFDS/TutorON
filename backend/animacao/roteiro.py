"""Roteiro de animação: o JSON que a IA devolve, validado antes de chegar ao Manim.

Por que roteiro e não código: a IA nunca escreve Python. Ela escolhe um dos modelos de cena
(árvore de recursão, vetor, grafo, tabela) e preenche os dados; quem desenha é o código
confiável de backend/animacao/cena.py. Assim um texto malicioso na pergunta ou numa foto não
vira código executado no servidor, e a animação não quebra por erro de sintaxe da IA.
"""
from __future__ import annotations

import json
import math
import re
from typing import Annotated, Literal, Union

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, field_validator, model_validator

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
    posicoes: dict[Curto, list[float]] = Field(default_factory=dict)

    @model_validator(mode="after")
    def coerente(self):
        if len(set(self.nos)) != len(self.nos):
            raise ValueError("nós repetidos")
        nos = set(self.nos)
        if self.posicoes and (set(self.posicoes) != nos or any(
                len(p) != 2 or not all(math.isfinite(x) for x in p) or abs(p[0]) > 5.5 or abs(p[1]) > 2.1
                for p in self.posicoes.values())):
            raise ValueError('posições devem cobrir os nós e ficar dentro do desenho')
        if self.posicoes and len({tuple(p) for p in self.posicoes.values()}) != len(self.posicoes):
            raise ValueError('posições repetidas')
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


class _Parcial(_Base):
    model_config = ConfigDict(extra='forbid')


class GradeDP(_Parcial):
    modelo: Literal['grade_dp']
    custos: list[list[int]] = Field(min_length=2, max_length=5)
    bloqueios: list[list[int]] = Field(default_factory=list, max_length=12)
    foco: list[int] = Field(default_factory=lambda: [1, 1], min_length=2, max_length=2)

    @model_validator(mode='after')
    def grade(self):
        nl, nc = len(self.custos), len(self.custos[0])
        if not 2 <= nc <= 5 or any(len(l) != nc for l in self.custos):
            raise ValueError('grade retangular de 2 a 5 linhas/colunas')
        if any(not 0 <= x <= 99 for linha in self.custos for x in linha):
            raise ValueError('custos entre 0 e 99')
        if any(len(c) != 2 or not 0 <= c[0] < nl or not 0 <= c[1] < nc for c in self.bloqueios):
            raise ValueError('bloqueio fora da grade')
        if [0, 0] in self.bloqueios or [nl - 1, nc - 1] in self.bloqueios:
            raise ValueError('início e destino precisam estar livres')
        i, j = self.foco
        if not (0 < i < nl and 0 < j < nc) or self.foco in self.bloqueios:
            raise ValueError('foco interno livre, com vizinhos acima e à esquerda')
        return self


class ArestaFluxo(BaseModel):
    model_config = ConfigDict(extra='forbid')
    de: Curto
    para: Curto
    capacidade: int = Field(ge=1, le=99)
    fluxo: int = Field(default=0, ge=0)

    @model_validator(mode='after')
    def limite(self):
        if self.fluxo > self.capacidade:
            raise ValueError('fluxo excede a capacidade')
        return self


class Fluxo(_Parcial):
    modelo: Literal['fluxo']
    nos: list[Curto] = Field(min_length=3, max_length=6)
    fonte: Curto = 's'
    destino: Curto = 't'
    arestas: list[ArestaFluxo] = Field(min_length=2, max_length=12)
    primeiro_passo: list[Curto] = Field(min_length=2, max_length=2)

    @model_validator(mode='after')
    def rede(self):
        if len(set(self.nos)) != len(self.nos) or self.fonte == self.destino:
            raise ValueError('nós únicos e terminais distintos')
        if self.fonte not in self.nos or self.destino not in self.nos:
            raise ValueError('terminais precisam existir')
        pares = set()
        saldo = dict.fromkeys(self.nos, 0)
        for a in self.arestas:
            if a.de not in saldo or a.para not in saldo or a.de == a.para:
                raise ValueError('aresta inválida')
            if (a.de, a.para) in pares or (a.para, a.de) in pares:
                raise ValueError('use uma aresta por par de nós neste desenho')
            pares.add((a.de, a.para))
            saldo[a.de] -= a.fluxo
            saldo[a.para] += a.fluxo
        if any(v != 0 for n, v in saldo.items() if n not in (self.fonte, self.destino)):
            raise ValueError('fluxo precisa conservar-se nos nós internos')
        if saldo[self.fonte] > 0 or saldo[self.destino] < 0:
            raise ValueError('a fonte envia fluxo e o destino recebe')
        a, b = self.primeiro_passo
        if a != self.fonte or b == self.destino or not any(
                e.de == a and e.para == b and e.fluxo < e.capacidade for e in self.arestas):
            raise ValueError('mostrar só uma saída disponível da fonte, sem completar um caminho')
        return self


class Karnaugh(_Parcial):
    modelo: Literal['karnaugh']
    # Ordem Gray definida pelo renderizador: a IA não pode trocá-la por ordem binária.
    celulas: list[list[Literal['0', '1', 'X', '?']]] = Field(min_length=2, max_length=4)
    grupo: list[list[int]] = Field(default_factory=list, max_length=8)

    @model_validator(mode='after')
    def agrupamento(self):
        nl, nc = len(self.celulas), len(self.celulas[0])
        if nl not in (2, 4) or nc not in (2, 4) or any(len(l) != nc for l in self.celulas):
            raise ValueError('mapa 2x2, 2x4, 4x2 ou 4x4')
        grupo = {tuple(c) for c in self.grupo}
        if len(grupo) != len(self.grupo) or any(len(c) != 2 or not 0 <= c[0] < nl or not 0 <= c[1] < nc for c in grupo):
            raise ValueError('células do grupo inválidas')
        if grupo:
            ls, cs = {i for i, _ in grupo}, {j for _, j in grupo}
            def intervalo_ciclico(indices, tamanho):
                return len(indices) in (1, 2, 4) and any(
                    indices == {(inicio + k) % tamanho for k in range(len(indices))} for inicio in range(tamanho))
            if not intervalo_ciclico(ls, nl) or not intervalo_ciclico(cs, nc) or len(grupo) != len(ls) * len(cs):
                raise ValueError('grupo deve ser retangular, com lados potência de dois e adjacência cíclica')
            if any(self.celulas[i][j] not in ('1', 'X') for i, j in grupo):
                raise ValueError('grupo de uns não pode incluir zero obrigatório nem célula desconhecida')
            uns = {(i, j) for i, linha in enumerate(self.celulas) for j, v in enumerate(linha) if v == '1'}
            if not (grupo & uns) or not (uns - grupo):
                raise ValueError('mostrar um grupo parcial: deve conter um 1 e deixar outros uns para o aluno')
        return self


class Porta(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: Curto
    tipo: Literal['AND', 'OR', 'XOR', 'NAND', 'NOR', 'NOT']
    entradas: list[Curto] = Field(min_length=1, max_length=2)


class Circuito(_Parcial):
    modelo: Literal['circuito']
    entradas: list[Curto] = Field(min_length=2, max_length=3)
    portas: list[Porta] = Field(min_length=1, max_length=3)
    linha_foco: int = Field(default=1, ge=0)

    @model_validator(mode='after')
    def conexoes(self):
        conhecidos = set(self.entradas)
        if len(conhecidos) != len(self.entradas) or self.linha_foco >= 2 ** len(self.entradas):
            raise ValueError('entradas únicas e linha existente na tabela')
        for p in self.portas:
            if p.id in conhecidos or any(e not in conhecidos for e in p.entradas):
                raise ValueError('portas únicas em ordem de dependência, sem ciclos ou entradas ausentes')
            if len(p.entradas) != (1 if p.tipo == 'NOT' else 2):
                raise ValueError('número de entradas incompatível com a porta')
            conhecidos.add(p.id)
        return self


class Reducao(_Parcial):
    modelo: Literal['reducao']
    # Diagrama conceitual: o render não apresenta uma redução específica resolvida.
    origem: Curto = 'Problema A'
    destino: Curto = 'Problema B'


Roteiro = Annotated[Union[ArvoreRecursao, Vetor, Grafo, Tabela, GradeDP, Fluxo, Karnaugh, Circuito, Reducao],
                   Field(discriminator="modelo")]
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


def validar(dados: dict | str) -> ArvoreRecursao | Vetor | Grafo | Tabela | GradeDP | Fluxo | Karnaugh | Circuito | Reducao:
    if isinstance(dados, str):
        dados = extrair_json(dados)
    return _ADAPTADOR.validate_python(dados)
