---
id: cg-rasterizacao-de-retas-dda-algoritmo-de-bresenham-ponto-medio-parametro-de-decisao
titulo: Rasterização de retas: equação da reta e DDA, algoritmo de Bresenham (ponto médio) com parâmetro de decisão, incrementos E e NE; exemplo de (1,1) a (8,5)
assunto: cg-01-fundamentos-e-rasterizacao
tipo: exercicio_resolvido
questao: aula de Rasterização e atividade do algoritmo de Bresenham
resolucao: sim
fonte: Exercícios e provas de Computação Gráfica do Prof. Marcelo Costa Oliveira (IC-UFAL)
curso: Ciência da Computação (UFAL), COMP381 Computação Gráfica; aulas de 2012 a 2017 e provas de 2014 e 2021.2 (Prof. Marcelo Costa Oliveira)
fontes_catalogo: ufal-marcelo-aulas-cg,ufal-cg-provas-exercicios
autoria: Questões do Prof. Marcelo Costa Oliveira (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Gráfica (IC-UFAL), aula de Rasterização e atividade do algoritmo de Bresenham (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Rasterização:** converter primitivas vetoriais (retas, círculos, polígonos) em pixels.

**Equação da reta:** $y = y_1 + m(x - x_1)$ com $m = \dfrac{y_2-y_1}{x_2-x_1}$. O **DDA** soma $m$ a $y$ a cada passo em $x$ e arredonda: usa ponto flutuante.

**Bresenham (ponto médio)**, para $0 \le m \le 1$, só com inteiros:
- $dx = x_2 - x_1$, $dy = y_2 - y_1$;
- parâmetro inicial $p = 2dy - dx$;
- a cada passo $x$ aumenta 1; se $p < 0$ escolhe **E** (mesmo $y$) e faz $p \mathrel{+}= 2dy$; senão escolhe **NE** ($y$ aumenta 1) e faz $p \mathrel{+}= 2(dy - dx)$.

**Exemplo de (1,1) a (8,5):** $dx = 7$, $dy = 4$, $p_0 = 1$, $\text{inc}_E = 8$, $\text{inc}_{NE} = -6$.

| x | y | p | escolha |
|---|---|---|---|
| 1 | 1 | 1 | NE |
| 2 | 2 | −5 | E |
| 3 | 2 | 3 | NE |
| 4 | 3 | −3 | E |
| 5 | 3 | 5 | NE |
| 6 | 4 | −1 | E |
| 7 | 4 | 7 | NE |
| 8 | 5 | — | fim |

Pixels: (1,1), (2,2), (3,2), (4,3), (5,3), (6,4), (7,4), (8,5).

Para outras inclinações troque os papéis de $x$ e $y$ ($|m| > 1$) ou o sentido do passo ($m < 0$).

```python
def bresenham(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    p, pts, y = 2 * dy - dx, [], y1
    for x in range(x1, x2 + 1):
        pts.append((x, y))
        if p < 0:
            p += 2 * dy
        else:
            y, p = y + 1, p + 2 * (dy - dx)
    return pts
```

**Verificação:** `test_bresenham` roda o código e confere os 8 pixels e que cada um está a menos de meio pixel da reta ideal.
