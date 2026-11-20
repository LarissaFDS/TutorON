---
id: ingles-voz-passiva
titulo: Voz passiva em textos técnicos — como reconhecer verbo to be + particípio passado (is used, was hypothesized, can be transmitted, is being abandoned) e o agente com by
assunto: ingles-07-tempos-verbais-voz-passiva
tipo: material_estudo
resolucao: sim
fonte: Texto da prova de proficiência em leitura de Inglês Instrumental (trecho de Pavela, 2016) e Wilson et al., Best Practices for Scientific Computing (PLOS Biology, 2014), exercício de voz passiva
autoria: Textos: Roman Pavela (2016) e Greg Wilson e coautores (2014), citados em trechos curtos; exercício e explicações da equipe TutorON
licenca: Pavela 2016: CC BY-NC 4.0; Wilson et al. 2014: CC BY 4.0 (trechos com atribuição); exercício: texto próprio da equipe
publicacao_transcricao: só trechos curtos, com atribuição; os textos integrais ficam fora do repositório
fontes_catalogo: ufal-ingles-texto-prova,pavela-2016-pps,wilson-2014-best-practices
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exercício da equipe TutorON. As formas passivas citadas foram conferidas no texto em `tests_acervo/test_disciplina_ingles.py`.

**Como reconhecer:** voz passiva = forma do verbo **to be** (is, are, was, were, be, been, being) + **particípio passado** (verbo regular em -ed, ou irregular: *built*, *done*, *known*). O sujeito **sofre** a ação; quem faz (o agente), quando aparece, vem com **by**. Textos científicos usam muito a passiva porque o foco está no processo, não em quem fez. O tempo da passiva está no verbo *to be*.

No texto da prova:
- *“they are used to eliminate damage”* — presente simples: são usados.
- *“90% of the mortality rate attributed to malaria is experienced by infants and young children”* — presente, com agente (*by infants*): é sofrida por bebês e crianças.
- *“a significant association of malaria incidence with all cancer mortality in 50 U.S. states was highlighted”* — passado: foi destacada.
- *“it was hypothesized that”* — passado, sujeito formal *it*: levantou-se a hipótese de que.
- *“can be transmitted through the bites of Aedes aegypti”* — modal + be + particípio: pode ser transmitido.
- *“their use is being gradually abandoned”* — presente contínuo da passiva (*is being* + particípio): está sendo abandonado aos poucos.
- *“the world population is expected to grow”* — espera-se que a população cresça.

Em computação (Wilson et al., 2014): *“Automated output and intermediate files can be regenerated as needed.”* — arquivos gerados podem ser regenerados quando preciso.

Cuidado: nem todo *be* + palavra em -ed é passiva. *“is very important”* tem adjetivo, não particípio; *“has increased”* é present perfect ativo (*have* + particípio, sem *to be*).

Tradução: use "ser + particípio" (foi destacada) ou a forma com "se" (destacou-se, espera-se).

**Verificação:** cada trecho citado contém uma forma de *to be* seguida (com no máximo um advérbio entre eles) de um particípio, e está no texto indicado (conferido por script).
