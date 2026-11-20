---
id: controle-anot-diagrama-blocos
titulo: Diagrama de blocos: série, paralelo e realimentação; função de transferência de malha fechada Y(s)/R(s) = G(s)/(1 + G(s)H(s)) com realimentação negativa pelo sensor H(s) e G/(1 − GH) com positiva; mover somador e ponto de ramificação
assunto: controle-03-diagramas-blocos
tipo: resolucao
resolucao: sim
fonte: Anotações "Diagrama de Blocos" (1º out. 2026), p. 1–4
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

**Resumo:** para achar $\frac{Y(s)}{R(s)}$ de uma malha com realimentação negativa $H(s)$, reduza série e paralelo e use $\frac{G}{1 + GH}$.

**Elementos:** bloco $Y = GU$; somador (cada entrada com seu sinal); ponto de ramificação (o sinal segue igual para vários ramos).

**Estruturas:** série $G_1G_2$; paralelo: soma com os sinais do somador (ex.: $G_1 + G_2 - G_3$).

**Realimentação:** controlador $C(s)$ e planta $G_p(s)$ no ramo direto, $G = CG_p$; sensor $H(s)$ no retorno; erro $E = R - HY$ (realimentação **negativa**). Então $Y = G(R - HY)$ e a função de transferência de **malha fechada** é
$$G_{mf}(s) = \frac{Y(s)}{R(s)} = \frac{G(s)}{1 + G(s)H(s)} = \frac{C G_p}{1 + C G_pH}$$ (ganho do ramo direto sobre um mais o ganho de malha). $G$ é o ganho do ramo direto e $GH$ o ganho de **malha aberta**. $H = 1$: realimentação unitária.

**Sinal (complemento das anotações, que deixam "ver como fica o sinal"):** realimentação negativa dá $1 + GH$ no denominador; **positiva** ($E = R + HY$) dá $\frac{G}{1 - GH}$.

**Mover blocos:** somador de depois para antes de $G$: a entrada $X$ passa por $1/G$; de antes para depois: $X$ passa por $G$. Ponto de ramificação de antes para depois de $G$: o ramo ganha $1/G$; de depois para antes: ganha $G$.

**Verificação:** `sympy.solve` de $Y = G(R \mp HY)$ dá $G/(1 \pm GH)$; com $G = 2/(s+1)$, $H = 1$: $Y/R = 2/(s+3)$.
