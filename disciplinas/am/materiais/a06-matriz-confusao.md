---
id: am-matriz-de-confusao-acuracia-precisao-cobertura-recall-f1
titulo: Matriz de confusão e métricas: acurácia, taxa de erro, precisão, cobertura (recall, sensibilidade), especificidade e F1; quando preferir cada uma (diagnóstico médico, bolsa de valores)
assunto: am-02-classificacao
tipo: prova
questao: slides 05 e resumo da AB1 (exercício diabetes × normal)
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
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), slides 05 e resumo da AB1 (exercício diabetes × normal) (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Matriz de confusão:** tabela de **classe real × classe prevista**. Para duas classes, com "positivo" a classe de interesse: VP (positivo previsto positivo), FN (positivo previsto negativo), FP (negativo previsto positivo), VN.

**Métricas:**
- **acurácia** $= \frac{VP + VN}{\text{total}}$; taxa de erro $= 1 -$ acurácia;
- **precisão** $= \frac{VP}{VP + FP}$: dos que o modelo disse positivos, quantos são;
- **cobertura** (*recall*, sensibilidade) $= \frac{VP}{VP + FN}$: dos positivos reais, quantos o modelo achou;
- **especificidade** $= \frac{VN}{VN + FP}$;
- **F1** $= \frac{2 \cdot \text{precisão} \cdot \text{cobertura}}{\text{precisão} + \text{cobertura}}$ (média harmônica).

**Exercício dos slides** (linhas = classe real, colunas = prevista; positivo = diabetes):

| real \ prevista | diabetes | normal |
|---|---|---|
| diabetes | 40 | 20 |
| normal | 10 | 30 |

Acurácia $= 70/100 = 0{,}70$. Precisão $= 40/50 = 0{,}80$. Cobertura $= 40/60 \approx 0{,}667$. Especificidade $= 30/40 = 0{,}75$. F1 $\approx 0{,}727$. Se a orientação da tabela for a outra (colunas = real), precisão e cobertura trocam de lugar: confira sempre o rótulo dos eixos.

**Qual métrica:** acurácia engana com **classes desbalanceadas** (99% normais: dizer sempre "normal" dá 99%). **Diagnóstico médico:** priorize a **cobertura** (um doente não detectado é pior que um alarme falso). **Apostas e bolsa:** priorize a **precisão** (cada "compre" errado custa dinheiro).

**Verificação:** `test_matriz_de_confusao` monta os 100 rótulos do exercício, confere a matriz com `confusion_matrix` e as métricas com `accuracy_score`, `precision_score`, `recall_score` e `f1_score` do scikit-learn.
