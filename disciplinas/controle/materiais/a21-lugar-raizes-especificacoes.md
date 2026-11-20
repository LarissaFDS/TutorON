---
id: controle-anot-lugar-raizes-intro
titulo: Lugar das raízes: região dos polos pelas especificações (ζ mínimo, σ mínimo, ωn mínimo); exemplo K/(s(s+1)) e complemento K/(s(s+2)): como desenhar, ponto de saída −1 e assíntotas
assunto: controle-07-lugar-raizes
tipo: resolucao
resolucao: sim
fonte: Anotações "Método Lugar das raízes" (11 nov. 2026), p. 1–3
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

**Região desejada (realimentação negativa, ganho $K$ em série com $G$):** polos de malha fechada são raízes de $1 + KG(s) = 0$.
- $M_p \le M_{p,max}$: $\zeta \ge \zeta_{min} = \frac{|\ln M_{p,max}|}{\sqrt{\pi^2 + \ln^2M_{p,max}}}$; polos dentro do setor $\theta \le \arccos\zeta_{min}$.
- $t_s \le t_{s,max}$ (2%): $|\sigma| \ge 4/t_{s,max}$ ($\sigma$: parte real do polo dominante).
- $t_r \le t_{r,max}$: $\omega_n \ge 1{,}8/t_{r,max}$ (fora do semicírculo de raio $\omega_n$).

**Lugar das raízes:** caminho dos polos de malha fechada quando $K$ vai de $0$ a $+\infty$.

**Exemplo:** $G = \frac{1}{s(s + 1)}$: $s^2 + s + K = 0$, $p = -\frac12 \pm \frac{\sqrt{1 - 4K}}{2}$. $K = 0$: polos de malha aberta $0$ e $-1$; $0 < K < 1/4$: reais distintos, aproximando-se; $K = 1/4$: duplo em $-1/2$; $K > 1/4$: $-\frac12 \pm j\frac{\sqrt{4K - 1}}{2}$, subindo na reta vertical $\sigma = -1/2$.

**Complemento da equipe, mesmo método:** $G = \frac{K}{s(s + 2)}$: $s^2 + 2s + K = 0$. Eixo real: segmento $[-2, 0]$. Duas assíntotas a $\pm90^\circ$ com centro $\sigma = \frac{0 + (-2)}{2} = -1$. Ponto de saída: $\frac{d}{ds}[s(s + 2)] = 0 \Rightarrow s = -1$, com $K = 1$. Para $K > 1$: $-1 \pm j\sqrt{K - 1}$ (reta $\sigma = -1$). Estável para todo $K > 0$.

**Verificação:** `numpy.roots` de $s^2 + 2s + K$ para $K = 0{,}5;\ 1;\ 5$ dá $-0{,}29$ e $-1{,}71$; $-1$ duplo; $-1 \pm 2j$.
