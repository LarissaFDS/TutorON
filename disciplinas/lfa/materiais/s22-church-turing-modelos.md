---
id: lfa-tese-de-church-turing-modelos
titulo: Tese de Church-Turing e modelos de computação equivalentes — variantes da MT (várias fitas, não determinística), programas LOOP/WHILE, funções recursivas, cálculo lambda
assunto: lfa-06-maquinas-de-turing
tipo: material_estudo
resolucao: nao
fonte: Aula 6 das notas de Sipser (MIT, Holden Lee), variantes de MT e tese de Church-Turing; apostila 01 (Profa. Simone Prado); ementa de ECOM014
fontes_catalogo: lee-sipser-notas-2012,mit-ocw-18-404j,unesp-prado-apostilas-tc,turing-1950-imitation-game
autoria: Aulas de Michael Sipser (MIT) nas notas de Holden Lee; paráfrase da equipe TutorON
licenca: Notas sem licença declarada; paráfrase. Curso aberto MIT OCW 18.404J sob CC BY-NC-SA 4.0
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
revisao_humana: pendente
---
**Tese de Church-Turing:** "algoritmo" (procedimento efetivo) é o mesmo que máquina de Turing que sempre para. Não é um teorema: liga a noção intuitiva de algoritmo a um modelo formal. O apoio vem de todos os modelos razoáveis já propostos serem equivalentes à MT.

**Modelos equivalentes (mesmo poder):**
- **MT de várias fitas:** simulada por uma fita, com as fitas lado a lado e as cabeças marcadas. O tempo pode ficar quadrático, mas o que é computável não muda.
- **MT não determinística:** simulada por busca em **largura** na árvore de computações (em profundidade, poderia cair num ramo infinito). O tempo pode ficar exponencial.
- **Enumeradores:** uma linguagem é Turing-reconhecível se, e só se, algum enumerador a lista.
- **Programas com WHILE ou GOTO** (máquina Norma, LPM com GOTO), **funções $\mu$-recursivas** e **cálculo lambda**.

**Modelos mais fracos:**
- autômato finito (sem memória além do estado);
- autômato com pilha (memória só no topo);
- programas só com **LOOP** de repetição definida: computam as funções **recursivas primitivas**, que sempre param. A função de Ackermann é computável e não é recursiva primitiva.

Para que serve na disciplina: depois da tese, uma prova de que "nenhum algoritmo resolve X" vale para qualquer linguagem de programação. Ela é feita sobre MT e se aplica a todas.

O artigo de Turing de 1950 (o "jogo da imitação") trata de outra pergunta, se máquinas podem pensar, e está no material só como leitura.

**Verificação:** o simulador de MT e o interpretador de programas LOOP/GOTO de `tests_acervo/lfa_verif.py` calculam as mesmas funções nos exemplos da disciplina (cópia de fita, soma, comparação); este bloco não tem conta própria.
