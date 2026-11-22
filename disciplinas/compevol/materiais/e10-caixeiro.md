---
id: compevol-caixeiro-viajante-representacao-por-permutacao-cruzamento-ox-mutacao-por-troca
titulo: Problema do caixeiro-viajante com AG: representação por permutação, por que o cruzamento de um ponto falha, cruzamento de ordem (OX) e mutação por troca
assunto: compevol-02-operadores
tipo: exercicio_resolvido
questao: Lacerda e Carvalho, seção 3.5
resolucao: sim
fonte: Apostilas e textos da pasta da turma (Lucas, UFRGS 2002; Lacerda e Carvalho; Dianati, Song e Treiber)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: lacerda-carvalho-ag
autoria: Exercício clássico dos textos da pasta da turma; resolução da equipe TutorON
licenca: Textos sem licença aberta declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Lacerda e Carvalho, seção 3.5 (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Problema:** dadas $n$ cidades e as distâncias, achar o **ciclo de menor comprimento** que visita cada cidade uma vez. Há $(n - 1)!/2$ rotas distintas: com 10 cidades, 181 440; com 20, cerca de $6 \times 10^{16}$. Força bruta só serve para $n$ pequeno.

**Representação:** o cromossomo é uma **permutação** das cidades (ex.: `3 1 4 0 2`); a aptidão é o inverso do comprimento da rota (ou minimiza-se o comprimento).

**Por que o cruzamento de um ponto falha:** pais `0 1 2 3 4` e `3 4 0 1 2`, corte depois da 2ª posição: filho `0 1 0 1 2`, com cidades repetidas e faltando: rota **inválida**.

**Cruzamento de ordem (OX):** copia um trecho do pai 1 e completa com as cidades que faltam **na ordem em que aparecem no pai 2**, a partir do fim do trecho. Exemplo: pai 1 = `0 1 2 3 4 5 6 7`, pai 2 = `3 7 5 1 6 0 2 4`, trecho das posições 2 a 4 do pai 1 (`2 3 4`). Percorrendo o pai 2 a partir da posição 5 (`0 2 4 3 7 5 1 6`) e pulando 2, 3 e 4, sobram `0 7 5 1 6`, que preenchem as posições 5, 6, 7, 0, 1: filho = `1 6 2 3 4 0 7 5`. Sempre é uma permutação válida.

**Mutação:** **troca** de duas cidades, **inversão** de um trecho (como o 2-opt) ou inserção.

**Verificação:** `test_caixeiro_viajante` confere o filho do exemplo de OX e que o OX sempre gera permutações em 1000 sorteios, e roda um AG (OX, inversão, torneio, elitismo) com semente fixa em 8 cidades, que acha o comprimento ótimo calculado por força bruta.
