---
id: ga-retas-plano-angulo
titulo: Ângulo entre duas retas no plano (pelos vetores diretores ou normais) e ponto de interseção: x − y = 0 e 3x + 4y − 12 = 0; x + y + 1 = 0 e reta paramétrica
assunto: ga-03-retas-no-plano
tipo: prova
questao: 2a; 4b; 4b
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Reavaliação AB1 (24.05.2017), Q2a; 1ª Avaliação (10.02.2017), Q4b; 1ª Avaliação (11.02.2017), Q4b
fontes_catalogo: ufal-ga-provas-2017
autoria: Enunciado: Instituto de Matemática da UFAL (professor não impresso na prova), parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

**Ângulo entre retas** (entre 0° e 90°): $\cos\theta = \dfrac{|\mathbf{d}_1\cdot\mathbf{d}_2|}{\|\mathbf{d}_1\|\|\mathbf{d}_2\|}$, com os vetores diretores; com os normais dá o mesmo. O módulo escolhe o ângulo agudo.

**r: x − y = 0 e s: 3x + 4y − 12 = 0.** Normais $(1, -1)$ e $(3, 4)$.
- Interseção: y = x em s dá $7x = 12$, ponto $(\tfrac{12}{7}, \tfrac{12}{7})$.
- $\cos\theta = \dfrac{|3 - 4|}{\sqrt2\cdot5} = \dfrac{1}{5\sqrt2}$, $\theta \approx 81{,}87°$.

**x + y + 1 = 0 e x = 1 − 2t, y = 2 + 5t.** Diretores $(1, -1)$ e $(-2, 5)$: $\cos\theta = \dfrac{|-2 - 5|}{\sqrt2\sqrt{29}} = \dfrac{7}{\sqrt{58}}$, $\theta \approx 23{,}2°$.

**x + 2y = 0 e x = 2 + t, y = 2 − 3t.** Diretores $(2, -1)$ e $(1, -3)$: $\cos\theta = \dfrac{5}{\sqrt5\sqrt{10}} = \dfrac{\sqrt2}{2}$, $\theta = 45°$.

Interseção com reta paramétrica: substitua x(t) e y(t) na equação geral e resolva em t.

**Verificação:** $(\tfrac{12}{7}, \tfrac{12}{7})$ em s: $\tfrac{36 + 48}{7} = 12$; pelos coeficientes angulares 1 e −3/4: $\tan\theta = \left|\dfrac{1 + 3/4}{1 - 3/4}\right| = 7$ e $\arctan 7 \approx 81{,}87°$.
