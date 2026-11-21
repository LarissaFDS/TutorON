---
id: ga-quadricas-identificar
titulo: Quádricas: superfície cujos traços nos planos x = 0 e y = 0 são elipses dadas (elipsoide), identificar y² − x² + z − 2y − 1 = 0 (paraboloide hiperbólico, sela) e mostrar que 3x² + 2y² + 4z² − 2xy − 2yz + 2xz = 0 é um ponto
assunto: ga-12-quadricas-superficies
tipo: prova
questao: 1a; 3b, 4
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Reavaliação AB2 (24.05.2017), Q1a; 4ª Avaliação (12.05.2017), Q3b e Q4
fontes_catalogo: ufal-ga-provas-2017
autoria: Enunciado: Instituto de Matemática da UFAL (professor não impresso na prova), parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

Identifique uma quádrica pelos **traços**: as curvas que ela forma com planos paralelos aos planos coordenados.

**Traços $\tfrac{y^2}{16} + \tfrac{z^2}{9} = 1$ em x = 0 e $\tfrac{x^2}{4} + \tfrac{z^2}{9} = 1$ em y = 0.** O elipsoide $\dfrac{x^2}{4} + \dfrac{y^2}{16} + \dfrac{z^2}{9} = 1$ serve: com x = 0 e com y = 0 ele dá as duas elipses. Semieixos 2, 4 e 3; em z = 0, o traço é $\tfrac{x^2}{4} + \tfrac{y^2}{16} = 1$.

**$y^2 - x^2 + z - 2y - 1 = 0$.** Completando o quadrado: $z = 2 + x^2 - (y - 1)^2$. É um **paraboloide hiperbólico** (sela) com ponto de sela (0, 1, 2). Traços: em y = 1, a parábola $z = 2 + x^2$, para cima; em x = 0, $z = 2 - (y-1)^2$, para baixo; em z = 2, as retas $x = \pm(y - 1)$.

**$3x^2 + 2y^2 + 4z^2 - 2xy - 2yz + 2xz = 0$ é um ponto.** Escreva como soma de quadrados: $(x - y)^2 + (y - z)^2 + (x + z)^2 + x^2 + 2z^2$. A soma só é zero se todos os termos forem zero: $x = 0$, $z = 0$ e então $y = 0$. A única solução é (0, 0, 0). Com matrizes: a forma tem matriz $\begin{pmatrix}3 & -1 & 1\\ -1 & 2 & -1\\ 1 & -1 & 4\end{pmatrix}$, de menores principais 3, 5 e 17, positivos: definida positiva.

**Verificação:** expandir a soma de quadrados reproduz o polinômio ($x^2$: 3; $y^2$: 2; $z^2$: 4; xy: −2; yz: −2; xz: 2); o ponto (1, 1, 3) está na sela ($1 - 1 + 3 - 2 - 1 = 0$) e satisfaz $z = 2 + 1 - 0$.
