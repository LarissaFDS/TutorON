---
id: alglin-lista2-codigo-axiomas-combinacao
titulo: Lista 2 em Python — conferir axiomas de espaço vetorial complexo com NumPy, o erro de usar |β| no produto por escalar e testar combinação linear resolvendo um sistema
assunto: alglin-04-algebra-linear-computacional
tipo: exercicio_resolvido
resolucao: sim
fonte: Códigos-base da Lista 2 de Álgebra Linear (arquivos .py do material do 2º período de Engenharia de Computação) | enunciados parafraseados
curso: Engenharia de Computação (UFAL), ECOM011 Álgebra Linear, 2º período (também no 3º período de Ciência da Computação); semestre não identificado
fontes_catalogo: ufal-alglin-listas
autoria: Enunciados da lista da disciplina; resoluções da equipe TutorON com apoio de IA, conferidas com SymPy e NumPy
licenca: Não declarada (códigos-base da disciplina; arquivos não versionados)
publicacao_transcricao: não autorizada; enunciados parafraseados
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Álgebra Linear, Lista 2 em Python (NumPy). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Axiomas em $\mathbb C^3$.** O código-base define vetores complexos (`dtype=complex128`) e escalares complexos $\beta$, e pede as funções `soma`, `produto`, vetor nulo e oposto.
- `produto(beta, u)` deve ser `beta * u`. Usar `abs(beta) * u` é um erro: troca o escalar por um real e quebra $(\beta + \gamma)u = \beta u + \gamma u$, porque $|\beta + \gamma| \ne |\beta| + |\gamma|$ em geral. Ex.: $\beta = 1$, $\gamma = -1$ dá $0 \cdot u$ de um lado e $2u$ do outro.
- Conferir só `shape` e `dtype` mostra o fechamento, não os outros axiomas.
- Compare com tolerância (`np.allclose`), não com igualdade exata (`np.array_equal`): com números como $e^{-\pi/2}$ o arredondamento pode fazer um axioma verdadeiro "falhar".

**Combinação linear.** O alvo $b$ é combinação de $v_1, \dots, v_k$ se o sistema $V c = b$ (vetores nas colunas de $V$) tem solução. Teste: `posto(V) == posto([V | b])`; os coeficientes saem de `np.linalg.lstsq`. Na eliminação de Gauss do código-base, pivô zero acusa "sistema singular", mas um sistema singular pode ter solução: use o posto. Ex.: $(1, 2, 3)$ em $\{(0,0,1), (0,1,0), (1,0,0)\}$ tem $c = (3, 2, 1)$; no caso de 4 vetores múltiplos uns dos outros (posto 1), $(1, 2, 3, 4)$ não é combinação.

**Soma de sinais.** Somar dois áudios amostrados é somar vetores (corte os dois no menor tamanho antes). Ao converter de volta para `int16`, valores fora de $[-32768, 32767]$ não cabem e saem errados (estouro): normalize ou limite com `np.clip` antes.

**Verificação:** axiomas, contraexemplo de $|\beta|$ e combinações refeitos com NumPy em `test_codigo_axiomas_combinacao`.
