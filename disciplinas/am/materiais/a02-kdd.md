---
id: am-kdd-descoberta-de-conhecimento-etapas-mineracao-de-dados
titulo: Como se dá o processo de descoberta de conhecimento em banco de dados (KDD): seleção, pré-processamento, transformação, mineração, interpretação e avaliação; dados, informação e conhecimento
assunto: am-01-fundamentos-e-kdd
tipo: prova
questao: AB1 Q2
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
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), AB1 Q2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**KDD (Knowledge Discovery in Databases):** processo de achar conhecimento **novo, válido, útil e compreensível** em grandes bases. A **mineração de dados** (*data mining*) é a **etapa principal** do KDD, não o processo todo.

**Dados, informação e conhecimento** (exemplo dos slides): dado é o registro `37,8`; informação é o dado com contexto, `37,8 °C de temperatura axilar`; conhecimento é o que permite decidir, "se a temperatura passa de 37,8 °C, há febre".

**Etapas:**
1. **Seleção:** escolher a base e os atributos e registros relevantes para o objetivo.
2. **Pré-processamento (limpeza):** remover duplicatas e erros, tratar **valores faltantes** (remover ou imputar por média, mediana ou moda), tratar ruído e outliers.
3. **Transformação:** mudar a representação: **normalizar** escalas (metros e quilômetros), discretizar, criar ou reduzir atributos.
4. **Mineração:** aplicar o algoritmo: classificação (árvore, k-NN, Bayes), agrupamento (k-means), regras de associação (Apriori).
5. **Interpretação e avaliação:** medir com métricas (acurácia, precisão, cobertura), visualizar e validar com o especialista; se não serve, voltar a etapas anteriores. O processo é **iterativo**.

**Mineração preditiva** (modelos que preveem um atributo; aprendizagem supervisionada) × **descritiva** (modelos que descrevem padrões; não supervisionada).

A resposta que só citava seleção, pré-processamento e transformação estava **incompleta**: faltavam a mineração e a avaliação.

**Verificação:** `test_kdd_preprocessamento_muda_o_resultado` mostra com scikit-learn que, numa base com atributos em escalas muito diferentes, o k-NN acerta bem mais depois da normalização (etapa de transformação), e que a imputação pela média preenche todos os faltantes.
