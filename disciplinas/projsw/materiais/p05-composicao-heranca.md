---
id: projsw-composicao-versus-heranca-acoplamento
titulo: Composição ou herança — "é um" versus "tem um", Conta tem uma Pessoa, por que a herança acopla mais (mudanças na classe base quebram subclasses), na dúvida escolha composição
assunto: projsw-03-heranca-composicao
tipo: notas
questao: perguntas sobre mudanças na classe base
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seção "Reuso por composição e herança"
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
Notas de aula de Programação II da UFCG, seção "Reuso por composição e herança" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Herança** (`class ContaPoupanca extends ContaCorrente`) expressa "**é um** tipo especial de": a subclasse herda atributos e métodos e pode sobrescrevê-los. **Composição** expressa "**tem um**": `Conta` tem um atributo `Pessoa titular` e **delega** a ele (`getNomeTitular()` chama `titular.getNome()`).

Teste rápido: "uma Conta **é uma** Pessoa?" Não; "uma Conta **tem** um titular?" Sim: composição.

**Perguntas das notas (o que acontece quando a classe base muda?):**
- muda a representação de um campo visível às subclasses: as subclasses que o usam podem quebrar;
- muda a implementação de um método: subclasses que contavam com o comportamento antigo podem quebrar (com composição também pode ocorrer);
- a interface muda: métodos removidos quebram as subclasses; métodos novos exigem decidir se é preciso sobrescrever; um método abstrato novo obriga todas as subclasses a implementá-lo. Use `@Deprecated` para dar tempo à mudança.

**Vantagens da composição:** acoplamento menor (ainda menor se o atributo for de um tipo interface) e o objeto composto pode ser trocado em tempo de execução. A herança é definida na compilação.

**Regra das notas:** na dúvida, escolha a composição; use herança quando houver mesmo um "é um" e for útil tratar a subclasse como a superclasse (polimorfismo).

**Verificação:** `test_composicao` roda `tests_acervo/projsw_java/composicao`: a conta delega o nome ao titular e mantém o saldo ao trocar de titular em tempo de execução.
