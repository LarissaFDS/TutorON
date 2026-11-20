---
id: pcom-anot-am-potencia-eficiencia
titulo: Potência do AM: Pt = Pc + PLSB + PUSB = (A²/2)(1 + μ²/2); eficiência μ²/(2 + μ²); DSB-SC gasta potência só nas bandas laterais
assunto: pcom-02-am-dsb
tipo: material_estudo
resolucao: sim
fonte: Anotações "fórmulas fundamentais para a prova 1" (7 set. 2026), p. 2–3; Anotações "Simulação Modulação AM" (30 ago. 2026), p. 8–10
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

Potência média de uma senoide de amplitude $a$ numa carga de 1 Ω: $a^2/2$ (numa carga $R$: $a^2/(2R)$). Cada componente do AM soma a sua:
$$P_T = P_c + P_{LSB} + P_{USB} = \frac{A^2}{2} + 2\cdot\frac{(A\mu/2)^2}{2} = \frac{A^2}{2}\left(1 + \frac{\mu^2}{2}\right).$$ A **eficiência** (fração da potência que está nas bandas laterais, onde está a informação) é $\eta = \frac{\mu^2}{2 + \mu^2}$; no máximo 1/3, com $\mu = 1$.

**Simulação:** com $K = 1$ ($s = [1 + \cos\omega_m t]\cos\omega_c t$, $\mu = 1$): $P_c = \frac{1}{2R}$, $P_{USB} = P_{LSB} = \frac{(1/2)^2}{2R} = \frac{1}{8R}$, total $\frac{3}{4R}$. Com $K = 0$ (DSB-SC): só as bandas, $\frac{1}{8R} + \frac{1}{8R} = \frac{1}{4R}$. O DSB-SC é mais eficiente em potência; o AM gasta $\frac{1}{2R}$ na portadora, que não leva informação, em troca de um receptor simples (detector de envoltória). Somar a portadora não muda a largura de banda.

**Verificação:** a média de $s^2(t)$ simulada em muitos períodos dá 0,750 (com $K = 1$) e 0,250 (com $K = 0$), para $R = 1$.
