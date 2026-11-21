---
id: ga-retas-plano-parametricas
titulo: Equações paramétricas de retas no plano: paralela e perpendicular a uma reta dada por um ponto, reta com vetor diretor 2u − v, equação cartesiana (geral) da perpendicular
assunto: ga-03-retas-no-plano
tipo: prova
questao: vários
semestre: 2016.2 e 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Prova sem cabeçalho (foto), Q3; 1ª Avaliação (11.02.2017), Q3; 1ª Avaliação (10.02.2017), Q3a; Final (14.11.2016), Q1; Reavaliação 1 (03.11.2016), Q2
fontes_catalogo: ufal-ga-provas-sem-cabecalho,ufal-ga-provas-2017,ufal-ga-provas-2016
autoria: Enunciados: provas de Geometria Analítica do Instituto de Matemática da UFAL (ver fontes_catalogo), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

Formas da reta no plano: **paramétrica** $(x, y) = P_0 + t\,\mathbf{d}$ (ponto e vetor diretor d); **geral** $ax + by + c = 0$, com vetor normal $\mathbf{n} = (a, b)$. Se $\mathbf{d} = (d_1, d_2)$, um normal é $(d_2, -d_1)$.

**P(−1, 2) e r: y = 2x + 1.** Diretor de r: $\mathbf{d} = (1, 2)$; normal $(2, -1)$.
- Paralela: $x = -1 + t$, $y = 2 + 2t$.
- Perpendicular (diretor = normal de r): $x = -1 + 2t$, $y = 2 - t$.

**P(−2, 3) e r: 2x − y = 1.** Normal $(2,-1)$, diretor $(1, 2)$. Paralela: $x = -2 + t$, $y = 3 + 2t$; perpendicular: $x = -2 + 2t$, $y = 3 - t$.

**Reta por A(2, −1) paralela a 2u − v**, u = (1, 2), v = (1, 1): diretor $(1, 3)$; $x = 2 + t$, $y = -1 + 3t$.

**Final 2016, Q1.** r: $x = 1 - 2t$, $y = -2 + 2t$, diretor $(-2, 2)$. A perpendicular s por (−2, 2) tem normal $(-2, 2)$, ou $(1, -1)$: forma geral $x - y + 4 = 0$. Paralela a s por (3, 5): diretor $(1, 1)$, $x = 3 + t$, $y = 5 + t$. (Na Reavaliação 1, r tem $x = 1 - t$: s fica $x - 2y + 6 = 0$ e a paralela $x = 3 + 2t$, $y = 5 + t$.)

**Verificação:** cada ponto dado satisfaz sua reta em t = 0 (ex.: −2 − 2 + 4 = 0); diretores perpendiculares têm produto escalar nulo: (1, 2)·(2, −1) = 0 e (−2, 2)·(1, 1) = 0.
