---
id: compevol-representacao-real-funcao-f6-schaffer-dois-parametros
titulo: Otimização com dois parâmetros: função F6 de Schaffer em [−100, 100]², máximo global, anéis de máximos locais, representação real e operadores para números reais
assunto: compevol-02-operadores
tipo: exercicio_resolvido
questao: Problema 3.2 de Lacerda e Carvalho
resolucao: sim
fonte: Apostilas e textos da pasta da turma (Lucas, UFRGS 2002; Lacerda e Carvalho; Dianati, Song e Treiber)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: lacerda-carvalho-ag
autoria: Exercício clássico dos textos da pasta da turma; resolução da equipe TutorON
licenca: Textos sem licença aberta declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Problema 3.2 de Lacerda e Carvalho (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Problema:** maximizar
$$f(x, y) = 0{,}5 - \frac{\text{sen}^2\!\left(\sqrt{x^2 + y^2}\right) - 0{,}5}{\left(1 + 0{,}001\,(x^2 + y^2)\right)^2}, \quad -100 \le x, y \le 100$$
Em palavras: 0,5 menos (seno ao quadrado da distância à origem, menos 0,5) dividido pelo quadrado de (1 mais um milésimo do quadrado da distância).

**Análise:** a função só depende de $r = \sqrt{x^2 + y^2}$. Em $r = 0$: $\text{sen}^2 0 = 0$, logo $f = 0{,}5 + 0{,}5 = 1$, o **máximo global**. Ao redor há **anéis concêntricos** de máximos locais (onde $\text{sen}^2 r = 0$, ou seja $r = k\pi$), com valores que caem devagar ($f(\pi, 0) \approx 0{,}990$). Um AG precisa de precisão alta para sair do primeiro anel e chegar exatamente à origem.

**Representação binária:** com 6 casas decimais em $[-100, 100]$: $200 \cdot 10^6$ valores, $2^{27} < 2 \cdot 10^8 \le 2^{28}$: 28 bits por variável, 56 no cromossomo.

**Representação real:** o cromossomo é $(x, y)$. Operadores:
- **cruzamento aritmético** (combinação convexa dos pais) ou **BLX-α** (sorteia em um intervalo um pouco maior que o dos pais);
- **mutação gaussiana**: soma $N(0, \sigma^2)$, respeitando os limites do domínio;
- vantagem: sem decodificação e sem perda de precisão.

**Verificação:** `test_funcao_f6` confere $f(0, 0) = 1$, o valor no primeiro anel ($\approx 0{,}990$ em $r = \pi$), os 28 bits por variável, e roda um AG real (torneio, aritmético, gaussiana, elitismo) com semente fixa que passa de $0{,}99$.
