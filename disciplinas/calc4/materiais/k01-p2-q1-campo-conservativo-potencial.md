---
id: calc4-p2-q1-campo-conservativo
titulo: P2 de Cálculo IV, Q1 — F = x² i + y² j é conservativo? Função potencial e integral de linha sobre a parábola y = 2x² de (−1, 2) a (2, 8)
assunto: calc4-01-campos-conservativos-integrais-de-linha
tipo: prova
questao: 1
resolucao: sim
fonte: Prova 2 de Cálculo IV (Instituto de Computação, UFAL; Prof. Gleydson Santos da Silva; arquivo P2C4.pdf), questão 1 | enunciado parafraseado
curso: Engenharia de Computação (UFAL), ECOM023 Cálculo 4, 4º período; semestre não identificado
fontes_catalogo: ufal-calc4-p2-gleydson
autoria: Enunciado: Prof. Gleydson Santos da Silva (IC-UFAL); resolução da equipe TutorON, conferida com SymPy
licenca: Não declarada (prova da disciplina); PDF não versionado
publicacao_transcricao: não autorizada; enunciado parafraseado
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Prova 2 de Cálculo IV (IC-UFAL, Prof. Gleydson Santos da Silva), questão 1, parafraseada. Status da resolução: pendente de confirmação do professor (a prova não traz gabarito; a resolução é da equipe TutorON e não é gabarito do professor). Prova é atividade avaliativa: o tutor guia, não entrega.

**Enunciado.** Decidir se $\mathbf F(x,y) = x^2\,\mathbf i + y^2\,\mathbf j$ é conservativo, dar uma função potencial e calcular $\int_C \mathbf F\cdot d\mathbf r$ no arco da parábola $y = 2x^2$ de $(-1, 2)$ a $(2, 8)$.

**Teste.** Com $P = x^2$ e $Q = y^2$: $\partial Q/\partial x = 0 = \partial P/\partial y$, e $\mathbf F$ é definido em todo o plano (simplesmente conexo). Logo é conservativo.

**Potencial.** Procure $f$ com $f_x = x^2$ e $f_y = y^2$: integrando a primeira, $f = \frac{x^3}{3} + g(y)$; derivando em $y$, $g'(y) = y^2$. Então $f(x,y) = \frac{x^3}{3} + \frac{y^3}{3}$ (mais uma constante).

**Integral.** Pelo teorema fundamental das integrais de linha, só importam as pontas:
$$\int_C \mathbf F\cdot d\mathbf r = f(2,8) - f(-1,2) = \frac{8 + 512}{3} - \frac{-1 + 8}{3} = \frac{513}{3} = 171.$$
A forma da parábola não entra. Conferência direta: com $x = t$, $y = 2t^2$, $t \in [-1, 2]$, a integral $\int_{-1}^{2}(t^2 + 16t^5)\,dt$ também dá 171.

Erro comum: esquecer que o teste $Q_x = P_y$ só garante potencial num domínio simplesmente conexo.

**Verificação:** `test_p2_q1_campo_conservativo` confere o rotacional, o potencial e a integral pela parametrização.
