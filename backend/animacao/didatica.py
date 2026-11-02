"""Cenas parciais: desenham dependências e perguntas, sem calcular a solução."""
from __future__ import annotations

import math

from manim import (DOWN, LEFT, RIGHT, UP, Arrow, Circle, Create, FadeIn, Indicate, Line,
                   Rectangle, SurroundingRectangle, Text, VGroup, config)

from .roteiro import Circuito, Esquema, Fluxo, GradeDP, Karnaugh, Reducao

FUNDO, TINTA, CINZA = '#FBFAF7', '#14213D', '#4F5868'
AZUL, AMARELO = '#066D83', '#E8A317'


def txt(s, tamanho=24, cor=TINTA, largura=None):
    t = Text(str(s), font_size=tamanho, color=cor)
    if largura and t.width > largura:
        t.scale_to_fit_width(largura)
    return t


def grade(celulas, centro, lado=.72):
    nl, nc = len(celulas), len(celulas[0])
    caixas, textos = {}, {}
    for i, linha in enumerate(celulas):
        for j, valor in enumerate(linha):
            pos = [centro[0] + (j - (nc - 1) / 2) * lado,
                   centro[1] + ((nl - 1) / 2 - i) * lado, 0]
            caixa = Rectangle(width=lado, height=lado, color=CINZA, stroke_width=1.5).move_to(pos)
            if valor == '#':
                caixa.set_fill(CINZA, opacity=.18)
            caixas[i, j] = caixa
            textos[i, j] = txt('×' if valor == '#' else valor, 23, CINZA if valor == '#' else TINTA,
                               lado * .75).move_to(pos)
    return VGroup(*caixas.values(), *textos.values()), caixas, textos


def grade_dp(cena, r: GradeDP):
    nl, nc = len(r.custos), len(r.custos[0])
    custos = [[str(v) if [i, j] not in r.bloqueios else '#' for j, v in enumerate(linha)]
              for i, linha in enumerate(r.custos)]
    pendente = [['#' if [i, j] in r.bloqueios else '?' for j in range(nc)] for i in range(nl)]
    terreno, casas, _ = grade(custos, [-3.3, .25])
    tabela, estados, _ = grade(pendente, [3.0, .25])
    titulos = VGroup(txt('Custos do terreno', 25).move_to([-3.3, 2.5, 0]),
                     txt('Sua tabela dp[i][j]', 25).move_to([3.0, 2.5, 0]))
    cena.play(FadeIn(titulos), Create(terreno), Create(tabela), run_time=1.2)
    indices = VGroup(*[txt(f'j={j}', 14, CINZA).next_to(estados[0, j], UP, buff=.12) for j in range(nc)],
                     *[txt(f'i={i}', 14, CINZA).next_to(estados[i, 0], LEFT, buff=.12) for i in range(nl)])
    cena.play(FadeIn(indices), run_time=.4)
    inicio, fim = casas[0, 0], casas[nl - 1, nc - 1]
    marcadores = VGroup(SurroundingRectangle(inicio, color=AZUL, buff=-.03),
                        SurroundingRectangle(fim, color=AZUL, buff=-.03))
    marcadores.add(txt('início', 17, AZUL).next_to(inicio, UP, buff=.08),
                   txt('destino', 17, AZUL).next_to(fim, DOWN, buff=.08))
    cena.play(Create(marcadores), run_time=.7)
    movimentos = VGroup(Arrow(LEFT * .35, RIGHT * .35, color=AZUL, buff=0),
                        Arrow(UP * .35, DOWN * .35, color=AZUL, buff=0)).arrange(RIGHT, buff=.6)
    movimentos.move_to([-3.3, -2.35, 0])
    cena.play(FadeIn(movimentos), run_time=.6)
    cena.legendar('O robô só anda para a direita ou para baixo. × representa uma célula bloqueada.')
    cena.wait(1.2)
    i, j = r.foco
    cena.play(Indicate(casas[i, j], color=AMARELO),
              estados[i, j].animate.set_stroke(AMARELO, width=5), run_time=.9)
    for vizinho in ((i - 1, j), (i, j - 1)):
        cor = CINZA if list(vizinho) in r.bloqueios else AZUL
        cena.play(estados[vizinho].animate.set_stroke(cor, width=4),
                  Indicate(casas[vizinho], color=cor), run_time=.65)
    cena.legendar('Olhe para os predecessores: um vem de cima, outro da esquerda. Nenhum valor foi calculado.')
    cena.wait(1.2)


