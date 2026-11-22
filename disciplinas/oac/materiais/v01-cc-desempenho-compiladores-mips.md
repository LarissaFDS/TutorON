---
id: oac-cc-desempenho-compiladores
titulo: Desempenho com dois compiladores: CPI médio, clock equivalente e ganho de um compilador novo; por que MIPS não compara arquiteturas diferentes
assunto: oac-02-desempenho
tipo: prova
fonte: Provas de OAC do Prof. Erick de Andrade Barboza (IC-UFAL, cursos de Engenharia e Ciência da Computação) | Prova 1 de 2017.2 (Q1 e Q2)
curso: Ciência da Computação (UFAL), prova comum às turmas de Engenharia e Ciência da Computação, 2017.2
autoria: Enunciados: provas do Prof. Erick de Andrade Barboza, parafraseadas pela equipe TutorON; resolução da equipe TutorON com auxílio de IA, conferida com o gabarito do professor e por simulação
licenca: Não declarada (prova com gabarito); os PDFs não estão no repositório
publicacao_transcricao: não se aplica: o enunciado é parafraseado e só os dados foram mantidos
fontes_catalogo: ufal-cc-oac-provas-erick-2017
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões da prova 1 de 2017.2 (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com o gabarito do professor e em Python; a prova é de 2017 e usa MIPS, não RISC-V).

**Tempo = instruções × CPI × período do clock.** Com clock de 1 ns:
- Compilador A: $10^9$ instruções em 1,1 s, então $CPI_A=\dfrac{1{,}1}{10^9\cdot10^{-9}}=1{,}1$.
- Compilador B: $1{,}2\cdot10^9$ instruções em 1,5 s, então $CPI_B=\dfrac{1{,}5}{1{,}2}=1{,}25$.

**Mesmo tempo em dois processadores:** $N_A\,CPI_A/f_A=N_B\,CPI_B/f_B$ dá $f_A/f_B=\dfrac{1{,}1}{1{,}5}\approx0{,}733$: o clock do processador do código A é cerca de 27% mais lento. O gabarito anulou esse item (a pergunta dizia "mais rápido").

**Compilador novo:** $6\cdot10^8$ instruções com CPI 1,1 levam $0{,}66$ s. Em relação a A, $1{,}1/0{,}66\approx1{,}67$ (67% melhor); em relação a B, $1{,}5/0{,}66\approx2{,}27$.

**Verdadeiro ou falso da mesma prova:**
- Trocar a multiplicação da ALU por um multiplicador dedicado muda a organização, não a arquitetura: o código antigo continua rodando (V).
- Hardware dedicado para uma operação complica o datapath e simplifica a unidade de controle, não o contrário (F).
- Um processador mais rápido diminui o tempo de resposta e aumenta a vazão (throughput) (F, se disser que aumenta os dois).
- **Não** dá para comparar arquiteturas diferentes por MIPS: uma ISA pode precisar de mais instruções para o mesmo programa e ter MIPS maior sendo mais lenta (F, se disser que dá).

**Verificação:** as contas foram refeitas em Python, e o teste confere 1,1, 1,25, 0,733, 0,66, 1,67 e 2,27.
