# Curadoria — Ciência de Dados

Situação: **em validação**. Revisão humana pendente em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `Ênfases/Sistemas Inteligentes/COMP401 -
Ciência de Dados`). O professor é o Prof. Bruno Pimentel (IC-UFAL).

**Ementa não conferida.** O Projeto Pedagógico de CC disponível (matriz 2011) não tem a disciplina
COMP401. A ementa não foi inventada: os tópicos vêm das provas e listas:
- fundamentos (Ciência de Dados, Estatística, Aprendizagem de Máquina, Mineração, Big Data);
- pré-processamento e avaliação de modelos;
- agrupamento, k-NN, Naive Bayes, árvores, Random Forest, regressão, SVM e redes neurais;
- séries temporais, meta-aprendizado e visualização de dados.

## O que entrou
14 blocos (`materiais/c01`–`c14`) com as questões das provas AB1, AB2, finais e reavaliações de
2020.1, 2020.2 e 2021.1 (as perguntas se repetem entre semestres) e das listas 1 e 2.
Enunciados parafraseados; resoluções da equipe TutorON, conferidas com NumPy, SciPy e scikit-learn,
com semente fixa, em `tests_acervo/test_disciplina_cd.py`.

- `c01` e `c02` têm verificação `parcial`: são conceituais.
- `c08` refaz à mão o exercício de Naive Bayes da Lista 2 (texto "what do you mean").
- `c12` cita a série de medicamentos da Lista 2 sem os dados: o arquivo do professor não está na
  pasta, e o bloco pede para conferir com os dados.
- `c14` usa as contagens de pedidos recebidos e processados da Lista 2.

## O que não entrou
- PDFs das provas e listas: sem licença declarada. As provas de 2021.1 trazem nome e matrícula
  de um aluno; nada disso foi copiado.
- Listas de 2021.1 que estão só em imagem.
- O projeto da disciplina (dados do Poder Executivo Federal): é atividade avaliativa, e o tutor só
  guia com perguntas.
- Livro *Storytelling with Data* (Knaflic): protegido, só referência para as seis etapas.

## Decisões pendentes
- Sem ligação em `disciplinas/cursos.json`. É optativa de ênfase, fora da matriz do arquivo.
- Ementa oficial da COMP401 a conferir com a coordenação.
