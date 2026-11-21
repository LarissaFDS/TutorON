---
id: lfa-mt-inserir-separador-entre-0-e-1
titulo: Máquina de Turing transdutora — inserir o separador # entre todo 0 seguido de 1 (deslocar a fita para a direita), questão da Prova 2
assunto: lfa-06-maquinas-de-turing
tipo: prova
questao: 2
resolucao: sim
fonte: Segunda avaliação de Teoria da Computação 2017.1, Profa. Eliana (UFAL), questão 2
fontes_catalogo: ufal-eliana-prova2-2017-1
autoria: Questão de prova da Profa. Eliana (UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Prova 2 de 2017.1, questão 2 (enunciado parafraseado): construir uma máquina de Turing que, para todo 0 seguido de 1 na entrada, insira o separador # entre eles. Exemplo: $0011 \mapsto 00\#11$ e $0101 \mapsto 0\#10\#1$. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Ideia:** percorra a fita; ao achar um 1 logo depois de um 0, escreva # no lugar do 1 e **desloque** o resto da fita uma célula para a direita. O símbolo que está sendo carregado fica guardado no estado.

| Estado | Lê | Escreve, move, vai para | Significado |
|---|---|---|---|
| $q_0$ | 0 | 0, D, $q_1$ | o último lido é 0 |
| $q_0$ | 1 | 1, D, $q_0$ | |
| $q_0$ | ⊔ | ⊔, D, aceita | |
| $q_1$ | 0 | 0, D, $q_1$ | |
| $q_1$ | 1 | #, D, $c_1$ | insere # e carrega o 1 |
| $q_1$ | ⊔ | ⊔, D, aceita | |
| $c_1$ | 0 | 1, D, $c_0$ | escreve o carregado, carrega o lido |
| $c_1$ | 1 | 1, D, $c_1$ | |
| $c_1$ | ⊔ | 1, E, volta | |
| $c_0$ | 0 | 0, D, $c_0$ | |
| $c_0$ | 1 | 0, D, $c_1$ | |
| $c_0$ | ⊔ | 0, E, volta | |
| volta | 0 ou 1 | igual, E, volta | |
| volta | # | #, D, $q_0$ | retoma logo depois do # |

Depois de voltar, $q_0$ lê o 1 que veio depois do #, e a varredura continua. Os # já inseridos ficam sempre à esquerda da cabeça, então nunca são lidos de novo. Para entradas sem "01", a máquina só percorre a fita e aceita.

Custo: cada inserção desloca o resto da fita, então são $O(n^2)$ passos no pior caso. Por exemplo, $(01)^k$ faz $k$ deslocamentos.

**Verificação:** a tabela (15 transições) foi simulada para todas as cadeias sobre $\{0,1\}$ até comprimento 9, e a fita final é igual a trocar cada "01" por "0#1" (por exemplo, $0101 \to 0\#10\#1$, $1100 \to 1100$).
