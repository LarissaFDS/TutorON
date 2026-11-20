---
id: controle-anot-especificacoes-k
titulo: Exemplo: escolher K em K·2/(s(s+4)) com realimentação unitária para resposta subamortecida, sobressinal até 5% e tempo de subida 10–90% até 1,8 s: 2 < K ≤ 4,2
assunto: controle-05-resposta-temporal
tipo: resolucao
resolucao: sim
fonte: Anotações "Análise de Resposta Temporal" (1º out. 2026), p. 9–11
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

**Enunciado (paráfrase):** ganho $K$ em série com $\frac{2}{s(s + 4)}$, realimentação **unitária negativa**. Achar $K$ para (a) resposta subamortecida, (b) $M_p \le 5\%$, (c) $t_r$ (10–90%) $\le 1{,}8$ s.

**Malha fechada:** $G_{mf} = \frac{2K}{s^2 + 4s + 2K}$, segunda ordem padrão com ganho estático $1$. Comparando com $s^2 + 2\zeta\omega_ns + \omega_n^2$: $\omega_n = \sqrt{2K}$ e $2\zeta\omega_n = 4$, logo $\zeta = \frac{2}{\sqrt{2K}}$.

- (a) $\zeta < 1 \Rightarrow \sqrt{2K} > 2 \Rightarrow K > 2$.
- (b) $M_p \le 5\% \Rightarrow \zeta \ge 0{,}69 \Rightarrow \sqrt{2K} \le 2{,}90 \Rightarrow K \le 4{,}2$.
- (c) $t_r \approx 1{,}8/\omega_n \le 1{,}8 \Rightarrow \omega_n \ge 1 \Rightarrow K \ge 0{,}5$.

**Resposta:** $2 < K \le 4{,}2$.

**Verificação:** `scipy.signal.step` com $K = 4{,}2$: sobressinal de cerca de $5\%$; com $K = 3$, menor. O tipo 1 (polo na origem em malha aberta) garante erro nulo ao degrau.
