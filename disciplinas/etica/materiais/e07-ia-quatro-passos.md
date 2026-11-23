---
id: etica-estudo-de-caso-inteligencia-artificial-tecnica-dos-4-passos-codigo-de-etica-ieee-vies-algoritmico
titulo: Estudo de caso de inteligência artificial e ética resolvido pela técnica dos 4 passos (reunir os dados relevantes, analisar os dados, negociar um acordo, avaliar as alternativas) com o código de ética do IEEE; viés algorítmico e decisões automatizadas
assunto: etica-03-etica-profissional-e-lgpd
tipo: exercicio
questao: Avaliação Final, questão 2
resolucao: sim
fonte: Reavaliações da AB1 e da AB2 (turmas X e M) e Avaliação Final de Computação, Sociedade e Ética do IC-UFAL, 2020.2 (entregas em maio e junho de 2021)
curso: Ciência da Computação (UFAL), COMP361 Computação, Sociedade e Ética; turmas X e M, semestre 2020.2 (aulas em 2021)
fontes_catalogo: ufal-etica-avaliacoes,ieee-codigo-etica,lgpd-planalto
autoria: Enunciados das avaliações da disciplina (IC-UFAL; professor não identificado nos arquivos); orientação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Computação, Sociedade e Ética (IC-UFAL, 2020.2), Avaliação Final, questão 2 (parafraseado). Status da resolução: validada. A orientação é da equipe TutorON e não é gabarito do professor.

As avaliações são **trabalhos escritos avaliados**: aqui vão o método, um roteiro e pontos de discussão, não o texto pronto.

**Técnica dos 4 passos** (como no enunciado):
1. **Reunir os dados relevantes:** fatos do caso, **partes interessadas** (quem decide, quem é afetado, quem desenvolve) e o que cada uma quer.
2. **Analisar os dados:** quais **valores e deveres** estão em conflito (justiça, privacidade, segurança, transparência, lucro) e quais itens do **código de ética do IEEE** se aplicam. Cite pelo texto oficial, sem inventar numeração.
3. **Negociar um acordo:** buscar uma solução que as partes possam aceitar. O que cada uma cede, e que salvaguardas a tornam aceitável?
4. **Avaliar as alternativas:** liste 2 ou 3 caminhos (por exemplo, lançar, adiar e corrigir, não lançar), com consequências para cada parte e coerência com o código. Escolha e justifique.

**Exemplo parecido** (escolha o seu caso): uma empresa usa um modelo de IA para triar currículos. O modelo aprendeu com contratações antigas e passa a rebaixar candidatas mulheres.
- **Dados:** empresa, candidatos, equipe de dados, histórico enviesado.
- **Análise:** é um caso de **viés algorítmico**. Há conflito entre eficiência e **não discriminação**. O código do IEEE pede tratar as pessoas com justiça e não discriminar, e priorizar o bem-estar do público. A LGPD também traz o princípio da não discriminação (art. 6º, IX) e o direito a pedir revisão de decisão automatizada (art. 20).
- **Acordo:** suspender o uso automático, auditar o viés, informar os candidatos e deixar a decisão final para pessoas.
- **Alternativas:** manter, que viola o código; corrigir e auditar, que é a escolha justificada; abandonar, que tem custo alto mas é seguro.

**Divergência:** IA auditada pode ser mais consistente que humanos, mas é opaca e erra em escala.

**Verificação:** `test_quatro_passos_na_ordem` confere a ordem dos 4 passos do enunciado no bloco, e `test_lgpd_principios_e_bases` confere os incisos citados (art. 6º, IX; art. 20).
