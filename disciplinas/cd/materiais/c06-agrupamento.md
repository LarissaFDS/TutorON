---
id: cd-agrupamento-hierarquico-dendrograma-numero-de-grupos-cotovelo-silhueta
titulo: Análise de agrupamento: quando preferir agrupamento hierárquico (aplicação), como definir o número de grupos (dendrograma, cotovelo, silhueta)
assunto: cd-03-metodos
tipo: prova
questao: AB1 2020.1 Q6; REAV 1 Q4; REAV AB1 2020.2 Q4
resolucao: sim
fonte: Provas e listas de Ciência de Dados do Prof. Bruno Pimentel (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Ciência de Dados (COMP401); turmas 2020.1, 2020.2 e 2021.1
fontes_catalogo: ufal-pimentel-provas-cd
autoria: Questões do Prof. Bruno Pimentel (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB1 2020.1 Q6; REAV 1 Q4; REAV AB1 2020.2 Q4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Agrupamento hierárquico:** constrói uma **hierarquia de grupos**. O **aglomerativo** começa com cada objeto sozinho e, a cada passo, une os **dois grupos mais próximos** até sobrar um. A distância entre grupos é o **ligamento** (*linkage*): simples (mínima), completo (máxima), médio ou **Ward** (menor aumento da soma dos quadrados). O resultado é o **dendrograma**: uma árvore em que a altura de cada junção é a distância em que os grupos se uniram.

**Quando preferir o hierárquico:**
- quando o **número de grupos não é conhecido** antes;
- quando a **própria hierarquia interessa**: **taxonomia** de espécies ou **filogenia** a partir de sequências genéticas, **genes com perfis de expressão parecidos**, organização de documentos em temas e subtemas, segmentação de clientes em níveis;
- bases pequenas ou médias (o custo é pelo menos quadrático no número de objetos).

**Definir o número de grupos:**
- **dendrograma:** corte horizontal onde há o **maior salto** de altura entre junções consecutivas; o número de ramos cortados é o número de grupos;
- **método do cotovelo** (k-means): a soma dos quadrados dentro dos grupos cai com $k$; escolha o $k$ onde a queda deixa de ser grande;
- **silhueta:** para cada ponto, $s = \frac{b - a}{\max(a, b)}$, com $a$ a distância média ao próprio grupo e $b$ ao grupo vizinho mais próximo; escolha o $k$ com **maior silhueta média** (perto de 1 é bom);
- **conhecimento do domínio** (quantos segmentos a empresa consegue atender).

**Verificação:** `test_numero_de_grupos` gera 4 grupos com `make_blobs`, confere com SciPy que o maior salto do dendrograma de Ward indica 4 grupos e com scikit-learn que a silhueta média é máxima em $k = 4$.
