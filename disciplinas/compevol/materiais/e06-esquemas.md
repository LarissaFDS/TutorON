---
id: compevol-teorema-dos-esquemas-ordem-comprimento-definidor-blocos-construtivos
titulo: Esquemas (schemata): ordem, comprimento definidor, teorema dos esquemas de Holland e hipótese dos blocos construtivos
assunto: compevol-01-fundamentos
tipo: exercicio_resolvido
questao: Apostila de Lucas, seção 6.1; Dianati, Song e Treiber, seção III
resolucao: sim
fonte: Apostilas e textos da pasta da turma (Lucas, UFRGS 2002; Lacerda e Carvalho; Dianati, Song e Treiber)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: lucas-apostila-ag,dianati-gaes
autoria: Exercício clássico dos textos da pasta da turma; resolução da equipe TutorON
licenca: Textos sem licença aberta declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Apostila de Lucas, seção 6.1; Dianati, Song e Treiber, seção III (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Esquema:** padrão sobre o alfabeto $\{0, 1, *\}$, em que $*$ vale "qualquer bit". O esquema `1**0` representa as cadeias `1000`, `1010`, `1100`, `1110`. Um esquema com $r$ asteriscos representa $2^r$ cadeias; cada cadeia de $L$ bits pertence a $2^L$ esquemas.

**Ordem** $o(H)$: número de posições fixas (não $*$). **Comprimento definidor** $\delta(H)$: distância entre a primeira e a última posição fixa.
Exemplo: $H =$ `*0*1*10*` tem posições fixas 2, 4, 6 e 7: $o(H) = 4$ e $\delta(H) = 7 - 2 = 5$.

**Teorema dos esquemas** (Holland), com seleção proporcional, cruzamento de um ponto e mutação por bit:
$$m(H, t+1) \ge m(H, t)\,\frac{f(H)}{\bar{f}}\left[1 - p_c \frac{\delta(H)}{L - 1} - o(H)\,p_m\right]$$
Em palavras: o número esperado de cópias do esquema na próxima geração é pelo menos o número atual vezes sua aptidão média relativa à média da população, descontada a chance de o cruzamento cortá-lo (cresce com $\delta$) e de a mutação alterá-lo (cresce com $o$).

**Consequência:** esquemas **curtos, de ordem baixa e aptidão acima da média** (os **blocos construtivos**) crescem exponencialmente. A **hipótese dos blocos construtivos** (Goldberg) diz que o AG funciona combinando esses blocos. É uma cota inferior, não uma previsão exata, e foi criticada (Grefenstette, Fogel e Ghozeil).

**Paralelismo implícito:** avaliar $n$ cadeias dá informação sobre muitos esquemas ao mesmo tempo.

**Verificação:** `test_esquemas` calcula ordem e comprimento definidor de `*0*1*10*` (4 e 5), confere que `1**0` casa com 4 cadeias de 4 bits e que uma cadeia de 8 bits pertence a $2^8$ esquemas, e avalia a cota do teorema num exemplo.
