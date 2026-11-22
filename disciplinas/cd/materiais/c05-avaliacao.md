---
id: cd-avaliacao-de-modelos-overfitting-leave-one-out-k-fold-f-measure-knn-iris
titulo: Importância de métodos de avaliação; como detectar overfitting; quando preferir leave-one-out a k-fold; script com k-NN na base Iris usando F-measure e k-fold
assunto: cd-02-preparacao-e-avaliacao
tipo: prova
questao: AB1 2020.1 Q5; Lista 1 Q8-Q10
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
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB1 2020.1 Q5; Lista 1 Q8-Q10 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Importância:** sem avaliação em dados não vistos, não se sabe se o modelo **generaliza**; também é como se comparam métodos e se escolhem parâmetros. Use métricas adequadas (acurácia, **F-measure**, AUC) e amostragem (k-fold, leave-one-out, bootstrap).

**Detectar overfitting:** desempenho **muito melhor no treino que na validação**; curva de validação que piora enquanto a de treino melhora com a complexidade (profundidade da árvore, $k$ pequeno no k-NN).

**Leave-one-out × k-fold:** LOO é preferível com **bases muito pequenas** (aproveita $n - 1$ exemplos no treino, estimativa quase sem viés) e quando treinar é barato. Com bases grandes, o custo ($n$ treinos) e a variância alta da estimativa favorecem k-fold com $k = 5$ ou 10.

**F-measure:** $F_1 = \frac{2PR}{P + R}$, média harmônica de precisão e cobertura; com mais de duas classes, use a **média macro** (média simples das $F_1$ por classe).

Script da Lista 1 Q10 (comparar valores de $k$):
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

x, y = load_iris(return_X_y=True)
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
for k in (1, 3, 5, 7, 15):
    f = cross_val_score(KNeighborsClassifier(n_neighbors=k), x, y,
                        cv=cv, scoring="f1_macro")
    print(k, round(f.mean(), 3), round(f.std(), 3))
```
Para dizer se a diferença entre dois $k$ é real, compare as médias **e** os desvios, ou aplique um teste pareado nas 10 dobras.

**Verificação:** `test_knn_iris_f_measure` roda o script: todos os $k$ ficam com F-macro acima de 0,9; e confere com LOO numa base de 30 exemplos que o número de treinos é 30.
