---
id: bd-aula-modelo-er
titulo: Aula de BD — modelo entidade-relacionamento: entidades, atributos, chaves, relacionamentos e cardinalidade
assunto: bd-03-modelo-er
tipo: material_estudo
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 2 "Modelagem Conceitual", parte 1
fontes_catalogo: ufal-bd-slides,watt-dbdesign
autoria: Profª Maria Cristina Tenório (slides, com créditos a material dos professores Tarsis Marinho e Patrick Brito), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
revisao_humana: pendente
---
O modelo entidade-relacionamento (MER, de Peter Chen) descreve o minimundo como entidades e relacionamentos entre elas. O diagrama (DER) é o esquema conceitual: diz quais dados serão guardados, não como.

- Entidade: objeto do mundo real distinguível dos outros (um cliente). Conjunto de entidades: entidades do mesmo tipo (todos os clientes). Conjuntos não precisam ser disjuntos: uma pessoa pode ser funcionário e cliente.
- Atributo: propriedade da entidade. Tipos: simples ou composto (endereço = rua, número, cidade), monovalorado ou multivalorado (vários telefones), e complexo (composto e multivalorado). Atributo derivado é calculado de outro (idade a partir da data de nascimento).
- Atributo chave (identificador): valor único que identifica cada entidade.
- Relacionamento: associação entre entidades (cliente faz compra).

Cardinalidade (razão de mapeamento) diz a quantas entidades de B uma entidade de A pode se associar:
- 1:1 — A se associa a no máximo uma B, e B a no máximo uma A;
- 1:N — A se associa a várias B; cada B a no máximo uma A;
- N:1 — o inverso;
- N:M — cada A a várias B e cada B a várias A.
A participação é total quando toda entidade precisa participar (todo pedido tem um cliente) e parcial quando não precisa.

Dicas para ler um enunciado: substantivo costuma indicar entidade, verbo indica relacionamento e adjetivo indica atributo. É só uma pista: "endereço" é substantivo e normalmente é atributo.

Notação: os slides usam a notação de Chen (retângulo para entidade, losango para relacionamento, elipse para atributo). Livros e ferramentas também usam a notação pé de galinha; a cardinalidade é a mesma, só o desenho muda.
