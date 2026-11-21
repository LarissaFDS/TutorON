---
id: ga-triangulo-projecao-altura
titulo: Triângulo A(3, 3), B(0, 1), C(1, 6): verificar ângulo reto pelo produto escalar, projeção do cateto sobre a hipotenusa e pé da altura
assunto: ga-01-vetores-operacoes
tipo: prova
questao: 3; 4
semestre: 2016.2
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Final (14.11.2016), Q3; Reavaliação 1 (03.11.2016), Q4
fontes_catalogo: ufal-ga-provas-2016
autoria: Enunciado: Prof. Adelailson Peixoto (Instituto de Matemática, UFAL), nome impresso no cabeçalho da prova, parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

Triângulo de vértices A(3, 3), B(0, 1) e C(1, 6).

**a) Retângulo em A.** $\overrightarrow{AB} = (-3,-2)$ e $\overrightarrow{AC} = (-2, 3)$; $\overrightarrow{AB}\cdot\overrightarrow{AC} = 6 - 6 = 0$: o ângulo em A é reto e BC é a hipotenusa.

**b) Projeção do cateto BA sobre a hipotenusa BC.** $\overrightarrow{BA} = (3, 2)$, $\overrightarrow{BC} = (1, 5)$, $\overrightarrow{BA}\cdot\overrightarrow{BC} = 13$, $\|\overrightarrow{BC}\|^2 = 26$: projeção $\tfrac{13}{26}(1,5) = (\tfrac12, \tfrac52)$, de comprimento $\tfrac{\sqrt{26}}{2}$, metade da hipotenusa. (A Reavaliação 1 pede "AB sobre a hipotenusa": é o mesmo vetor a partir de B; diga qual origem usou.)

**c) Pé da altura relativa a A.** É o ponto H de BC com $\overrightarrow{BH}$ igual à projeção: $H = B + (\tfrac12, \tfrac52) = (\tfrac12, \tfrac72)$.

Método geral: o pé da perpendicular de V à reta por B com diretor $\mathbf{d}$ é $H = B + \dfrac{\overrightarrow{BV}\cdot\mathbf{d}}{\|\mathbf{d}\|^2}\mathbf{d}$.

**Verificação:** $\overrightarrow{AH} = (-\tfrac52, \tfrac12)$ e $(-\tfrac52, \tfrac12)\cdot(1, 5) = 0$, então AH é perpendicular a BC; H está em BC porque $H - B$ é múltiplo de (1, 5).
