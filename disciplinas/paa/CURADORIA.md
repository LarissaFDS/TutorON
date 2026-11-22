# PAA: curadoria do material de Ciência da Computação

O acervo principal de PAA vem do pipeline de OCR (`pipeline/02-acervo`). Este arquivo registra só o complemento com material da turma de Ciência da Computação da UFAL (pasta de origem `16. COMP374 - Projeto e Análise de Algoritmos`), recebido em 22/11/2026.

## Ementa
O PPC de Ciência da Computação (matriz 2011, https://ufal.br/estudante/graduacao/projetos-pedagogicos/campus-maceio/ProjetoPedagogicoCCompMatriz2011_PROGRAD.pdf) traz os tópicos de PAA de Engenharia: análise assintótica, recorrências, paradigmas de projeto, grafos, NP-completude. O material da turma tem ainda árvores B (slides da Profa. Alla), TSP e FFT (resumos da AB2), que não têm bloco no acervo. A diferença não justifica disciplina separada.

## O que entrou
Dois **candidatos** em `disciplinas/paa/candidatos/`, ambos com `revisado: false`. Eles **não estão no acervo nem na busca**. Para entrar, iriam para `materiais/Equipe/`, mas dois testes existentes não aceitam isso sem mudança, e testes antigos não foram alterados:
- `tests_acervo/test_equipe_pd.py` exige que todo arquivo de `materiais/Equipe/` seja de programação dinâmica (com `Tabela:`) e fixa a lista e01–e05.
- `tests_acervo/test_recuperacao_notacao.py::test_ranking_lexico_de_paa_preservado` guarda um instantâneo do ranking léxico de PAA, que muda com qualquer bloco novo.

A decisão fica com a equipe: ajustar esses testes ou escolher outro caminho. Os candidatos são:
- `e06`: O, Ω e Θ de sete pares de funções e a recorrência T(n) = T(n/3) + n³ (Teorema Mestre, caso 3, e forma fechada 27/26 (n³ − 1)). Vem de uma prova 1 de 2012 respondida por um aluno. A equipe refez a resolução, e as respostas do aluno estavam certas.
- `e07`: verdadeiro ou falso sobre P, NP e NP-completo e a redução de clique para conjunto independente. Vem de uma prova 4 do Prof. André Lins respondida por um aluno. A justificativa do item (e) estava errada: o problema é o tempo exponencial, não a memória. O item (b) fala em tempo médio, e só a versão de pior caso se prova como está.

As contas e a redução são conferidas em `tests_acervo/test_equipe_cc_paa.py`.

## O que ficou fora
- Provas com nome de aluno no arquivo e as fotos de provas (`Provas/PAA (1)`, `Provas/Paes`). Nenhum nome de aluno entrou no acervo.
- A revisão da reavaliação da AB1, feita por uma aluna. O conteúdo (seleção de atividades) já está no acervo.
- As listas de exercícios do Prof. André L. L. Aquino, que só citam exercícios do Cormen (livro protegido).
- O material da UFCG, os slides da Profa. Alla e os resumos da AB2. Os tópicos já estão no acervo ou ficam pendentes.
- Os livros do Cormen, que são protegidos.

## Pendências
1. Decidir como os candidatos entram no acervo (ver acima) e fazer a revisão humana de `e06` e `e07`.
2. Decidir se árvores B, TSP e FFT ganham bloco.
