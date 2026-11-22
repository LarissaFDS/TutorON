---
id: circ-davi-amp-op-media-ab2-q1
titulo: Amp-op em cascata: somador inversor que tira a média de três sensores e inversor que ajusta o ganho
assunto: circ-06-amp-op
tipo: material_estudo
resolucao: sim
fonte: Prova AB2 do Prof. Davi (2017), questão 1, e resolução fotografada
autoria: Prof. Davi Bibiano Brito (IC/UFAL), material de aula e provas de Circuitos Elétricos (2017); resolução da equipe TutorON, conferida por código
licenca: Não declarada (slides e provas do professor; fotos de resoluções sem identificação de aluno); arquivos fora do repositório
publicacao_transcricao: não declarada: conteúdo parafraseado, sem copiar slides, enunciados ou fotos; nomes e e-mails omitidos; confirmação da equipe pendente
fontes_catalogo: ufal-circ-davi-2017
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Material do Prof. Davi (IC/UFAL), parafraseado; resolução da equipe TutorON conferida por código, não é gabarito oficial. Status da resolução: corrigida.

**Problema (paráfrase).** Três termômetros dão 0 V a 0 °C e sobem $25$ mV por °C. Um somador inversor ($R_1, R_2, R_3$ nas entradas, $R_f$ na realimentação, saída $v_x$) seguido de um inversor ($R_A$ na entrada, $R_B$ na realimentação, saída $v_o$) deve dar $v_o$ positivo, com $1$ V para cada $10$ °C de temperatura **média**.

**Resolução.** Com amp-ops ideais (curto virtual, correntes de entrada nulas):
$$v_x = -R_f\left(\frac{v_1}{R_1} + \frac{v_2}{R_2} + \frac{v_3}{R_3}\right),\qquad v_o = -\frac{R_B}{R_A}v_x .$$
Escolhendo $R_1 = R_2 = R_3 = 3R_f$: $v_x = -\dfrac{v_1+v_2+v_3}{3}$ e $v_o = \dfrac{R_B}{R_A}\cdot\dfrac{v_1+v_2+v_3}{3}$, positivo como pedido.

Subir $10$ °C na média sobe a média das tensões em $0{,}25$ V. Para $\Delta v_o = 1$ V: $\dfrac{R_B}{R_A} = \dfrac{1}{0{,}25} = 4$. Com $R_f = R_A = 1$ kΩ: $R_1 = R_2 = R_3 = 3$ kΩ e $R_B = 4$ kΩ.

**Correções:** a resolução fotografada chega ao ganho 4, mas depois escreve $R_B/R_A = 12$, como se só um termômetro variasse e o fator $1/3$ entrasse de novo. Com $R_B = 12$ kΩ a saída daria $3$ V a cada $10$ °C.

**Verificação:** com os três sensores a $40$ °C ($1$ V cada), $v_x = -1$ V e $v_o = 4$ V, ou seja, $1$ V por $10$ °C. Para não saturar, a alimentação precisa passar de $17$ V (saída a $170$ °C).
