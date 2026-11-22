---
id: am-qual-algoritmo-de-agrupamento-para-cada-base-formas-ruido
titulo: Que algoritmo de agrupamento usar para cada base da figura (grupos globulares, formas alongadas não convexas, grupos com muito ruído) e por quê
assunto: am-03-agrupamento-e-associacao
tipo: prova
questao: AB2 Q2 (figura com três bases)
resolucao: sim
fonte: Provas de Aprendizagem de Máquina do Prof. Aydano Machado (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Aprendizagem de Máquina (COMP390); provas AB1 e AB2 (uma delas de 2021.1)
fontes_catalogo: ufal-aydano-provas-am
autoria: Questões do Prof. Aydano Machado (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), AB2 Q2 (figura com três bases) (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Figura descrita em texto: **base 1** tem um grupo grande e redondo e três grupos pequenos e compactos; **base 2** tem grupos em forma de **curvas e espirais** entrelaçadas; **base 3** tem grupos de formas variadas (um redondo, um alongado e irregular) cercados por **pontos de ruído** espalhados.

**Base 1: k-means** (ou k-medoids). Grupos **convexos** e bem separados, aproximadamente circulares: a atribuição ao centroide mais próximo separa bem, e o $k = 4$ é visível. Atenção: o k-means tende a gerar grupos de tamanhos parecidos e pode "roubar" pontos do grupo grande para os pequenos; se isso acontecer, o DBSCAN também serve.

**Base 2: DBSCAN.** Grupos **não convexos**: dois pontos do mesmo grupo podem estar mais longe entre si que de pontos de outro grupo. Os métodos por centroide cortam as curvas ao meio; o DBSCAN segue as regiões **densas** conectadas, qualquer que seja a forma.

**Base 3: DBSCAN.** Há **ruído** e formas **irregulares**: o DBSCAN marca os pontos esparsos como ruído e não os força a entrar em grupos. O k-medoids (resposta comum na turma) é **mais robusto** a outliers que o k-means, mas ainda **atribui todo ponto de ruído a algum grupo** e não acompanha o grupo alongado. A justificativa é o que a questão avalia: k-medoids é aceitável se o argumento for a robustez a ruído, mas o DBSCAN atende melhor às duas dificuldades.

Regra prática: formas convexas e $k$ conhecido, k-means; outliers moderados, k-medoids; forma arbitrária ou ruído, DBSCAN (ajuste $\varepsilon$ pelo gráfico das distâncias ao k-ésimo vizinho).

**Verificação:** `test_escolha_por_forma_da_base` gera com scikit-learn bases parecidas (`make_blobs`, `make_moons` e luas com ruído uniforme) e mede o índice de Rand ajustado: k-means vence nas bolhas, DBSCAN vence nas luas e na base com ruído, e marca o ruído como -1.
