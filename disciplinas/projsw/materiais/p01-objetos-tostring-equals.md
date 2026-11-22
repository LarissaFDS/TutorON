---
id: projsw-objetos-referencias-tostring-equals
titulo: Objetos e referências — o que imprime umaConta.toString(), == compara referências e equals compara conteúdo, equals com hashCode, testes da classe Pessoa
assunto: projsw-01-classes-objetos
tipo: notas
questao: pergunta da aula 3 e exercício para casa da aula 6
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seções "Usando objetos" e "Criação de Classes"
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
Notas de aula de Programação II da UFCG, seções "Usando objetos" e "Criação de Classes" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Objeto e referência:** `ContaSimples umaConta = new ContaSimples("Joao", "30914060506", 1);` cria o objeto com `new` (chama o construtor) e guarda na variável uma **referência** a ele. Um objeto sem nenhuma referência pode ser recolhido pelo coletor de lixo.

**Pergunta da aula:** `System.out.println(umaConta)` é o mesmo que `System.out.println(umaConta.toString())`. Nas notas a saída é do tipo `ContaSimples numero 1, titular Joao, data ..., saldo R$700,00`: aparece uma **data** (de abertura da conta) que não foi passada ao construtor, ou seja, um atributo que o próprio construtor preenche. Se a classe não sobrescreve `toString`, sai o de `Object` (nome da classe, `@` e um código em hexadecimal).

**Igualdade (teste 3 do exercício da classe Pessoa: duas pessoas com o mesmo nome e CPF):**
```java
Pessoa a = new Pessoa("Joao", "113"), b = new Pessoa("Joao", "113");
a == b        // false: são dois objetos
a.equals(b)   // true só se Pessoa sobrescrever equals
```
Sem sobrescrever, `equals` herdado de `Object` compara referências como `==`. Quem sobrescreve `equals` deve sobrescrever `hashCode` com os mesmos campos; senão um `HashSet` guarda as duas pessoas "iguais".

**Testes de unidade (JUnit):** um caso de teste cria o objeto, chama um método e verifica o resultado com `assertEquals(esperado, obtido)`; escreva um teste por comportamento (criar, alterar CPF, comparar duas pessoas).

Erros comuns: comparar `String` com `==`; esquecer `hashCode`.

**Verificação:** `test_objetos_e_igualdade` compila e roda `tests_acervo/projsw_java/pessoa`: `a == b` falso, `a.equals(b)` verdadeiro, o `HashSet` fica com 1 elemento e a classe sem `equals` dá falso.
