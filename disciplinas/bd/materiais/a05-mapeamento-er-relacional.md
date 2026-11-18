---
id: bd-aula-mapeamento-er-relacional
titulo: Aula de BD — modelo lógico: mapeamento do ER para tabelas (entidade, 1:1, 1:N, N:M), chave primária e estrangeira
assunto: bd-05-mapeamento-er-relacional
tipo: material_estudo
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 3 "Modelo Lógico", parte 1
fontes_catalogo: ufal-bd-slides,sqlite-docs
autoria: Profª Maria Cristina Tenório (slides, com créditos a material dos professores Tarsis Marinho e Patrick Brito), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Projeto em três etapas: conceitual (ER), lógico (tabelas do SGBD de destino) e físico (desempenho). O esquema relacional lista as relações (tabelas), os atributos (colunas) e as restrições de integridade.

Chave primária (PK): coluna ou combinação de colunas que distingue cada linha. Chave estrangeira (FK): coluna cujos valores precisam aparecer na chave primária de outra tabela; é assim que o relacionamento vira tabela.

Como mapear o modelo ER para tabelas (clínica veterinária):
1. Entidade vira tabela, atributo vira coluna, identificador vira PK.
2. N:M vira uma tabela própria com as PKs dos dois lados como FK (Consulta liga Veterinário e Animal).
3. 1:N: a PK do lado 1 vai como FK para o lado N (Animal recebe o CPF do Cliente dono).
4. 1:1: as duas entidades podem virar uma tabela só (Conferência com os dados da comissão organizadora) ou uma recebe a FK da outra com UNIQUE.

```sql
CREATE TABLE Veterinario (CRMV INTEGER PRIMARY KEY, nome TEXT NOT NULL, data_adm DATE, salario NUMERIC);
CREATE TABLE Cliente (CPF CHAR(11) PRIMARY KEY, nome TEXT NOT NULL, tel TEXT);
CREATE TABLE Animal (codigo INTEGER PRIMARY KEY, nome TEXT, ano INTEGER, raca TEXT,
                     CPF CHAR(11) NOT NULL REFERENCES Cliente (CPF));
CREATE TABLE Consulta (ID INTEGER PRIMARY KEY, CRMV INTEGER NOT NULL REFERENCES Veterinario (CRMV),
                       codigo INTEGER NOT NULL REFERENCES Animal (codigo), data DATE, hora TIME, motivo TEXT);
INSERT INTO Veterinario VALUES (1, 'Rosa', '2020-01-10', 5000);
INSERT INTO Cliente VALUES ('12345678901', 'Téo', '82 9999-0000');
INSERT INTO Animal VALUES (7, 'Bolinha', 2019, 'vira-lata', '12345678901');
INSERT INTO Consulta VALUES (1, 1, 7, '2024-05-02', '10:00', 'vacina');
SELECT v.nome, a.nome, c.nome FROM Consulta k
JOIN Veterinario v ON v.CRMV = k.CRMV JOIN Animal a ON a.codigo = k.codigo JOIN Cliente c ON c.CPF = a.CPF;
```

Resultado:

| veterinário | animal | dono |
|---|---|---|
| Rosa | Bolinha | Téo |

No SQLite a FK só é conferida depois de `PRAGMA foreign_keys = ON;`.

Correções da equipe
- O slide de esquema relacional chama os atributos de tuplas, entre parênteses "colunas". Tupla é a linha; atributo é a coluna.
