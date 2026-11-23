# Curadoria — Interação Humano-Computador

Situação: **em validação**. Revisão humana pendente em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `Ênfases/Sistemas de Informação/COMP395 -
Interação Homem Máquina`), turma 2020.2, com aulas em 2021. O professor citado nos trabalhos é o
Prof. Fábio Paraguaçu (IC-UFAL).

A pasta tem pouco material:
- um conjunto de 18 slides, "A Nova Informática: Design centrado no Usuário";
- dois trabalhos de um grupo de alunos (microteste de usabilidade, AB1 e AB2).

**Ementa não conferida.** A ementa oficial de COMP395 não estava disponível e não foi inventada. Os
tópicos vêm dos slides e das etapas do projeto:
- design centrado no usuário e seus métodos;
- microteste de usabilidade e pensamento em voz alta;
- árvore de tarefas e modelo mental;
- personas;
- SUS;
- heurísticas;
- acessibilidade.

## O que entrou
8 blocos (`materiais/h01`–`h08`).
- `h01`, `h02`: slides parafraseados.
- `h03`–`h05`: etapas do projeto pedidas pelo professor, conhecidas pelos enunciados citados nos
  trabalhos. Trazem o método e um exemplo parecido com outra interface, sem o trabalho pronto.
- `h06`–`h08`: tópicos fundamentais ligados ao material, com fontes externas citadas:
  - SUS, citado nos trabalhos correlatos;
  - heurísticas de Nielsen, citado nos slides;
  - acessibilidade (WCAG), pela utilização universal e pelas dificuldades do público idoso.

As contas (SUS, razão de contraste do WCAG, taxa de sucesso), a lista das 10 heurísticas e os
exemplos estruturados são conferidos em `tests_acervo/test_disciplina_ihc.py`.

## O que ficou de fora
- **Os dois trabalhos de alunos:** trazem nomes, notas e links de vídeos com participantes. Não
  foram versionados. Serviram só para conhecer as etapas pedidas, e nenhuma análise ou persona do
  grupo foi copiada.
- **Livros** (Shneiderman, Nielsen) e o artigo do Nielsen Norman Group: só referência.

## Fronteiras
Projeto de Software (`projsw`) cobre processo, requisitos e UML; Metodologia da Pesquisa
(`metodologia`) cobre método científico e escrita. O isolamento é testado nos dois sentidos.

## Pendências
- Revisão humana dos 8 blocos e conferência do professor.
- Ementa oficial de COMP395.
- Mais material da turma (provas, listas), se houver.
- Rodar as perguntas de exemplo com a IA real e conferir.
