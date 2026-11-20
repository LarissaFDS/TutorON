---
id: controle-anot-routh-ganho
titulo: Faixa de ganho K para estabilidade em malha fechada por Routh: controlador proporcional K com planta (s+1)/(s(s−1)(s+6)), realimentação unitária negativa: K > 7,5
assunto: controle-04-estabilidade-routh
tipo: resolucao
resolucao: sim
fonte: Anotações "Estabilidade de SLIT contínuo" (9 set. 2026), p. 9–10
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Enunciado (paráfrase):** controlador proporcional $K$ em série com $G(s) = \frac{s + 1}{s(s - 1)(s + 6)}$ (planta instável em malha aberta: polo em $+1$; polo na origem, integrador), realimentação **unitária negativa**. Para que $K$ a malha fechada é estável?

**Malha fechada:** $G_{mf} = \frac{KG}{1 + KG} = \frac{K(s + 1)}{s^3 + 5s^2 + (K - 6)s + K}$.

**Routh de $A(s) = s^3 + 5s^2 + (K - 6)s + K$:**
- $s^3$: $1,\ K - 6$
- $s^2$: $5,\ K$
- $s^1$: $\frac{5(K - 6) - K}{5} = \frac{4K - 30}{5}$
- $s^0$: $K$

Sem mudança de sinal: $4K - 30 > 0$ e $K > 0$, logo **$K > 7{,}5$**.

**Verificação:** com $K = 7{,}5$ há par de polos em $\pm j\sqrt{1{,}5}$ (limite); `roots` com $K = 8$ dá todos com parte real negativa e com $K = 7$ dá um par no semiplano direito.
