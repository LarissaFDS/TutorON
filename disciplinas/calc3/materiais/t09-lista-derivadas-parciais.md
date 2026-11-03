---
id: calc3-lista-derivadas-parciais
titulo: Exercícios resolvidos de derivadas parciais — definição, equação do calor, Clairaut e cúbicas harmônicas
assunto: calc3-08-limites-derivadas-parciais
tipo: gabarito
questao: 1 a 5
resolucao: sim
fonte: Exercicios_Limites_Derivadas.pdf (página do Notion "Cálculo 3"; resolução manuscrita escaneada), páginas de derivadas parciais
autoria: Resolução manuscrita anexada ao Notion da turma (autoria não identificada no arquivo); paráfrase e revisão da equipe TutorON
licenca: Não declarada (material de turma); o PDF não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia a resolução e não reproduz o manuscrito
fontes_catalogo: ufal-calc3-notion-resolucoes
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Resolução manuscrita da turma, parafraseada. Status da resolução: validada (todas as contas conferidas com SymPy). O original numera dois exercícios como "3"; aqui eles são 3a e 3b.

Ex. 1. Pela definição, para $f = xy^2$: $f_x = \lim_{h\to0} \frac{(x+h)y^2 - xy^2}{h} = y^2$ e $f_y = \lim_{h\to0} \frac{x(y+h)^2 - xy^2}{h} = \lim_{h\to0}(2xy + xh) = 2xy$.

Ex. 2. $u(x,t) = \dfrac{1}{2\sqrt{\pi t}}\,e^{-x^2/(4t)}$ (t > 0) satisfaz a equação do calor $u_t = u_{xx}$: as duas derivadas dão $u \cdot \left(\dfrac{x^2}{4t^2} - \dfrac{1}{2t}\right)$.

Ex. 3a. Não existe f com $f_x = xy$ e $f_y = x^2$: se existisse (com derivadas segundas contínuas), pelo Teorema de Clairaut $f_{xy} = f_{yx}$, mas $(xy)_y = x$ e $(x^2)_x = 2x$, diferentes para x ≠ 0.

Ex. 3b. Com derivadas contínuas, $f_{yxx} = f_{xyx}$ (= $f_{xxy}$): Clairaut permite trocar a ordem das derivadas parciais.

Ex. 4. $u = \operatorname{sen}(mx)\,e^{-m^2 t}$ resolve $u_t = u_{xx}$: $u_t = -m^2 u$ e $u_{xx} = -m^2 u$.

Ex. 5. A cúbica $f = ax^3 + bx^2y + cxy^2 + dy^3$ é harmônica ($f_{xx} + f_{yy} = 0$) se e só se $c = -3a$ e $b = -3d$: $f_{xx} + f_{yy} = (6a + 2c)x + (2b + 6d)y$, e os dois coeficientes têm de ser zero.

**Verificação:** no ex. 5, com a = 1, d = 0: $f = x^3 - 3xy^2$, $f_{xx} = 6x$, $f_{yy} = -6x$, soma 0 (é a parte real de $(x+iy)^3$).
