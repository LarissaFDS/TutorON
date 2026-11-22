---
id: sd-ecom012-ab2
titulo: Circuitos Digitais (ECOM012), AB2 e prova final — latch SR com NAND, flip-flop de borda, registradores, combinacional × sequencial
assunto: sd-07-latches-flip-flops
tipo: prova
resolucao: sim
questao: 1-6
fonte: fotos da AB2 (2015 e 2016), da prova de reposição e da prova final de Circuitos Digitais (UFAL) | enunciados parafraseados
fontes_catalogo: ufal-ecom012-provas-2015-2016
autoria: Enunciados: provas da disciplina Circuitos Digitais (UFAL), professor não identificado. Resoluções: equipe TutorON com apoio de IA; latch e detector de borda conferidos por simulação
licenca: Não declarada (prova da disciplina; fotos de aluno, não versionadas)
publicacao_transcricao: não autorizada; enunciados parafraseados a partir das fotos, sem nomes, notas ou imagens
curadoria: aprovado
natureza: material_da_disciplina
revisao_humana: pendente
verificacao: parcial
---
Circuitos Digitais (ECOM012) — AB2, reposição e prova final (2015–2016)

1. Qual o estado de repouso (quiescente) das entradas S e R num latch SR feito com duas NAND?
Resolução: as entradas são ativas em nível baixo (S', R'). Em repouso, **S' = R' = 1** e o latch guarda Q. S' = 0 faz Q = 1; R' = 0 faz Q = 0; as duas em 0 é a combinação proibida.

2. Figura: o clock entra num NOT e numa AND junto com o próprio clock; a saída dessa AND (pulso curto) habilita duas AND que levam D e D' a um latch de duas NOR (saídas Q e Q'). É um flip-flop D disparado na borda de subida. Modifique para disparar na borda de descida.
Resolução: o pulso nasce porque o NOT atrasa: logo após a subida, clock = 1 e o NOT ainda dá 1. Para a descida, troque a AND do gerador de pulso por uma **NOR** (logo após a descida, clock = 0 e o NOT ainda dá 0), ou ponha um inversor na entrada do clock.

3. Diferença entre flip-flop D e RS: o D tem uma entrada só e copia D na borda, sem combinação proibida; o RS tem set e reset separados e proíbe S = R = 1.

4. Função do clock num registrador de deslocamento: a cada borda, todos os flip-flops copiam ao mesmo tempo a saída do vizinho, e o dado anda uma posição.

5. Combinacional × sequencial: a saída do combinacional depende só das entradas atuais; a do sequencial depende também do estado guardado (memória, em geral com clock).

6. Registrador de 8 bits: 8 flip-flops D com o mesmo clock, cada Dᵢ ligado ao bit i da entrada e Qᵢ ao bit i da saída (com carga, um MUX 2:1 em cada D escolhe entre manter Qᵢ e carregar).

**Verificação:** latch NAND e detector de borda simulados em tests_acervo/test_sd_ecom012.py; as respostas discursivas (3–6) não têm conferência por código.
