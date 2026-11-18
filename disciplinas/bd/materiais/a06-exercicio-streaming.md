---
id: bd-aula-exercicio-streaming
titulo: Exercício de BD — mapear para tabelas o ER do serviço de streaming (usuário, vídeo, ator, mensalidade)
assunto: bd-05-mapeamento-er-relacional
tipo: exercicio_resolvido
resolucao: sim
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 3 "Modelo Lógico", exercício (requisitos e diagrama ER)
fontes_catalogo: ufal-bd-slides,sqlite-docs
autoria: Profª Maria Cristina Tenório (enunciado e diagrama); resolução da equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Status da resolução: pendente de confirmação do professor (resolução da equipe TutorON; os slides não trazem gabarito).

Diagrama: USUÁRIO (CPF e e-mail sublinhados, senha, nome, telefone, endereço, cartão); VIDEO (título sublinhado, ano, duração, tipo, temporada, episódio, produtora); ATOR (nome sublinhado, data e local de nascimento); entidade fraca MENSALIDADE (chave parcial mês/ano, valor pago) ligada a USUÁRIO por "paga" 1:N; "avalia" N:M com atributo avaliação (nota de 0 a 10); "atua em" N:M; autorrelacionamento "segue" 1:1 em VIDEO (anterior e próximo episódio).

Mapeamento:
- Entidade forte vira tabela. USUÁRIO tem duas chaves candidatas: uma vira PK e a outra fica UNIQUE NOT NULL.
- Entidade fraca: PK = PK do dono + chave parcial.
- N:M vira tabela com as duas FKs como PK; o atributo do relacionamento vai junto.
- 1:1 recursivo vira FK para a própria tabela, com UNIQUE.

```sql
CREATE TABLE usuario (cpf CHAR(11) PRIMARY KEY, email TEXT NOT NULL UNIQUE, senha TEXT NOT NULL, nome TEXT,
                      telefone TEXT, endereco TEXT, cartao TEXT);
CREATE TABLE video (titulo TEXT PRIMARY KEY, ano INTEGER, duracao INTEGER, tipo TEXT, temporada INTEGER,
                    episodio INTEGER, produtora TEXT, proximo TEXT UNIQUE REFERENCES video (titulo));
CREATE TABLE ator (nome TEXT PRIMARY KEY, data_nasc DATE, local_nasc TEXT);
CREATE TABLE mensalidade (cpf CHAR(11) NOT NULL REFERENCES usuario (cpf), mes_ano CHAR(7) NOT NULL,
                          valor_pago NUMERIC, PRIMARY KEY (cpf, mes_ano));
CREATE TABLE avalia (cpf CHAR(11) REFERENCES usuario (cpf), titulo TEXT REFERENCES video (titulo),
                     nota INTEGER NOT NULL CHECK (nota BETWEEN 0 AND 10), PRIMARY KEY (cpf, titulo));
CREATE TABLE atua (nome TEXT REFERENCES ator (nome), titulo TEXT REFERENCES video (titulo),
                   PRIMARY KEY (nome, titulo));
```

A PK de `avalia` garante uma nota por usuário e vídeo. A mensalidade pendente (requisito 2) não está no diagrama; seria mais uma coluna em `mensalidade`.

Observação da equipe: título e nome como chave impedem vídeos com o mesmo título e atores homônimos; um código (id) evitaria isso.
