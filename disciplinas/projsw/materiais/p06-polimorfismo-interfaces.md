---
id: projsw-polimorfismo-interfaces-selecionavel-por-nome
titulo: Polimorfismo e interfaces — um só cliente para coleções de alunos, professores e disciplinas (Nomeavel, SelecionavelPorNome), ligação dinâmica, programar para a interface
assunto: projsw-04-polimorfismo-interfaces
tipo: notas
questao: exemplo do selecionador por nome
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seções "Polimorfismo", "Interfaces" e "Regras básicas de projeto OO (II)"
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
Notas de aula de Programação II da UFCG, seções "Polimorfismo", "Interfaces" e "Regras básicas de projeto OO (II)" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Polimorfismo:** uma referência de um tipo geral (`Nomeavel n`) aponta para objetos de classes diferentes, e a chamada `n.getNome()` executa o método da classe **real** do objeto (ligação dinâmica, decidida na execução).

**Interface:** só declara o comportamento comum (`interface Nomeavel { String getNome(); }`); classes sem parentesco a implementam (`class Aluno implements Nomeavel`). Uma classe herda de uma só superclasse, mas implementa várias interfaces.

**Exemplo das notas:** coleções de alunos, de professores e de disciplinas não estão na mesma hierarquia, mas uma tela precisa listar os itens com certo nome. Com
```java
interface SelecionavelPorNome { Iterator<Nomeavel> getIteradorPorNome(String nome); }
```
há polimorfismo em dois lugares: o cliente recebe qualquer `SelecionavelPorNome` e percorre qualquer `Nomeavel`. Um só cliente serve para as três coleções, e uma coleção nova não muda o cliente.

**Regra (programe para a interface):** declare variáveis e parâmetros com o tipo mais alto da hierarquia que basta (`List<String> l = new ArrayList<>()`, não `ArrayList<String> l`). Mas não crie interfaces sem necessidade: isso também se corrige refatorando.

Erros comuns: achar que o tipo da **variável** escolhe o método sobrescrito (ele escolhe só quais métodos podem ser chamados); confundir sobrescrita (mesma assinatura na subclasse) com sobrecarga (mesmo nome, parâmetros diferentes).

**Verificação:** `test_polimorfismo_e_interfaces` roda `tests_acervo/projsw_java/interfaces`: o mesmo método conta 2 alunos "Joao", 1 disciplina "Programacao" e 0 disciplinas "Joao", e `println` de um `Nomeavel` usa o `toString` de `Disciplina`.
