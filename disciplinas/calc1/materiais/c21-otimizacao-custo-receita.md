---
id: calc1-otimizacao-custo
titulo: Otimização de custo: caixa de base quadrada para 40.000 m³ com faces de preços diferentes
assunto: calc1-10-otimizacao
tipo: prova
questao: 4
semestre: 2012.2
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 4ª Avaliação (16.03.2013), Q4
fontes_catalogo: ufal-im-calc1-provas-fotos
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL (professor não impresso nas provas), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questão de prova (enunciado parafraseado). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

Caixa em forma de paralelepípedo, base quadrada de lado x e altura h, para 40.000 m³ de areia. Preços por m²: laterais 0,10 real, tampa 1 real, base 7 reais. Quais dimensões minimizam o custo?

1. Restrição: $x^2h = 40000$, logo $h = \dfrac{40000}{x^2}$, com $x > 0$.
2. Custo: $C = 0{,}10\cdot4xh + 1\cdot x^2 + 7\cdot x^2 = 8x^2 + 0{,}4xh = 8x^2 + \dfrac{16000}{x}$.
3. $C'(x) = 16x - \dfrac{16000}{x^2} = 0 \iff x^3 = 1000 \iff x = 10$.
4. $C''(x) = 16 + \dfrac{32000}{x^3} > 0$ para $x > 0$: mínimo absoluto em $(0, \infty)$ (único crítico e côncava para cima).
5. Dimensões: base 10 m × 10 m e altura $h = 400$ m; custo mínimo $C(10) = 800 + 1600 = 2400$ reais.

O domínio aqui é aberto, $(0, \infty)$: não há extremidades para comparar, por isso o argumento do único número crítico com $C'' > 0$ é necessário.

Erro comum: somar tampa e base com o mesmo preço, ou esquecer que são quatro faces laterais.

**Verificação:** $C(9) \approx 2425{,}8$ e $C(11) \approx 2422{,}5$, ambos maiores que $C(10) = 2400$.
