---
id: pcom-anot-dsb-sc
titulo: DSB-SC (banda lateral dupla com portadora suprimida): s(t) = Ac m(t) cos(2π fc t), S(f) = (Ac/2)[M(f − fc) + M(f + fc)], sem portadora no espectro
assunto: pcom-02-am-dsb
tipo: material_estudo
resolucao: sim
fonte: Anotações "Modulação AM" (25 ago. 2026), p. 1–2
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

**DSB-SC** (double sideband suppressed carrier): $s(t) = A_c\,m(t)\cos(2\pi f_c t)$, ou seja, $s(t) = m(t)c(t)$. No domínio da frequência:
$$S(f) = \frac{A_c}{2}[M(f - f_c) + M(f + f_c)]$$ (o espectro da mensagem deslocado para $\pm f_c$, com fator $A_c/2$). As duas bandas laterais (inferior, abaixo de $f_c$; superior, acima) carregam a mesma informação. Largura de banda: $B_T = 2W$, se a mensagem vai até $W$ Hz.

**Exemplo:** $m(t) = \cos(2\pi\,2t)$ e $c(t) = \cos(2\pi\,10t)$ (Hz) dão
$$s(t) = \frac{1}{2}\cos(2\pi\,12t) + \frac{1}{2}\cos(2\pi\,8t),$$ com quatro linhas simétricas, em $\pm 8$ Hz e $\pm 12$ Hz, cada uma de peso 1/4. O espectro da mensagem tem linhas em $\pm 2$ Hz de peso 1/2.

**Para recuperar $m(t)$ (demodulação coerente):** multiplique $s(t)$ pela portadora local $\cos(2\pi f_c t)$, obtendo $\tfrac{1}{2}m(t) + \tfrac{1}{2}m(t)\cos(4\pi f_c t)$, e passe por um **filtro passa-baixas**, não por um filtro em torno de $f_c$. O corte fica entre a banda da mensagem e a cópia em $2f_c$: $W \le f_{corte} \le 2f_c - W$.

Correção: a anotação desenha também uma linha da portadora em $\pm 10$ Hz ("carrier"). Em DSB-SC a portadora é **suprimida**: não há linha em $f_c$. Ela aparece no AM convencional.

**Verificação:** FFT de $s(t)$ em 1 s: picos de 0,25 em 8 e 12 Hz e nada (menos de $10^{-12}$) em 10 Hz.
