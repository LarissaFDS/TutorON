# Curadoria: Projeto de Software (Programação 2, Ciência da Computação)

Disciplina nova, criada em 22/11/2026 a partir da pasta da turma de Ciência da Computação (COMP372, fila CC, parte 2).
Situação: **em validação**. Revisão humana e do professor: pendentes em todos os blocos.

## Ementa (PPC de CC, matriz 2011, CCOM016, 60 h) e cobertura

| Tópico da ementa | Assunto | Blocos |
|---|---|---|
| Abstração de dados; classes e instâncias | `projsw-01-classes-objetos` | p01 |
| Programação genérica; iteradores | `projsw-02-colecoes-genericos` | p02, p03 |
| Herança | `projsw-03-heranca-composicao` | p04, p05 |
| Polimorfismo; padrões de projeto OO | `projsw-04-polimorfismo-interfaces` | p06, p07 |
| (das notas) regras de projeto OO | `projsw-05-regras-de-projeto` | p08, p09 |
| (das notas) refatoramento | `projsw-06-refatoramento` | p10 |
| Tratamento de exceções; (das notas) arquivos | `projsw-07-excecoes-arquivos` | p11, p12 |
| Sobrecarga de operadores, templates, objetos função (C++) | — | **sem bloco**: o material da turma é em Java, que não tem sobrecarga de operadores |
| (das notas) recursividade | — | **sem bloco**: aprofundada em Programação 1 e Estrutura de Dados |

**Diferença de ementas:** a ementa de CC cita C++ (bibliografia de Stroustrup), mas diz "uma determinada linguagem orientada a objetos"; o material da turma é em Java. **Sem ligação em `disciplinas/cursos.json`:** ligar a Programação 2 de CC muda as disciplinas preferidas do 4º período de CC, que `backend/tests/test_versao_final.py` fixa em `{paa, lfa}`; mudar esse teste fica para decisão da equipe. A ECOM015 (Projeto de Software de Engenharia) também não foi ligada, porque a ementa de Engenharia não foi conferida nesta fila. O aluno escolhe a disciplina pelo seletor.

## Material
- **Usado (paráfrase, PDF não versionado):** notas de aula de Programação II da UFCG (Profs. Jacques Sauvé, Raquel Lopes e Dalton Serey). Os exemplos têm "Copyright (C) 1999 UFCG": o código dos blocos foi reescrito pela equipe em `tests_acervo/projsw_java` e é compilado nos testes. O metadado de autor do PDF é de quem montou o arquivo, não dos professores, e não entra no acervo.
- **Só referência (fora do zip):** Fowler (*Refactoring*), Gamma e outros (*Design Patterns*), Kerievsky (*Refactoring to Patterns*), Stroustrup.

## Resoluções
- **Corrigida:** o `compareTo` das notas (`this.getMatricula() - outro.getMatricula()` com `long`) não compila; o bloco usa `Long.compare` e o teste confere o erro do `javac`.
- O resto é `validada`, com saída conferida no JDK 11.
- Strategy: as notas só indicam o estudo; o bloco p07 é exemplo da equipe.

## Fronteiras
C e ponteiros em Programação 1; estruturas de dados em Estrutura de Dados; SQL em Banco de Dados. O teste confere que essas buscas não trazem blocos de Projeto de Software, e o contrário.
