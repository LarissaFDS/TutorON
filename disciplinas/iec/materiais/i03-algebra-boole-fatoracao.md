---
id: iec-algebra-boole-fatoracao
titulo: Álgebra de Boole: propriedades, De Morgan e simplificação por fatoração
assunto: iec-07-portas-boole
tipo: material_estudo
resolucao: sim
fonte: Slides Álgebra de Boole e Simplificação de Circuitos Lógicos, Prof. José Augusto Baranauskas (FFCLRP-USP), slides 7 a 20
fontes_catalogo: usp-baranauskas-boole
autoria: Prof. José Augusto Baranauskas (USP), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

Propriedades (cada uma se confere pela tabela-verdade): identidade $A+0=A$, $A\cdot1=A$; nulo $A+1=1$, $A\cdot0=0$; idempotência $A+A=A$; complemento $A+\overline{A}=1$, $A\cdot\overline{A}=0$; distributivas $A(B+C)=AB+AC$ e $A+BC=(A+B)(A+C)$; absorção $A+AB=A$ e $A(A+B)=A$; $A+\overline{A}B=A+B$; De Morgan $\overline{AB}=\overline{A}+\overline{B}$ e $\overline{A+B}=\overline{A}\,\overline{B}$ (vale para $n$ variáveis).

**Exemplos de fatoração dos slides:**
1. $S=\overline{A}\,\overline{B}\,\overline{C}+\overline{A}B\overline{C}+A\overline{B}C$: dos dois primeiros, $\overline{A}\,\overline{C}(\overline{B}+B)=\overline{A}\,\overline{C}$; logo $S=\overline{A}\,\overline{C}+A\overline{B}C$.
2. $S=\overline{A}\,\overline{B}+\overline{A}B=\overline{A}(\overline{B}+B)=\overline{A}$.
3. $S=\overline{A}\,\overline{B}\,\overline{C}+\overline{A}BC+\overline{A}B\overline{C}+A\overline{B}\,\overline{C}+AB\overline{C}$: ponha $\overline{C}$ em evidência: $\overline{C}(\overline{A}\,\overline{B}+\overline{A}B+A\overline{B}+AB)=\overline{C}$; sobra $\overline{A}BC+\overline{C}=\overline{A}B+\overline{C}$ (por $X+\overline{X}Y=X+Y$).
4. $S=(A+B+C)(\overline{A}+\overline{B}+C)$: distribuindo e cortando $A\overline{A}=0$ e $B\overline{B}=0$, os termos com $C$ somam $C$; resta $S=A\overline{B}+\overline{A}B+C$.
5. $ABC+A\overline{C}+A\overline{B}=A$ (a soma cobre todas as combinações de $B$ e $C$ com $A=1$).

**Verificação:** cada resultado foi comparado com a expressão original nas 8 linhas da tabela-verdade (força bruta em Python): todas iguais.
