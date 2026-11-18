---
id: bd-aula-algebra-selecao-projecao
titulo: Aula de BD — álgebra relacional: seleção (sigma), projeção (pi) e renomear (rho), com o SQL equivalente
assunto: bd-06-algebra-relacional
tipo: material_estudo
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 4 "Álgebra Relacional", parte 1
fontes_catalogo: ufal-bd-slides,relax,sqlite-docs
banco_teste: empregado
autoria: Profª Maria Cristina Tenório (slides, com créditos a material dos professores Tarsis Marinho e Patrick Brito), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Álgebra relacional: operações sobre relações (tabelas) que produzem novas relações; é a base formal do SQL. Termos: tupla é a linha, atributo é o cabeçalho da coluna, relação é a tabela e domínio é o tipo de valor de uma coluna. Operações unárias básicas:

- Seleção (sigma, σ): filtra linhas por um predicado. $\sigma_{\text{SALARIO} > 4000}(\text{EMPREGADO})$ em SQL é `WHERE SALARIO > 4000`. O predicado usa =, ≠, <, ≤, >, ≥ com AND, OR e NOT; seleções em sequência comutam.
- Projeção (pi, π): escolhe colunas e elimina tuplas repetidas. $\pi_{\text{SEXO},\,\text{SALARIO}}(\text{EMPREGADO})$ em SQL precisa de `SELECT DISTINCT`.
- Renomear (rho, ρ): dá nome à relação e aos atributos. $\rho_{\text{FUNCIONARIO}(\text{Nome},\,\text{Sobrenome},\,\text{Remuneracao})}(\pi_{\text{PNOME},\,\text{UNOME},\,\text{SALARIO}}(\text{EMPREGADO}))$.

```sql
SELECT PNOME FROM EMPREGADO WHERE SALARIO > 4000 AND SEXO = 'F';
```

Resultado:

| PNOME |
|---|
| Maria |
| Josefa |
| Luana |

```sql
SELECT DISTINCT SEXO, SALARIO FROM EMPREGADO;
```

Resultado (quatro empregados, três tuplas, porque duas mulheres ganham 7500):

| SEXO | SALARIO |
|---|---|
| F | 7500 |
| F | 8000 |
| M | 3850 |

```sql
CREATE VIEW FUNCIONARIO (Nome, Sobrenome, Remuneracao) AS SELECT PNOME, UNOME, SALARIO FROM EMPREGADO;
SELECT Nome, Remuneracao FROM FUNCIONARIO WHERE Remuneracao < 4000;
```

Resultado:

| Nome | Remuneracao |
|---|---|
| Rafael | 3850 |

Correções da equipe
- O slide escreve a notação da projeção com um predicado; o índice de π é uma lista de atributos.
- O slide diz que a projeção resulta em "uma coluna": o resultado tem as colunas da lista.
- No exemplo de renomear, o slide põe os nomes antigos no índice de ρ; os nomes novos (e o nome FUNCIONARIO) vão em ρ, e a projeção vai dentro.
