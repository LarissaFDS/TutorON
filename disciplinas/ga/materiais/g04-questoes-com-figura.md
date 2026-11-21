---
id: ga-questoes-com-figura
titulo: Questões que dependem de figura: forças F, F₁, F₂ com ângulos de 30° e 60° (resultante F ou 2F) e vetor w no triângulo com A(1, 1), |u| = 3, |v| = 6 e ângulo de 60°
assunto: ga-01-vetores-operacoes
tipo: prova
questao: 1; 1; 1b
semestre: 2016.2 e 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Reavaliação 1 (03.11.2016), Q1; prova sem cabeçalho (foto), Q1; 1ª Avaliação (11.02.2017), Q1b
fontes_catalogo: ufal-ga-provas-2016,ufal-ga-provas-sem-cabecalho,ufal-ga-provas-2017
autoria: Enunciados: provas de Geometria Analítica do Instituto de Matemática da UFAL (ver fontes_catalogo), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Questões de prova que dependem da figura. Status da resolução: pendente de confirmação do professor (a resolução da equipe TutorON, conferida com SymPy, depende da nossa leitura da figura, que não está no repositório).

**Forças.** $\|F\| = \sqrt3$, $\|F_1\| = 2$, $\|F_2\| = 1$. Leitura da figura: $F_1$ horizontal para a direita; $F$ a 30° acima de $F_1$; $F_2$ para baixo e para a esquerda, a 60° do semieixo horizontal esquerdo. Então $F_1 = (2, 0)$, $F = (\tfrac32, \tfrac{\sqrt3}{2})$ e $F_2 = (-\tfrac12, -\tfrac{\sqrt3}{2})$.
- Resultante F: $aF_1 + bF_2 = F$. Na componente y, $-\tfrac{\sqrt3}{2}b = \tfrac{\sqrt3}{2}$, logo $b = -1$; na x, $2a + \tfrac12 = \tfrac32$, logo $a = \tfrac12$. $F_1$ fica com metade do módulo; $F_2$ inverte o sentido.
- Resultante 2F (versão da Reavaliação 1 de 2016): $a = 1$ e $b = -2$.

**Vetor w (1ª Avaliação de 2017, Q1b).** O enunciado traz "$\|\vec u = 3\|$"; lemos $\|\vec u\| = 3$. Leitura da figura: $\mathbf{u} = \overrightarrow{AB}$ horizontal, $\mathbf{v} = \overrightarrow{AC}$ a 60° de u, $\mathbf{w} = \overrightarrow{CB}$. Com A(1, 1): $\mathbf{u} = (3, 0)$, $\mathbf{v} = (3, 3\sqrt3)$, $\mathbf{w} = \mathbf{u} - \mathbf{v} = (0, -3\sqrt3)$. Com esses dados, B = (4, 1) fica exatamente abaixo de C; a figura da prova não está em escala.

**Verificação:** $\tfrac12(2,0) - (-\tfrac12, -\tfrac{\sqrt3}{2}) = (\tfrac32, \tfrac{\sqrt3}{2}) = F$, de norma $\sqrt{9/4 + 3/4} = \sqrt3$; $\|\mathbf{w}\|^2 = 27 = 9 + 36 - 2\cdot3\cdot6\cos60°$ (lei dos cossenos).
