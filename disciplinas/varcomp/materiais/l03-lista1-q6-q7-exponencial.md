---
id: varcomp-lista1-q6-q7-exponencial
titulo: Lista 1, Q6 e Q7 — exponencial complexa: e^{2 ± 3πi} = −e², e^{(2 + πi)/4}, e as soluções de e^z = −2, e^z = 1 + i√3 e e^{2z − 1} = 1
assunto: varcomp-03-funcoes-elementares
tipo: lista
questao: 6 e 7
resolucao: sim
fonte: Lista nº 1 de Variável Complexa (Instituto de Computação, UFAL; arquivo Lista_1.pdf), questão 6 e 7
autoria: Enunciado: lista da disciplina (Instituto de Computação, UFAL; autor não identificado no arquivo), parafraseado pela equipe TutorON; resolução da equipe TutorON, conferida com SymPy
licenca: Não declarada (lista da disciplina); PDFs e imagens fora do repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
fontes_catalogo: ufal-varcomp-lista1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Lista nº 1 de Variável Complexa (IC/UFAL), questão 6 e 7. Enunciado parafraseado. Status da resolução: pendente de confirmação do professor (a lista não tem gabarito oficial; a resolução é da equipe TutorON, conferida com SymPy em `tests_acervo/test_disciplina_varcomp.py`).

Ferramenta: $e^{x + iy} = e^x(\cos y + i\sin y)$, e $e^z$ tem **período $2\pi i$**. Por isso as equações $e^z = w$ têm infinitas soluções: $z = \ln|w| + i(\arg w + 2k\pi)$, $k \in \mathbb{Z}$.

**Q6.** (a) $e^{2 \pm 3\pi i} = e^2(\cos 3\pi \pm i\sin 3\pi) = -e^2$. (b) $e^{(2 + \pi i)/4} = e^{1/2}\left(\cos\frac\pi4 + i\sin\frac\pi4\right) = \sqrt e\,\frac{\sqrt2}{2}(1 + i)$.

**Q7.** (a) $e^z = -2$: $|w| = 2$, $\arg w = \pi$, então $z = \ln 2 + i(\pi + 2k\pi)$. (b) $e^z = 1 + i\sqrt3$ (o arquivo perde a raiz na extração; com $\sqrt3$ o argumento é notável): $|w| = 2$, $\arg w = \pi/3$, $z = \ln 2 + i\left(\frac\pi3 + 2k\pi\right)$. (c) $e^{2z - 1} = 1$: $2z - 1 = 2k\pi i$, logo $z = \frac12 + k\pi i$.

Erro comum: dar só a solução com $k = 0$; ou escrever $\ln(-2)$ como se fosse real.

**Verificação:** SymPy confirma os valores de Q6 e que $e^z$ aplicado às soluções de Q7 (para vários $k$) devolve $-2$, $1 + i\sqrt3$ e, em (c), $e^{2z-1} = 1$.
