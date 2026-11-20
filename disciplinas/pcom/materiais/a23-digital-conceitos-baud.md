---
id: pcom-anot-digital-conceitos-baud
titulo: Modulação digital ASK, FSK, PSK e QAM; M = 2^k símbolos; taxa de modulação em bauds e taxa de transmissão em bit/s, VT = Vm·k; ciclos da portadora por símbolo
assunto: pcom-06-modulacao-digital
tipo: material_estudo
resolucao: sim
fonte: Anotações "Modulação Digital" (23 set. 2026), p. 1–4
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Princípios de Comunicação 2026.2; docente Jobson de Araújo Nascimento, conforme os cabeçalhos das simulações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de listas e de provas parafraseados; fotos de slide, capturas de tela e figuras coladas não foram copiadas
fontes_catalogo: ufal-pcom-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

Na modulação digital a portadora $c(t) = A_0\cos(2\pi f_c t + \phi_c)$ muda entre valores fixos, um por **símbolo**:
- **ASK** (chaveamento de amplitude): muda a amplitude. BASK/OOK: $s(t) = A\,b(t)\cos(2\pi f_c t)$, com $b(t) \in \{0, 1\}$; pode ser unipolar ou bipolar.
- **FSK:** muda a frequência. **PSK:** muda a fase (BPSK: 0° e 180°). **QAM:** muda amplitude e fase (duas portadoras em quadratura).

**Bits e símbolos:** com $k$ bits por símbolo há $M = 2^k$ símbolos (2 bits: 00, 01, 10, 11, quatro símbolos; 3 bits, oito).

**Taxas:**
- taxa de modulação $V_m$, em **bauds** (símbolos por segundo);
- taxa de transmissão $V_T$, em **bit/s**: $V_T = V_m\cdot k = V_m\log_2 M$;
- se cada símbolo dura $n$ ciclos da portadora: $V_m = f_p/n$.

Baud e bit/s só coincidem com 1 bit por símbolo; confundir as duas é o erro mais comum.

**Verificação:** 16-QAM a 50 kbauds dá $50\cdot\log_2 16 = 200$ kbit/s; portadora de 2,4 kHz com 2 ciclos por símbolo dá 1,2 kbaud.
