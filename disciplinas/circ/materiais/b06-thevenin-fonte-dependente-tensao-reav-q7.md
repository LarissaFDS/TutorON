---
id: circ-davi-supermalha-ccvs-reav-q7
titulo: Supermalha e Thévenin com fonte de tensão dependente (controlada por corrente)
assunto: circ-04-thevenin-norton
tipo: material_estudo
resolucao: sim
fonte: Reavaliação AB1 do Prof. Davi, questão 7, resolvida no caderno
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

Como achar o equivalente de Thévenin com uma fonte dependente de tensão? A fonte dependente **fica ligada**; ache $V_{Th}$ em aberto e $R_{Th}$ com fonte de teste, ou por $V_{oc}/I_{cc}$.

**Circuito (paráfrase).** Nó a no + de uma fonte de $6$ V; $6$ kΩ de a até b; $2$ kΩ de b à referência, com $I_x$ para baixo. Fonte de tensão dependente $2000\,I_x$ entre b e c, com + em c. Uma fonte de $3$ mA empurra corrente da referência para c. De c, $4$ kΩ até d, e a saída $V_o$ é a tensão num resistor de $4$ kΩ de d à referência.

**Malhas.** Malha 1: $8\text{k}I_1 - 2\text{k}I_2 = 6$, com $I_x = I_1 - I_2$. A fonte de $3$ mA é comum às malhas 2 e 3: supermalha, com $I_3 = I_2 + 3$ mA. LKT na supermalha: $2\text{k}(I_2 - I_1) - 2000I_x + 8\text{k}I_3 = 0$, ou $-4I_1 + 12I_2 = -24$ (mA). Daí $I_2 = -21/11$ mA, $I_3 = 12/11$ mA e
$$V_o = 4\text{k}\cdot I_3 = \tfrac{48}{11} \approx 4{,}36\text{ V}.$$

**Thévenin visto pela saída** (cálculo da equipe): sem o resistor de saída, $V_{Th} = 12$ V; com a fonte de $6$ V em curto, a de $3$ mA aberta e uma fonte de teste em d, $R_{Th} = 7$ kΩ. Com a carga de $4$ kΩ: $12 \cdot 4/11 = 48/11$ V.

**Correções:** o caderno acha $I_2 \approx -1{,}90$ mA certo, mas escreve $I_3 = 4{,}9$ mA (somou o valor de $I_2$ sem o sinal) e chega a $V_o = 19{,}6$ V. O certo é $I_3 = 3 - 1{,}91 \approx 1{,}09$ mA. A polaridade da fonte de $6$ V foi lida da equação do caderno; a foto não deixa claro.

**Verificação:** pelo Thévenin, $V_o = V_{Th}\,\dfrac{4}{7+4} = \dfrac{48}{11}$ V, igual às malhas; o balanço de potências dá zero.
