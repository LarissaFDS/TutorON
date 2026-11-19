---
id: circ-anot-rlc-ab2-q1
titulo: RLC série criticamente amortecido (AB2, questão 1): Thévenin visto pelo LC, α = ω₀ = 20, resposta vs = 16t e^(−20t)
assunto: circ-08-segunda-ordem
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Lista para AB 2" (16 jun. 2026), lista do Prof. Jobson de Araújo Nascimento, questão 1
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Circuitos Elétricos 2026.1, Prof. Jobson de Araújo Nascimento, IC/UFAL); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-circ-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Circuito (descrito):** o restante do circuito, visto pelos terminais do conjunto L–C, foi reduzido a um equivalente de Thévenin $V_{Th} = 2$ V, $R_{Th} = 4$ Ω; com o resistor de 1 Ω do ramo, a malha série fica com $R = 5$ Ω, $L = \tfrac{1}{8}$ H e $C = \tfrac{1}{50}$ F. Corrente $i$ no sentido horário, convenção passiva em todos os elementos.

**Parâmetros:**
$$\alpha = \frac{R}{2L} = \frac{5}{2\cdot\frac18} = 20\ \text{s}^{-1},\qquad \omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{\frac{1}{400}}} = 20\ \text{rad/s}.$$
Alfa igual a ômega zero: **amortecimento crítico**, raiz dupla $s = -20$.

**Condições iniciais (das anotações):** capacitor e indutor descarregados no instante da comutação; a resposta de interesse começa em zero.

**Resposta:**
$$v_s(t) = 16\,t\,e^{-20t}\ \text{V},\quad t \ge 0 .$$
Em palavras: dezesseis vezes t vezes exponencial de menos vinte t; sobe, atinge o pico em $t = 1/20$ s e volta a zero sem oscilar.

**Verificação:** `dsolve` da equação $x'' + 40x' + 400x = 0$ com as condições iniciais da questão devolve $16te^{-20t}$; o pico vale $16\cdot\frac{1}{20}e^{-1} \approx 0{,}29$ V.
