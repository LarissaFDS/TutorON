---
id: compevol-selecao-roleta-torneio-ranking-elitismo-aptidao-relativa
titulo: Métodos de seleção: roleta (proporcional à aptidão), torneio, ranking, elitismo e escalonamento; exemplo da roleta para F(x) = 15x − x² com 6 cromossomos de 4 bits
assunto: compevol-02-operadores
tipo: exercicio_resolvido
questao: Dianati, Song e Treiber, tabela 1; apostila de Lucas, seção 4.3
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
Computação Evolucionária (UFAL, turma 2021.1), Dianati, Song e Treiber, tabela 1; apostila de Lucas, seção 4.3 (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Seleção:** escolhe quem se reproduz, favorecendo os mais aptos sem eliminar a diversidade.

**Roleta** (proporcional à aptidão): cada indivíduo recebe uma fatia proporcional a $f_i / \sum_j f_j$; gira-se a roleta uma vez por pai.

Exemplo (maximizar $F(x) = 15x - x^2$, cromossomos de 4 bits):

| cromossomo | $x$ | $F$ | fatia |
|---|---|---|---|
| 1100 | 12 | 36 | 16,5% |
| 0100 | 4 | 44 | 20,2% |
| 0001 | 1 | 14 | 6,4% |
| 1110 | 14 | 14 | 6,4% |
| 0111 | 7 | 56 | 25,7% |
| 1001 | 9 | 54 | 24,8% |

Soma 218. O ótimo seria $x = 7$ ou $8$ ($F = 56$).

**Problemas da roleta:** exige aptidão positiva; um "superindivíduo" toma a roleta cedo (**convergência prematura**); no fim, com aptidões parecidas, a pressão some. Remédios: **escalonamento** (linear, sigma) ou outros métodos.

**Torneio:** sorteiam-se $k$ indivíduos e vence o mais apto. A pressão seletiva cresce com $k$; não depende da escala da aptidão e funciona com minimização.

**Ranking:** ordena-se a população e a probabilidade depende da **posição**, não do valor; evita superindivíduos.

**Elitismo:** copia-se o(s) melhor(es) direto para a próxima geração, para não perder a melhor solução já encontrada.

**Verificação:** `test_roleta_e_torneio` refaz a tabela (aptidões, soma 218 e fatias), sorteia 100 000 giros da roleta com semente fixa e confere as frequências com tolerância de 0,5 ponto percentual, e mostra que o torneio de tamanho 2 escolhe o melhor com probabilidade $1 - (1 - 1/n)^2$.
