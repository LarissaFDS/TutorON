---
id: circ-davi-maxima-transferencia-ab1-q5
titulo: Máxima transferência de potência: conta de P máxima conferida (prova AB1)
assunto: circ-05-maxima-transferencia
tipo: material_estudo
resolucao: sim
fonte: Prova AB1 do Prof. Davi (2017), questão 5, e resolução fotografada
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

**Problema (paráfrase).** Escolher a resistência de carga que recebe a maior potência de um circuito e dizer quanto ela recebe.

**Receita.** (1) Tire a carga e ache $V_{Th}$ em aberto entre os terminais; (2) desligue as fontes independentes (tensão vira curto, corrente vira aberto) e ache $R_{Th}$, ou use fonte de teste se houver fonte dependente; (3) a carga ótima é $R_L = R_{Th}$; (4)
$$P_{max} = \frac{V_{Th}^2}{4R_{Th}} .$$
Isso vale para uma carga ajustável com o resto do circuito fixo. Na condição ótima, metade da potência do equivalente de Thévenin fica na carga.

**Resolução da prova.** A resolução fotografada acha $R_{Th} = 2{,}5$ kΩ e $V_{Th} = 8$ V. Então $R_L = 2{,}5$ kΩ e
$$P_{max} = \frac{8^2}{4\cdot 2500} = 6{,}4\ \text{mW}.$$

**Correções:** a foto escreve $P_{max} = 6{,}391$ mW, que não fecha com os próprios valores dela; $8^2/10\,000 = 6{,}4\times10^{-3}$ W exatamente. O circuito da questão não foi remontado nesta versão, só a conta final.

**Verificação:** com $R_L = 2{,}5$ kΩ, a corrente é $8/5000 = 1{,}6$ mA e $P = R_L i^2 = 2500 \cdot (1{,}6\times10^{-3})^2 = 6{,}4$ mW.
