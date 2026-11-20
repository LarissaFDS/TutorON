---
id: controle-anot-revisao-sensor
titulo: Revisão prova 1, questão 1: malha com controlador K1/(s+a), planta 2/(s+1) e sensor K2/(s+0,1); K2 = 0,1 para saída senoidal não amortecida com período 19,87 s
assunto: controle-04-estabilidade-routh
tipo: resolucao
resolucao: sim
fonte: Anotações "Revisão prova 1" (2 out. 2026), questão 1
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

**Enunciado (paráfrase):** controlador $C = \frac{K_1}{s + a}$, planta $G = \frac{2}{s + 1}$, sensor $H = \frac{K_2}{s + 0{,}1}$, realimentação negativa. Com $a = 0$ e $K_1 = 0{,}55$, achar $K_2$ para que a saída ao degrau tenha, em regime, uma senoide **não amortecida**, e o período dela.

**Malha fechada:** $G_{mf} = \frac{CG}{1 + CGH} = \frac{1{,}1(s + 0{,}1)}{s^3 + 1{,}1s^2 + 0{,}1s + 1{,}1K_2}$.

**Condição:** um par de polos no eixo imaginário e o terceiro estável: $s^3 + 1{,}1s^2 + 0{,}1s + 1{,}1K_2 = (s + 1{,}1)(s^2 + \omega^2)$. Comparando: $\omega^2 = 0{,}1$ e $1{,}1\omega^2 = 1{,}1K_2 \Rightarrow K_2 = 0{,}1$. Período $T = 2\pi/\sqrt{0{,}1} = 19{,}87$ s.

É o limite de estabilidade: pelo Routh, a linha $s^1$ é $0{,}1 - K_2$, que zera em $K_2 = 0{,}1$. A malha fechada **não** é BIBO estável (polos $\pm j0{,}316$).

**Verificação:** `roots` de $s^3 + 1{,}1s^2 + 0{,}1s + 0{,}11$ dá $-1{,}1$ e $\pm 0{,}3162j$.
