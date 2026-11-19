---
id: prob-anot-bayes-teste-diagnostico
titulo: Teorema de Bayes em teste diagnóstico — doença com prevalência de 1% e 5% de falsos positivos e falsos negativos
assunto: prob-02-bayes
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Probabilidade _250907_210206.pdf" (2025.2), pág. 5
autoria: Otávio Joshua Costa Brandão Menezes (aluno, equipe TutorON), anotações de estudo; paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações pessoais do aluno); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia as anotações e não reproduz imagens
fontes_catalogo: ufal-prob-anotacoes-2025-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Anotações de aluno (2025.2), parafraseadas. Status da resolução: validada (a montagem das anotações está certa; o valor final, que elas não calculam, foi completado). Conferido com `fractions` e simulação.

**Enunciado:** uma doença atinge 1% da população. O teste tem 5% de falsos positivos e 5% de falsos negativos. Qual a probabilidade de a pessoa ter a doença, dado que o teste deu positivo?

**Eventos:** D = tem a doença; $\bar D$ = não tem; + = teste positivo. $P(D)=0{,}01$, $P(\bar D)=0{,}99$, $P(+\mid D)=0{,}95$ (sensibilidade), $P(+\mid \bar D)=0{,}05$ (falso positivo).

As anotações nomeiam: positivo verdadeiro (RP) $= 0{,}95\cdot 0{,}01 = 0{,}0095$; falso positivo (FP) $= 0{,}05\cdot 0{,}99 = 0{,}0495$; total de positivos (TP) $= \text{RP} + \text{FP} = 0{,}059$.

$$P(D\mid +) = \frac{P(+\mid D)P(D)}{P(+\mid D)P(D) + P(+\mid \bar D)P(\bar D)} = \frac{0{,}0095}{0{,}059} \approx 0{,}1610.$$

Só cerca de 16% dos positivos estão doentes: como a doença é rara, os falsos positivos (vindos dos 99% sadios) superam os verdadeiros. Confundir $P(D\mid +)$ com $P(+\mid D) = 0{,}95$ é o erro clássico.

**Verificação:** em 10 000 pessoas, 100 doentes dão 95 positivos e 9 900 sadias dão 495 positivos; 95/590 ≈ 0,1610.
