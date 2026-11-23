---
id: clp-palavras-reservadas-versus-palavras-chave
titulo: Palavras reservadas × palavras-chave na especificação de uma linguagem e como cada escolha afeta a inclusão de uma nova palavra especial
assunto: clp-02-nomes-vinculacao-escopo
tipo: prova
questao: AB1 2013.1 Q4
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
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB1 2013.1 Q4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Palavra reservada:** palavra especial que **não pode ser usada como nome** (identificador) em nenhum contexto. Exemplos: `int`, `while`, `return` em C; `class` em Java.

**Palavra-chave:** palavra que é especial **só em certos contextos** e pode ser usada como nome fora deles. Exemplo clássico: em FORTRAN, `INTEGER REAL` declara uma variável inteira chamada `REAL`, e `REAL INTEGER` declara uma real chamada `INTEGER`. Em Python moderno, `match` e `case` são *palavras-chave suaves*: `match = 3` é válido.

**Efeito sobre a inclusão de uma palavra nova (Q4b):**
- Com **palavras reservadas**, acrescentar uma nova **quebra programas antigos** que usavam essa palavra como nome. Exemplo real: `async` virou reservada no Python 3.7, e código com variável `async` deixou de compilar.
- Com **palavras-chave** contextuais, a palavra nova pode entrar **sem quebrar** programas antigos. O custo é para a legibilidade (o leitor precisa do contexto) e para o analisador sintático.

Resumo: reservadas favorecem a legibilidade e a análise; palavras-chave favorecem a compatibilidade na evolução da linguagem.

**Verificação:** `test_palavras_reservadas_e_chave` usa o próprio Python: `keyword.iskeyword("while")` é verdadeiro e `while = 1` não compila; `match` é palavra-chave suave (`keyword.issoftkeyword`) e `match = 3` compila.
