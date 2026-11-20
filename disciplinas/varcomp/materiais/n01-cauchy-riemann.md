---
id: varcomp-nota-ia-cauchy-riemann
titulo: Nota — equações de Cauchy-Riemann, funções analíticas: u_x = v_y, u_y = −v_x; exemplos z² e conjugado de z
assunto: varcomp-02-funcoes-analiticas-cauchy-riemann
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON escrita com IA (não é material do professor)
autoria: Equipe TutorON (rascunho gerado por IA); revisão humana pendente
licenca: Texto próprio da equipe
publicacao_transcricao: não se aplica
fontes_catalogo: beck-first-course-complex-analysis,mit-ocw-1804-2018
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Rascunho escrito por IA, aguardando revisão humana; fora da busca. Contas conferidas com SymPy em `tests_acervo/test_disciplina_varcomp.py`.

Escreva $f(z) = u(x, y) + i\,v(x, y)$ com $z = x + iy$. Se f é derivável em $z_0$, então valem as **equações de Cauchy-Riemann** (em palavras: u x igual a v y, u y igual a menos v x):
$$u_x = v_y, \qquad u_y = -v_x,$$
e $f'(z_0) = u_x + i v_x$. A recíproca precisa de hipótese: se as parciais de u e v existem, são contínuas numa vizinhança e satisfazem Cauchy-Riemann, então f é derivável ali. f é **analítica** (holomorfa) num aberto se é derivável em todos os pontos dele.

Exemplo 1: $f(z) = z^2 = (x^2 - y^2) + i(2xy)$. $u_x = 2x = v_y$; $u_y = -2y = -v_x$. Valem em todo o plano: $z^2$ é inteira, e $f' = 2x + 2iy = 2z$.

Exemplo 2: $f(z) = \bar z = x - iy$. $u_x = 1$, $v_y = -1$: falha em todo ponto. $\bar z$ não é derivável em lugar nenhum.

Exemplo 3: $f(z) = |z|^2 = x^2 + y^2$ ($v = 0$): $u_x = 2x = 0$ e $u_y = 2y = 0$ só em $z = 0$; é derivável só na origem e não é analítica em nenhum aberto.

**Verificação:** em $z^2$, a derivada pela definição na direção real ($\partial f/\partial x$) e na imaginária ($-i\,\partial f/\partial y$) dão ambas $2z$.
