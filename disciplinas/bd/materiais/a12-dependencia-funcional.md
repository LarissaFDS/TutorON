---
id: bd-aula-dependencia-funcional
titulo: Aula de BD — dependência funcional, regras de inferência e fecho de atributos para achar chaves
assunto: bd-07-dependencia-normalizacao
tipo: material_estudo
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 5 "Normalização" (dependência funcional)
fontes_catalogo: ufal-bd-slides,watt-dbdesign
autoria: Profª Maria Cristina Tenório (slides, com créditos a material dos professores Tarsis Marinho e Patrick Brito), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Dependência funcional (DF) A → B numa relação R: duas tuplas com o mesmo valor de A têm sempre o mesmo valor de B. Lê-se "A determina B". Ela vem do significado dos dados, não de uma instância: uma tabela de exemplo pode mostrar que uma DF não vale, mas não prova que vale.

Regras usadas na aula (com exemplos de CPF):
- Separação (decomposição): se A → BC, então A → B e A → C. CPF → nome, endereço dá CPF → nome.
- Acumulação (aumento): se A → B, então AC → B. CPF → endereço dá CPF, idade → endereço.
- Transitividade: se A → B e B → C, então A → C. CPF → código_cidade e código_cidade → nome_cidade dão CPF → nome_cidade.
- União: se A → B e A → C, então A → BC.

Fecho de atributos X⁺: tudo o que X determina. Comece com X e, enquanto houver uma DF Y → Z com Y contido no conjunto, acrescente Z. Se X⁺ contém todos os atributos de R, X é superchave; se nenhum subconjunto próprio de X também é, X é chave candidata.

Exemplo (Produto da aula de 2FN): atributos cod_cliente, cod_produto, nome_produto, preco, quantidade, com cod_produto → nome_produto, preco e cod_cliente, cod_produto → quantidade.
- {cod_produto}⁺ = {cod_produto, nome_produto, preco}: não é chave (falta cod_cliente e quantidade).
- {cod_cliente, cod_produto}⁺ = todos os atributos: é superchave, e nem cod_cliente nem cod_produto sozinhos determinam tudo, logo é chave candidata.

Atributo primário é o que pertence a alguma chave candidata; os outros são não primários. As formas normais (1FN, 2FN, 3FN) são definidas a partir dessas DFs e chaves.

Correções da equipe
- Nos slides de DF, a seta das dependências aparece como um caractere trocado (problema de fonte do PDF). Toda DF se escreve com seta: A → B.
