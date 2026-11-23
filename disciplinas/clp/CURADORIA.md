# Curadoria — Conceitos de Linguagens de Programação

Situação: **em validação**. Revisão humana pendente em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `COMP389 - Conceitos de Linguagens de
Programação`, ênfase Sistemas de Informação). No PPC de CC (matriz 2011) a disciplina é a **CCOM027**,
60 h, 4º semestre: fundamentos da análise de linguagens; nomes, ligação, checagem de tipos e
escopos; tipos de dados; expressões, atribuição e estruturas de controle; subprogramas. Não há
disciplina equivalente cadastrada para Engenharia de Computação.

## O que entrou
14 blocos (`materiais/c01`–`c14`) com as questões das provas do Prof. Alcino Dall'Igna Jr.:
AB1 de 2013.1, AB2 de 2011.2 (com o nome antigo "Teoria e Paradigmas de Linguagens de
Programação") e final de 2012.2. Enunciados parafraseados; resoluções da equipe TutorON,
conferidas em `tests_acervo/test_disciplina_clp.py`. O código C é compilado com gcc. Ruby, Haskell
e Prolog não estão no ambiente de testes e foram reproduzidos em Python com a mesma semântica.

## O que não entrou
- Fotos e PDFs das provas: têm nome e matrícula de alunos. Nada versionado.
- Respostas de alunos, anotações de aula e trabalhos (Fortran 90, JavaScript, Python, Ruby, Go,
  Groovy, matrizes associativas, corrotinas): trabalhos identificados, só como evidência dos tópicos.
- Respostas às questões de revisão do Sebesta (`Revisao_Capitulo6.txt`), slides e PDFs do livro:
  material protegido, só referência por capítulo.
- Questão 3 da AB1 de 2013.1 (premissas das linguagens): coberta só conceitualmente, sem código.

## Decisões pendentes
- Sem ligação em `disciplinas/cursos.json`: CLP é do 4º período de CC, e ligar mudaria as
  preferidas desse período, fixadas em `backend/tests/test_versao_final.py` (`{paa, lfa}`).
- Paradigmas (funcional, lógico) só aparecem nas questões de prova; CCOM036 Paradigmas de
  Linguagens de Programação não tem material.
