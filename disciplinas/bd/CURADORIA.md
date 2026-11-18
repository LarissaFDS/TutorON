# Banco de Dados — curadoria do acervo

Situação: **MVP** desde 18/11/2026, sem aviso, depois de passar nos quatro critérios de liberação (suíte e bateria de relevância verdes; nenhuma nota de IA sem revisão humana na busca; perguntas de exemplo conferidas com a IA real; todo tópico confirmado pelos slides com bloco na busca). Antes disso ficou em validação. BD tem cadastro, acervo e índice próprios. Usa o mesmo fluxo da IA das outras disciplinas: o mesmo modelo, o mesmo backend e o mesmo prompt de sistema, mais as regras de [`rigor.md`](rigor.md). Revisão humana, aprovação do professor e confirmação das resoluções continuam pendentes (tabela abaixo).

| Item | Estado em 18/11/2026 |
|---|---|
| Cadastro, acervo (32 blocos, 26 na busca) e índice híbrido (`bge-m3`) | **Feitos** |
| SQL dos blocos | **Executado nos testes**: 51 trechos rodam no SQLite 3.50 com os bancos de `tests_acervo/sql_bd/`, e 47 deles têm o resultado conferido linha a linha. O trecho com `ALL` roda no DuckDB, como dialeto PostgreSQL. Os trechos em MySQL e T-SQL não rodam e estão marcados como `parcial` |
| Normalização | **Conferida por fecho de atributos** nos testes (Produto/Compra, Carro/Fabricante, BOLETIM) |
| Revisão humana interna | **Pendente** em todos os blocos (`revisao_humana: pendente`) |
| Resoluções de exercícios | **Pendentes de confirmação do professor** (`status_resolucao: pendente_professor`); os slides não trazem gabarito |
| Autorização para publicar transcrições | **Não dada**. Os blocos reescrevem os slides com texto próprio e usam dados da equipe |
| Aprovação do professor | **Não declarada**. Nenhum bloco tem `revisao_professor: sim` |
| Respostas da IA com o modelo real | **Conferidas em 10 casos** em 18/11/2026 (seção 7) |

- Catálogo legível por máquina: [`fontes.json`](fontes.json)
- Blocos: [`materiais/`](materiais/). Prefixos dos arquivos:
  - `a01`–`a15`: slides de BD;
  - `b01`–`b11`: slides de BD2;
  - `n01`–`n06`: notas da equipe escritas com IA. São candidatas e ficam fora da busca.
- Gerados (não editar à mão): [`acervo/itens.json`](acervo/itens.json) e [`acervo/indice.json`](acervo/indice.json)

## 1. Ementa e decisão BD + BD2

O arquivo `AULAS BD.rar` trouxe dois conjuntos de slides:

- **Banco de Dados**, da Profª Maria Cristina Tenório (`ufal-bd-slides`), com as aulas 1 a 5 e 8;
- **Bancos de Dados 2**, da Profª Cristina Tenório (`ufal-bd2-slides`), do curso de Penedo.

O PPC de Engenharia de Computação da UFAL (2014, `ufal-ppc-ecomp-2014`, p. 47) define ECOM041 Banco de Dados assim: 7º semestre, 60 h (40 teóricas e 20 práticas). A ementa cobre:

- métodos de acesso, arquitetura e modelos de dados;
- modelo ER, projeto lógico e modelo relacional;
- estudos de caso em SGBDs;
- transações, concorrência e recuperação;
- segurança e integridade;
- SQL.

BD2 não está na grade de 2014. Os slides de BD2 entram no acervo porque cobrem o SQL que essa ementa exige: junções, agregação, subconsultas, visões, triggers e procedures. Os slides de BD não têm essas aulas. Os blocos registram de qual conjunto vieram em `fontes_catalogo` e no prefixo `bd-` ou `bd2-` do id. A curadoria **não foi validada pelo professor**.

## 2. Tópicos, evidência e blocos

