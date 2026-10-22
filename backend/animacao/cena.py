"""Desenha um roteiro validado com o Manim (Community, 0.19). Roda em processo separado:

    python -m backend.animacao.cena roteiro.json pasta_saida

Processo separado porque o Manim é síncrono, usa CPU por segundos e guarda estado global
de configuração; assim o servidor não trava e uma falha aqui não derruba o site.
Só usa Text (Pango): não precisa de LaTeX instalado.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from manim import (DOWN, LEFT, RIGHT, UP, Arrow, Circle, Create, FadeIn, FadeOut, Indicate, Line, Rectangle,
                   Scene, SurroundingRectangle, Text, Transform, VGroup, Write, config, tempconfig)

from .roteiro import ArvoreRecursao, Grafo, Tabela, Vetor, validar

FUNDO = "#FBFAF7"
TINTA = "#1D2433"
MUTED = "#6B7280"
PRIMARIA = "#1F4FD8"
DESTAQUE = "#E8A317"
OK = "#1E8E5A"
GRUPOS = ["#1F4FD8", "#E8A317", "#1E8E5A", "#C2410C", "#7C3AED", "#0E7490"]


def texto(s: str, tam: int = 28, cor: str = TINTA, **kw) -> Text:
    return Text(s or " ", font_size=tam, color=cor, **kw)


def quebrar(s: str, largura: int = 72) -> str:
    """Legenda longa em até duas linhas, quebrando entre palavras."""
    if len(s) <= largura:
        return s
    corte = s.rfind(" ", 0, largura)
    corte = corte if corte > 0 else largura
    return s[:corte] + "\n" + s[corte:].strip()


def contiguo(celulas: list[list[int]]) -> bool:
    linhas = sorted({i for i, _ in celulas})
    colunas = sorted({j for _, j in celulas})
    seguidas = lambda v: v == list(range(v[0], v[-1] + 1))  # noqa: E731
    return seguidas(linhas) and seguidas(colunas) and len({tuple(c) for c in celulas}) == len(linhas) * len(colunas)


class CenaTutor(Scene):
    roteiro = None

    def construct(self):
        r = self.roteiro
        titulo = texto(r.titulo or "Vamos visualizar", 34, weight="BOLD").to_edge(UP, buff=0.35)
        self.play(Write(titulo), run_time=0.8)
        self.legenda = texto("", 24, MUTED).to_edge(DOWN, buff=0.35)
        self.add(self.legenda)
        {ArvoreRecursao: self.arvore, Vetor: self.vetor, Grafo: self.grafo, Tabela: self.tabela}[type(r)](r)
        if r.pergunta_final:
            self.legendar("Sua vez: " + r.pergunta_final, cor=PRIMARIA)
        self.wait(2.5)

    # ------------------------------------------------------------------ utilidades
    def legendar(self, s: str, cor: str = MUTED) -> None:
        nova = texto(quebrar(s), 24, cor, line_spacing=0.8).to_edge(DOWN, buff=0.3)
        if nova.width > config.frame_width - 0.8:
            nova.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Transform(self.legenda, nova), run_time=0.5)

    # ------------------------------------------------------------------ árvore de recursão
    def arvore(self, r: ArvoreRecursao) -> None:
        topo, base = 2.3, -2.2
        dy = (topo - base) / max(1, r.niveis - 1) if r.niveis > 1 else 0
        largura, cx = 7.6, -1.9  # árvore à esquerda; os custos ficam numa coluna à direita
        niveis, anteriores = [], []
        for nivel in range(r.niveis):
            qtd = r.a ** nivel
            div = r.b ** nivel
            rotulo = "n" if nivel == 0 else f"n/{div}"  # tamanho do subproblema em cada nó
            y = topo - nivel * dy
            resumido = qtd > 9 or (anteriores and len(anteriores) < r.a ** (nivel - 1))
            if resumido:  # nível largo demais: as duas pontas e reticências no meio
                xs = [cx - largura / 2 + 0.4, cx - largura / 2 + 1.3, cx, cx + largura / 2 - 1.3, cx + largura / 2 - 0.4]
                nos = VGroup(*[self._no(rotulo if i != 2 else "…", x, y) for i, x in enumerate(xs)])
            else:
                passo = largura / qtd
                nos = VGroup(*[self._no(rotulo, cx - largura / 2 + passo * (i + 0.5), y) for i in range(qtd)])
            ligacoes = VGroup()
            if anteriores and not resumido:
                for i, filho in enumerate(nos):  # cada nó tem exatamente a filhos
                    pai = anteriores[i // r.a]
                    ligacoes.add(Line(pai.get_bottom(), filho.get_top(), color=MUTED, stroke_width=2))
            elif anteriores:  # resumido: as pontas ligam às pontas de cima
                for filho, pai in ((nos[0], anteriores[0]), (nos[1], anteriores[0]),
                                   (nos[3], anteriores[-1]), (nos[4], anteriores[-1])):
                    ligacoes.add(Line(pai.get_bottom(), filho.get_top(), color=MUTED, stroke_width=2))
            self.play(Create(ligacoes), FadeIn(nos), run_time=0.9)
            custo = texto("custo: " + r.custos_nivel[nivel], 22,
                          DESTAQUE if r.custos_nivel[nivel].strip().endswith("?") else OK)
            if custo.width > 4.2:
                custo.scale_to_fit_width(4.2)
            custo.move_to([cx + largura / 2 + 0.5 + custo.width / 2, y, 0])
            self.legendar(f"Nível {nivel}: {qtd} subproblema(s) de tamanho n/{div}" if nivel else
                          f"T(n) = {r.a}·T(n/{r.b}) + {r.f}")
            self.play(FadeIn(custo), run_time=0.6)
            niveis.append(nos)
            anteriores = list(nos)
        self.legendar("Quantos níveis a árvore tem até chegar em tamanho 1?")
        self.wait(1)

    def _no(self, rotulo: str, x: float, y: float) -> VGroup:
        t = texto(rotulo, 20)
        caixa = Rectangle(width=max(0.7, t.width + 0.25), height=0.5, color=PRIMARIA, stroke_width=2)
        g = VGroup(caixa, t.move_to(caixa)).move_to([x, y, 0])
        if g.width > 1.6:
            g.scale_to_fit_width(1.6)
        return g

    # ------------------------------------------------------------------ vetor
    def vetor(self, r: Vetor) -> None:
        n = len(r.valores)
        lado = min(0.95, 11.0 / n)
        celulas = VGroup()
        for i, v in enumerate(r.valores):
            caixa = Rectangle(width=lado, height=lado, color=TINTA, stroke_width=2)
            celulas.add(VGroup(caixa, texto(v, 26).move_to(caixa)))
        celulas.arrange(RIGHT, buff=0).move_to([0, 0.3, 0])
        indices = VGroup(*[texto(str(i), 16, MUTED).next_to(c, DOWN, buff=0.12) for i, c in enumerate(celulas)])
        self.play(FadeIn(celulas), FadeIn(indices), run_time=0.8)
        ponteiros = VGroup()
        for p in r.passos:
            anim = []
            for i, c in enumerate(celulas):
                cor = DESTAQUE if i in p.destacar else None
                anim.append(c[0].animate.set_fill(cor or FUNDO, opacity=0.35 if cor else 0))
            novos = VGroup()
            for nome, i in p.ponteiros.items():
                seta = Arrow(start=UP * 0.9, end=UP * 0.05, color=PRIMARIA, buff=0, stroke_width=3)
                seta.next_to(celulas[i], UP, buff=0.05)
                novos.add(VGroup(seta, texto(nome, 20, PRIMARIA).next_to(seta, UP, buff=0.05)))
            self.play(*anim, FadeOut(ponteiros), FadeIn(novos), run_time=0.6)
            ponteiros = novos
            if p.legenda:
                self.legendar(p.legenda)
            if p.trocar:
                i, j = p.trocar
                ti, tj = celulas[i][1], celulas[j][1]
                self.play(ti.animate.move_to(celulas[j][0]), tj.animate.move_to(celulas[i][0]), run_time=0.8)
                celulas[i].remove(ti)
                celulas[j].remove(tj)
                celulas[i].add(tj)
                celulas[j].add(ti)
            self.wait(0.6)

    # ------------------------------------------------------------------ grafo
    def grafo(self, r: Grafo) -> None:
        import math

        n = len(r.nos)
        raio = 2.1 if n > 4 else 1.7
        pos = {no: [raio * 1.5 * math.cos(math.pi / 2 - 2 * math.pi * k / n),
                    raio * math.sin(math.pi / 2 - 2 * math.pi * k / n) - 0.1, 0] for k, no in enumerate(r.nos)}
        circulos = {}
        for no in r.nos:
            c = Circle(radius=0.33, color=PRIMARIA, stroke_width=3).move_to(pos[no])
            circulos[no] = VGroup(c, texto(no, 24).move_to(c))
        arestas = {}
        rotulos = VGroup()
        for a, b, rot in r.arestas:
            ini, fim = circulos[a][0], circulos[b][0]
            tipo = Arrow if r.dirigido else Line
            kw = {"buff": 0.35, "stroke_width": 3, "color": MUTED}
            if r.dirigido:
                kw["max_tip_length_to_length_ratio"] = 0.12
            linha = tipo(ini.get_center(), fim.get_center(), **kw)
            arestas[(a, b)] = linha
            if not r.dirigido:
                arestas[(b, a)] = linha
            if rot:
                rotulos.add(texto(rot, 20, TINTA).move_to(linha.get_center() + [0.18, 0.18, 0]))
        self.play(*[Create(l) for l in set(arestas.values())], *[FadeIn(c) for c in circulos.values()],
                  FadeIn(rotulos), run_time=1.2)
        for p in r.passos:
            anim = [circulos[no][0].animate.set_fill(DESTAQUE, opacity=0.45) for no in p.nos]
            anim += [arestas[tuple(a)].animate.set_color(DESTAQUE).set_stroke(width=6)
                     for a in p.arestas if tuple(a) in arestas]
            if anim:
                self.play(*anim, run_time=0.7)
            if p.legenda:
                self.legendar(p.legenda)
            self.wait(0.6)

    # ------------------------------------------------------------------ tabela
    def tabela(self, r: Tabela) -> None:
        nl, nc = len(r.linhas), len(r.colunas)
        lado = min(0.9, 9.0 / (nc + 1), 4.6 / (nl + 1))
        x0 = -lado * (nc + 1) / 2 + lado / 2
        y0 = lado * (nl + 1) / 2 - lado / 2 + 0.1
        centro = lambda i, j: [x0 + (j + 1) * lado, y0 - (i + 1) * lado, 0]  # noqa: E731
        grade = VGroup()
        for i in range(nl):
            for j in range(nc):
                grade.add(Rectangle(width=lado, height=lado, color=TINTA, stroke_width=1.5).move_to(centro(i, j)))
        cab = VGroup(*[texto(c, 20, PRIMARIA).move_to([x0 + (j + 1) * lado, y0, 0]) for j, c in enumerate(r.colunas)],
                     *[texto(l, 20, PRIMARIA).move_to([x0, y0 - (i + 1) * lado, 0]) for i, l in enumerate(r.linhas)])
        self.play(Create(grade), FadeIn(cab), run_time=1)
        passo = max(0.15, min(0.45, 6.0 / max(1, len(r.ordem))))
        for i, j in r.ordem:
            valor = r.celulas[i][j]
            if not valor:
                continue
            t = texto(valor, 22, DESTAQUE if valor == "?" else TINTA).move_to(centro(i, j))
            self.play(FadeIn(t), Indicate(grade[i * nc + j], color=DESTAQUE, scale_factor=1.05), run_time=passo)
        for k, g in enumerate(r.grupos):
            cor = GRUPOS[k % len(GRUPOS)]
            if contiguo(g.celulas):
                alvo = VGroup(*[grade[i * nc + j] for i, j in g.celulas])
                caixas = [SurroundingRectangle(alvo, color=cor, buff=0.06, corner_radius=0.12, stroke_width=4)]
            else:  # grupo que "dá a volta" no mapa de Karnaugh (cantos, bordas): uma marca por célula
                caixas = [SurroundingRectangle(grade[i * nc + j], color=cor, buff=-0.05, corner_radius=0.12,
                                               stroke_width=4) for i, j in g.celulas]
            self.play(*[Create(c) for c in caixas], run_time=0.7)
            if g.legenda:
                self.legendar(g.legenda, cor=cor)
            self.wait(0.5)


def renderizar(roteiro: dict, saida: Path, qualidade: str = "low_quality") -> Path:
    r = validar(roteiro)
    saida.mkdir(parents=True, exist_ok=True)
    cena = type("CenaTutorRender", (CenaTutor,), {"roteiro": r})
    with tempconfig({"quality": qualidade, "background_color": FUNDO, "media_dir": str(saida / "media"),
                     "output_file": "animacao", "disable_caching": True, "verbosity": "ERROR",
                     "progress_bar": "none", "frame_rate": 24}):
        c = cena()
        c.render()
        return Path(c.renderer.file_writer.movie_file_path)


if __name__ == "__main__":
    dados = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    video = renderizar(dados, Path(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else "low_quality")
    print(json.dumps({"video": str(video)}))
