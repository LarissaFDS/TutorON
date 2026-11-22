---
id: circ-davi-nodal-thevenin-reav-q4-q5
titulo: Análise nodal, potência fornecida por cada fonte, Thévenin e máxima transferência no mesmo circuito
assunto: circ-05-maxima-transferencia
tipo: material_estudo
resolucao: sim
fonte: Reavaliação AB1 do Prof. Davi, questões 4 e 5, resolvidas no quadro e no caderno
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

**Circuito (paráfrase).** Nó 1 no + de uma fonte de $12$ V (– na referência). Do nó 1 saem uma fonte de $2$ mA para o nó 2 e um resistor de $2$ kΩ para o nó 3. Entre os nós 2 e 3, $1$ kΩ. Do nó 2 à referência, $2$ kΩ com $i_o$ para baixo. Uma fonte de $4$ mA empurra corrente da referência para o nó 3.

**Q4, nodal.** LKC no nó 2: $\dfrac{v_2}{2\text{k}} + \dfrac{v_2 - v_3}{1\text{k}} = 2$ mA, logo $3v_2 - 2v_3 = 4$. No nó 3: $\dfrac{v_3 - v_2}{1\text{k}} + \dfrac{v_3 - 12}{2\text{k}} = 4$ mA, logo $3v_3 - 2v_2 = 20$. Daí $v_2 = 10{,}4$ V, $v_3 = 13{,}6$ V e $i_o = 5{,}2$ mA.

Como encontrar a potência fornecida por uma fonte com análise nodal? Com as tensões de nó, ache a corrente da fonte pela LKC e use $p = vi$. Pelo + da fonte de $12$ V saem $2$ mA para a fonte de corrente e chegam $0{,}8$ mA pelo resistor de $2$ kΩ; ela entrega $1{,}2$ mA e **fornece** $14{,}4$ mW. A de $4$ mA fornece $13{,}6 \cdot 4 = 54{,}4$ mW; a de $2$ mA, com $1{,}6$ V entre seus terminais, **absorve** $3{,}2$ mW.

**Q5, Thévenin e máxima transferência**, vistos pelo resistor de $2$ kΩ do nó 2: $V_{Th} = 26$ V e $R_{Th} = 3$ kΩ (fontes desligadas: $2$ k e $1$ k em série). Com $R_L = R_{Th}$, $P_{max} = \dfrac{V_{Th}^2}{4R_{Th}} = \dfrac{26^2}{12\text{ k}} \approx 56{,}3$ mW.

**Correções:** a foto da Q5 traz o resultado em "milivolts"; potência se mede em **watts** ($56{,}3$ mW). Na Q4, um passo anota $v_2 = 10{,}9$ V, mas a conta segue com o valor certo, $10{,}4$ V.

**Verificação:** $i_o = 26/(3\text{k} + 2\text{k}) = 5{,}2$ mA, igual à nodal. Balanço em mW: $-14{,}4 + 3{,}2 - 54{,}4 + 1{,}28 + 10{,}24 + 54{,}08 = 0$.