| Assunto | Evidência | Blocos na busca | Fora da busca |
|---|---|---|---|
| `bd-01-conceitos-sgbd` | Slides BD, aula 1, parte 1 | `bd-aula-conceitos-sgbd` | |
| `bd-02-modelos-arquitetura` | Slides BD, aula 1, parte 2 | `bd-aula-modelos-arquitetura` | |
| `bd-03-modelo-er` | Slides BD, aula 2 | `bd-aula-modelo-er`, `bd-aula-exercicios-er` | |
| `bd-04-er-estendido` | Só na ementa e nos livros | | `bd-nota-er-estendido` |
| `bd-05-mapeamento-er-relacional` | Slides BD, aula 3 | `bd-aula-mapeamento-er-relacional`, `bd-aula-exercicio-streaming` | |
| `bd-06-algebra-relacional` | Slides BD, aula 4 | `bd-aula-algebra-selecao-projecao`, `bd-aula-algebra-conjuntos`, `bd-aula-exercicios-algebra-selecao`, `bd-aula-exercicios-algebra-projecao`, `bd-aula-exercicios-algebra-renomear` | `bd-nota-juncao-divisao` |
| `bd-07-dependencia-normalizacao` | Slides BD, aula 5 | `bd-aula-dependencia-funcional`, `bd-aula-formas-normais`, `bd-aula-exercicios-normalizacao` | `bd-nota-bcnf` |
| `bd-08-sql-ddl-dml` | Slides BD2, aulas 1-2 | `bd2-aula-sql-revisao-dml` | `bd-nota-ddl-restricoes` |
| `bd-09-consultas-agregacao` | Slides BD2 | `bd2-aula-agregacao-like`, `bd2-aula-group-by-having`, `bd2-aula-case` | |
| `bd-10-juncoes-uniao` | Slides BD2, JOIN/HAVING | `bd2-aula-joins-inner-left`, `bd2-aula-joins-right-full-cross`, `bd2-aula-union` | |
| `bd-11-subconsultas` | Slides BD, aula 8, e BD2 | `bd-aula-subconsultas`, `bd2-aula-exists-any-all` | |
| `bd-12-visoes-procedures-triggers` | Slides BD2, PROCEDURE e AB2 | `bd2-aula-visoes`, `bd2-aula-triggers`, `bd2-aula-procedures` | |
| `bd-13-indices-acesso` | Só na ementa | | `bd-nota-indices` |
| `bd-14-transacoes-concorrencia-recuperacao` | Só na ementa | | `bd-nota-transacoes` |
| `bd-15-avancados` | Só na ementa (segurança e estudos de caso) | | |

**Lacunas.** Os assuntos `bd-04`, `bd-13` e `bd-14` só têm notas da equipe, e elas ficam fora da busca até alguém da equipe revisá-las. `bd-15` não tem bloco. Faltam as aulas 6 e 7 dos slides de BD; o arquivo vai da 5 para a 8. Todos os tópicos que os slides confirmam têm bloco na busca, e `tests_acervo/test_disciplina_bd.py` confere isso.

## 3. Erros encontrados nos slides

Os blocos corrigem esses pontos na seção "Correções da equipe", sem repetir a forma errada. O teste confere que as formas erradas não aparecem nos blocos.

| Bloco | Problema no slide | Correção no acervo |
|---|---|---|
| `bd-aula-modelos-arquitetura` | Atributos chamados de tuplas | Tupla = linha; atributo = coluna |
| `bd-aula-algebra-selecao-projecao` | Índice de π com predicado; renomear com os nomes antigos em ρ | π recebe lista de atributos; nomes novos em ρ |
| `bd-aula-algebra-conjuntos` | Nome da relação intermediária com erro; falta a compatibilidade da união | DEP5; compatibilidade na definição |
| `bd-aula-dependencia-funcional`, `bd-aula-formas-normais` | Seta das DFs trocada por outro caractere (fonte do PDF); regra da chave simples incompleta | A → B; a regra vale quando todas as chaves candidatas são simples |
| `bd-aula-subconsultas` | ORDER BY proibido na subconsulta; BETWEEN sem subconsulta; nome da coluna de nota diferente | Ambos funcionam no SQLite e no PostgreSQL; `nota_total` |
| `bd2-aula-sql-revisao-dml` | `INSERT` sem parênteses em VALUES; "maior ou igual" invertido | `VALUES (...)`; `>=` |
| `bd2-aula-agregacao-like` | Modelos de BETWEEN e NOT IN repetem os de COUNT e MAX | Forma certa no bloco |
| `bd2-aula-joins-inner-left`, `bd2-aula-joins-right-full-cross` | OUTER antes de LEFT/FULL; RIGHT com letras trocadas; RIGHT descrito como preservando a esquerda; CROSS JOIN com 9 linhas em vez de 12; nome de coluna diferente | `LEFT OUTER JOIN`, `FULL OUTER JOIN`; RIGHT preserva a direita; 12 linhas; `CodCargo` |
| `bd2-aula-union` | Nome da tabela de fornecedores com uma letra a menos | `Suppliers` |
| `bd2-aula-group-by-having` | Agrupa pelo sobrenome; homônimos se somam | Agrupar pela chave |
| `bd2-aula-exists-any-all` | Explicação errada de ALL | Compara com todos os valores da subconsulta |
| `bd2-aula-visoes` | Colchetes (SQL Server) com `CREATE OR REPLACE VIEW` | Nome sem espaço e o comando do SGBD |
| `bd2-aula-triggers` | REPLACE como evento; BEFORE sem a última letra | Eventos INSERT, UPDATE, DELETE; `BEFORE` |
| `bd2-aula-procedures` | `GO` tratado como SQL; procedures de mesmo nome recriadas | `GO` é separador de lotes; `CREATE OR ALTER` ou `DROP` antes |
| `bd-aula-conceitos-sgbd` | Duas comparações ligadas por "ou" | `AND` |

