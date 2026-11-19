---
id: sinais-anot-lista-impulso
titulo: Lista: integrais com impulso (propriedade da amostragem), δ(2t − 4) e esboço de degraus refletidos
assunto: sinais-03-sinais-elementares
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Lista Sinais e Sistemas" (27 abr. 2026), questões 3 e 4
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

**Questão 3 (integrais de $-\infty$ a $\infty$), pela amostragem $\int \phi(t)\delta(t - t_0)\,dt = \phi(t_0)$:**
- $\int \cos(2t)\,\delta(t)\,dt = \cos 0 = 1$.
- $\int \mathrm{sen}(2t)\,\delta(t - \pi/4)\,dt = \mathrm{sen}(\pi/2) = 1$.
- $\int \cos[2(t - \pi/4)]\,\delta(t - \pi/4)\,dt = \cos 0 = 1$.
- $\int \mathrm{sen}(t - 1)\,\delta(t - 2)\,dt = \mathrm{sen}\,1 \approx 0{,}841$.
- $\int \mathrm{sen}(t - 1)\,\delta(2t - 4)\,dt$: como $\delta(2t - 4) = \delta(2(t - 2)) = \tfrac12\delta(t - 2)$ (escalonamento do impulso, $\delta(at) = \delta(t)/|a|$), o resultado é $\tfrac12\mathrm{sen}\,1 \approx 0{,}421$.

**Questão 4 (esboços):** $u(-t) = 1$ para $t \le 0$; $u(3 - t) = 1$ para $t \le 3$; $t\,u(-t)$ é a reta $t$ só para $t \le 0$ (valores negativos); $(t - 3)u(3 - t)$ é a reta $t - 3$ só para $t \le 3$.

Todas as respostas das anotações conferem.

**Verificação:** SymPy (`integrate(sin(t-1)*DiracDelta(2*t-4), (t,-oo,oo))`) devolve $\mathrm{sen}(1)/2$; os outros quatro valores também foram refeitos nos testes.
