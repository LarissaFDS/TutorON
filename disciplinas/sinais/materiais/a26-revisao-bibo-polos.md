---
id: sinais-anot-revisao-bibo
titulo: Revisão prova 2, questão 1: G(s) = (s + 1)/(s² + 3s − 4) é BIBO estável? Polos 1 e −4; ajuste de K1 e K2 para G = 1/(s + 4); resposta a t·e^{−4t}
assunto: sinais-10-funcao-transferencia
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Revisão Prova 2" (30 jun. 2026), questão 1
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

**Enunciado (paráfrase):** $\ddot y + (3 + K_2)\dot y - (4 - K_1)y = \dot u + u$.

**(a) $K_1 = K_2 = 0$:** com CI nulas, $G(s) = \frac{s + 1}{s^2 + 3s - 4} = \frac{s + 1}{(s - 1)(s + 4)}$. Zero em $-1$; polos em $1$ e $-4$.

**Critério (correção):** a revisão anota "estabilidade: todas as partes reais negativas (>0)"; o "(>0)" contradiz a regra. Para um sistema causal com $G$ racional: **BIBO estável se e só se todos os polos têm parte real negativa** (estritamente menor que zero), depois de cancelar fatores comuns. Os **zeros não decidem** a estabilidade.

**Conclusão:** o polo $s = 1$ está no semiplano direito: **não é BIBO estável** (a resposta ao impulso tem o termo $e^{t}$). O zero $-1$ não cancela nenhum polo.

**(b) $K_1$ e $K_2$ para $G = \frac{1}{s + 4}$:** o denominador tem de ser $(s + 1)(s + 4) = s^2 + 5s + 4$, para o fator $s + 1$ cancelar o zero: $3 + K_2 = 5 \Rightarrow K_2 = 2$; $-(4 - K_1) = 4 \Rightarrow K_1 = 8$.

**(c)** Com $u = te^{-4t}u_{-1}(t)$: $U = \frac{1}{(s + 4)^2}$ (deslocamento em $s$), $Y = \frac{1}{(s+4)^3}$ e
$$y(t) = \frac{t^2}{2}e^{-4t},\quad t \ge 0.$$

**Verificação:** `roots` de $s^2 + 3s - 4$ dá $1$ e $-4$; a resposta ao impulso $\frac25e^{t} + \frac35e^{-4t}$ cresce sem limite; em (b), $(s+1)/(s^2+5s+4)$ simplifica para $1/(s+4)$; em (c), `inverse_laplace_transform` confirma.
