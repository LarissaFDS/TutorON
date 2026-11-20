---
id: eletronica-anot-modelo-re
titulo: Modelo re de pequenos sinais do TBJ em emissor comum com polarização fixa: re = 26 mV/IE, Zi = RB ∥ βre, Zo = RC ∥ ro, Av = −(RC ∥ ro)/re; exemplo 470 kΩ, 3 kΩ, β = 100
assunto: eletronica-08-pequenos-sinais
tipo: resolucao
resolucao: sim
fonte: Anotações "Transistor TBJ" (8 nov. 2026), p. 1–3 (exemplo de slide de aula, parafraseado)
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

**Passos:** (1) análise CC para achar $I_E$; (2) análise CA: fontes CC viram curto (o $V_{CC}$ vai ao terra), capacitores de acoplamento e de desvio viram curto; (3) troque o transistor pelo modelo $r_e$: entre base e emissor, $\beta r_e$; entre coletor e emissor, a fonte de corrente $\beta I_b$ em paralelo com $r_o$.

$r_e = \frac{26\ \mathrm{mV}}{I_E}$; $Z_i = R_B \parallel \beta r_e$; $Z_o = R_C \parallel r_o$; $A_v = \frac{v_o}{v_i} = -\frac{R_C \parallel r_o}{r_e}$ (sinal negativo: o emissor comum inverte a fase).

**Exemplo:** $V_{CC} = 12$ V, $R_B = 470$ kΩ, $R_C = 3$ kΩ, $\beta = 100$.
- CC: $I_B = 11{,}3/470\mathrm{k} = 24{,}04\ \mu$A; $I_E = 101\cdot I_B = 2{,}428$ mA.
- (a) $r_e = 10{,}71\ \Omega$; (b) $Z_i = 470\mathrm{k} \parallel 1{,}071\mathrm{k} = 1{,}07$ kΩ.
- (c) com $r_o \to \infty$: $Z_o = R_C = 3$ kΩ; (d) $A_v = -3000/10{,}71 = -280$.
- (e) com $r_o = 50$ kΩ: $Z_o = 2{,}83$ kΩ e $A_v = -264$.

**Correção:** a anotação escreve $r_e \approx V_A/I_{CQ}$ (com a tensão de Early $V_A$). Essa fórmula é de $r_o$, a resistência de saída: $r_o \approx V_A/I_{CQ}$. Ela também escreve $A_v = -Z_o/r_o$; o certo é dividir por $r_e$.

**Verificação:** a análise nodal (SymPy) do modelo $\beta r_e$ com $\beta I_b$ e $r_o$ dá $A_v = -264{,}3$ e $Z_o = 2{,}83$ kΩ.
