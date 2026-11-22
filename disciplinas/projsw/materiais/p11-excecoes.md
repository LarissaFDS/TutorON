---
id: projsw-excecoes-try-catch-soma-argumentos
titulo: Tratamento de exceções — qual a saída para os argumentos 2 4 "oi" com try fora e dentro do laço, NumberFormatException, ordem dos catch, checked e unchecked
assunto: projsw-07-excecoes-arquivos
tipo: notas
questao: "qual a saída do programa para os argumentos 2 4 oi?"
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seção "Tratamento de erros com exceções"
curso: Ciência da Computação (UFAL), pasta da turma de Programação 2 / Projeto de Software (COMP372); notas de aula da UFCG usadas pela turma
fontes_catalogo: ufcg-notas-programacao2
autoria: Notas de aula dos Profs. Jacques Sauvé, Raquel Lopes e Dalton Serey (DSC-UFCG); resolução e código da equipe TutorON
licenca: Copyright da UFCG nos exemplos; paráfrase, PDF não versionado
publicacao_transcricao: não autorizada; o bloco traz paráfrase e código próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Notas de aula de Programação II da UFCG, seção "Tratamento de erros com exceções" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Pergunta da aula:** o programa soma os argumentos com `Integer.parseInt`. Qual a saída para `2 4 oi`?

**Versão 1 (try em volta do laço):** `parseInt("oi")` lança `NumberFormatException`; o controle salta para o `catch`, e a linha `Sum = ...` **não é impressa**. Sai só a mensagem de erro (em `System.err`).

**Versão 2 (try dentro do laço):** o erro é tratado por argumento e o laço continua:
```java
for (String a : args) {
    try {
        sum += Integer.parseInt(a);
    } catch (NumberFormatException nfe) {
        System.err.println("[" + a + "] is not an integer and will not be included in the sum.");
    }
}
System.out.println("Sum = " + sum);   // Sum = 6
```
O lugar do `try` decide **até onde** o erro desfaz o trabalho.

**Mais regras:**
- descobrir o erro e tratá-lo podem ficar em lugares diferentes: o método lança (`throw`) ou repassa (`throws`), e quem chamou trata;
- vários `catch`: o primeiro compatível ganha; ponha os **mais específicos primeiro** (`FileNotFoundException` antes de `IOException`; ao contrário nem compila);
- *checked* (ex.: `IOException`) obriga tratar ou declarar; *unchecked* (`RuntimeException`, como `NumberFormatException`) costuma indicar bug, mas às vezes vale tratar, como aqui;
- `finally` roda sempre, com ou sem exceção.

**Verificação:** `test_excecoes_soma` roda `tests_acervo/projsw_java/excecoes` com `2 4 oi`: a versão 1 não imprime soma e a versão 2 imprime a mensagem de `[oi]` e `Sum = 6`.
