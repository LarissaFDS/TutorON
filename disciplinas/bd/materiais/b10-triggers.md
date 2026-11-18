---
id: bd2-aula-triggers
titulo: Aula de BD2 — triggers (gatilhos): BEFORE e AFTER, INSERT, UPDATE e DELETE, OLD e NEW, no SQLite e no MySQL
assunto: bd-12-visoes-procedures-triggers
tipo: material_estudo
fonte: Slides de Bancos de Dados 2 (UFAL, Profª Cristina Tenório), avaliação AB2 "Triggers"
fontes_catalogo: ufal-bd2-slides,sqlite-docs
banco_teste: loja
autoria: Profª Cristina Tenório (slides), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
revisao_humana: pendente
---
Trigger (gatilho) é uma rotina guardada no banco e disparada automaticamente por um evento numa tabela: ninguém a chama. Define-se o momento (BEFORE ou AFTER), o evento (INSERT, UPDATE ou DELETE), a tabela e o corpo. `FOR EACH ROW` roda o corpo uma vez por linha afetada. No corpo, OLD é a linha antes e NEW a linha depois: INSERT só tem NEW, DELETE só tem OLD e UPDATE tem os dois.

Exemplo da aula: ao excluir um produto, apagar antes os itens de pedido dele. Versão SQLite (roda como está):

```sql
CREATE TRIGGER exclusao_de_produto
BEFORE DELETE ON produto
FOR EACH ROW
BEGIN
    DELETE FROM item_pedido WHERE id_produto = OLD.id_produto;
END;
DELETE FROM produto WHERE id_produto = 1;
SELECT COUNT(*) FROM item_pedido;
```

Resultado (havia 7 itens; os 2 do produto 1 saíram junto):

| COUNT(*) |
|---|
| 5 |

A mesma trigger no MySQL, onde o cliente de linha de comando precisa trocar o delimitador para o `;` do corpo não encerrar o comando:

```sql
-- dialeto: mysql
DELIMITER //
CREATE TRIGGER exclusao_de_produto BEFORE DELETE ON produto
FOR EACH ROW
BEGIN
    DELETE FROM item_pedido WHERE id_produto = OLD.id_produto;
END //
DELIMITER ;
```

O trecho MySQL não foi executado (não há MySQL no ambiente de testes do TutorON).

Para apagar em cascata, a alternativa declarativa é a chave estrangeira com `ON DELETE CASCADE`. No SQLite as chaves estrangeiras só valem com `PRAGMA foreign_keys = ON;`.

Correções da equipe
- O slide lista REPLACE entre os eventos de trigger. Os eventos são INSERT, UPDATE e DELETE; no MySQL, um REPLACE dispara as triggers de DELETE e INSERT (ou de INSERT), não um evento próprio. A nota sobre OLD e NEW também cita REPLACE pelo mesmo motivo.
- O momento "antes" está escrito sem a última letra no slide; a palavra-chave é BEFORE.
