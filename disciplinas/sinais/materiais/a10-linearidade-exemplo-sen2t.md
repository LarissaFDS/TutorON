---
id: sinais-anot-linearidade
titulo: Linearidade (homogeneidade e aditividade) e análise completa de y(t) = sen(2t)·u(t): memória, invertibilidade, causalidade, BIBO, invariância
assunto: sinais-04-propriedades-sistemas
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Propriedades de Sistemas" (8 abr. 2026)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sinais e Sistemas 2026.1; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-sinais-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Linear** = superposição: se $u_1 \to y_1$ e $u_2 \to y_2$, então $\alpha_1u_1 + \alpha_2u_2 \to \alpha_1y_1 + \alpha_2y_2$ (homogeneidade + aditividade).

- $\dot y + 2y = 2u$ (condições iniciais nulas): somando $\alpha_1$ vezes a equação de $y_1$ com $\alpha_2$ vezes a de $y_2$ sai a mesma equação para $\alpha_1y_1 + \alpha_2y_2$: **linear**.
- $y = u^2$: $(\alpha_1u_1 + \alpha_2u_2)^2 = \alpha_1^2y_1 + \alpha_2^2y_2 + 2\alpha_1\alpha_2u_1u_2 \ne \alpha_1y_1 + \alpha_2y_2$: **não linear**.

**Exemplo de prova: $y(t) = \mathrm{sen}(2t)\,u(t)$** ($u$ é a entrada):
1. Sem memória: só usa $u(t)$ no instante atual.
2. Não invertível: em $t = \pi/2$ (ou $\pi$) a saída é 0 para qualquer entrada.
3. Causal: não usa entrada futura.
4. BIBO estável: $|y| = |\mathrm{sen}\,2t|\,|u| \le 1\cdot M$.
5. **Variante:** $y(t - T) = \mathrm{sen}[2(t - T)]u(t - T)$, mas $T[u(t - T)] = \mathrm{sen}(2t)u(t - T)$.
6. Linear: $\mathrm{sen}(2t)[\alpha_1u_1 + \alpha_2u_2] = \alpha_1y_1 + \alpha_2y_2$.

**Verificação:** com $u = 1$, $T = \pi/4$ e $t = \pi/4$: um caminho dá $\mathrm{sen}\,0 = 0$, o outro $\mathrm{sen}(\pi/2) = 1$; a soma testada nos testes com SymPy fecha para o item 6 e falha para $u^2$.
