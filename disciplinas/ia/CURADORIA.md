# Curadoria — Inteligência Artificial

Situação: **MVP** desde 23/11/2026, por decisão da equipe para a parte 3 da fila de Ciência da Computação.
Revisão humana e do professor pendentes em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `20. COMP380 - Inteligência Artificial`),
listas de 2020.2 do Prof. Evandro de Barros Costa (IC-UFAL).

A pasta tem:
- duas aulas do Prof. Evandro Costa: Representação de Conhecimento e Raciocínio (2016) e Lógica
  Proposicional, consequência lógica (2013);
- um slide de regras de inferência;
- seis slides do Prof. Jacson R. C. Silva (UFES), usados na turma: introdução, agentes, representação de
  conhecimento, sistemas especialistas, métodos de busca e árvore de jogos;
- as listas 1 e 2 de 2020.2, em cópias respondidas por um aluno.

**Ementa não conferida.** A ementa oficial de COMP380 não foi encontrada no PPC disponível e não foi
inventada. Os tópicos saíram do material.

## O que entrou
14 blocos (`materiais/i01`–`i14`), todos na busca:
- fundamentos: IA e agentes;
- busca e jogos: busca cega, heurística e A*, satisfação de restrições (oito rainhas), minimax e alfa-beta;
- conhecimento e raciocínio: RCR, lógica proposicional e consequência lógica, regras de inferência,
  encadeamento para frente e para trás, sistemas especialistas;
- incerteza e aprendizado: árvore de decisão ID3 na base de risco de crédito, raciocínio baseado em casos,
  redes bayesianas e lógica fuzzy de Mamdani.

Toda conta e algoritmo foram conferidos em Python em `tests_acervo/test_disciplina_ia.py` (ordens de
busca, totais do aprofundamento iterativo, A* e gulosa, 92 soluções das oito rainhas, minimax e poda,
tabelas-verdade, encadeamentos, entropia e ganhos do ID3, enumeração bayesiana e centroide fuzzy).

## O que ficou de fora
- **Respostas do aluno nas listas:** as cópias têm nome e matrícula. Só os enunciados foram
  parafraseados; os programas e as saídas do Weka do aluno não foram usados como resolução. Os ganhos
  do ID3 foram recalculados pela equipe.
- **Russell e Norvig** (inglês, espanhol e capítulos soltos): livro protegido, não entregue nem
  versionado; só referência por capítulo.
- Os enunciados exatos da Lista 1 estão em imagens nas cópias; os blocos reconstroem a estrutura dos
  exercícios a partir das respostas, sem copiar o texto do aluno.
- Os exemplos de redes bayesianas e de fuzzy são da equipe (com números próprios), porque os do aluno
  dependem de telas das ferramentas Netica e Unfuzzy que não vieram em texto.

## Fronteiras
Aprendizagem de Máquina (`am`) cobre árvores de decisão, k-NN e avaliação em profundidade; Lógica para
Computação (`logica`) cobre tableaux, dedução natural e Prolog; Processamento de Linguagem Natural (`pln`)
e Computação Evolucionária (`compevol`) são disciplinas próprias. O isolamento é testado nos dois sentidos.

## Pendências
- Revisão humana dos 14 blocos e revisão do professor.
- Ementa de COMP380.
- Planejamento, aprendizado por reforço e redes neurais não têm material da turma nesta pasta.
