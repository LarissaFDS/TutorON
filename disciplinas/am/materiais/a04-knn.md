---
id: am-k-nn-vizinhos-mais-proximos-distancia-euclidiana-escolha-de-k-normalizacao
titulo: Classificador k-NN (k vizinhos mais próximos): aprendizagem por analogia, distância euclidiana, escolha do k (ímpar), normalização dos atributos
assunto: am-02-classificacao
tipo: prova
questao: slides 04 e resumo da AB1
resolucao: sim
fonte: Provas de Aprendizagem de Máquina do Prof. Aydano Machado (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Aprendizagem de Máquina (COMP390); provas AB1 e AB2 (uma delas de 2021.1)
fontes_catalogo: ufal-aydano-provas-am, ufal-aydano-slides-am
autoria: Questões do Prof. Aydano Machado (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), slides 04 e resumo da AB1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**k-NN:** aprendizagem **por analogia** (preguiçosa): não constrói modelo; guarda os exemplos de treino como **pontos num espaço de $n$ dimensões**. Para classificar um novo ponto:
1. calcule a distância dele a todos os exemplos de treino;
2. pegue os **$k$ mais próximos**;
3. atribua a **classe majoritária** entre eles (ou uma votação ponderada pelo inverso da distância).

**Distância euclidiana** entre $x$ e $y$:
$$d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$$
Em palavras: a raiz da soma dos quadrados das diferenças atributo a atributo.

**Cuidados:**
- exige **atributos numéricos** (categóricos precisam ser codificados);
- atributos em escalas diferentes dominam a distância: **normalize** (ex.: min-max para $[0, 1]$, $x' = \frac{x - \min}{\max - \min}$);
- **escolha de $k$:** $k$ pequeno é sensível a ruído; $k$ grande borra as fronteiras. Com duas classes, use $k$ **ímpar** para evitar empate; escolha por validação cruzada;
- classificar é caro: compara com todos os exemplos.

Exemplo: treino A=(1, 1, classe +), B=(2, 2, +), C=(5, 5, −), D=(6, 5, −), E=(1, 2, +); ponto (2, 3). Distâncias: A 2,24; B 1; C 3,61; D 4,47; E 1,41. Com $k = 3$, os vizinhos são B, E e A, todos +: classe **+**.

**Verificação:** `test_knn_exemplo_e_escala` refaz as distâncias e a classe + à mão, confere com o `KNeighborsClassifier(n_neighbors=3)` do scikit-learn e mostra que um atributo de renda, em escala de milhares, muda os vizinhos se não for normalizado.
