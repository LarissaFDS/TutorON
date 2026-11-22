---
id: grafos-digrafos-graus-entrada-saida-aciclicos
titulo: Grafos orientados (dígrafos) — soma dos graus de entrada = soma dos graus de saída = |E|, grafos sem circuitos (acíclicos, DAG) e ordenação topológica
assunto: grafos-07-digrafos-fluxos
tipo: lista
questao: 4.5
resolucao: sim
fonte: Lista de exercícios de Teoria dos Grafos 2020.1, Prof. Rian Gabriel Pinheiro (IC-UFAL)
curso: Ciência da Computação (UFAL), Teoria dos Grafos (COMP369), 2020.1
fontes_catalogo: ufal-rian-lista-2020-1
autoria: Questões do Prof. Rian Gabriel Pinheiro (UFAL); resolução da equipe TutorON
licenca: Não declarada (lista, prova e slides); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista 2020.1, questão 4.5 (enunciado parafraseado); grafos sem circuitos vêm da ementa. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Graus num dígrafo:** $d^-(v)$ é o grau de entrada (arcos que chegam a $v$) e $d^+(v)$ o de saída. Cada arco sai de exatamente um vértice e chega a exatamente um, então
$$\sum_{v} d^-(v) = |E| = \sum_{v} d^+(v)$$
(em palavras: somando as entradas, ou as saídas, cada arco é contado uma vez).

**Grafo sem circuitos (DAG):** dígrafo sem ciclo orientado. Todo DAG não vazio tem um vértice com $d^- = 0$ (uma fonte): ande para trás pelos arcos; como não há ciclo e o grafo é finito, a caminhada termina numa fonte.

**Ordenação topológica:** repita "retire uma fonte e ponha-a no fim da lista". A ordem obtida põe a origem de cada arco antes do destino. Se em algum momento não houver fonte, o grafo tem ciclo. Exemplo: ordem de disciplinas respeitando pré-requisitos.

**Verificação:** `test_digrafos` confere a soma dos graus em dígrafos aleatórios e, com NetworkX, que a ordem topológica respeita todos os arcos e que um dígrafo com ciclo não tem ordem.
