---
id: circ-davi-amp-op-ideal-inversor
titulo: Amplificador operacional ideal: hipóteses, ganho do inversor, somador e não inversor
assunto: circ-06-amp-op
tipo: material_estudo
resolucao: nao
fonte: Slides do Prof. Davi, aula 5 (amplificadores operacionais)
autoria: Prof. Davi Bibiano Brito (IC/UFAL), material de aula e provas de Circuitos Elétricos (2017); resolução da equipe TutorON, conferida por código
licenca: Não declarada (slides e provas do professor; fotos de resoluções sem identificação de aluno); arquivos fora do repositório
publicacao_transcricao: não declarada: conteúdo parafraseado, sem copiar slides, enunciados ou fotos; nomes e e-mails omitidos; confirmação da equipe pendente
fontes_catalogo: ufal-circ-davi-2017
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Material do Prof. Davi (IC/UFAL), parafraseado; resolução da equipe TutorON conferida por código, não é gabarito oficial. Status da resolução: validada.

Qual o ganho de um amplificador inversor? Primeiro, as **hipóteses do amp-op ideal**, que valem com realimentação negativa (resistor da saída para a entrada inversora) e saída dentro da alimentação ($-V_{CC} < v_o < V_{CC}$):
- correntes nas entradas nulas: $i_p = i_n = 0$;
- tensões nas entradas iguais: $v_p = v_n$ (ganho de malha aberta infinito, o "curto virtual").

**Inversor.** Entrada $v_s$ por $R_s$ até a entrada inversora, $R_f$ da saída para a mesma entrada, entrada não inversora no terra. Como $v_n = v_p = 0$, a LKC no nó inversor dá $\dfrac{v_s}{R_s} + \dfrac{v_o}{R_f} = 0$, então
$$v_o = -\frac{R_f}{R_s}\,v_s .$$
O ganho é $-R_f/R_s$; o sinal menos é a inversão. Vale enquanto $|v_o| < V_{CC}$; além disso a saída satura.

**Somador inversor.** Entradas $v_a, v_b, v_c$ por $R_a, R_b, R_c$ no mesmo nó: $v_o = -\left(\dfrac{R_f}{R_a}v_a + \dfrac{R_f}{R_b}v_b + \dfrac{R_f}{R_c}v_c\right)$. Com $R_a = R_b = R_c = 3R_f$, a saída é menos a média das três entradas.

**Não inversor.** Entrada na entrada não inversora, $R_s$ da inversora para o terra e $R_f$ da saída para ela: $v_o = \left(1 + \dfrac{R_f}{R_s}\right)v_g$.

**Diferença.** Com $R_a/R_b = R_c/R_d$: $v_o = \dfrac{R_b}{R_a}(v_b - v_a)$.

No modelo realista, a resistência de entrada é finita, a de saída não é nula e o ganho $A$ é finito; o ideal é o limite $A \to \infty$.

**Verificação:** no inversor com $R_s = 1$ kΩ, $R_f = 4$ kΩ e $v_s = 0{,}5$ V, $v_o = -2$ V; os $0{,}5$ mA que entram por $R_s$ saem por $R_f$ (LKC no nó inversor, com $i_n = 0$).
