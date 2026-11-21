---
id: lfa-simplificacao-glc-producoes-vazias-unitarias
titulo: Simplificação de GLC — retirada de produções vazias (conjunto de anuláveis), de produções unitárias A → B (fecho) e de símbolos inúteis, exemplos 10 e 11
assunto: lfa-05-livres-de-contexto
tipo: exercicio_resolvido
questao: exemplos 10 e 11
resolucao: sim
fonte: Apostila 03 (Profa. Simone Prado, UNESP), seção 5 e exemplos 10 e 11
fontes_catalogo: unesp-prado-apostilas-tc
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exemplos 10 e 11 da apostila, conferidos. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**1. Produções vazias.**
- Calcule os **anuláveis**: comece com as variáveis que têm $A \to \varepsilon$ e acrescente $X$ sempre que $X \to X_1 \dots X_n$ tem todos os $X_i$ anuláveis.
- Para cada produção, acrescente as versões sem cada combinação de anuláveis (sem gerar $A \to \varepsilon$).
- Se $S$ era anulável, recoloque $S \to \varepsilon$.

**2. Produções unitárias $A \to B$.** Calcule o fecho de cada variável (quem ela alcança só por unitárias). Copie para $A$ as produções não unitárias das variáveis do fecho e apague as unitárias.

**3. Símbolos inúteis.**
- Primeiro, retire as variáveis que não geram nenhuma palavra terminal.
- Depois, retire os símbolos não atingíveis a partir de $S$.
- A ordem importa: fazer ao contrário pode deixar símbolos inúteis.

**Exemplo 10:** $S \to aXa \mid bXb \mid \varepsilon$, $X \to a \mid b \mid Y$, $Y \to ab \mid \varepsilon$.
- Anuláveis: $\{S, Y, X\}$; $X$ entra porque $X \to Y$.
- Resultado: $S \to aXa \mid bXb \mid aa \mid bb \mid \varepsilon$, $X \to a \mid b \mid Y$, $Y \to ab$.

**Exemplo 11** (unitárias, sobre o resultado do 10):
- fecho-$X = \{Y\}$, então $X$ ganha $X \to ab$ e perde $X \to Y$.
- Resultado: $S \to aXa \mid bXb \mid aa \mid bb \mid \varepsilon$, $X \to a \mid b \mid ab$, $Y \to ab$.

O passo 3 ainda retiraria $Y$, que ficou inatingível a partir de $S$. A apostila para antes e mantém $Y$; a linguagem não muda.

A linguagem das três gramáticas é a mesma: $\{\varepsilon, aa, bb, aaa, aba, bab, bbb, aaba, babb\}$, 9 palavras.

**Verificação:** o reconhecedor de Earley mostra que a gramática original, a do exemplo 10 e a do 11 geram exatamente essas 9 palavras entre todas as palavras até comprimento 6.
