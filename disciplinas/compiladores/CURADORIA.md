# Curadoria — Compiladores

Situação: **MVP** desde 23/11/2026, por decisão da equipe para a parte 3 da fila de Ciência da Computação.
Revisão humana e do professor pendentes em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (Compiladores, COMP263). O cabeçalho da AB1 de 2017.1
também cita COMP026 e ECOM045, então a prova pode ter sido comum a mais de uma turma; a disciplina é uma só
no acervo. Os trabalhos de 2010 e 2016 e as correções de 2015.2 citam o Prof. Alcino Dall'Igna Júnior
(IC-UFAL). As provas de 2017.1 não trazem nome de professor.

A pasta tem:
- **provas:** fotos de 2013 e 2014 com respostas de alunos; 2015.2 com resoluções; AB1 e AB2 de 2017.1
  em fotos; duas provas de 2009 e 2010 do Prof. Marcus Ramos com respostas (a instituição não aparece nos
  arquivos);
- **trabalhos:** enunciados de 2017.1 (1º e 2º bimestre); trabalhos de alunos (especificações das
  linguagens LDS de 2010, 2M de 2016 e "friday" de 2017, analisadores em C e Java);
- **tabelas** de precedência e preditiva de um trabalho;
- **anotações** de alunos;
- uma **apostila** da URI-Erechim (2001);
- **áudios** de revisão da AB2.

**Ementa não conferida.** A ementa de COMP263 não foi encontrada e não foi inventada. Os tópicos saíram
das provas e dos enunciados dos trabalhos.

## O que entrou
11 blocos (`materiais/c01`–`c11`), todos na busca, em três assuntos:
- **fundamentos e análise léxica:** conceitos, diagramas T, bootstrapping; tokens e reconhecedor de
  números;
- **análise sintática:** FIRST, FOLLOW e LL(1); transformação em LL(1); preditivo tabular e recursivo;
  precedência de operadores; SLR(1);
- **semântica e código intermediário:** atributos herdados e sintetizados; repeat, for e laço por
  contador; código de três endereços, AST e DAG; verificação de tipos e coerção.

Tudo é refeito em Python em `tests_acervo/test_disciplina_compiladores.py`. Isso inclui FIRST e FOLLOW,
tabelas LL(1) e SLR(1), simulação das pilhas, execução do código gerado e verificação de tipos.

**Correções:**
- `c11` (corrigida): a resolução da cópia de 2015.2 trocava `T1.nome` por `E1.nome` e testava o operando
  errado em `T = T1 * F`.
- `c09`: segue a resolução marcada como correta na cópia. Uma das respostas de aluno do repeat não repete
  o corpo.
- `c06`: uma resposta da AB1 de 2017.1 juntava todos os operadores num nível só e perdia a precedência.

## O que ficou de fora
- **Livros:** Price e Toscani (Implementação de Linguagens de Programação) e Aho et al. (Compiladores:
  Princípios, Técnicas e Ferramentas) não foram entregues nem versionados; são só referência.
- **Áudios da AB2:** não versionados e não transcritos, porque têm a voz de pessoas sem autorização
  registrada. Só a anotação escrita sobre o número de iterações foi usada, em `c09`.
- **Fotos de provas com nome e matrícula de alunos e respostas de alunos:** só os enunciados foram
  parafraseados, e nenhum nome entrou no acervo.
- **Trabalhos de alunos:** especificações de linguagens, analisadores e tabelas são avaliativos e
  identificados. Não entraram; serviram só como evidência dos tópicos.
- **Apostila da URI-Erechim:** licença não declarada; não versionada.
- **Gabarito do POSCOMP:** o arquivo está quase vazio (texto não extraível).

## Fronteiras
- Linguagens Formais e Autômatos (`lfa`): autômatos e gramáticas como teoria.
- Conceitos de Linguagens de Programação (`clp`): paradigmas e semântica das linguagens.
- Projeto e Análise de Algoritmos (`paa`): vizinha testada.

O isolamento é testado nos dois sentidos.

## Pendências
- Revisão humana dos 11 blocos e revisão do professor.
- Ementa de COMP263.
- Os seguintes tópicos aparecem nas provas mas não ganharam bloco nesta versão:
  - backpatching;
  - análise LR(1) canônica e LALR;
  - recuperação de erros;
  - otimização e geração de código final.
- As provas de 2013, 2014 e 2016 (fotos) foram lidas por amostragem.
