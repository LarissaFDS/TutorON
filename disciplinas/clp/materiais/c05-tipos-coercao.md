---
id: clp-coercao-verificacao-de-tipo-tipagem-forte-conversao-int-float
titulo: Coerção, verificação de tipo e tipagem forte; perda de precisão nas conversões int ↔ float e int ↔ double (32 e 64 bits)
assunto: clp-03-tipos
tipo: prova
questao: AB1 2013.1 Q7; final 2012.2 Q5 e Q8; AB2 2011.2 Q3
resolucao: sim
fonte: Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (IC-UFAL)
curso: Ciência da Computação (UFAL), Conceitos de Linguagens de Programação (CCOM027); provas de 2011.2 a 2013.1
fontes_catalogo: ufal-alcino-provas-clp
autoria: Questões do Prof. Alcino Dall'Igna Jr. (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB1 2013.1 Q7; final 2012.2 Q5 e Q8; AB2 2011.2 Q3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Definições:**
- **Coerção:** conversão de tipo **implícita**, feita pelo compilador ou interpretador, para permitir uma operação com operandos de tipos diferentes (é o recurso perguntado na AB2: `int + float`). Enfraquece a detecção de erros.
- **Verificação de tipo:** garantir que os operandos de um operador (e os argumentos de uma chamada, e o valor de retorno) são de **tipos compatíveis**. Pode ser estática (compilação) ou dinâmica (execução).
- **Tipagem forte:** a linguagem **detecta sempre** os erros de tipo. C não é fortemente tipada (uniões sem verificação, ponteiros convertidos); Java e Haskell chegam perto, mas as coerções de Java ainda enfraquecem a detecção.

**Conversões (final, Q8), com `int` e `float` de 32 bits e `double` de 64:**
- `int → float`: o `float` tem **24 bits de mantissa** e o `int` usa 31 bits de valor. Inteiros acima de $2^{24} = 16\,777\,216$ podem **perder precisão**: `16777217` vira `16777216.0`. Não perde magnitude.
- `float → int`: **trunca** a parte fracionária (3.9 vira 3) e, se o valor passar do intervalo do `int`, o resultado é indefinido em C.
- `int → double`: o `double` tem 53 bits de mantissa: **todo `int` de 32 bits cabe exato**. É uma conversão de alargamento, segura.
- `double → int`: trunca, como em `float → int`, e pode estourar.

Resumo: alargamento (`int → double`) é seguro; `int → float` pode perder precisão mesmo sendo alargamento nominal; estreitamento (`float`/`double → int`) perde a fração e pode estourar.

**Verificação:** `test_conversoes_em_c` compila com gcc um programa que faz `(float)16777217`, `(int)3.9f`, `(double)2147483647` e volta, e confere 16777216, 3 e 2147483647 exato.
