---
id: circ-davi-divisores-wheatstone
titulo: Divisor de tensão, divisor de corrente, ponte de Wheatstone e transformação Δ-Y
assunto: circ-01-grandezas-potencia
tipo: material_estudo
resolucao: nao
fonte: Slides do Prof. Davi, aula 3 (associação de resistores)
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

Como montar um divisor de corrente? Ligue resistores **em paralelo** a uma fonte de corrente $i_s$: todos ficam com a mesma tensão $v = i_s R_{eq}$, e cada ramo leva $i_k = v/R_k$. Para dois resistores:
$$i_1 = \frac{R_2}{R_1 + R_2}\,i_s,\qquad i_2 = \frac{R_1}{R_1 + R_2}\,i_s .$$
A corrente maior passa pelo resistor **menor** (no numerador vai a resistência do outro ramo). Com condutâncias, $i_k = \dfrac{G_k}{\sum G}\,i_s$.

**Divisor de tensão.** Resistores **em série** com uma fonte $v_s$ têm a mesma corrente, e $v_k = \dfrac{R_k}{\sum R}\,v_s$. Uma carga ligada na saída muda o divisor: ela fica em paralelo com o resistor de baixo.

**Ponte de Wheatstone.** Dois divisores na mesma fonte ($R_1$ com $R_2$; $R_3$ com $R_x$). A ponte está **equilibrada** quando o detector entre os pontos médios marca zero, o que exige $R_1 R_x = R_2 R_3$, isto é, $R_x = \dfrac{R_2}{R_1}R_3$. Equilibrada, o ramo do detector não leva corrente e pode ser tirado sem mudar o resto.

**Δ para Y.** Cada resistor do Y é o produto dos dois lados do Δ que tocam aquele vértice, dividido pela soma dos três: $R_1 = \dfrac{R_b R_c}{R_a + R_b + R_c}$. De Y para Δ: $R_a = \dfrac{R_1R_2 + R_2R_3 + R_3R_1}{R_1}$, com o resistor do Y oposto no denominador. Com tudo igual, $R_Y = R_\Delta/3$.

**Verificação:** $i_s = 6$ mA em $R_1 = 1$ kΩ e $R_2 = 2$ kΩ dá $i_1 = 4$ mA e $i_2 = 2$ mA; as duas tensões valem $4$ V e as correntes somam $6$ mA (LKC). Um Δ de três resistores de $9$ Ω vira um Y de três de $3$ Ω.
