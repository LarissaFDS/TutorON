---
id: prob-anot-poisson-exponencial
titulo: Relação Poisson–exponencial: contar falhas por dia (Poisson) x tempo entre falhas (exponencial)
assunto: prob-07-exponencial
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas digitalizadas "Distribuição Exponencial e Combinação Linear _251011_140915.pdf" (2025.2), págs. 1, 3 e 5
autoria: Otávio Joshua Costa Brandão Menezes (aluno, equipe TutorON), anotações de estudo; paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações pessoais do aluno); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia as anotações e não reproduz imagens
fontes_catalogo: ufal-prob-anotacoes-2025-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Resumo digitado do aluno (2025.2), parafraseado. Status da resolução: validada. Conferido com `scipy.stats`.

Mesma taxa λ, perguntas diferentes:

| Aspecto | Poisson | Exponencial |
|---|---|---|
| Tipo | discreta | contínua |
| Mede | número de eventos num intervalo | tempo (ou distância) entre eventos |
| Exemplo | nº de chamadas em 1 min | tempo até a próxima chamada |
| Parâmetro | λ eventos no intervalo | taxa λ (média 1/λ) |

**Exemplo (fábrica):** média de 3 falhas por dia.
a) Mais de 4 falhas num dia: contagem, **Poisson** com λ = 3: $P(X > 4) \approx 0{,}1847$ (`ppois(4, 3, lower.tail = FALSE)`).
b) Tempo entre falhas maior que 8 horas: tempo, **exponencial**. Taxa em horas: $3/24 = 0{,}125$ por hora. $P(T > 8) = e^{-0{,}125 \cdot 8} = e^{-1} \approx 0{,}3679$ (`pexp(8, rate = 3/24, lower.tail = FALSE)`).

Ligação: "nenhuma falha em 8 horas" é Poisson com média $0{,}125\cdot 8 = 1$ e $P(N = 0) = e^{-1}$, o mesmo valor do item b.

**Verificação:** `poisson.pmf(0, 1)` = `expon(scale=8).sf(8)` = 0,3679.
