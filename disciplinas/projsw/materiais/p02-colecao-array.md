---
id: projsw-colecao-array-quatro-operacoes
titulo: Coleção com array — como implementar adicionar, remover, pesquisar e iterar; o que acontece com mais de 10 nomes (ArrayIndexOutOfBoundsException)
assunto: projsw-02-colecoes-genericos
tipo: notas
questao: perguntas da aula de coleções (cadastro de pessoas)
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seção "Coleções de objetos"
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
Notas de aula de Programação II da UFCG, seção "Coleções de objetos" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Pergunta da aula:** usando um array como coleção, como implementar as 4 operações? E o que ocorre se o usuário digitar mais de 10 nomes?

Guarde o array e um contador `n` de posições ocupadas (os elementos ficam em `nomes[0..n-1]`):
- **adicionar:** se `n == MAX`, recuse (ou cresça o array); senão `nomes[n++] = nome`;
- **pesquisar:** percorra de 0 a `n-1` comparando com `equals`; devolva o índice ou `-1`;
- **remover:** pesquise; se a ordem não importa, copie o último para o buraco e faça `nomes[--n] = null`; se importa, desloque os seguintes uma posição para a esquerda;
- **iterar:** laço de 0 a `n-1` (não até `nomes.length`, para não pegar `null`).

```java
boolean adicionar(String nome) {
    if (n == MAX) return false;
    nomes[n++] = nome;
    return true;
}
```
**Mais de 10 nomes:** sem o teste, a 11ª escrita em `nomes[10]` lança `ArrayIndexOutOfBoundsException`, porque os índices válidos vão de 0 a 9. As soluções são avisar e não cadastrar (como nas notas) ou trocar o array por uma `ArrayList`, que cresce sozinha.

Erros comuns: iterar até `length` e tropeçar em `null`; esquecer de decrementar `n` ao remover.

**Verificação:** `test_colecao_com_array` roda `tests_acervo/projsw_java/cadastro`: a 11ª inserção é recusada, `pesquisar` acha `p3` no índice 2, a remoção traz `p10` para o buraco e a escrita fora do limite lança a exceção.
