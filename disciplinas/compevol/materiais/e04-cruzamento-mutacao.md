---
id: compevol-cruzamento-um-ponto-dois-pontos-uniforme-mutacao-bit-taxa
titulo: Operadores de cruzamento (um ponto, dois pontos, uniforme, aritmético) e de mutação (inversão de bit, gaussiana); taxas de cruzamento e de mutação; exemplo 00110011 × 10110000
assunto: compevol-02-operadores
tipo: exercicio_resolvido
questao: Dianati, Song e Treiber, fig. 5; apostila de Lucas, seções 4.4-4.5
resolucao: sim
fonte: Apostilas e textos da pasta da turma (Lucas, UFRGS 2002; Lacerda e Carvalho; Dianati, Song e Treiber)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: dianati-gaes,lucas-apostila-ag
autoria: Exercício clássico dos textos da pasta da turma; resolução da equipe TutorON
licenca: Textos sem licença aberta declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Dianati, Song e Treiber, fig. 5; apostila de Lucas, seções 4.4-4.5 (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Cruzamento** (recombinação): combina partes de dois pais. Aplica-se a cada par com probabilidade $p_c$ (tipicamente 0,6 a 0,9); senão os filhos são cópias.
- **um ponto:** sorteia-se um corte e trocam-se as caudas.
  Exemplo: pais `00110011` e `10110000`, corte depois do 1º bit: filhos `10110011` e `00110000` (só o primeiro bit mudou de dono);
- **dois pontos:** troca-se o trecho entre dois cortes;
- **uniforme:** para cada gene, sorteia-se de qual pai vem (máscara aleatória);
- **aritmético** (representação real): $c_1 = a\,p_1 + (1 - a)\,p_2$ e $c_2 = (1 - a)\,p_1 + a\,p_2$, com $a \in [0, 1]$.

**Mutação:** altera genes ao acaso, mantendo **diversidade** e permitindo chegar a qualquer ponto do espaço:
- binária: cada bit é invertido com probabilidade $p_m$ (pequena, como $1/L$ ou 0,001 a 0,01);
- real: soma-se ruído gaussiano $N(0, \sigma^2)$ ao gene;
- permutação: troca de duas posições.

**Papéis:** o cruzamento **explora combinando** blocos bons já existentes; a mutação **introduz material novo**. Sem mutação, um bit perdido por toda a população não volta; com mutação alta demais, o AG vira busca aleatória.

**Taxas:** com $L$ bits e $p_m$ por bit, o número esperado de bits mutados por indivíduo é $L \cdot p_m$. Com $L = 22$ e $p_m = 0{,}01$: 0,22 bit por indivíduo, e a chance de nenhum bit mudar é $0{,}99^{22} \approx 0{,}80$.

**Verificação:** `test_cruzamento_e_mutacao` refaz o exemplo de um ponto, confere que o uniforme só copia genes dos pais, que o aritmético fica entre os pais, e mede com semente fixa a média de bits mutados ($\approx 0{,}22$) e a fração sem mutação ($\approx 0{,}80$).
