---
id: controle-anot-fracoes-parciais
titulo: Resposta de um sistema por frações parciais: polos reais (s+1)/(s²+5s+6), complexos 10/(s²+12s+100) e múltiplos (s²+2s+3)/(s+1)³
assunto: controle-01-laplace-ft
tipo: resolucao
resolucao: sim
fonte: Anotações "Revisão de Laplace e Sistemas mecânicos" (19 ago. 2026), p. 4 e 10–16
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Função de transferência:** $G(s) = \frac{Y(s)}{U(s)} = \frac{B(s)}{A(s)}$ com **condições iniciais nulas**; polos são raízes de $A$ (polinômio característico), zeros de $B$; $Y = GU$. Resíduo de um polo simples: $A_i = (s - p_i)Y(s)|_{s = p_i}$; $y(t) = \sum A_ie^{p_it}$.

**Ex. 1 (polos reais), degrau:** $Y = \frac{s + 1}{s(s + 2)(s + 3)}$; $A_1 = 1/6$, $A_2 = 1/2$, $A_3 = -2/3$:
$$y(t) = \tfrac16 + \tfrac12e^{-2t} - \tfrac23e^{-3t},\ t \ge 0.$$ O termo $1/6$ vem da entrada; as exponenciais, dos polos de $G$.

**Ex. 2 (polos complexos), degrau:** $G = \frac{10}{s^2 + 12s + 100}$, polos $-6 \pm j8$; $A_1 = 0{,}1$; $A_2 = \frac{1}{16}e^{-j(\theta + \pi/2)}$ com $\theta = \angle(-6 + j8) = 126{,}87^\circ$ (parte real negativa: $\pi + \arctan(8/-6)$). Juntando os conjugados:
$$y(t) = 0{,}1 + \tfrac18e^{-6t}\cos(8t - \theta - \pi/2).$$

**Ex. 3 (polo múltiplo):** $G = \frac{s^2 + 2s + 3}{(s + 1)^2}$, $u = e^{-t}$: $Y = \frac{s^2 + 2s + 3}{(s + 1)^3}$; $D_1 = 2$, $D_2 = 0$, $D_3 = 1$, logo $Y = \frac{1}{s + 1} + \frac{2}{(s + 1)^3}$.

**Correção:** as anotações escrevem no fim $y = e^{-t} + t^2e^{-3t}$; o certo é
$$y(t) = e^{-t} + t^2e^{-t},\ t \ge 0,$$ porque $\mathcal{L}^{-1}\{2/(s+1)^3\} = t^2e^{-t}$.

**Verificação:** $y(0) = 0$ nos exemplos 1 e 2 e $y(0) = 1$ no 3 (grau igual); `inverse_laplace_transform` confirma as três respostas.
