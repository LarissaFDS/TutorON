---
id: fis2-notion-pendulos
titulo: Anotações da turma (Notion) — pêndulo de torção, pêndulo simples e pêndulo físico
assunto: fis2-04-oscilacoes
tipo: material_estudo
resolucao: nao
fonte: Notion da turma, página "Oscilações" (texto lido; imagens com fórmulas não versionadas, transcritas e conferidas pela equipe)
fontes_catalogo: ufal-fis2-notion
autoria: Anotações de alunos da turma de Física 2 (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma); imagens fora do repositório
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio as anotações e corrige os erros indicados no fim
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Oscilador angular (pêndulo de torção): torque restaurador $\tau = -\kappa\theta$ (κ = constante de torção do fio, N·m/rad). Período: $T = 2\pi\sqrt{I/\kappa}$ (I = momento de inércia em relação ao eixo do fio). Analogia: MHS linear usa k e m; MHS angular usa κ e I. Esfera maciça em torno de um diâmetro: $I = \tfrac25 m r^2$.

Pêndulo (pequenas oscilações): o torque da gravidade em relação ao ponto de suspensão é $\tau = -L\,(mg\sin\theta)$; com $\sin\theta \approx \theta$ (θ em radianos, pequeno), $I\alpha = -mgL\theta$, que é MHS angular com $\omega = \sqrt{mgL/I}$.

Pêndulo simples (massa pontual na ponta de um fio de comprimento L, $I = mL^2$):
$$T = 2\pi\sqrt{L/g}$$
Ex.: L = 1 m, g = 9,8 m/s² → T ≈ 2,0 s. O período não depende da massa nem (para pequenas amplitudes) da amplitude.

Pêndulo físico (corpo rígido): $T = 2\pi\sqrt{\dfrac{I}{mgh}}$, com h = distância do ponto de suspensão ao centro de massa e I em relação ao **ponto de suspensão** (teorema dos eixos paralelos: $I = I_{cm} + mh^2$).

Ex.: barra homogênea de comprimento L suspensa por uma extremidade: $I_{cm} = mL^2/12$, h = L/2, $I = mL^2/12 + m(L/2)^2 = mL^2/3$, logo $T = 2\pi\sqrt{2L/(3g)}$ e $g = 8\pi^2 L/(3T^2)$. A anotação dá $mL^2/12$ como inércia e a fórmula de g sem dizer que o eixo é a extremidade: com $mL^2/12$ a fórmula não sai.

Correções da equipe: a anotação escreve o período do pêndulo simples como $2\pi\sqrt{I/(mgL)}$ (fórmula do físico); com $I = mL^2$ ela vira $2\pi\sqrt{L/g}$. Eixo paralelo explicitado; κ (torção) separado de k (mola).
