---
id: iec-formas-canonicas
titulo: Da tabela-verdade à expressão: mintermos (soma de produtos) e maxtermos (produto de somas)
assunto: iec-07-portas-boole
tipo: material_estudo
resolucao: sim
fonte: Slides Álgebra de Boole e Simplificação de Circuitos Lógicos, Prof. José Augusto Baranauskas (FFCLRP-USP), slides 21 a 27
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

Toda função tem duas formas padronizadas, lidas direto da tabela-verdade:
- **Mintermo** (forma normal disjuntiva, soma de produtos): para cada linha com $S=1$, um produto com todas as variáveis; variável que vale 0 entra barrada. Escreve-se $S=\sum m(\dots)$.
- **Maxtermo** (forma normal conjuntiva, produto de somas): para cada linha com $S=0$, uma soma com todas as variáveis; variável que vale **1** entra barrada. Escreve-se $S=\prod M(\dots)$.

Exemplo (NAND de duas entradas, também nas notas de Grace Deaecto): $S=1$ nas linhas 0, 1 e 2.
- Mintermos: $S=\overline{A}\,\overline{B}+\overline{A}B+A\overline{B}$.
- Maxtermo (linha 3, $A=B=1$): $S=\overline{A}+\overline{B}$.
- Simplificando a primeira: $\overline{A}(\overline{B}+B)+A\overline{B}=\overline{A}+A\overline{B}=\overline{A}+\overline{B}$, a mesma função.

Método para montar o circuito de qualquer função (Tanenbaum): escreva a tabela-verdade; gere o complemento de cada entrada com inversores; uma porta AND por linha com $S=1$; uma porta OR juntando as saídas das ANDs. Depois simplifique (álgebra ou Karnaugh) para gastar menos portas.

**Verificação:** as duas formas valem 1 exatamente nas linhas 0, 1 e 2 e 0 na linha 3.
