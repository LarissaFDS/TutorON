---
id: ga-retas-plano-distancia
titulo: Distância de ponto a reta no plano e entre retas paralelas, fórmula |Ax₀ + By₀ + C|/√(A² + B²), altura de triângulo relativa a um lado
assunto: ga-03-retas-no-plano
tipo: prova
questao: 4a; 4a; 2b
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | 1ª Avaliação (10.02.2017), Q4a; 1ª Avaliação (11.02.2017), Q4a; Reavaliação AB1 (24.05.2017), Q2b
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

**Distância de um ponto a uma reta no plano.** Para a reta $Ax + By + C = 0$ (vetor normal $\mathbf{n} = (A, B)$) e $P(x_0, y_0)$: $d = \dfrac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$. De onde vem: tome Q na reta; d é o módulo da projeção de $\overrightarrow{QP}$ sobre n, $|\overrightarrow{QP}\cdot\mathbf{n}|/\|\mathbf{n}\|$, e $\mathbf{n}\cdot Q = -C$. Na 1ª Avaliação (11/02), a reta $Ax = -By$ tem $C = 0$, e a fórmula vira $\dfrac{|Ax_0 + By_0|}{\sqrt{A^2+B^2}}$. Não esqueça de dividir pela norma de n.

**Distância entre x + 2y = 2 e x = 2t, y = 2 − t.** Diretor da segunda: $(2, -1)$; normal $(1, 2)$, a mesma da primeira: são paralelas. A segunda passa por (0, 2), então sua forma geral é $x + 2y = 4$. Distância: $\dfrac{|4 - 2|}{\sqrt5} = \dfrac{2}{\sqrt5}$.

**Altura do triângulo A(−2, −4), B(1, −2), C(2, 5) relativa a AB.** $\overrightarrow{AB} = (3, 2)$, $\overrightarrow{AC} = (4, 9)$. A altura é a distância de C à reta AB: $h = \dfrac{|3\cdot9 - 2\cdot4|}{\sqrt{13}} = \dfrac{19}{\sqrt{13}}$. Pela fórmula: reta AB com normal $(2, -3)$, $2x - 3y - 8 = 0$, e $|4 - 15 - 8|/\sqrt{13}$ dá o mesmo.

**Verificação:** 19/√13 ≈ 5,27; área $= \tfrac12\sqrt{13}\cdot\tfrac{19}{\sqrt{13}} = 9{,}5 = \tfrac12|3\cdot9 - 2\cdot4|$; o ponto (0, 1) da primeira reta está a $|0 + 2 - 4|/\sqrt5$ da segunda.
