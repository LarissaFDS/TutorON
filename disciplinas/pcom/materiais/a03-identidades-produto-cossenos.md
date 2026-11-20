---
id: pcom-anot-identidades-produto-cossenos
titulo: Identidades trigonométricas da modulação: cos A cos B = ½[cos(A+B) + cos(A−B)], cos²A = (1 + cos 2A)/2; produto gera soma e diferença de frequências
assunto: pcom-01-sinais-espectro
tipo: material_estudo
resolucao: sim
fonte: Anotações "fórmulas fundamentais para a prova 1" (7 set. 2026), p. 1 e 3; Anotações "Revisão prova 1" (30 ago. 2026), p. 3; Anotações "Revisão Final prova 1" (9 set. 2026), p. 3 e 8
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Princípios de Comunicação 2026.2; docente Jobson de Araújo Nascimento, conforme os cabeçalhos das simulações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de listas e de provas parafraseados; fotos de slide, capturas de tela e figuras coladas não foram copiadas
fontes_catalogo: ufal-pcom-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

Multiplicar senoides (o que um modulador ou demodulador faz) cria a **soma e a diferença** das frequências:
$$\cos A\cos B = \frac{1}{2}[\cos(A + B) + \cos(A - B)]$$ (cosseno de A vezes cosseno de B é meio da soma dos cossenos da soma e da diferença) e
$$\cos^2 A = \frac{1 + \cos 2A}{2}.$$

**Exemplo (Revisão Final):** $2\cos(1000\pi t)\cos(5000\pi t) = \cos(6000\pi t) + \cos(4000\pi t) = \cos(2\pi\,3000t) + \cos(2\pi\,2000t)$: componentes em 3 kHz e 2 kHz, cada uma com peso 1/2 no espectro em Hz.

**Uso em demodulação:** $2\cos^2(\omega_c t) = 1 + \cos(2\omega_c t)$, por isso multiplicar de novo pela portadora devolve a mensagem em banda básica mais uma cópia em $2f_c$.

Correção: na Revisão prova 1 a identidade aparece escrita como $\frac{1}{2}[\cos(a + b) - \cos(a - b)]$; o sinal certo é **mais**. O desenvolvimento seguinte já usa o sinal certo, e o resultado (19 W) não muda.

**Verificação:** as duas identidades foram conferidas simbolicamente (SymPy) e o exemplo numericamente em 1000 instantes.
