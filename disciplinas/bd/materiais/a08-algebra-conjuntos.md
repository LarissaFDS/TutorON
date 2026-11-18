---
id: bd-aula-algebra-conjuntos
titulo: Aula de BD — álgebra relacional: união, interseção, diferença e produto cartesiano, com o SQL equivalente
assunto: bd-06-algebra-relacional
tipo: material_estudo
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 4 "Álgebra Relacional", parte 1 (operações de conjuntos)
fontes_catalogo: ufal-bd-slides,relax,sqlite-docs
autoria: Profª Maria Cristina Tenório (slides, com créditos a material dos professores Tarsis Marinho e Patrick Brito), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Operações binárias de conjuntos: união (∪, UNION), interseção (∩, INTERSECT), diferença (−, EXCEPT) e produto cartesiano (×, CROSS JOIN). União, interseção e diferença exigem relações compatíveis: mesmo número de atributos e domínios compatíveis, coluna a coluna. A união junta as tuplas das duas relações e elimina duplicatas.

Exemplo da aula: seguro social dos empregados que trabalham no departamento 5 ou que supervisionam diretamente alguém do departamento 5.

$$\text{DEP5} \leftarrow \sigma_{\text{ndepto} = 5}(\text{Empregado})$$
$$\text{R1} \leftarrow \pi_{\text{seguroSocial}}(\text{DEP5}) \qquad \text{R2} \leftarrow \pi_{\text{supervisor\_ss}}(\text{DEP5})$$
$$\text{RESULTADO} \leftarrow \text{R1} \cup \text{R2}$$

R1 e R2 têm um atributo cada, do mesmo domínio (seguro social): são compatíveis.

```sql
CREATE TABLE Empregado (seguroSocial TEXT PRIMARY KEY, pnome TEXT, supervisor_ss TEXT, ndepto INTEGER);
INSERT INTO Empregado VALUES ('111', 'Ana', NULL, 1), ('222', 'Beto', '111', 5), ('333', 'Caio', '111', 5),
                             ('444', 'Dora', '222', 4), ('555', 'Eva', '444', 5);
SELECT seguroSocial FROM Empregado WHERE ndepto = 5
UNION
SELECT supervisor_ss FROM Empregado WHERE ndepto = 5
ORDER BY 1;
```

Resultado (222, 333 e 555 são do departamento 5; 111 e 444 supervisionam alguém de lá; 111 aparece uma vez só):

| seguroSocial |
|---|
| 111 |
| 222 |
| 333 |
| 444 |
| 555 |

Trocando UNION por EXCEPT, sobram os empregados do departamento 5 que não supervisionam ninguém de lá: 222, 333 e 555 (nenhum deles é supervisor de alguém do departamento 5). UNION ALL mantém as repetições.

Correções da equipe
- A primeira relação intermediária do slide tem um erro de digitação no nome; aqui ela se chama DEP5.
- O slide não diz que a união exige relações compatíveis; essa condição é parte da definição.
