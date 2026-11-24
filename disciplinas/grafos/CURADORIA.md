# Curadoria: Teoria dos Grafos (Ciência da Computação)

Disciplina nova, criada em 22/11/2026 a partir da pasta da turma de Ciência da Computação (fila CC, parte 2).
Situação: **em validação**. Revisão humana e do professor: pendentes em todos os blocos.

## Ementa (PPC de CC, matriz 2011, CCOM030, 30 h) e cobertura

| Tópico da ementa | Assunto | Blocos |
|---|---|---|
| Introdução; grafos orientados, não orientados e bipartidos; subgrafos | `grafos-01-conceitos` | g01, g02 |
| Árvores e árvores geradoras; conectividade | `grafos-02-arvores-conectividade` | g03, g04, g14 |
| Percursos; caminhos; eulerianos e hamiltonianos | `grafos-03-percursos-caminhos` | g05, g06 |
| Casamentos; cliques; estabilidade | `grafos-04-emparelhamento-estabilidade` | g07, g08 |
| Número cromático | `grafos-05-coloracao` | g09, g10 |
| Grafos planares | `grafos-06-planaridade` | g11 |
| Grafos sem circuitos; redes e fluxos | `grafos-07-digrafos-fluxos` | g12, g13 |
| Hipergrafos e matróides | — | **sem material da turma; sem bloco** |

## Material usado e excluído
- **Usado (paráfrase, PDF não versionado):** lista 2020.1 do Prof. Rian Gabriel Pinheiro (40 questões); 2ª avaliação de 2016.2 do Prof. Leonardo Viana (questões 2, 3, 4 e 5); tópicos dos slides da Profa. Patrícia Machado (UFCG, 2012).
- **Só referência:** lista 2020.2; 1ª avaliação de 2018.1; exercícios do Prof. Feofiloff (IME-USP, licença não conferida); cadernos do POSCOMP 2002–2013 (conferir cada questão contra o gabarito oficial fica para depois).
- **Fora do acervo (dados pessoais):** listas resolvidas por alunos, com nomes e matrículas, e uma resolução de 2011 com nome e e-mail de aluno. Nada foi copiado; só serviram para apontar erros comuns.
- **Livros protegidos:** Bondy e Murty, Goldbarg, Szwarcfiter e Boaventura Netto: só citação.

### Complemento do 4º período de Engenharia de Computação (ECOM033)
- **Usado (paráfrase, arquivos não versionados):** Prática 1 de caminho mínimo (`ufal-ecom033-pratica1-caminho-minimo`), com os três cenários e seus arquivos de entrada: `grafos-pratica1-estacao-central-floyd` (Floyd-Warshall, estação central 9 com soma 219), `grafos-pratica1-bellman-ford-regeneracao` (pesos negativos, 0 → 3 → 5 → 6 com custo 8) e `grafos-pratica1-robo-grid-dijkstra` (grid 10 × 15, custo 26). Os dados de entrada ficam no teste, para recalcular os números.
- **Só evidência:** os slides ECOM033 (introdução, representação, árvores, coloração) tratam de assuntos que já têm bloco (g01 a g10); o repositório `Minimum-path-algoritms-scenarios` (soluções de aluno, sem arquivo de licença) e os cadernos e páginas `.html` soltos. Nada deles foi copiado.

## Resoluções
Todas as resoluções são da equipe TutorON e foram conferidas por código em `tests_acervo/test_disciplina_grafos.py` (NetworkX 3.7 e força bruta).
- Não resolvidas: questão 4.4 da lista (mapa do Brasil), porque depende da lista de fronteiras entre estados, que não foi conferida; questões 1, 3 e 6 da prova de 2016.2, que dependem de figuras não reproduzidas.

## Fronteiras
Representação e BFS/DFS como código ficam em Estrutura de Dados; complexidade e NP-completude, em PAA; indução e contagem, em Matemática Discreta. Os índices são separados e o teste confere que a busca dessas disciplinas não traz blocos de grafos.
