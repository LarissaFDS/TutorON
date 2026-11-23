---
id: am-metodologia-avaliar-classificadores-holdout-validacao-cruzada-k-fold-estratificada
titulo: Que metodologia usar para construir e avaliar classificadores: holdout, random subsampling, validação cruzada k-fold, estratificada e leave-one-out; overfitting
assunto: am-02-classificacao
tipo: prova
questao: AB1 Q3
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
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), AB1 Q3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Princípio:** avaliar em dados **que não foram usados no treino**; acertar no treino pode ser só **memorização** (*overfitting*). Antes, defina a **métrica** pelo problema (ver o bloco de matriz de confusão).

**Técnicas de divisão:**
- **Holdout:** divisão aleatória em treino (2/3) e teste (1/3). Simples, mas o resultado depende da sorte da divisão.
- **Random subsampling:** repete o holdout $k$ vezes; a acurácia é a **média** das $k$ execuções.
- **Validação cruzada k-fold:** divide a base em $k$ partes de tamanho parecido; executa $k$ vezes, cada vez com **1 parte de teste e $k-1$ de treino**; **toda parte é testada uma vez**; o resultado é a média (com desvio padrão). Usual: $k = 10$.
- **Estratificada:** cada parte mantém a **proporção de classes** da base original (essencial com classes desbalanceadas).
- **Leave-one-out:** k-fold com $k$ igual ao número de exemplos; bom para **bases pequenas**, caro para grandes.

**Metodologia completa (resposta esperada):**
1. pré-processar e separar, se possível, um **conjunto de teste final** que não é tocado até o fim;
2. comparar algoritmos e ajustar parâmetros (ex.: o $k$ do k-NN, a profundidade da árvore) com **k-fold estratificado** no restante;
3. escolher pela métrica certa (acurácia, precisão ou cobertura) e comparar médias **e** desvios;
4. medir uma vez no teste final; treinar o modelo escolhido com **toda a base** antes de entregar.
Base pequena: k-fold ou leave-one-out; base enorme: holdout já é estável e mais barato.

**Verificação:** `test_kfold_estratificado` confere com o scikit-learn que o `StratifiedKFold(5)` testa cada exemplo exatamente uma vez e mantém a proporção de classes em cada parte, e que uma árvore sem limite acerta 100% no treino mas menos na validação cruzada (overfitting).
