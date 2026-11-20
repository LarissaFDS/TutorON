---
id: eletronica-anot-realimentacao-coletor
titulo: TBJ com realimentação de coletor (RF do coletor à base): IB = (VCC − VBE)/(RF + (β+1)(RC + RE)); exemplo com 10 V, 250 kΩ, 4,7 kΩ, 1,2 kΩ e β = 90
assunto: eletronica-07-tbj-polarizacao
tipo: resolucao
resolucao: sim
fonte: Anotações "Exercício parte 2" (22 out. 2026), p. 5–6 (exemplo deixado em "continuar")
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Eletrônica 2026.2, IC/UFAL; docente indicado no cabeçalho: Prof. João Raphael Souza Martins); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de slides parafraseados; fotos de quadro, de slides e figuras de livro não foram copiadas
fontes_catalogo: ufal-eletronica-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Circuito:** $R_C$ do $V_{CC}$ ao coletor; $R_F$ do coletor à base (realimentação); $R_E$ do emissor ao terra. Por $R_C$ passa $I_C' = I_C + I_B = I_E$.

**Malha $V_{CC}$ → $R_C$ → $R_F$ → base → emissor → $R_E$:**
$-V_{CC} + R_C I_E + R_F I_B + V_{BE} + R_E I_E = 0$, com $I_E = (\beta + 1)I_B$:
$$I_B = \frac{V_{CC} - V_{BE}}{R_F + (\beta + 1)(R_C + R_E)}$$
**Malha do coletor:** $V_{CE} = V_{CC} - (R_C + R_E)I_E$.

**Exemplo (terminado pela equipe):** $V_{CC} = 10$ V, $R_F = 250$ kΩ, $R_C = 4{,}7$ kΩ, $R_E = 1{,}2$ kΩ, $\beta = 90$:
$I_B = \frac{9{,}3}{250\mathrm{k} + 91\cdot5{,}9\mathrm{k}} = 11{,}82\ \mu$A; $I_C = 1{,}064$ mA; $V_{CE} = 10 - 5{,}9\mathrm{k}\cdot1{,}076\mathrm{m} = 3{,}65$ V.

**Correção:** na malha do coletor, a anotação usa $I_C$ em $R_C$ e $R_E$, chegando a $V_{CE} = V_{CC} - (R_C + R_E)I_C$ (3,72 V). Isso é aproximação ($I_E \approx I_C$). Pelos dois resistores passa $I_E$; a diferença aqui é 0,07 V. O exemplo ficou sem conta nas anotações ("continuar") e foi completado pela equipe.

**Verificação:** a LKT na malha da base fecha com $10 - 4{,}7\cdot1{,}076 - 250\cdot0{,}01182 - 0{,}7 - 1{,}2\cdot1{,}076 \approx 0$; $V_{CE} = 3{,}65$ V $> 0{,}2$ V: região ativa.
