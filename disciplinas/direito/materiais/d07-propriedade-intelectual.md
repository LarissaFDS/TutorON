---
id: direito-propriedade-intelectual-software-registro-inpi-hash-codigo-fonte-direito-autoral-patente-marca-trade-dress
titulo: Propriedade intelectual em computação: programa de computador (Lei 9.609/1998, registro no INPI com resumo hash do código-fonte), direito autoral, patente, marca, trade dress (conjunto-imagem) e concorrência desleal
assunto: dir-03-direito-civil-e-digital
tipo: prova
questao: Avaliação de 2020.2, questões sobre registro de software e trade dress
resolucao: sim
fonte: Avaliações de Noções de Direito da Profa. Jessica Hind (IC-UFAL), 2020.2 (setembro e outubro de 2021), e slides "Noções Iniciais" da disciplina
curso: Ciência da Computação (UFAL), COMP387 Noções de Direito (7º período); turma 2020.2 (aulas em 2021)
fontes_catalogo: ufal-direito-avaliacoes,lei-software-planalto
autoria: Questões da Profa. Jessica Hind (IC-UFAL); explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Noções de Direito (IC-UFAL, 2020.2), Avaliação de 2020.2, questões sobre registro de software e trade dress (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Conteúdo de estudo, não é aconselhamento jurídico.

**Programa de computador** (Lei 9.609/1998): protegido pelo regime do **direito autoral**, com regras próprias. A proteção **não depende de registro**. O registro no **INPI** é opcional e serve como prova de autoria e data.

No registro, o código-fonte não é entregue aberto. O titular gera um **resumo digital (hash)** do arquivo com o código e informa só esse resumo, guardando o original. Se houver disputa, o arquivo guardado é comparado com o hash registrado: qualquer alteração muda o resumo. Por isso, na avaliação, o hash é requisito do registro de **software** (programa de computador).

**Não confunda:**
- **direito autoral:** obras (textos, músicas, software). Nasce com a criação;
- **patente** (Lei 9.279/1996): invenção ou modelo de utilidade. Exige registro, novidade e aplicação industrial. Programa de computador "em si" não é patenteável no Brasil;
- **marca:** sinal que identifica produto ou serviço, registrado no INPI;
- **trade dress** (conjunto-imagem): cores, letras, forma e apresentação que identificam visualmente um produto. Exemplo da avaliação: embalagens parecidas de amido de milho de marcas diferentes.

O trade dress **não tem registro próprio** no Brasil. É protegido sobretudo pela repressão à **concorrência desleal**, e às vezes pelo registro de marca mista ou tridimensional. O gabarito da avaliação o relacionou à **marca**. Mostre as duas leituras.

**Verificação:** `test_hash_do_codigo_fonte` gera o SHA-256 de um código-fonte de exemplo e mostra que alterar um caractere muda o resumo (a ideia do registro no INPI).