def fluxo(cena, r: Fluxo):
    internos = [n for n in r.nos if n not in (r.fonte, r.destino)]
    pos = {r.fonte: [-5, 0, 0], r.destino: [5, 0, 0]}
    if len(internos) <= 2:
        locais = [[0, 1.45, 0], [0, -1.45, 0]]
    else:
        locais = [[-1.7, 1.45, 0], [-1.7, -1.45, 0], [1.7, 1.45, 0], [1.7, -1.45, 0]]
    pos.update(zip(internos, locais))
    nos = {n: VGroup(Circle(.34, color=AZUL, fill_color=FUNDO, fill_opacity=1), txt(n, 24))
           .move_to(pos[n]) for n in r.nos}
    linhas, rotulos = {}, VGroup()
    for a in r.arestas:
        linha = Arrow(pos[a.de], pos[a.para], buff=.4, color=CINZA, stroke_width=3,
                      max_tip_length_to_length_ratio=.1)
        linhas[a.de, a.para] = linha
        rotulo = txt(f'{a.fluxo}/{a.capacidade}', 22).move_to(linha.get_center() + UP * .27)
        rotulo.add_background_rectangle(color=FUNDO, opacity=1, buff=.03)
        rotulos.add(rotulo)
    cena.play(*[Create(l) for l in linhas.values()], *[FadeIn(n) for n in nos.values()],
              FadeIn(rotulos), run_time=1.4)
    legenda = txt('Rótulo: fluxo atual / capacidade', 23, CINZA).move_to([0, 2.35, 0])
    cena.play(FadeIn(legenda), run_time=.5)
    cena.legendar('A capacidade total e o espaço ainda disponível são quantidades diferentes.')
    cena.wait(1.2)
    a, b = r.primeiro_passo
    cena.play(linhas[a, b].animate.set_color(AMARELO).set_stroke(width=6),
              Indicate(nos[a], color=AMARELO), run_time=.8)
    conta = txt('capacidade − fluxo = ?', 25, AZUL).move_to([0, -2.25, 0])
    cena.play(FadeIn(conta), run_time=.6)
    cena.legendar('Examine apenas essa aresta. O restante do caminho e o fluxo máximo ficam para você.')
    cena.wait(1.2)


def karnaugh(cena, r: Karnaugh):
    nl, nc = len(r.celulas), len(r.celulas[0])
    labels_l = ['0', '1'] if nl == 2 else ['00', '01', '11', '10']
    labels_c = ['0', '1'] if nc == 2 else ['00', '01', '11', '10']
    lado = .85
    desenho, caixas, _ = grade(r.celulas, [0, -.05], lado)
    cabecalhos = VGroup(*[txt(l, 24, AZUL).next_to(caixas[i, 0], LEFT, buff=.24) for i, l in enumerate(labels_l)],
                         *[txt(l, 24, AZUL).next_to(caixas[0, j], UP, buff=.22) for j, l in enumerate(labels_c)])
    cena.play(Create(desenho), FadeIn(cabecalhos), run_time=1.3)
    nota = txt('Ordem Gray: só um bit muda entre vizinhos', 25, AZUL).move_to([0, 2.65, 0])
    cena.play(FadeIn(nota), run_time=.5)
    cena.legendar('As bordas opostas também são vizinhas. Zero obrigatório não entra num grupo de uns.')
    cena.play(Indicate(cabecalhos[-1], color=AMARELO), run_time=.7)
    cena.wait(1)
    if r.grupo:
        destaques = VGroup(*[SurroundingRectangle(caixas[i, j], color=AMARELO, buff=-.06,
                                                 corner_radius=.1, stroke_width=4) for i, j in r.grupo])
        cena.play(Create(destaques), run_time=.9)
        cena.legendar('Este é só um grupo possível. Ainda há uns sem grupo; nenhuma expressão foi simplificada.')
        cena.wait(1.5)


