---
id: sd-nota-fsm
titulo: Nota — projeto de máquina de estados finitos (Moore e Mealy), passo a passo
assunto: sd-09-maquinas-de-estados
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: mit-ocw-6004,wikibooks-digital-circuits,free-range-vhdl
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Máquinas de estados finitos (FSM) — controladores

Moore: as saídas dependem só do estado (escritas dentro do círculo do estado). Mealy: as saídas dependem do estado e das entradas (escritas nas transições); costumam ter menos estados, mas a saída muda junto com a entrada.

Procedimento de projeto do controlador:
1. Capturar o comportamento: desenhe a FSM com estado inicial, transições rotuladas por condições das entradas e saídas de cada estado. Confira que, em cada estado, as condições das transições de saída cobrem todas as combinações de entrada sem se sobrepor (o que não estiver escrito significa "fica no estado").
2. Arquitetura: registrador de estado (flip-flops D) + lógica combinacional que calcula o próximo estado e as saídas.
3. Codificação: com k estados, use ⌈log₂ k⌉ bits (binária). Também existem a one-hot (um flip-flop por estado) e a Gray (vizinhos diferindo em um bit).
4. Tabela de estados: para cada estado atual e cada combinação de entradas, o próximo estado codificado e as saídas.
5. Equações: para cada bit de próximo estado e cada saída, escreva a soma de produtos da tabela e simplifique (Karnaugh). Ligue as equações nas entradas D dos flip-flops.

Verificação: escolha uma sequência de entradas, simule alguns ciclos pela tabela e pelas equações e veja se percorrem os mesmos estados.

Exemplo curto (detector de "11", Moore): estados S0 (nenhum 1), S1 (um 1), S2 (dois ou mais, saída 1). x = 1: S0 → S1 → S2 → S2; x = 0: volta a S0. Codificando S0 = 00, S1 = 01 e S2 = 10: n1 = x·(s1 + s0), n0 = x·s1'·s0' e z = s1.

Leitura de circuito sequencial (análise): escreva as equações de entrada dos flip-flops, monte a tabela de próximo estado e desenhe o diagrama de estados.
