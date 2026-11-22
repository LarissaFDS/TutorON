---
id: discreta-cc-conjuntos-extensao-leis
titulo: Conjuntos por extensão, diagrama de Venn e leis da álgebra dos conjuntos (provas de CC)
assunto: discreta-03-conjuntos
tipo: resolucao
resolucao: sim
questao: Prova 1 de 2017 (Q1 a Q3); Prova 1 2020.2 e 2021.1 (Q1); Reavaliação 1 e Final 2020.2 (Q1)
fonte: Prova Escrita 01 de Matemática Discreta (COMP208, Prof. Lucas Amorim, 2017) e provas do Prof. Bruno Pimentel (2020.2 e 2021.1)
curso: Ciência da Computação (UFAL), turmas de 2017 (Prof. Lucas Amorim) e 2020.2/2021.1 (Prof. Bruno Pimentel)
fontes_catalogo: ufal-cc-discreta-prova-lucas-2017,ufal-cc-discreta-provas-bruno
autoria: Profs. Lucas Amorim e Bruno Pimentel (IC-UFAL), enunciados parafraseados; resolução da equipe TutorON com auxílio de IA
licenca: Não declarada (provas do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia os enunciados e traz resolução própria; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Resolução da equipe TutorON, não é gabarito do professor. Status da resolução: validada.

**Por extensão** (prova de 2017, universo $U=\{0,1,\dots,10\}$, $A=\{1,2,3,4,5\}$, $B=\{0,3,6,7\}$): $A\cap B=\{3\}$; $A\cup B=\{0,\dots,7\}$; $A-B=\{1,2,4,5\}$; $B^c=\{1,2,4,5,8,9,10\}$; $B^c-A=\{8,9,10\}$.

Cuidados com a notação de compreensão:
- $\{2x \mid x\in\mathbb{Z},\ 6<x<12\}$: os elementos são os **dobros**, $\{14,16,18,20,22\}$, não os valores de x nem números decimais;
- $\{x^2 \mid x\in\mathbb{Z},\ -10<x<10\}=\{0,1,4,9,\dots,81\}$: quadrados repetidos contam uma vez;
- $\{x\in\mathbb{Z}\mid x^2<10\}=\{-3,\dots,3\}$: não esqueça os negativos;
- $\{x-y\mid x,y \text{ ímpares},\ 0<x<y<10\}=\{-8,-6,-4,-2\}$.

**Venn:** a região "em pelo menos dois dos três conjuntos" é $(A\cap B)\cup(B\cap C)\cup(A\cap C)$, e não $A\cap B\cap C$ (essa é só o miolo).

**Leis da álgebra dos conjuntos** (provas de 2020.2 e 2021.1). Escreva uma lei por passo:
- $(A\cap B)\cup(A\cap B^c)=A\cap(B\cup B^c)=A\cap U=A$ (distributiva, complemento, identidade);
- $[(A\cap B)\cup(A\cap B^c)]\cap(A^c\cup B)=A\cap(A^c\cup B)=(A\cap A^c)\cup(A\cap B)=A\cap B$;
- $(A\cup B)\cup(A\cap B)=A\cup B$ (absorção, pois $A\cap B\subseteq A\cup B$);
- $(A\cap B)\cup(A-B)=A$, usando $A-B=A\cap B^c$ e o primeiro item.

Na dúvida, teste com conjuntos pequenos antes de provar; mas o teste não substitui a prova pelas leis.

**Verificação:** as igualdades foram conferidas por força bruta em todos os pares de subconjuntos de um universo de 4 elementos, e os conjuntos por extensão foram gerados em Python.
