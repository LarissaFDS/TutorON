---
id: compevol-algoritmo-genetico-otimizacao-maximo-global-x-sen-10-pi-x
titulo: O que são algoritmos genéticos; otimização, espaço de busca, função de aptidão, máximos locais e global; achar o máximo de f(x) = x sen(10πx) + 1 em [−1, 2]
assunto: compevol-01-fundamentos
tipo: exercicio_resolvido
questao: Problema 3.1 de Lacerda e Carvalho; apostila de Lucas, cap. 1-2
resolucao: sim
fonte: Apostilas e textos da pasta da turma (Lucas, UFRGS 2002; Lacerda e Carvalho; Dianati, Song e Treiber)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: lacerda-carvalho-ag,lucas-apostila-ag
autoria: Exercício clássico dos textos da pasta da turma; resolução da equipe TutorON
licenca: Textos sem licença aberta declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Problema 3.1 de Lacerda e Carvalho; apostila de Lucas, cap. 1-2 (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Algoritmo genético (AG):** método de **busca e otimização** inspirado na evolução (Holland, 1975; popularizado por Goldberg, 1989). Mantém uma **população** de soluções candidatas (**indivíduos**, codificados em **cromossomos**), avalia cada uma por uma **função de aptidão** e gera novas soluções por **seleção**, **cruzamento** e **mutação**: os mais aptos têm mais chance de se reproduzir.

**Vocabulário de otimização:**
- **espaço de busca:** todas as soluções possíveis;
- **função objetivo** (ou de aptidão): dá uma nota a cada solução; otimizar é achar o ponto de **máximo** (ou mínimo);
- **máximo local:** maior que os vizinhos, mas não o maior de todos; **máximo global:** o maior valor no domínio inteiro.

**Exemplo clássico:** maximizar
$$f(x) = x\,\text{sen}(10\pi x) + 1, \quad -1 \le x \le 2$$
Em palavras: $x$ vezes o seno de $10\pi x$, mais um. A função oscila com período $0{,}2$ e amplitude que cresce com $|x|$: há **dezenas de máximos locais**. Um método de subida que parte de um ponto qualquer para no pico mais próximo; o AG explora vários pontos ao mesmo tempo e combina os bons.

**Resposta:** o máximo global fica perto de $x \approx 1{,}8505$, com $f \approx 2{,}8503$. Perto de $x = 1{,}65$ há um máximo local com $f \approx 2{,}65$, armadilha comum.

**Características dos AGs:** trabalham com uma **codificação** dos parâmetros, não com eles; buscam a partir de uma **população**, não de um ponto; usam só a **aptidão** (não precisam de derivadas nem de continuidade); usam regras de transição **probabilísticas**. Não garantem o ótimo: dão boas soluções em tempo razoável.

**Verificação:** `test_maximo_de_x_sen` varre $[-1, 2]$ com passo $10^{-6}$ e confere o máximo $2{,}8503$ em $x \approx 1{,}8505$, além de contar mais de 10 máximos locais.
