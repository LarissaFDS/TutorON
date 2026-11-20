---
id: controle-anot-polo-zero-adicional
titulo: Efeito de polo e de zero adicionais na resposta ao degrau de segunda ordem (ζ = 0,5, ωn = 1): polo real perto da origem suaviza e domina; zero perto aumenta o sobressinal; zero quase cancelando polo
assunto: controle-05-resposta-temporal
tipo: resolucao
resolucao: sim
fonte: Anotações "Análise de Resposta Temporal" (1º out. 2026), p. 11–15
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

**Polo adicional:** $G = \frac{1}{(s/\beta + 1)(s^2 + s + 1)}$ ($\zeta = 0{,}5$, $\omega_n = 1$, ganho 1). Sem o polo, o sobressinal é $16{,}3\%$; com $\beta = 5$ e $\beta = 1{,}5$ ainda há sobressinal, menor; com $\beta = 0{,}5$, praticamente nenhum. Polo real adicional **reduz o sobressinal e deixa a resposta mais lenta**; quanto mais perto da origem, maior o efeito (o polo real passa a dominar).

**Zero quase cancelando polo:** $G_1 = \frac{6}{(s + 1)(s + 6)}$ e $G_2 = \frac{6(s + 1{,}1)}{1{,}1(s + 1)(s + 6)}$ (mesmo ganho estático 1):
$$y_1 = 1 - 1{,}2e^{-t} + 0{,}2e^{-6t},\qquad y_2 = 1 - 0{,}109e^{-t} - 0{,}891e^{-6t}.$$ O zero em $-1{,}1$ quase cancela o polo $-1$: o resíduo dele fica pequeno e o polo $-6$ passa a dominar (resposta mais rápida).

**Zero adicional:** $G = \frac{s/\beta + 1}{s^2 + s + 1}$: quanto mais perto da origem o zero ($\beta$ menor), **maior o sobressinal e menor o tempo de subida**.

Nesses casos as fórmulas de 2ª ordem padrão **não** valem: simule.

**Verificação:** `scipy.signal.step` de cada caso e `apart` de $Y_2$.
