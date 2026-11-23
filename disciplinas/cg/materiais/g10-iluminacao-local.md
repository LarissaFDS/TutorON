---
id: cg-iluminacao-local-luz-ambiente-reflexao-difusa-lambert-especular-phong-fontes-de-luz-atenuacao
titulo: Iluminação local: fontes de luz (pontual, direcional, de área, spot) e atenuação; luz ambiente, reflexão difusa (lei de Lambert) e especular (modelo de Phong com expoente de brilho); POSCOMP 2011
assunto: cg-03-modelagem-iluminacao-e-textura
tipo: prova
questao: aula de Iluminação, AB2 de 2021.2 (questões 4 e 5), AB2 de 2014.1 e reavaliação da AB2 de 2021.2 (POSCOMP 2011)
resolucao: sim
fonte: Exercícios e provas de Computação Gráfica do Prof. Marcelo Costa Oliveira (IC-UFAL)
curso: Ciência da Computação (UFAL), COMP381 Computação Gráfica; aulas de 2012 a 2017 e provas de 2014 e 2021.2 (Prof. Marcelo Costa Oliveira)
fontes_catalogo: ufal-marcelo-aulas-cg,ufal-cg-provas-exercicios
autoria: Questões do Prof. Marcelo Costa Oliveira (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Computação Gráfica (IC-UFAL), aula de Iluminação, AB2 de 2021.2 (questões 4 e 5), AB2 de 2014.1 e reavaliação da AB2 de 2021.2 (POSCOMP 2011) (parafraseado). Status da resolução: pendente do professor. A resolução é da equipe TutorON e não é gabarito do professor.

**Fontes de luz:**
- **pontual:** posição $(x,y,z)$, raios divergentes; local, com atenuação $f(d) = \dfrac{1}{a_0 + a_1 d + a_2 d^2}$;
- **no infinito (direcional):** raios paralelos, intensidade constante;
- **spot (cone):** ilumina só o que está dentro de um cone em torno da direção;
- **de área:** superfície emissora, como uma luminária.

**Modelo local (Phong):**
$$I = k_a I_a + f(d)\,I_l\left[k_d\,(\vec N \cdot \vec L) + k_s\,(\vec R \cdot \vec V)^n\right]$$
- **ambiente** $k_a I_a$: aproxima as múltiplas reflexões da cena; igual em todo ponto;
- **difusa (Lambert):** proporcional ao **cosseno** do ângulo entre a normal $\vec N$ e a direção da luz $\vec L$; igual em todas as direções, **não depende do observador**; dá aparência fosca;
- **especular:** proporcional a $\cos^n$ do ângulo entre a reflexão ideal $\vec R$ e o observador $\vec V$; **depende da posição do observador**; $n$ grande dá brilho pequeno e metálico.

**AB2 de 2021.2, questão 4:** "mesma intensidade em todas as direções": D; "depende da posição do observador": E; "depende do ângulo entre observação e reflexão": E; "efeito mais opaco ou metálico": E (controlado pelo expoente $n$ e por $k_s$).

**POSCOMP 2011:** I é falsa (a difusa não depende do observador); IV é verdadeira; II é verdadeira na forma do modelo de Phong (cosseno do ângulo, elevado a $n$); III fala em "proporcional ao ângulo", e Lambert diz **cosseno** do ângulo. A resposta depende de aceitar essa imprecisão em III: confira o gabarito oficial antes de usar.

**Verificação:** `test_phong` calcula as três parcelas para vetores dados e confere que a difusa não muda com o observador e que a especular cai com o expoente.
