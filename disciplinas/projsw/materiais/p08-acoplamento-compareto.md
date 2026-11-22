---
id: projsw-acoplamento-comparable-lista-ordenada
titulo: Fraco acoplamento — lista ordenada de alunos que conhece a matrícula, compareTo no próprio Aluno, Comparable<T> e lista genérica; o compareTo das notas não compila (long para int)
assunto: projsw-05-regras-de-projeto
tipo: notas
questao: exemplo de ordenação de alunos por matrícula (soluções 1 a 3)
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seção "Regras básicas de projeto OO (II)", regra 4
curso: Ciência da Computação (UFAL), pasta da turma de Programação 2 / Projeto de Software (COMP372); notas de aula da UFCG usadas pela turma
fontes_catalogo: ufcg-notas-programacao2
autoria: Notas de aula dos Profs. Jacques Sauvé, Raquel Lopes e Dalton Serey (DSC-UFCG); resolução e código da equipe TutorON
licenca: Copyright da UFCG nos exemplos; paráfrase, PDF não versionado
publicacao_transcricao: não autorizada; o bloco traz paráfrase e código próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Notas de aula de Programação II da UFCG, seção "Regras básicas de projeto OO (II)", regra 4 (paráfrase; código da equipe TutorON). Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Regras das notas:** (1) KISS, mantenha simples; (2) **especialista da informação**: dê a responsabilidade à classe que tem os dados; (3) **alta coesão**: responsabilidades focadas; (4) **fraco acoplamento**: dependa de poucas classes. Acoplamento aparece quando X tem atributo, parâmetro, variável local ou retorno do tipo Y, herda de Y ou implementa Y; herança é o mais forte.

**Exemplo:** `ListaOrdenada.add(Aluno x)` chama `getMatricula()` e compara com `<`. A lista sabe que alunos se comparam pela matrícula, que ela é `long` e como compará-la. **Solução 2:** o aluno se compara (`x.compareTo(outro)`). **Solução 3:** `class Aluno implements Comparable<Aluno>` e `ListaOrdenada<T extends Comparable<T>>`, que serve para qualquer tipo comparável.

**Correção:** nas notas, `compareTo` devolve `this.getMatricula() - outro.getMatricula()` com matrícula `long`. Isso **não compila** (de `long` para `int` pode perder valor), e o cast `(int)` daria sinal errado com diferenças grandes. Use:
```java
@Override public int compareTo(Aluno outro) {
    return Long.compare(matricula, outro.matricula);
}
```
(A solução 3 das notas também usa `outroAluno` em vez do parâmetro `outro`.)

Cuidado: reduzir acoplamento não é juntar tudo numa "classe Deus" com as outras como depósitos de dados.

**Verificação:** `test_acoplamento_compareto` confere que a versão das notas falha no `javac` com "lossy conversion" e que a lista genérica corrigida ordena matrículas até 3 bilhões e também `String`.
