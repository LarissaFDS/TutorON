# Curadoria — Computação Gráfica

Situação: **MVP** desde 23/11/2026, por decisão da equipe para a parte 3 da fila de Ciência da Computação.
Revisão humana e do professor pendentes em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `21. COMP381 - Computação Gráfica`). As aulas são
do Prof. Marcelo Costa Oliveira (IC-UFAL), com datas de 2009 a 2017. Os exercícios e as provas cobrem
2014, a prova bimestral I.2 e 2021.2.

A pasta tem:
- 15 aulas: introdução, dispositivos, rasterização, aliasing, transformações 2D e 3D, cores, observação
  de cenas 3D, recorte, modelagem, iluminação, iluminação global e textura;
- 5 exercícios com respostas de alunos;
- a AB1 de 2021.2, reescrita de memória por um aluno, e a prova bimestral I.2 com resoluções de alunos;
- a AB2 e a reavaliação de 2021.2;
- um resumo de questões de 2014 enviado por e-mail por um aluno;
- uma lista de questões de AB2 respondidas por alunos;
- fotos de provas de 2013;
- a apostila de CG do ICMC-USP (Traina e Oliveira, 2006);
- um guia de OpenGL escrito por uma aluna da UFAL;
- um artigo de seminário (UFBA).

**Ementa não conferida.** A ementa oficial de COMP381 não foi encontrada no PPC disponível e não foi
inventada. Os tópicos saíram das aulas e das provas.

## O que entrou
13 blocos (`materiais/g01`–`g13`), todos na busca, em três assuntos:
- fundamentos e rasterização: frame buffer e LUT, Bresenham, aliasing;
- transformações, projeção e recorte: 2D e 3D, projeções, Cohen-Sutherland, Sutherland-Hodgman;
- modelagem, iluminação e textura: cores, modelagem (quadtree e octree), iluminação local, sombreamento,
  iluminação global e textura.

As contas e algoritmos são refeitos com NumPy e Python em `tests_acervo/test_disciplina_cg.py`.

**Correções:**
- `g01` (corrigida): o exercício de fundamentos dava a área em m², mas a unidade certa é mm²; algumas
  divisões da normalização estavam invertidas, embora os resultados estivessem certos.
- `g06` (corrigida): uma resolução de aluno calculava $y = 30$ na interseção; o certo é $C = (15, 20)$.
- `g07`: segue a correção do monitor sobre a lista circular de arestas.

**Pendentes do professor:**
- `g10`: a questão do POSCOMP 2011 tem uma afirmação imprecisa (diz "proporcional ao ângulo" em vez de
  "ao cosseno").
- `g11`: a alternativa IV da questão de sombreamento depende da leitura. Os gabaritos oficiais não
  foram conferidos.

## O que ficou de fora
- **Livros:** Azevedo e Conci, Hearn e Baker, OpenGL SuperBible e o livro de ambientes 3-D não foram
  entregues nem versionados; são só referência.
- **Fotos de provas, respostas de alunos, resumo por e-mail e lista respondida:** contêm nomes e e-mail.
  Só os enunciados foram parafraseados; nenhum nome entrou no acervo.
- **Apostila do ICMC-USP e guia de OpenGL:** a licença não está declarada; usados só como evidência de
  tópicos, não versionados.
- **Artigo do seminário** (calibração de câmera, UFBA): é um tema de seminário, não da ementa; não usado.
- **Aula "Observação de Cenas 3D"** (arquivo com nome trocado de "Especificação do Programa - Teste de
  Software"): usada só nas projeções.

## Fronteiras
Geometria Analítica (`ga`) cobre vetores e matrizes como álgebra; Sinais e Sistemas (`sinais`) cobre a
teoria da amostragem; Inteligência Artificial (`ia`) foi testada como vizinha da mesma fila. O isolamento
é testado nos dois sentidos.

## Pendências
- Revisão humana dos 13 blocos e revisão do professor.
- Ementa de COMP381.
- Gabaritos oficiais das questões de ENADE e POSCOMP.
- Rasterização de círculos e de polígonos (preenchimento por varredura), pipeline do OpenGL e curvas
  (Bézier, B-spline) aparecem nas aulas, mas não ganharam bloco nesta versão.
