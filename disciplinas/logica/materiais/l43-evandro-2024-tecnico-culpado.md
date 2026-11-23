---
id: logica-evandro-2024-tecnico-culpado
titulo: Argumento do técnico culpado (time, campeonato, torcedores): consequência lógica por modus tollens e modus ponens
assunto: logica-03-consequencia-equivalencia
tipo: prova
resolucao: sim
fonte: Lista 1 e prova 1 de Lógica Aplicada à Computação, Prof. Evandro Costa, 2024.1 (Engenharia de Computação, UFAL); enunciado parafraseado
curso: Engenharia de Computação (UFAL), turma do Prof. Evandro Costa, ECOM007, 2024.1
semestre: 2024.1
fontes_catalogo: ufal-evandro-2024-lista-prova
autoria: Prof. Evandro Costa (IC-UFAL); enunciado parafraseado pela equipe TutorON com auxílio de IA, sem nada das respostas do aluno
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio; as fotos e imagens originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questão de lista e de prova (paráfrase do enunciado) com resolução. Prova é atividade avaliativa: o tutor guia, não entrega. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

Enunciado (paráfrase): mostre que "o técnico é o culpado" é consequência lógica das premissas: (1) se o time joga bem, ganha o campeonato; (2) se o time não joga bem, o técnico é culpado; (3) se o time ganha o campeonato, os torcedores ficam contentes; (4) os torcedores não estão contentes.

Simbolização: $J$ = joga bem, $G$ = ganha o campeonato, $T$ = o técnico é culpado, $C$ = torcedores contentes. Premissas $J\to G$, $\neg J\to T$, $G\to C$, $\neg C$; conclusão $T$.

Caminho por regras de inferência:
1. De $G\to C$ e $\neg C$, por **modus tollens**: $\neg G$.
2. De $J\to G$ e $\neg G$, por modus tollens: $\neg J$.
3. De $\neg J\to T$ e $\neg J$, por **modus ponens**: $T$.

Caminho pela definição de consequência: procure na tabela-verdade (16 linhas) uma linha com as quatro premissas verdadeiras e $T$ falso. Não existe: com $C$ falso, $G$ tem de ser falso, então $J$ é falso, então $T$ é verdadeiro. Logo $\{J\to G,\neg J\to T,G\to C,\neg C\}\models T$.

Erro comum: montar a tabela e olhar só as linhas em que a conclusão é verdadeira. O que importa são as linhas em que **todas as premissas** são verdadeiras: a conclusão tem de ser verdadeira em todas elas.

**Verificação:** a consequência foi conferida por tabela-verdade completa em Python (nenhum contramodelo).
