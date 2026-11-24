---
id: fis1-ab2-2022-variacoes
titulo: AB2 de 2022 — as mesmas questões da AB2 de 2017 com g = 10 m/s², bola de 8 kg e o caso m1 = 0 da máquina de Atwood com disco; massa do disco faltando na prova
assunto: fis1-06-rotacao
tipo: prova
resolucao: sim
fonte: Prova AB2 de Física 1, 27/06/2022, Prof. Osvaldo A. Rosso (UFAL), PDF da turma (Engenharia de Computação, 2º período); enunciado parafraseado
fontes_catalogo: ufal-rosso-ab2-2022,halliday-fundamentos-vol1
autoria: Prova do Prof. Osvaldo A. Rosso (UFAL), questões adaptadas do Halliday; enunciado parafraseado e resolução independente da equipe TutorON
licenca: Não declarada (prova da turma); PDF não versionado
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Prova AB2 (2022), comparada com a AB2 e a reavaliação de 2017 (enunciado parafraseado). Status da resolução: pendente_professor. A resolução é da equipe TutorON e não é gabarito do professor. Prova é atividade avaliativa: o tutor guia, não entrega.

A prova de 2022 repete quatro questões de 2017 (esferas penduradas com colisão elástica, Atwood com disco, barata no carrossel e bola na rampa), agora com **g = 10 m/s²**. O método é o mesmo dos blocos de 2017; mudam os números:
- **Colisão elástica** (30 g, 75 g, 8 cm): $v_{1i}=\sqrt{2gh}$ ≈ 1,26 m/s; depois do choque, esfera 1 ≈ −0,54 m/s (volta), esfera 2 ≈ 0,72 m/s; altura da esfera 2 ≈ 0,026 m.
- **Barata no disco:** dados iguais aos de 2017, $\omega_f$ ≈ 1,37 rad/s (g não entra).
- **Bola de 8 kg na rampa de 30°** (desce 1,20 m): aceleração $a = g\,\text{sen}\,\theta/(1+I/MR^2)$ e atrito estático $f_s = Mg\,\text{sen}\,\theta - Ma$, rampa acima. Esfera maciça ($\tfrac25$): a ≈ 3,57 m/s², $f_s$ ≈ 11,43 N, v ≈ 4,14 m/s. Leitura de disco ($\tfrac12$): a ≈ 3,33 m/s², $f_s$ ≈ 13,33 N, v ≈ 4,00 m/s. A velocidade angular na base é $\omega = v/R$; a prova não dá R, então fica literal.

**Atwood com disco, item novo: e se $m_1 = 0$?** Com o lado esquerdo sem bloco, $T_1 = 0$ e só $m_2$ puxa: $a = \dfrac{m_2\,g}{m_2 + M/2}$, e a tração do lado direito é $T_2 = m_2(g-a) = \dfrac{M}{2}a$ (é ela que dá o torque no disco). Sem disco ($M = 0$), $a = g$: queda livre.

**Pendente:** a prova de 2022 dá a massa do disco como "M = 12 cm", uma unidade de comprimento (12 cm é o raio na versão de 2017, que dá M = 500 kg, provavelmente 500 g). Lendo M = 500 g e R = 12 cm: com 400 g e 600 g, a ≈ 1,60 m/s², $T_1$ ≈ 4,64 N, $T_2$ ≈ 5,04 N; com $m_1 = 0$, a ≈ 7,06 m/s² e $T_2$ ≈ 1,76 N. Confirmar o dado com o professor.

**Verificação:** todos os números foram refeitos em Python com `tests_acervo/fis1_verif.py` (g = 10 m/s²), com conservação de momento e de energia na colisão e torque igual a $I\alpha$ no disco.