def circuito(cena, r: Circuito):
    pos, objetos, fios = {}, VGroup(), VGroup()
    for i, nome in enumerate(r.entradas):
        y = 1.4 - i * 1.2
        pos[nome] = [-5.7, y, 0]
        objetos.add(txt(nome, 25, AZUL).move_to([-6.05, y, 0]))
    centros = [-3.5] if len(r.portas) == 1 else [-3.8 + i * 1.55 for i in range(len(r.portas))]
    gates = []
    ordem_portas = {p.id: i for i, p in enumerate(r.portas)}
    for indice, (x, p) in enumerate(zip(centros, r.portas)):
        caixa = Rectangle(width=1.15, height=.95, color=AZUL).move_to([x, .1, 0])
        rotulo = txt(p.tipo, 20, largura=1).move_to(caixa)
        nome = txt(p.id, 18, CINZA).next_to(caixa, DOWN, buff=.12)
        gate = VGroup(caixa, rotulo, nome)
        gates.append(gate)
        objetos.add(gate)
        for k, entrada in enumerate(p.entradas):
            alvo = caixa.get_left() + UP * ((.2 if k == 0 else -.2) if len(p.entradas) == 2 else 0)
            origem = pos[entrada]
            if entrada in r.entradas:
                # Mantém fios de entradas posteriores fora das caixas das portas anteriores.
                antes = [alvo[0] - .18 - .12 * k, origem[1], 0]
                curva = [antes[0], alvo[1], 0]
                segmentos = [(origem, antes), (antes, curva), (curva, alvo)]
            elif ordem_portas[entrada] < indice - 1:
                altura = 1.7 + .2 * k
                p1 = [origem[0] + .15, origem[1], 0]
                p2 = [p1[0], altura, 0]
                p3 = [alvo[0] - .2, altura, 0]
                p4 = [p3[0], alvo[1], 0]
                segmentos = list(zip([origem, p1, p2, p3, p4], [p1, p2, p3, p4, alvo]))
            else:
                segmentos = [(origem, alvo)]
            for a, b in segmentos:
                if sum((a[m] - b[m]) ** 2 for m in range(3)) > .0001:
                    fios.add(Line(a, b, color=CINZA, stroke_width=2))
        pos[p.id] = caixa.get_right()
    saida = txt('saída ?', 20, AZUL).move_to([.65, .1, 0])
    fios.add(Line(pos[r.portas[-1].id], saida.get_left(), color=CINZA))
    cena.play(Create(fios), FadeIn(objetos), FadeIn(saida), run_time=1.4)
    colunas = r.entradas + [p.id for p in r.portas]
    linhas = []
    for n in range(2 ** len(r.entradas)):
        bits = list(f'{n:0{len(r.entradas)}b}')
        linhas.append(bits + ['?'] * len(r.portas))
    lado = min(.55, 4.6 / len(colunas), 3.6 / len(linhas))
    tabela, celulas, _ = grade(linhas, [3.75, -.1], lado)
    cab = VGroup(*[txt(c, 19, AZUL, lado * .9).next_to(celulas[0, j], UP, buff=.12)
                   for j, c in enumerate(colunas)])
    cena.play(Create(tabela), FadeIn(cab), run_time=1.1)
    alvo = VGroup(*[celulas[r.linha_foco, j] for j in range(len(colunas))])
    cena.play(Create(SurroundingRectangle(alvo, color=AMARELO, buff=.04)),
              Indicate(gates[0], color=AMARELO), run_time=.9)
    cena.legendar('As combinações de entrada estão dadas. Calcule primeiro um sinal intermediário da linha marcada.')
    cena.wait(1.8)


def reducao(cena, r: Reducao):
    cab = VGroup(txt('Instância x de ' + r.origem, 24, AZUL, 4).move_to([-4.4, 2.0, 0]),
                 txt('Instância f(x) de ' + r.destino, 24, AZUL, 4).move_to([4.4, 2.0, 0]))
    nos = [Circle(.2, color=AZUL).move_to([-4.4 + math.cos(a), .25 + math.sin(a), 0])
           for a in (0, 2 * math.pi / 3, 4 * math.pi / 3)]
    desenho = VGroup(*[Line(nos[i].get_center(), nos[(i + 1) % 3].get_center(), color=CINZA)
                       for i in range(3)], *nos)
    caixa = Rectangle(width=2.5, height=1.4, color=AZUL).move_to([0, .25, 0])
    funcao = txt('f: transformação\npolinomial', 25, AZUL, largura=2.2).move_to(caixa)
    desconhecida = VGroup(Rectangle(width=2.5, height=2, color=CINZA), txt('?', 46, AZUL)).move_to([4.4, .25, 0])
    cena.play(FadeIn(cab), Create(desenho), Create(caixa), FadeIn(funcao), run_time=1.2)
    seta1 = Arrow([-2.9, .25, 0], [-1.35, .25, 0], color=AZUL, buff=.08)
    seta2 = Arrow([1.35, .25, 0], [3, .25, 0], color=AZUL, buff=.08)
    cena.play(Create(seta1), Create(seta2), FadeIn(desconhecida), run_time=1)
    cena.legendar('Para provar B difícil, partimos de um problema A que já sabemos ser difícil.')
    cena.wait(1.5)
    condicao = txt('x é SIM em A  ⇔  f(x) é SIM em B', 28, AZUL, config.frame_width - 2).move_to([0, -1.85, 0])
    pendente = txt('Você ainda precisa construir f e justificar a equivalência.', 23, CINZA,
                   config.frame_width - 2).move_to([0, -2.5, 0])
    cena.play(FadeIn(condicao), FadeIn(pendente), run_time=.8)
    cena.wait(1.4)


