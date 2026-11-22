---
id: projsw-genericos-iterador-remocao
titulo: Generics e iteradores — por que List<String> evita o cast e a ClassCastException, Iterator e remoção segura com it.remove(), ConcurrentModificationException no for-each
assunto: projsw-02-colecoes-genericos
tipo: notas
questao: objetivos da aula de coleções (ausência de casts, iterador)
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seções "Coleções de objetos" e "framework de Coleções"
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
Notas de aula de Programação II da UFCG, seções "Coleções de objetos" e "framework de Coleções" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Sem generics** (`List lista = new ArrayList()`), a lista guarda `Object`: é preciso fazer cast na leitura, e um elemento do tipo errado só aparece na **execução**, como `ClassCastException`.

**Com generics** (`List<String> nomes = new ArrayList<>()`), o compilador confere o tipo: `nomes.add(42)` nem compila, e `nomes.get(0)` já é `String`, sem cast. Isso é **programação genérica**: a mesma classe `ArrayList<T>` serve para qualquer tipo `T`.

**Iterador:** `Iterator<String> it = nomes.iterator()` percorre qualquer coleção com `hasNext()` e `next()`, sem saber se ela é lista, conjunto ou árvore. Para remover durante o percurso, use `it.remove()`:
```java
for (Iterator<String> it = nomes.iterator(); it.hasNext();) {
    if (it.next().startsWith("B")) it.remove();
}
```
Chamar `nomes.remove(x)` dentro de um for-each muda a lista por fora do iterador e, em geral, o próximo `next()` lança `ConcurrentModificationException`.

**Qual coleção:** `ArrayList` (acesso por índice), `LinkedList` (inserção nas pontas), `HashSet` (sem repetição, sem ordem), `TreeSet` (ordenado), `HashMap` (chave → valor).

**Verificação:** `test_genericos_e_iteradores` compila `tests_acervo/projsw_java/genericos` (a versão sem generics dá `ClassCastException`; a remoção pelo iterador deixa `[Ana, Caio]`; a do for-each lança a exceção) e confere que `genericos_erro` **não** compila.
