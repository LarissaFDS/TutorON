---
id: ga-cc-revolucao-quadricas-provas-cc
titulo: Girar z = sen y, x = sen y e z = sen x, o círculo (x − 2)² + z² = 1 (toro) e quádricas com sinais trocados (provas de CC)
assunto: ga-12-quadricas-superficies
tipo: prova
questao: Prova AB2.2 e Reavaliações AB2 (2017.1), Q4 e Q5; Provas finais (06.12.2017), Q4 e Q7
semestre: 2017.1
resolucao: sim
fonte: Provas de Geometria Analítica 2017.1, IM-UFAL (turmas de Ciência da Computação) | Prova AB2.2 e Reavaliações AB2 (2017.1), Q4 e Q5; Provas finais (06.12.2017), Q4 e Q7
curso: Ciência da Computação (UFAL), provas de 2017.1 aplicadas em novembro e dezembro de 2017
fontes_catalogo: ufal-cc-ga-provas-2017-2
autoria: Enunciados: provas de Geometria Analítica do Instituto de Matemática da UFAL, parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

**Nas provas de CC:** em torno do eixo y, troque a outra coordenada por $\sqrt{x^2+z^2}$; em torno do eixo z, por $\sqrt{x^2+y^2}$.

- $z=\operatorname{sen}y$ (ou $x=\operatorname{sen}y$), $0\le y\le2\pi$, em torno do eixo y: $x^2+z^2=\operatorname{sen}^2y$. É um "colar de contas": o raio vai a zero em $y=0,\pi,2\pi$.
- $z=\operatorname{sen}x$, $0\le x\le2\pi$, em torno do eixo z: $z=\operatorname{sen}\sqrt{x^2+y^2}$, ondulação circular.
- O círculo $(x-2)^2+z^2=1$, $y=0$, em torno do eixo z: $\left(\sqrt{x^2+y^2}-2\right)^2+z^2=1$, um **toro** (boia).

**Quádricas pela contagem de sinais** (lado direito igual a 1):
- $-\tfrac{x^2}{25}+\tfrac{y^2}{9}+\tfrac{z^2}{4}=1$: um sinal negativo, **hiperboloide de uma folha** em torno do eixo x.
- $-\tfrac{x^2}{25}-\tfrac{y^2}{9}+\tfrac{z^2}{4}=1$ e $\tfrac{x^2}{9}-\tfrac{y^2}{16}-\tfrac{z^2}{16}=1$: dois negativos, **hiperboloide de duas folhas** (eixo z e eixo x).
- $\tfrac{x^2}{16}+\tfrac{y^2}{9}+\tfrac{z^2}{16}=1$: elipsoide.

Para esboçar, ache os traços nos planos coordenados e em planos paralelos (por exemplo, $z=k$).

**Verificação:** as equações de revolução foram conferidas com SymPy, substituindo pontos da curva girados por um ângulo qualquer.