def esquema(cena, r: Esquema):
    import textwrap
    n = len(r.blocos)
    graus = {b.id: 0 for b in r.blocos}
    saidas = {b.id: [] for b in r.blocos}
    for a, b in r.ligacoes:
        graus[b] += 1
        saidas[a].append(b)
    fila = [ident for ident, grau in graus.items() if grau == 0]
    nivel = dict.fromkeys(graus, 0)
    processados = 0
    for ident in fila:
        processados += 1
        for destino in saidas[ident]:
            nivel[destino] = max(nivel[destino], nivel[ident] + 1)
            graus[destino] -= 1
            if graus[destino] == 0:
                fila.append(destino)
    if processados != n:
        nivel = {b.id: i % 2 for i, b in enumerate(r.blocos)}
    colunas = max(nivel.values()) + 1
    largura_caixa = min(3.25, (config.frame_width - 1.2) / colunas - .3)
    distancia = min(4.1, largura_caixa + .65)
    posicoes = {}
    objetos, caixas = {}, {}
    for i, b in enumerate(r.blocos):
        coluna = nivel[b.id]
        colegas = [bloco.id for bloco in r.blocos if nivel[bloco.id] == coluna]
        linha = colegas.index(b.id)
        x = (coluna - (colunas - 1) / 2) * distancia
        y = ((len(colegas) - 1) / 2 - linha) * 1.6
        posicoes[b.id] = [x, y, 0]
        caixa = Rectangle(width=largura_caixa, height=1.25, color=AZUL,
                          fill_color=FUNDO, fill_opacity=1).move_to(posicoes[b.id])
        conteudo = '\n'.join(textwrap.wrap(b.texto, width=23))
        if b.lacuna:
            conteudo += '\n?'
        rotulo = txt(conteudo, 23, AZUL if b.lacuna else TINTA, largura=largura_caixa - .3)
        if rotulo.height > 1.05:
            rotulo.scale_to_fit_height(1.05)
        objetos[b.id] = VGroup(caixa, rotulo.move_to(caixa))
        caixas[b.id] = caixa
    for a, b in r.ligacoes:
        dx, dy = posicoes[b][0] - posicoes[a][0], posicoes[b][1] - posicoes[a][1]
        if abs(dx) >= abs(dy):
            inicio = caixas[a].get_right() if dx > 0 else caixas[a].get_left()
            fim = caixas[b].get_left() if dx > 0 else caixas[b].get_right()
        else:
            inicio = caixas[a].get_top() if dy > 0 else caixas[a].get_bottom()
            fim = caixas[b].get_bottom() if dy > 0 else caixas[b].get_top()
        seta = Arrow(inicio, fim, color=CINZA, buff=.08, stroke_width=2.5,
                     max_tip_length_to_length_ratio=.2)
        cena.play(Create(seta), run_time=.35)
    cena.play(*[FadeIn(o) for o in objetos.values()], run_time=1)
    cena.legendar('Observe como as partes se relacionam. O bloco com ? fica para você completar.')
    for ident in r.destacar:
        cena.play(Indicate(caixas[ident], color=AMARELO), run_time=.7)
    cena.wait(1.2)


def desenhar(cena, roteiro):
    {GradeDP: grade_dp, Fluxo: fluxo, Karnaugh: karnaugh, Circuito: circuito, Reducao: reducao,
     Esquema: esquema}[type(roteiro)](cena, roteiro)