## 4. Dialetos

- **SQLite 3**: o padrão dos blocos e da ferramenta indicada pela disciplina. Ele aceita `RIGHT JOIN` e `FULL JOIN` desde a versão 3.39.
- **PostgreSQL** (`-- dialeto: postgresql`): usado em `ANY`/`ALL`, que o SQLite não tem. O ambiente de testes não tem PostgreSQL, então esses trechos rodam no DuckDB, e o teste confere que o SQLite os rejeita.
- **MySQL** (`DELIMITER`, trigger dos slides) e **T-SQL** (procedures): mostrados para o aluno reconhecer a sintaxe da aula, mas não são executados. O teste confere que o SQLite os rejeita e que o bloco está marcado como `verificacao: parcial`.
- **Reescrita de `> ALL` com `MAX`**: as duas formas dão o mesmo resultado só quando a subconsulta tem linhas e nenhum NULL. Com a subconsulta vazia, `> ALL` é verdadeiro para todas as linhas (5 linhas no DuckDB), e `> (SELECT MAX ...)` não retorna nenhuma (0 linhas no SQLite). O bloco `bd2-aula-exists-any-all` registra essa ressalva.
- **Notação ER**: Chen nos slides. Pé de galinha e UML aparecem em outras fontes, e `rigor.md` pede que a IA diga qual notação está usando.

## 5. Dados pessoais e material excluídos

Ficaram fora do repositório:

- os PDFs e as imagens dos slides (o `sha256` de cada um está em `fontes.json`, no campo `arquivo_local`);
- os e-mails das professoras;
- o link do grupo de Telegram;
- as datas de prova de 2023.

O teste confere que nada disso aparece nos blocos.

## 6. Fontes

| Id | Uso | Dialeto / notação | SQL roda no SQLite | Licença |
|---|---|---|---|---|
| `ufal-bd-slides` | acervo | SQL genérico; ER de Chen | sim, com as correções | não declarada |
| `ufal-bd2-slides` | acervo | misto (SQL Server, MySQL, T-SQL) | em parte | não declarada |
| `sqlite-docs` | citada | SQLite 3 | sim | domínio público |
| `postgresql-docs` | citada | PostgreSQL | nem sempre | PostgreSQL License |
| `watt-dbdesign` | citada | Chen e pé de galinha | — | CC BY 4.0 |
| `relax` | citada | álgebra relacional | — | MIT |
| `ufal-ppc-ecomp-2014` | referência | — | — | documento institucional |
| `db4s` | referência | SQLite 3 | sim | MPL-2.0 / GPL-3.0 |
| `cmu-15445` | referência | — | — | não encontrada |
| `w3schools-sql` | referência | SQL Server, MySQL ou Access | em parte | todos os direitos reservados |
| `devmedia-sql` | referência | — | — | todos os direitos reservados |
| `livros-bd` | referência | — | — | todos os direitos reservados |

## 7. Respostas da IA com o modelo real (18/11/2026)

As 10 perguntas de BD de `eval/bateria_tutor.py` foram feitas ao Gemini com `TUTORON_LIBERAR_EM_VALIDACAO=bd`. Os modelos 3.8 e 3.7 deram erro 503, então as respostas vieram dos modelos da cadeia de fallback: 3.6, 3.5 e 3.1-flash-lite. O SQL das respostas foi rodado nos bancos de teste.

| Caso | Resultado |
|---|---|
| LEFT vs INNER JOIN | Correto. A consulta dá TADEU com cargo NULL, como no bloco `bd2-aula-joins-inner-left` |
| WHERE vs HAVING | Correto |
| Mapeamento N:M | Correto |
| 2FN/3FN | Correto, e guia o aluno até a conclusão |
| σ/π em SQL | Correto: σ vira `WHERE` e π vira `SELECT DISTINCT` |
| `NOT IN` com NULL | Correto: explica a lógica de três valores e indica `NOT EXISTS` |
| `ALL` no SQLite | Correto: diz que o SQLite não tem `ALL` e dá `MAX`/`MIN` e `NOT EXISTS`. **Lacuna:** não avisa que a troca por `MAX` falha com a subconsulta vazia (seção 4) |
| Procedure no SQLite | Correto: diz que o SQLite não tem procedures e dá alternativas (consulta parametrizada, visão, trigger) |
| "Execute meu SQL" | Recusa executar e sugere `sqlite3 :memory:` |
| Pergunta de Física | Redireciona para Física 2, sem fontes |

Nenhuma das respostas terminou com a linha "**Verificação:**" que `rigor.md` pede. Isso fica como pendência de prompt e de rigor, a acompanhar com alunos. Esses 10 casos não substituem a validação com a turma.
