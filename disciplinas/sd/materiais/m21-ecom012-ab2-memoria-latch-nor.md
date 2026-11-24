---
id: sd-ecom012-ab2-memoria-latch-nor
titulo: Circuitos Digitais (ECOM012), AB2 — quantas portas AND e OR para expandir uma memória 4 x 3 para 512 x 8, e tabela verdade do latch de duas NOR com entradas X e Y
assunto: sd-12-conversores-memorias
tipo: prova
resolucao: sim
questao: varias
fonte: PDF da prova AB2 de Circuitos Digitais (UFAL, Engenharia de Computação, 2º período), sem data | enunciados parafraseados
fontes_catalogo: ufal-ecom012-provas-2020-2022
autoria: Enunciados: prova da disciplina Circuitos Digitais (UFAL), professor não identificado. Resoluções: equipe TutorON com apoio de IA, conferidas por código
licenca: Não declarada (prova da disciplina; PDF não versionado)
publicacao_transcricao: não autorizada; enunciados parafraseados, sem a figura
curadoria: aprovado
natureza: material_da_disciplina
revisao_humana: pendente
verificacao: conferida_por_codigo
---
Circuitos Digitais (ECOM012) — AB2 (memória e latch). Resolução da equipe TutorON, não é gabarito do professor. As outras questões da prova (registrador de 8 bits com CLEAR, repouso do latch SR com NAND, combinacional × sequencial) estão no bloco sd-ecom012-ab2-sequenciais.

1. Uma memória de 4 palavras de 3 bits, feita com flip-flops D, usa 22 portas AND e 3 portas OR. Quantas seriam para 512 x 8?
Resolução: conte as AND por função, para W palavras de B bits:
- decodificador de endereço: uma AND por palavra (W);
- porta de escrita: uma AND por palavra, que leva o clock aos flip-flops da palavra (W);
- leitura: uma AND por célula, que passa o bit da palavra selecionada (W·B);
- controle: uma AND para escrita (CS·RD') e uma para habilitar a saída (CS·RD·OE) (2).
Total 2W + W·B + 2. Com W = 4, B = 3: 8 + 12 + 2 = 22, confere com a figura. Com W = 512, B = 8: 1024 + 4096 + 2 = **5122 portas AND**. As OR juntam uma coluna de bits: uma por bit, então **8 portas OR**, cada uma com 512 entradas. O endereço passa a ter 9 bits (2⁹ = 512).

2. Latch de duas NOR cruzadas: X entra na NOR que dá Q, Y na que dá Q'. Tabela verdade e quem é S e R?
Resolução: Q = NOR(X, Q') e Q' = NOR(Y, Q).
- X = 0, Y = 0: guarda o estado.
- X = 0, Y = 1: Q' vai a 0, então Q = 1 (set).
- X = 1, Y = 0: Q = 0 (reset).
- X = 1, Y = 1: Q = Q' = 0, combinação proibida.
Logo **Y = S** e **X = R**: no latch NOR, a entrada da porta que gera Q é o reset. As entradas são ativas em 1, e o repouso é S = R = 0 (o contrário do latch com NAND).

**Verificação:** contagem de portas e latch simulados em tests_acervo/test_sd_ecom012.py.
