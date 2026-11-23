---
id: projsw-padrao-strategy-comparator
titulo: Padrão de projeto Strategy — trocar o algoritmo em tempo de execução (Comparator para ordenar alunos por nome ou por média); Factory Method citado nas notas
assunto: projsw-04-polimorfismo-interfaces
tipo: notas
questao: indicação de estudo das notas (Strategy e Factory Method)
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), fim da seção "Interfaces"
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
Notas de aula de Programação II da UFCG, fim da seção "Interfaces" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As notas indicam estudar os padrões **Strategy** e **Factory Method** depois de interfaces, sem desenvolvê-los. A ementa de CC (CCOM016) pede padrões de projeto orientado a objetos.

**Strategy:** quando uma classe precisa de um algoritmo que pode variar, ponha o algoritmo atrás de uma interface e receba o objeto pronto. O cliente não muda quando surge um algoritmo novo.

Em Java, `Comparator<T>` é uma estratégia de comparação:
```java
static List<Aluno> ordenar(List<Aluno> alunos, Comparator<Aluno> estrategia) {
    List<Aluno> copia = new ArrayList<>(alunos);
    copia.sort(estrategia);
    return copia;
}
ordenar(turma, Comparator.comparing(a -> a.nome));                          // por nome
ordenar(turma, Comparator.comparingDouble((Aluno a) -> a.media).reversed()); // maior média primeiro
```
Compare com `Comparable` (bloco de fraco acoplamento): `Comparable` fixa **uma** ordem natural dentro da classe; `Comparator` permite várias ordens, de fora da classe.

**Factory Method:** um método cria o objeto e devolve o tipo abstrato (`Robo criaRobo(String tipo)`), e o cliente não usa `new` com a classe concreta.

Livros de padrões (Gamma e outros; Kerievsky) ficam só como referência por seção.

**Verificação:** `test_strategy` roda `tests_acervo/projsw_java/strategy`: a mesma lista sai `[Ana, Bia, Caio]` por nome e `[Ana, Caio, Bia]` por média decrescente.
