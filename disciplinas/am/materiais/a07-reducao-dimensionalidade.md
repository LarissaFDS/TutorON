---
id: am-reducao-de-dimensionalidade-selecao-de-atributos-pca-maldicao-da-dimensionalidade
titulo: Por que existe a necessidade de redução de dimensionalidade e como tratar: seleção de atributos (filtro, seleção para frente, eliminação para trás) e extração (PCA)
assunto: am-01-fundamentos-e-kdd
tipo: prova
questao: AB1 Q4
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
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), AB1 Q4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Por que reduzir:**
- **maldição da dimensionalidade:** com muitos atributos, os dados ficam **esparsos** e as distâncias perdem significado (todos os pontos parecem igualmente distantes), o que prejudica k-NN e agrupamento;
- **mais atributos irrelevantes ou redundantes** aumentam o risco de **overfitting** e de correlações espúrias;
- **custo** de treino, memória e coleta;
- modelos com menos atributos são mais **interpretáveis**.
(Dizer só "há atributos que não serão usados" é incompleto: falta o porquê.)

**Como tratar:**
1. **Conhecimento do domínio:** remover o que não tem relação com o problema (o telefone do paciente não ajuda no diagnóstico) e identificadores.
2. **Seleção de atributos** (mantém atributos originais):
   - **filtro:** ranquear por uma medida independente do modelo (correlação com a classe, ganho de informação, qui-quadrado) e remover atributos muito correlacionados entre si;
   - **wrapper:** **seleção para frente** (começa vazio e adiciona o atributo que mais melhora a validação cruzada) ou **eliminação para trás** (começa com todos e remove o que menos faz falta);
   - **embutida:** o próprio modelo seleciona (árvores, regularização L1).
3. **Extração de atributos** (cria novos): **PCA**, que projeta os dados nas direções de **maior variância** (componentes principais, ortogonais), mantendo, por exemplo, 95% da variância com bem menos dimensões.

Cuidado: escolha os atributos **dentro** da validação cruzada, senão o teste "vê" os dados e a estimativa fica otimista.

**Verificação:** `test_reducao_de_dimensionalidade` acrescenta 50 atributos de ruído à base Iris e mostra com scikit-learn que o k-NN piora; a seleção pela informação mútua recupera os atributos originais, e o PCA da base Iris guarda mais de 95% da variância com 2 componentes.
