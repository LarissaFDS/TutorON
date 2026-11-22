---
id: circ-davi-thevenin-malhas-reav-q6-q8
titulo: Thévenin com duas fontes de corrente e malhas com fonte de corrente dependente
assunto: circ-04-thevenin-norton
tipo: material_estudo
resolucao: sim
fonte: Reavaliação AB1 do Prof. Davi, questões 6 e 8, resolvidas no caderno
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

**Q6 (paráfrase).** Pede-se $I_o$ num resistor de $3$ kΩ. A equipe remontou o circuito assim: nó T no + de uma fonte de $18$ V cujo – está no nó L; $6$ kΩ de L à referência; $6$ kΩ de T ao nó N e $6$ kΩ de N à referência; uma fonte de $2$ mA tira corrente de N para a referência; dois resistores de $4$ kΩ em paralelo entre T e o nó A; uma fonte de $1$ mA empurra corrente da referência para A; a carga de $3$ kΩ vai de A à referência.

Sem a carga, $V_{Th} = 14$ V. Com as fontes desligadas, $R_{Th} = (6\text{k} \parallel 12\text{k}) + 2\text{k} = 4\text{k} + 2\text{k} = 6$ kΩ. Então $I_o = \dfrac{14}{6\text{k} + 3\text{k}} \approx 1{,}56$ mA.

**Q8 (paráfrase).** Malhas: a malha 1 tem uma fonte de $1$ mA só dela ($I_1 = 1$ mA); a malha 2 tem uma fonte de corrente dependente $V_x/4000$ ($I_2 = V_x/4\text{k}$); $V_x$ é a tensão no resistor de $3$ kΩ comum às malhas 1 e 3, $V_x = 3\text{k}(I_1 - I_3)$. LKT na malha 3, com $1$ kΩ comum à malha 2 e a saída em $3$ kΩ:
$$3\text{k}(I_3 - I_1) + 1\text{k}(I_3 - I_2) + 3\text{k}\,I_3 = 0 .$$
Substituindo $I_2 = \tfrac{3}{4}(1\text{ mA} - I_3)$: $31I_3 = 15$ mA, $I_3 = 15/31 \approx 0{,}484$ mA e $V_o = 3\text{k}\cdot I_3 \approx 1{,}45$ V.

Os dois resultados do caderno conferem com o código.

**Verificação:** na Q6, a análise nodal com a carga ligada dá $v_A = 3\text{k} \cdot I_o = 14/3$ V e a soma das potências é zero. Na Q8, $V_x = 3(1 - 15/31) = 48/31$ V e $I_2 = 12/31$ mA $= V_x/4\text{k}$.
