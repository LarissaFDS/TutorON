---
id: ga-distancia-retas-reversas
titulo: Como calcular a distância entre duas retas reversas pelo produto misto: diagonal do cubo de lado a e uma aresta que não a encontra (a√2/2)
assunto: ga-05-distancias-angulos-espaco
tipo: prova
questao: 4b
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Reavaliação AB2 (24.05.2017), Q4b
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
Questão de prova (enunciado parafraseado). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

**Retas reversas** não são paralelas nem se cortam. Para $r: P_1 + t\mathbf{d}_1$ e $s: P_2 + t\mathbf{d}_2$:
$d(r, s) = \dfrac{|(\mathbf{d}_1, \mathbf{d}_2, \overrightarrow{P_1P_2})|}{\|\mathbf{d}_1\times\mathbf{d}_2\|}$,
a altura do paralelepípedo de arestas $\mathbf{d}_1$, $\mathbf{d}_2$ e $\overrightarrow{P_1P_2}$. Se o produto misto der 0, as retas são concorrentes; se $\mathbf{d}_1\times\mathbf{d}_2 = \mathbf{0}$, são paralelas, e a distância é a de um ponto de uma à outra reta.

**Reavaliação AB2, Q4b: distância entre a diagonal do cubo de lado a e suas arestas.** Cubo em $[0, a]^3$.
- Diagonal: passa por (0, 0, 0), diretor $\mathbf{d}_1 = (1, 1, 1)$.
- As 6 arestas que saem de (0,0,0) ou de (a,a,a) tocam a diagonal (distância 0). As outras 6 são reversas a ela e, por simetria, estão à mesma distância. Exemplo: a aresta por $(a, 0, 0)$ com diretor $\mathbf{d}_2 = (0, 0, 1)$.
- $\mathbf{d}_1\times\mathbf{d}_2 = (1, -1, 0)$, norma $\sqrt2$; $\overrightarrow{P_1P_2} = (a, 0, 0)$; produto misto $= a$.
- $d = \dfrac{a}{\sqrt2} = \dfrac{a\sqrt2}{2}$, metade da diagonal de uma face.

**Verificação:** o segmento de $(\tfrac a2, \tfrac a2, \tfrac a2)$, na diagonal, até $(a, 0, \tfrac a2)$, na aresta, é $(\tfrac a2, -\tfrac a2, 0)$: perpendicular a (1, 1, 1) e a (0, 0, 1), com norma $\tfrac{a\sqrt2}{2}$. Com a = 1, minimizar numericamente a distância entre pontos das duas retas dá 0,7071.
