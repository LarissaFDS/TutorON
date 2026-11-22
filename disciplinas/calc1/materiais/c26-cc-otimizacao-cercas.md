---
id: calc1-cc-otimizacao-cercas
titulo: Otimização de cerca: menor custo para terreno de 200 m² e maior área com dois tipos de arame e 600 reais
assunto: calc1-10-otimizacao
tipo: prova
questao: 4ª prova 2006, Q1; 4ª prova 2007, Q2
semestre: 2006–2007
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 4ª prova (19.08.2006), Q1; 4ª prova (07.07.2007), Q2
curso: Ciência da Computação (UFAL), banco de questões da turma (provas do IM-UFAL aplicadas a vários cursos)
fontes_catalogo: ufal-cc-calc1-banco-provas
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL, parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova); PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

Roteiro: nomeie as variáveis, escreva a **restrição** e a **função objetivo**, elimine uma variável, derive, ache o ponto crítico no domínio e **justifique** que é máximo ou mínimo (segunda derivada ou sinal da primeira).

**Terreno retangular de 200 m², cerca de menor custo** (custo proporcional ao perímetro): $xy=200$ e $P(x)=2x+\tfrac{400}{x}$, $x>0$. $P'(x)=2-\tfrac{400}{x^2}=0$ dá $x=\sqrt{200}=10\sqrt2$ m, e $y=10\sqrt2$: o quadrado. $P''(x)=800/x^3>0$, mínimo. Perímetro $40\sqrt2\approx56{,}6$ m.

**Dois tipos de arame:** dois lados opostos (comprimento x cada) com arame a, 3 reais por metro; os outros dois (y cada) com arame b, 2 reais por metro; verba de 600 reais. Restrição $6x+4y=600$, então $y=150-\tfrac32x$ e $A(x)=x\left(150-\tfrac32x\right)$, $0<x<100$. $A'(x)=150-3x=0$ dá $x=50$ m e $y=75$ m; $A''=-3<0$, máximo. Área máxima 3750 m².

Erros comuns: esquecer que **dois** lados usam cada arame (o custo de um tipo é $2\cdot3x$), e não dizer o domínio da variável.

**Verificação:** pontos críticos e valores recalculados com SymPy ($10\sqrt2$; 50 e 75; 3750).
