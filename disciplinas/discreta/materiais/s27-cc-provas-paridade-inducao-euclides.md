---
id: discreta-cc-provas-paridade-inducao-euclides
titulo: Simplificação lógica, paridade, divisibilidade, indução de 2^(2n) - 1 e Euclides (provas de CC)
assunto: discreta-02-demonstracoes
tipo: resolucao
resolucao: sim
questao: Prova 2 2020.2 (Q1 a Q5); Final 2020.2 (Q2); Reavaliação 1 2020.2 (Q5)
fonte: Provas do Prof. Bruno Pimentel (2020.2)
curso: Ciência da Computação (UFAL), turma de 2020.2 (Prof. Bruno Pimentel)
fontes_catalogo: ufal-cc-discreta-provas-bruno
autoria: Prof. Bruno Pimentel (IC-UFAL), enunciados parafraseados; resolução da equipe TutorON com auxílio de IA
licenca: Não declarada (provas do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia os enunciados e traz resolução própria; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Resolução da equipe TutorON, não é gabarito do professor. Status da resolução: validada.

**Simplificar** (Prova 2): $[p\land\neg(\neg p\lor q)]\lor(p\land q)$. De Morgan: $\neg(\neg p\lor q)\equiv p\land\neg q$, então fica $(p\land\neg q)\lor(p\land q)\equiv p\land(\neg q\lor q)\equiv p$. E $(p\to r)\lor(q\to r)\equiv\neg p\lor\neg q\lor r\equiv(p\land q)\to r$.

**Paridade:** se a é par e b é ímpar, $a=2k$ e $b=2m+1$, logo $a+b=2(k+m)+1$, ímpar. Diga "sem perda de generalidade" para o caso trocado.

**Divisibilidade:** se $a\mid b$ e $b\mid c$, então $b=ak$ e $c=bm=a(km)$, logo $c^2=a\cdot(ak^2m^2)$ e $a\mid c^2$.

**Congruência:** se $a\equiv b \pmod m$, então $m\mid(a-b)$, logo $m\mid(a-b)c=ac-bc$, ou seja, $ac\equiv bc\pmod m$.

**Indução: $3\mid 2^{2n}-1$ para $n\ge1$.** Base: $2^2-1=3$. Passo: suponha $2^{2k}-1=3t$. Então $2^{2(k+1)}-1=4\cdot2^{2k}-1=4(3t+1)-1=3(4t+1)$. O erro comum é "provar" o passo testando n = 2 e n = 3: exemplos não são prova.

Também cai a soma $1+2+\dots+n=n(n+1)/2$: no passo, some $k+1$ dos dois lados.

**Euclides para mdc(4040, 125):** $4040=32\cdot125+40$; $125=3\cdot40+5$; $40=8\cdot5+0$. O último resto não nulo é 5.

**Verificação:** as equivalências foram conferidas por tabela-verdade, a divisibilidade de $2^{2n}-1$ e a soma para n de 1 a 200, e o mdc com math.gcd em Python.
