# Curadoria — Aprendizagem de Máquina

Situação: **em validação**. Revisão humana pendente em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `Ênfases/Sistemas Inteligentes/COMP390 -
Aprendizagem de Máquina`). O professor é o Prof. Aydano Machado (IC-UFAL).

**Ementa não conferida.** O Projeto Pedagógico de CC disponível (matriz 2011) não tem a disciplina
COMP390. Lá só aparecem Inteligência Artificial 1 e 2 (CCOM033) e Tópicos em IA. A ementa não foi
inventada: os tópicos vêm das provas e dos slides:
- fundamentos e KDD;
- árvore de decisão;
- k-NN;
- avaliação de classificadores;
- agrupamento;
- regras de associação e medidas de interesse;
- aprendizagem por reforço.

Não há disciplina equivalente cadastrada para Engenharia de Computação.

## O que entrou
12 blocos (`materiais/a01`–`a12`):
- Questões das provas AB1 e AB2, em duas versões (uma de 2021.1, a outra sem data), com as mesmas
  perguntas:
  - definição e tipos;
  - KDD;
  - metodologia de avaliação;
  - redução de dimensionalidade;
  - k-means, k-medoids e DBSCAN;
  - escolha de algoritmo por base;
  - Apriori;
  - reforço e Q-learning.
- Exemplos numéricos dos slides, parafraseados:
  - matriz de confusão diabetes × normal;
  - lift das regras de compras.

Resoluções da equipe TutorON, conferidas com scikit-learn e semente fixa em
`tests_acervo/test_disciplina_am.py`.

- `a12` tem `status_resolucao: corrigida`. A atualização do Q-learning na resposta da turma omitia o
  desconto $\gamma$ e o máximo sobre as ações do próximo estado.
- `a09` diverge da resposta da turma na base 3. A turma escolheu k-medoids; o bloco defende DBSCAN e
  explica quando o k-medoids é aceitável.

## O que não entrou
- PDFs das provas. Têm respostas de alunos (sem nome) e não têm licença declarada.
- Slides do professor. Só entram como paráfrase de exemplos.
- Resumos de aluno. Só servem de evidência dos tópicos.
- Introdução e KDD dos slides 01 e 07c. A extração Partition e os slides de reforço são imagens e
  foram cobertos só pelos tópicos das provas.
- Classificador bayesiano e regressão. São citados nos resumos, mas não têm questão nem slide na
  pasta; ficaram sem bloco.

## Decisões pendentes
- Sem ligação em `disciplinas/cursos.json`. É optativa de ênfase, fora da matriz do arquivo.
- Ementa oficial da COMP390 a conferir com a coordenação.
