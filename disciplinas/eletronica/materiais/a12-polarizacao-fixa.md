---
id: eletronica-anot-polarizacao-fixa
titulo: TBJ com polarização fixa (VCC 12 V, RB 240 kΩ, RC 2,2 kΩ): IB, IC = βIB e VCE para β = 50 e 100; como saber se o transistor está saturado (IC de saturação)
assunto: eletronica-07-tbj-polarizacao
tipo: resolucao
resolucao: sim
fonte: Anotações "Transistores - circuitos de polarização fixa" (9 out. 2026), p. 1–4, e "Circuitos de Polarização de Transistores" (23 out. 2026), item a (exercício de livro, parafraseado)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Eletrônica 2026.2, IC/UFAL; docente indicado no cabeçalho: Prof. João Raphael Souza Martins); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de slides parafraseados; fotos de quadro, de slides e figuras de livro não foram copiadas
fontes_catalogo: ufal-eletronica-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Análise CC:** os capacitores de acoplamento viram circuitos abertos e somem.

**Malha base-emissor:** $12 = 240\mathrm{k}\,I_B + V_{BE}$, silício $V_{BE} = 0{,}7$ V → $I_B = \frac{12 - 0{,}7}{240\ \mathrm{k\Omega}} = 47{,}08\ \mu$A.
**Malha coletor-emissor:** $V_{CE} = 12 - 2{,}2\mathrm{k}\,I_C$. Na região ativa, $I_C = \beta I_B$ e $I_E = I_C + I_B = (\beta + 1)I_B$.

| $\beta$ | $I_C$ | $V_{CE}$ |
|---|---|---|
| 50 | 2,354 mA | 6,82 V |
| 100 | 4,708 mA | 1,64 V |

Ao dobrar $\beta$, $I_C$ dobra (+100%) e $V_{CE}$ cai 5,18 V (−76%): a polarização fixa depende muito de $\beta$.

**Como saber se o transistor está saturado:** a região ativa vale só se $V_{CE}$ fica acima de $V_{CE,sat} \approx 0{,}2$ V. Equivalente: $\beta I_B$ menor que a corrente de saturação $I_{C,sat} = V_{CC}/R_C = 12/2{,}2\mathrm{k} = 5{,}45$ mA (supondo $V_{CE} \approx 0$). Aqui 4,708 mA < 5,45 mA: ativo. Com $\beta = 120$ daria 5,65 mA > 5,45 mA e $V_{CE}$ negativo, o que é impossível: o transistor satura, $I_C \approx 5{,}45$ mA, e $\beta$ não vale mais ($I_C < \beta I_B$). Na saturação não use $I_C = \beta I_B$.

**Verificação:** para $\beta = 100$, LKT na malha do coletor $12 - 2{,}2\cdot4{,}708 - 1{,}642 = 0$; $V_{CE} = 1{,}64 > 0{,}2$ V e a junção base-coletor reversa ($V_{BC} = 0{,}7 - 1{,}64 < 0$) confirmam a região ativa.
