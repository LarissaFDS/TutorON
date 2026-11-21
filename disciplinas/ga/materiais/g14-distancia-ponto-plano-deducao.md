---
id: ga-distancia-ponto-plano-deducao
titulo: Dedução da distância de ponto a plano pelo produto misto, d = |(u, v, AP)|/‖u × v‖ (altura do paralelepípedo), fórmula |ax₀ + by₀ + cz₀ + d|/√(a² + b² + c²) e cossenos diretores
assunto: ga-05-distancias-angulos-espaco
tipo: prova
questao: 2b; 3a, 3c, 4
semestre: 2016.2 e 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | Reavaliação AB2 (24.05.2017), Q2b; P2 (15.10.2016), Q3a, Q3c e Q4
fontes_catalogo: ufal-ga-provas-2017,ufal-ga-provas-2016
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

**Dedução geométrica.** Plano α por A, com vetores paralelos u e v. Monte o paralelepípedo de arestas u, v e $\overrightarrow{AP}$:
- a base é o paralelogramo de u e v, de área $\|\mathbf{u}\times\mathbf{v}\|$ (interpretação do produto vetorial);
- o volume é $|(\mathbf{u}, \mathbf{v}, \overrightarrow{AP})|$ (interpretação do produto misto);
- volume = área da base × altura, e a altura é a distância de P a α.
Logo $d = \dfrac{|(\mathbf{u}, \mathbf{v}, \overrightarrow{AP})|}{\|\mathbf{u}\times\mathbf{v}\|}$. Na P2 de 2016 a mesma ideia aparece com $\overrightarrow{AB}$ e $\overrightarrow{AC}$.

**Ligação com a fórmula vista em aula.** Com $\mathbf{n} = (a, b, c) = \mathbf{u}\times\mathbf{v}$ e o plano $ax + by + cz + d = 0$: $(\mathbf{u}, \mathbf{v}, \overrightarrow{AP}) = \mathbf{n}\cdot(P - A) = ax_0 + by_0 + cz_0 + d$. Então $d(P, \alpha) = \dfrac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}}$. Com A(1,2,2), B(0,−1,3), C(3,−1,1) e P(4,2,3), os dois caminhos dão $27/\sqrt{118}$.

**Cossenos diretores (P2, Q4).** Para $\mathbf{u} = (x, y, z) \neq \mathbf{0}$: $\cos\alpha = \dfrac{x}{\|\mathbf{u}\|}$, $\cos\beta = \dfrac{y}{\|\mathbf{u}\|}$, $\cos\delta = \dfrac{z}{\|\mathbf{u}\|}$ (produto escalar com i, j, k). Somando os quadrados: $\dfrac{x^2 + y^2 + z^2}{\|\mathbf{u}\|^2} = 1$.

**Verificação:** $(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AP}) = (6,1,9)\cdot(3,0,1) = 27$ e $\|(6,1,9)\| = \sqrt{118}$; para u = (1, 2, 2), os cossenos 1/3, 2/3 e 2/3 têm quadrados que somam 1.
