---
id: ga-forcas-combinacao-linear
titulo: Forças: manter as direções de F₁ e F₂ e escolher escalares para que a resultante seja F₃ (combinação linear de vetores no plano)
assunto: ga-01-vetores-operacoes
tipo: prova
questao: 2
semestre: nao_informado
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Prova sem cabeçalho (foto), Q2
fontes_catalogo: ufal-ga-provas-sem-cabecalho
autoria: Enunciado: autoria não identificada (foto de prova sem cabeçalho), parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questão de prova (enunciado parafraseado). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

Em um ponto atuam $F_1 = (-3,-4)$, $F_2 = (-1, 2)$ e $F_3 = (2, 1)$. Mantendo as direções de $F_1$ e $F_2$, como modificá-las para que a resultante delas seja $F_3$?

Ideia: "manter a direção" é multiplicar por um escalar, que pode ser negativo (inverte o sentido). Procuramos a e b com $aF_1 + bF_2 = F_3$, um sistema linear nas componentes:
- x: $-3a - b = 2$;
- y: $-4a + 2b = 1$.
Da primeira, $b = -2 - 3a$; na segunda, $-4a - 4 - 6a = 1$, logo $a = -\tfrac12$ e $b = -\tfrac12$.

Leitura: as duas forças passam a ter metade do módulo e sentido oposto: $-\tfrac12 F_1 = (\tfrac32, 2)$ e $-\tfrac12 F_2 = (\tfrac12, -1)$. A solução é única porque $F_1$ e $F_2$ não são paralelos: $\det\begin{pmatrix}-3 & -1\\ -4 & 2\end{pmatrix} = -10 \neq 0$.

**Verificação:** $(\tfrac32 + \tfrac12,\ 2 - 1) = (2, 1) = F_3$.
