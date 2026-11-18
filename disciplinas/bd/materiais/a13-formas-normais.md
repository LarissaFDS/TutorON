---
id: bd-aula-formas-normais
titulo: Aula de BD — normalização: primeira, segunda e terceira formas normais (1FN, 2FN, 3FN) com exemplos
assunto: bd-07-dependencia-normalizacao
tipo: material_estudo
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 5 "Normalização" (1FN, 2FN, 3FN)
fontes_catalogo: ufal-bd-slides,watt-dbdesign
autoria: Profª Maria Cristina Tenório (slides, com créditos a material dos professores Tarsis Marinho e Patrick Brito), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Normalização (Codd, 1972) depura o projeto: reduz redundância e anomalias de inserção, atualização e exclusão, decompondo relações a partir das dependências funcionais.

**1FN**: todos os atributos são atômicos; sem atributos multivalorados, compostos ou grupos de repetição. Correção: o grupo repetido vai para uma nova relação com a chave da original. Exemplo da aula: cliente com vários endereços de entrega vira cliente_nome(nro_cli, nome) e cliente_entrega(nro_cli, rua, numero), com chave {nro_cli, rua, numero} na segunda. Outro caso dos slides: livro com colunas Autor1, Autor2, Autor3 também viola a ideia (grupo de repetição em colunas) e vira uma relação livro_autor.

**2FN**: está na 1FN e todo atributo não primário depende totalmente de cada chave candidata (nenhum depende só de parte de uma chave composta). Exemplo: Produto(cod_cliente, cod_produto, nome_produto, preco, quantidade) com cod_produto → nome_produto, preco é dependência parcial. Decomposição: Produto(cod_produto, nome_produto, preco) e Compra(cod_cliente, cod_produto, quantidade). Se todas as chaves candidatas são simples, não há dependência parcial e a relação na 1FN já está na 2FN; uma chave primária simples sozinha não basta, se houver outra chave candidata composta.

**3FN**: está na 2FN e nenhum atributo não primário depende transitivamente de uma chave (X → Z → Y, com Z que não é superchave). Exemplo: Carro(placa, modelo, km_rodados, cod_fabricante, nome_fabricante), chave {placa, modelo}, com cod_fabricante → nome_fabricante. Decomposição: Carro(placa, modelo, km_rodados, cod_fabricante) e Fabricante(cod_fabricante, nome_fabricante).

Para saber em que forma normal uma tabela está: liste as DFs, ache as chaves candidatas pelo fecho de atributos e teste a primeira, a segunda e a terceira forma normal nessa ordem.

Em cada decomposição, o atributo em comum (cod_produto, cod_fabricante) é chave de uma das partes; assim a junção natural devolve a relação original sem tuplas espúrias.

Correções da equipe
- Nos slides, a seta das DFs aparece trocada por outro caractere; aqui está escrita como →.
- A regra "chave simples, então está na 2FN" vale quando todas as chaves candidatas são simples.
