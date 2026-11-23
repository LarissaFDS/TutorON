---
id: ia-representacao-de-conhecimento-e-raciocinio-base-de-conhecimento-mecanismo-de-inferencia-sintaxe-semantica
titulo: Representação de conhecimento e raciocínio (RCR): sistema baseado em conhecimento, base de conhecimento e mecanismo de inferência, sintaxe e semântica, métodos fracos e fortes
assunto: ia-03-conhecimento-e-raciocinio
tipo: material_estudo
questao: aula de Representação de Conhecimento e Raciocínio (2016) e slide 03 da UFES
resolucao: sim
fonte: Aulas de Representação de Conhecimento e Raciocínio e de Lógica Proposicional do Prof. Evandro Costa (IC-UFAL), 2013 e 2016
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufal-evandro-rcr-logica
autoria: Slides do Prof. Evandro Costa (IC-UFAL); explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), aula de Representação de Conhecimento e Raciocínio (2016) e slide 03 da UFES (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Sistema baseado em conhecimento** tem dois componentes:
- **base de conhecimento (BC):** conjunto de **sentenças** sobre um domínio, numa linguagem de representação;
- **mecanismo de inferência:** determina o que se pode concluir da BC.

**RCR** é a área da IA que estuda como representar conhecimento **simbolicamente** e manipulá-lo automaticamente. Há um compromisso entre representar de forma compreensível e raciocinar de forma eficiente. John McCarthy propôs o **Advice Taker**, que decidiria como agir raciocinando sobre uma BC explícita.

Uma **linguagem de representação** tem:
- **sintaxe:** quais configurações são sentenças;
- **semântica:** quando as sentenças são verdadeiras no mundo;
- **inferência:** procedimento que deriva sentenças novas. Deve ser **correto** (só deriva consequências lógicas) e, de preferência, **completo**.

**Operações sobre a BC:** TELL (acrescenta sentença) e ASK (pergunta se uma sentença decorre da BC).

**Métodos fracos e fortes** (slide 03 da UFES):
- **fracos:** gerais, baseados em busca heurística (Logic Theorist; General Problem Solver com análise meios-fim);
- **fortes:** usam muito conhecimento explícito de um domínio, como os sistemas especialistas;
- abordagens distribuídas e baseadas em agentes.

Formas de representação: lógica proposicional e de primeira ordem, regras de produção, redes semânticas e quadros (frames).

**Verificação:** `test_tell_ask` monta uma BC mínima com TELL e ASK e confere que só as consequências das regras são respondidas como verdadeiras.
