---
id: so-substituicao-paginas-fifo-lru-otimo
titulo: Substituição de páginas — quantas faltas de página têm FIFO, LRU e ótimo com 3 quadros; tabela passo a passo
assunto: so-05-memoria
tipo: material_estudo
resolucao: sim
fonte: Slides do Prof. André Aquino (UFAL), gerência de memória (algoritmos de substituição); caderno do Prof. Maziero, cap. 5; sequência de referências e tabelas da equipe TutorON, conferidas por simulação
fontes_catalogo: ufal-aquino-slides-so,maziero-socm-2013,maziero-caderno-2014,turma-listas-2021
autoria: Conteúdo dos slides do Prof. André Aquino (UFAL); exemplo numérico da equipe TutorON
licenca: Slides sob CC BY-NC-SA 4.0 (Aquino); exemplo e paráfrase da equipe
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Os algoritmos dos slides da disciplina, aplicados a um exemplo da equipe TutorON. Sequência de referências: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, com **3 quadros**, inicialmente vazios (as três primeiras referências já são faltas).

- **FIFO:** sai a página que **entrou** há mais tempo.
- **LRU** (*least recently used*): sai a que foi **usada** há mais tempo; um acesso "renova" a página.
- **Ótimo** (OPT): sai a que vai demorar mais para ser usada de novo (exige conhecer o futuro; serve de referência).

**LRU passo a passo** (F = falta; entre parênteses, o último uso de cada página presente):

| Ref. | Quadros | Falta? | Vítima |
|---|---|---|---|
| 7 | 7 | F | — |
| 0 | 7 0 | F | — |
| 1 | 7 0 1 | F | — |
| 2 | 0 1 2 | F | 7 (usada em 1) |
| 0 | 0 1 2 | acerto | — |
| 3 | 0 2 3 | F | 1 (0 em 5, 1 em 3, 2 em 4) |
| 0 | 0 2 3 | acerto | — |
| 4 | 0 3 4 | F | 2 |
| 2 | 0 4 2 | F | 3 |
| 3 | 4 2 3 | F | 0 |
| 0 | 2 3 0 | F | 4 |
| 3 | 2 3 0 | acerto | — |
| 2 | 2 3 0 | acerto | — |

**LRU: 9 faltas.** Com a mesma sequência: **FIFO: 10 faltas** (no 0 da 7ª referência o FIFO já expulsou a página 0, que tinha sido usada, porque ela era a mais antiga a entrar) e **ótimo: 7 faltas**.

Erro comum: fazer o LRU como FIFO, sem atualizar a idade da página num acerto. Na 5ª referência (0, acerto) a página 0 passa a ser a mais recente; por isso, na 6ª, a vítima do LRU é 1, enquanto a do FIFO seria 0.

O LRU exato é caro (registrar o instante de cada acesso); os sistemas usam aproximações com o **bit de referência**: segunda chance (relógio) e envelhecimento (*aging*).

**Verificação:** ótimo ≤ LRU ≤ FIFO (7 ≤ 9 ≤ 10), como esperado neste exemplo; cada tabela tem 13 linhas e o número de faltas é o de linhas marcadas F. Simulado em `tests_acervo/so_verif.py`.
