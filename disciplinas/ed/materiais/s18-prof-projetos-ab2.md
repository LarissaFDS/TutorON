---
id: ed-prof-projetos-ab2
titulo: Projetos da AB2 — entregas, contagem de comparações e gráficos
assunto: ed-14-projetos-depuracao
tipo: material_estudo
resolucao: nao
fonte: PDF "Preparatório para os Projetos – AB 2", Estruturas de Dados - ECOM008 (Márcio Ribeiro, UFAL, 16/04/2025)
fontes_catalogo: ufal-ed-prof-preparatorio
autoria: Márcio Ribeiro (UFAL, Instituto de Computação), slides da disciplina; parafraseado pela equipe TutorON
licenca: Não declarada (material do professor); o PDF não está no repositório
publicacao_transcricao: não autorizada: o bloco parafraseia, não transcreve
curadoria: aprovado
natureza: material_da_disciplina
verificacao: sem_resolucao
revisao_humana: pendente
---
Entregas da AB2, segundo o PDF do professor (parafraseado):
1. Huffman em C: compactar e descompactar qualquer arquivo; cabeçalho .huff obrigatório; `void*` nas estruturas; documentação estilo JavaDoc.
2. SAT Solver em C, lendo fórmulas no formato DIMACS.
3. Seminário sobre uma aplicação de estrutura de dados.
4. Contagem e gráfico: comparar, contando comparações, lista × árvore de busca, ou árvore sem balanceamento × AVL, ou fila de prioridade com e sem heap; o gráfico deve ser feito só em R ou Matlab.

Equipes de 3 a 5 pessoas, nota individual, projeto no GitHub.

Como estudar a Entrega 4 sem confundir as curvas: insira as mesmas chaves nas duas estruturas e conte uma comparação a cada teste de chave. Use chaves em ordem crescente (o pior caso da ABB, que vira lista, O(n) por busca) e chaves aleatórias. A ABB fica perto de log₂ n por busca no caso aleatório; a AVL fica perto de log₂ n nos dois casos. Use um contador global ou passado por ponteiro, zerado antes de cada medição.
