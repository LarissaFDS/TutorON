---
id: sinais-anot-modelos-edo
titulo: Sistemas descritos por equações diferenciais: RLC paralelo, massa-mola-amortecedor, tanque (não linear); coeficientes constantes e invariância
assunto: sinais-06-edo
tipo: resumo
resolucao: nao
fonte: Anotações manuscritas "Modelos por equações diferenciais" (1 maio 2026)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sinais e Sistemas 2026.1; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-sinais-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Forma geral do SLIT:** $\sum_i a_i\,y^{(i)}(t) = \sum_k b_k\,u^{(k)}(t)$. Coeficientes **constantes** dão sistema invariante no tempo; coeficientes que dependem de $t$ dão sistema variante. Termos como $\sqrt y$, $y^2$ ou $y\dot y$ tornam o sistema não linear.

**Exemplos das anotações:**
- RLC paralelo com fonte de corrente $u$ e saída $y = i_L$: $\ddot y + \frac{1}{RC}\dot y + \frac{1}{LC}y = \frac{1}{LC}u$.
- Massa-mola-amortecedor (força $u$, posição $y$): $\ddot y + \frac{b}{m}\dot y + \frac{k}{m}y = \frac1m u$.
- Tanque com vazão de entrada $K_m u$ e saída por orifício: $\dot y + \frac{a}{A}\sqrt{2gy} = \frac{K_m}{A}u$: **não linear** (raiz de $y$).

**Fronteira:** em Circuitos Elétricos o foco é montar a EDO do circuito; aqui o circuito é só um exemplo de sistema, e o foco é a classificação (linear, invariante) e a resposta.

**Verificação:** dimensão de cada termo do RLC: $\frac{1}{RC}$ e $\frac{1}{LC}$ têm unidades de s$^{-1}$ e s$^{-2}$; para o tanque, $y = 4$ dá $\sqrt{2g\cdot4}$ e $y = 1$ dá $\sqrt{2g}$: dobrar a "entrada" de nível não dobra a saída, logo não linear.
