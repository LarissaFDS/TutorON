---
id: varcomp-nota-ia-harmonicas
titulo: Nota — funções harmônicas e conjugada harmônica: Laplaciano nulo, u = x² − y², v = 2xy
assunto: varcomp-10-funcoes-harmonicas
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON escrita com IA (não é material do professor)
autoria: Equipe TutorON (rascunho gerado por IA); revisão humana pendente
licenca: Texto próprio da equipe
publicacao_transcricao: não se aplica
fontes_catalogo: mit-ocw-1804-2018,beck-first-course-complex-analysis
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Rascunho escrito por IA, aguardando revisão humana; fora da busca. Contas conferidas com SymPy em `tests_acervo/test_disciplina_varcomp.py`.

$u(x, y)$ é **harmônica** se tem derivadas de segunda ordem contínuas e $u_{xx} + u_{yy} = 0$ (Laplaciano nulo). Se $f = u + iv$ é analítica, u e v são harmônicas (derive as equações de Cauchy-Riemann: $u_{xx} = v_{yx} = v_{xy} = -u_{yy}$).

**Conjugada harmônica:** dada u harmônica num domínio simplesmente conexo, existe v com $u + iv$ analítica. Procedimento: $v_y = u_x$ (integre em y) e ajuste a "constante" em x com $v_x = -u_y$.

Exemplo: $u = x^2 - y^2$. $u_{xx} + u_{yy} = 2 - 2 = 0$. $v_y = u_x = 2x$ dá $v = 2xy + h(x)$; $v_x = 2y + h'(x) = -u_y = 2y$, então $h' = 0$ e $v = 2xy + C$. Assim $u + iv = z^2 + iC$.

**Verificação:** $\Delta(2xy) = 0$ e $(x + iy)^2 = x^2 - y^2 + 2ixy$ (SymPy).
