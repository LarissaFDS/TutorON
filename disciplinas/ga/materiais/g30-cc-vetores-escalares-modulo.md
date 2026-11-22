---
id: ga-cc-vetores-escalares-modulo
titulo: Vetores no plano: combinação linear com escalares, vetor de módulo dado, módulo de AB e vetor a partir da projeção
assunto: ga-01-vetores-operacoes
tipo: prova
questao: Reavaliações AB1 (22 e 29.11.2017), Q1; Provas finais (06.12.2017), Q1 e Q2
semestre: 2017.1
resolucao: sim
fonte: Provas de Geometria Analítica 2017.1, IM-UFAL (turmas de Ciência da Computação) | Reavaliações AB1 (22 e 29.11.2017), Q1; Provas finais (06.12.2017), Q1 e Q2
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

**Escalares de uma combinação linear.** Para escrever $v=(2,3)$ como $k_1u+k_2w$ com $u=(-1,2)$ e $w=(1,2)$, iguale coordenada a coordenada: $-k_1+k_2=2$ e $2k_1+2k_2=3$. Daí $k_1=-1/4$ e $k_2=7/4$.

**Vetor com direção dada e módulo dado.** Normalize e multiplique: com o sentido de $(3,4)$ e módulo 6, o vetor é $\tfrac{6}{5}(3,4)=(18/5,\,24/5)$. Com sentido contrário ao de $(-1,2)$ e módulo 5, é $-\tfrac{5}{\sqrt5}(-1,2)=(\sqrt5,\,-2\sqrt5)$.

**Módulo de AB.** Com $A(2,y)$ e $B(3,3)$, $AB=(1,\,3-y)$ e $1+(3-y)^2=25$, logo $y=3\pm2\sqrt6$ (duas respostas).

**Vetor a partir da projeção.** Se a projeção de v sobre $u=(4,2)$ é $(2,1)$ e o módulo de v é 6: a projeção é $\tfrac{v\cdot u}{|u|^2}u$, e $(2,1)=\tfrac12u$, então $v\cdot u=10$. Com $v=(a,b)$: $4a+2b=10$ e $a^2+b^2=36$, o que dá $a=2\pm\tfrac{\sqrt{155}}5$ e $b=1\mp\tfrac{2\sqrt{155}}5$ (dois vetores).

Erros comuns: esquecer a segunda solução da equação do segundo grau, e confundir a projeção (um vetor) com o comprimento da projeção (um número).

**Verificação:** sistemas e normas resolvidos com SymPy (solve e norm).
