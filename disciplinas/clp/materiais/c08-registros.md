---
id: clp-registros-referencia-qualificacao-completa-eliptica-cobol
titulo: Registros: referência com qualificação completa × referência elíptica a campos; COBOL como linguagem que aceita referência elíptica
assunto: clp-04-arrays-e-registros
tipo: prova
questao: AB1 2013.1 Q11; final 2012.2 Q6
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
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB1 2013.1 Q11; final 2012.2 Q6 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Qualificação completa:** a referência nomeia **todos os registros intermediários**, do mais externo até o campo. Em C: `empregado.nome.primeiro`. Em COBOL: `FIRST OF EMPLOYEE-NAME OF EMPLOYEE-RECORD`.

**Referência elíptica:** nomeia-se **o campo**, e **qualquer** dos registros que o envolvem pode ser **omitido**, desde que a referência continue **sem ambiguidade** no ambiente de referência.

**COBOL usa referência elíptica.** Com o registro
```cobol
01 EMPLOYEE-RECORD.
   02 EMPLOYEE-NAME.
      05 FIRST  PICTURE IS X(20).
      05 MIDDLE PICTURE IS X(10).
      05 LAST   PICTURE IS X(20).
   02 HOURLY-RATE PICTURE IS 99V99.
```
valem `FIRST`, `FIRST OF EMPLOYEE-NAME` e `FIRST OF EMPLOYEE-RECORD`, todas apontando o mesmo campo, se nenhum outro registro no programa tiver um campo `FIRST`. Se houver outro, é preciso qualificar o suficiente para desfazer a ambiguidade.

Comparação: a referência elíptica é cômoda para escrever, mas prejudica a legibilidade (o leitor precisa descobrir de que registro vem o campo) e complica o compilador. C, Java e Ada exigem qualificação completa (exceto dentro de construções como `with` de Pascal, que abre o escopo de um registro).

**Verificação:** `test_referencia_eliptica` implementa a regra: dado o caminho parcial, procura os campos cujo caminho completo termina com os nomes dados na ordem; `FIRST` acha um único campo, e com um segundo registro que também tem `FIRST`, a forma curta fica ambígua e `FIRST OF EMPLOYEE-NAME` volta a ser única.
