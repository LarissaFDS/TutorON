---
id: sinais-anot-edo-solucao
titulo: Solução de EDO: polinômio característico, raízes reais, repetidas e complexas, estabilidade pelas raízes; dy/dt + 2y = 2 com y(0) = 4; diagrama com integradores
assunto: sinais-06-edo
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Modelos por equações diferenciais" (1 maio 2026)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sinais e Sistemas 2026.1; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-sinais-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Resposta natural:** com $Q(\lambda) = \lambda^n + a_{n-1}\lambda^{n-1} + \dots + a_0$ (polinômio característico):
- raízes reais distintas: $\sum c_ie^{\lambda_it}$. Ex.: $\ddot y + 5\dot y + 6y$: $\lambda = -2, -3$.
- raiz repetida: $(c_1 + c_2t)e^{\lambda t}$. Ex.: $\ddot y + 4\dot y + 4y$: $\lambda = -2$ dupla.
- par complexo $\sigma \pm j\omega$: $2|c|e^{\sigma t}\cos(\omega t + \theta)$.

**Estabilidade (sistema causal):** todas as raízes com **parte real negativa** $\Rightarrow$ BIBO estável; alguma com parte real positiva (ou raiz repetida no eixo imaginário) $\Rightarrow$ instável; raízes simples com parte real zero $\Rightarrow$ marginalmente estável.

**Exemplo:** $\dot y + 2y = 2$, $y(0) = 4$: particular $y_p = 1$, natural $ce^{-2t}$; $y(0) = 1 + c = 4 \Rightarrow c = 3$:
$$y(t) = 1 + 3e^{-2t},\quad t \ge 0.$$

**Diagrama com integradores** para $a_3y^{(3)} + a_2\ddot y + a_1\dot y + a_0y = b_0u$: isole a derivada mais alta,
$$y^{(3)} = \frac{b_0}{a_3}u - \frac{a_2}{a_3}\ddot y - \frac{a_1}{a_3}\dot y - \frac{a_0}{a_3}y,$$
e ligue três integradores em cascata ($y^{(3)} \to \ddot y \to \dot y \to y$) com as realimentações. (Correção: a segunda versão das anotações escreve $-\frac{b_0}{a_3}u$; o sinal da entrada é positivo, como na primeira versão.)

**Verificação:** `dsolve` de $y' + 2y = 2$, $y(0) = 4$ devolve $1 + 3e^{-2t}$; $y(\infty) = 1 = 2/2$ (ganho DC).
