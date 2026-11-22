---
id: ga-cc-planos-retas-distancias
titulo: Plano por um ponto e dois vetores, distância de ponto a plano, retas reversas e sua distância, plano que contém ponto e reta, interseção de planos
assunto: ga-04-planos-retas-espaco
tipo: prova
questao: Reavaliações AB2 (22 e 29.11.2017), Q1 a Q3; Provas finais (06.12.2017), Q5 e Q6
semestre: 2017.1
resolucao: sim
fonte: Provas de Geometria Analítica 2017.1, IM-UFAL (turmas de Ciência da Computação) | Reavaliações AB2 (22 e 29.11.2017), Q1 a Q3; Provas finais (06.12.2017), Q5 e Q6
curso: Ciência da Computação (UFAL), provas de 2017.1 aplicadas em novembro e dezembro de 2017
fontes_catalogo: ufal-cc-ga-provas-2017-2
autoria: Enunciados: provas de Geometria Analítica do Instituto de Matemática da UFAL, parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); os PDFs não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: corrigida (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

**Plano por P(3, 1, 3) paralelo a $v_1=(2,1,-1)$ e $v_2=(-2,2,1)$:** a normal é $v_1\times v_2=(3,0,6)$, e o plano é $x+2z=9$. Distância de $P_1(1,2,-5)$: $\dfrac{|1-10-9|}{\sqrt5}=\dfrac{18}{\sqrt5}$. De $(2,-1,3)$: $\dfrac{1}{\sqrt5}$.

**Retas r: (1+t, −3t, 2t) e s: (−5+4t, 6−5t, 4+3t).** As direções $(1,-3,2)$ e $(4,-5,3)$ não são paralelas, e o sistema r = s não tem solução: são **reversas**. A distância é o produto misto sobre a área: $r\times s=(1,5,7)$, $(1,5,7)\cdot(-6,6,4)=52$, distância $\dfrac{52}{\sqrt{75}}=\dfrac{52\sqrt3}{15}$.

**Plano que contém um ponto e uma reta** ($P(1,-2,3)$ e s): use a direção da reta e o vetor de um ponto da reta até P; normal $(4,-5,3)\times(P-(-5,6,4))$ dá $(29,22,-2)$, e o plano é $29x+22y-2z=-21$.

**Distância de $(1,2,-1)$ à reta r:** $\dfrac{|(Q-r_0)\times d|}{|d|}=\dfrac{\sqrt{21}}{7}$. Retas por (1, 1, 1) e por (1, 1, 2), ambas com direção (1, 1, 1): paralelas distintas (o sistema não tem solução).

**Interseção de planos:** $-x+y+z=1$ e $x-y+z=1$ dão $z=1$, $x=y$: reta $(t,t,1)$. Os planos $x+y-z=1$ e $x-y+z=0$ dão $x=1/2$, $y=z+1/2$.

**Divergência:** numa prova final, $P_2$ e $P_3$ são o mesmo ponto $(-1,-2,1)$, e três pontos com dois iguais não definem um plano. **Correções da equipe:** o tutor deve apontar isso. Com os dados da outra turma, o plano é $2x+y+2z=2$ e a distância de (2, 2, 2) é 8/3.

**Verificação:** produtos vetoriais, mistos, sistemas e distâncias recalculados com SymPy.
