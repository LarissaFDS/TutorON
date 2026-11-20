---
id: controle-anot-suspensao
titulo: Modelo de suspensão de automóvel (1/4 de carro, duas massas): X1(s)/F(s) = (bs + K1)/(M1M2s⁴ + b(M1+M2)s³ + (M1K1 + M2K1 + M1K2)s² + bK2s + K1K2)
assunto: controle-02-modelagem
tipo: resolucao
resolucao: sim
fonte: Anotações "Revisão de Laplace e Sistemas mecânicos" (19 ago. 2026), p. 8–10
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Modelo:** massa do carro $M_1$ (deslocamento $x_1$) sobre a suspensão (mola $K_1$, amortecedor $b$); massa da roda $M_2$ ($x_2$) sobre o pneu (mola $K_2$); força $f(t)$ aplicada na roda. Figura descrita em texto.

**Forças (CI nulas):**
- $M_1$: $M_1\ddot x_1 = K_1(x_2 - x_1) + b(\dot x_2 - \dot x_1)$, ou $(M_1s^2 + bs + K_1)X_1 = (bs + K_1)X_2$.
- $M_2$: $M_2\ddot x_2 = K_1(x_1 - x_2) + b(\dot x_1 - \dot x_2) - K_2x_2 + f$, ou $(M_2s^2 + bs + K_1 + K_2)X_2 - (bs + K_1)X_1 = F$.

**Eliminando $X_2$:**
$$G(s) = \frac{X_1(s)}{F(s)} = \frac{bs + K_1}{M_1M_2s^4 + b(M_1 + M_2)s^3 + (M_1K_1 + M_2K_1 + M_1K_2)s^2 + bK_2s + K_1K_2}.$$
Nas anotações a expansão tem termos riscados no meio ($b^2s^2$ e $2bK_1s$ se cancelam); o resultado final confere.

**Verificação:** `sympy.solve` do sistema das duas equações dá o mesmo $G$; em regime com força constante, $G(0) = 1/K_2$ (só a mola do pneu $K_2$ apoia no chão).
