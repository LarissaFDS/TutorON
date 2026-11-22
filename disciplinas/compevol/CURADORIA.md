# Curadoria — Computação Evolucionária

Situação: **em validação**. Revisão humana pendente em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `Ênfases/Sistemas Inteligentes/COMP397 -
Computação Evolucionária`), turma 2021.1. O nome da docente não aparece nas capturas de tela.

**Ementa não conferida.** O Projeto Pedagógico de CC disponível (matriz 2011) não tem a disciplina
COMP397. A ementa não foi inventada: os tópicos vêm das apostilas e das atividades da turma.

## O que entrou
14 blocos (`materiais/e01`–`e14`):
- `e01`–`e10` e `e14`: conceitos e exercícios clássicos dos textos da pasta, parafraseados:
  - apostila de Diogo C. Lucas (UFRGS, 2002);
  - artigo de Dianati, Song e Treiber (Waterloo);
  - problemas do capítulo de Lacerda e Carvalho (só referência).
  Assuntos: otimização e máximos locais, representação binária, seleção, cruzamento e mutação, AG
  completo, esquemas, função F6, estratégias evolutivas, subida de encosta e meméticos,
  caixeiro-viajante e dilema do prisioneiro.
- `e11`–`e13`: atividades de 2021.1 (controle de parâmetros, multiobjetivo, alinhamento múltiplo de
  DNA). São avaliativas: os blocos explicam conceitos e trazem uma conta pequena, sem o programa
  pronto.

Os algoritmos são executados com semente fixa em `tests_acervo/test_disciplina_compevol.py`.
`e11` e `e14` têm verificação `exemplos_conferidos`.

## O que não entrou
- Capturas de tela da página do curso: só os enunciados foram parafraseados.
- Livro de Melanie Mitchell (MIT Press), artigo de Mitchell (1995) e capítulo de Lacerda e Carvalho:
  são protegidos e servem só de referência.
- PDFs das apostilas: não têm licença declarada e não foram versionados.
- Primeira atividade da 1ª ABN (rede neural para contar figuras) e o projeto com defesa: são de redes
  neurais ou avaliativos. A fronteira com Aprendizagem de Máquina e Ciência de Dados fica sem bloco.
- "Anotações da aula" citadas na página: o PDF não está na pasta.
- Não há provas na pasta.

## Decisões pendentes
- Sem ligação em `disciplinas/cursos.json`. É optativa de ênfase, fora da matriz do arquivo.
- Ementa oficial da COMP397 a conferir com a coordenação.
