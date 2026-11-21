---
id: ga-planos-posicoes-intersecoes
titulo: Planos paralelos e coincidentes (ax − 3y + cz + d = 0), interseção de plano com reta, interseção de dois planos e equações paramétricas de um plano
assunto: ga-04-planos-retas-espaco
tipo: prova
questao: vários
semestre: 2016.2 e 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | P2 (15.10.2016), Q2; Reposição 2 (03.11.2016), Q2b e Q3; Reavaliação AB2 (24.05.2017), Q3b
fontes_catalogo: ufal-ga-provas-2016,ufal-ga-provas-2017
autoria: Enunciados: provas de Geometria Analítica do Instituto de Matemática da UFAL (ver fontes_catalogo), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

Plano na forma geral $ax + by + cz + d = 0$: vetor normal $\mathbf{n} = (a, b, c)$. Dois planos são **paralelos** se os normais são múltiplos, e **coincidentes** se a equação inteira é múltipla.

**π: ax − 3y + cz + d = 0.**
- Paralelo a $5x + 2y + z = 4$: $(a, -3, c) = \lambda(5, 2, 1)$ com $\lambda = -\tfrac32$: $a = -\tfrac{15}{2}$, $c = -\tfrac32$ e $d \neq 6$ (com d = 6 seriam coincidentes).
- Coincidente com $x - y + 2z = -3$: multiplique $x - y + 2z + 3 = 0$ por 3: $a = 3$, $c = 6$, $d = 9$.
- Interseção com $r: x = 1 - 2t,\ y = 3 + t,\ z = -2 - 2t$: $(1 - 2t) - (3 + t) + 2(-2 - 2t) + 3 = -3 - 7t = 0$, $t = -\tfrac37$, ponto $(\tfrac{13}{7}, \tfrac{18}{7}, -\tfrac87)$.

**Interseção de dois planos (Reavaliação AB2, Q3b).** $3x - y + z = 1$ e o plano $x = 1 + 2s - t$, $y = -s - 2t$, $z = 2 - s + t$. Substituindo: $5 + 6s = 1$, $s = -\tfrac23$. Reta, na forma paramétrica: $x = -\tfrac13 - t$, $y = \tfrac23 - 2t$, $z = \tfrac83 + t$, com diretor $(-1, -2, 1)$.

**Paramétricas de $2x + y + 2z = 5$ (Reposição 2).** Isole y: $x = s$, $z = t$, $y = 5 - 2s - 2t$. Vetores do plano $(1, -2, 0)$ e $(0, -2, 1)$, ambos ortogonais a $(2, 1, 2)$.

**Verificação:** o diretor (−1, −2, 1) é ortogonal a (3, −1, 1) e ao normal do plano paramétrico, $(2,-1,-1)\times(-1,-2,1) = (-3,-1,-5)$; o ponto $(\tfrac{13}{7}, \tfrac{18}{7}, -\tfrac87)$ satisfaz $x - y + 2z = -3$.
