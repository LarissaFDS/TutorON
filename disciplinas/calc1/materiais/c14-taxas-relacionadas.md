---
id: calc1-taxas-relacionadas
titulo: Taxas relacionadas: tanque cônico enchendo, ponteiros do relógio, cilindro de volume constante, esfera inscrita num cubo (roteiro serve para escada deslizando e sombra)
assunto: calc1-06-taxas-aproximacao-linear
tipo: prova
questao: vários
semestre: 2014–2015
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 4ª prova (foto), Q2a; 3ª Avaliação (01.11.2014), Q1a e Q1b; Avaliação Final (03.12.2015), Q10
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-im-calc1-provas-pdf
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL (professor não impresso nas provas), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

**Roteiro (vale para escada deslizando na parede, sombra, balão, tanque):** (1) desenhe e nomeie as variáveis que mudam com o tempo; (2) escreva a relação geométrica entre elas (Pitágoras, semelhança, volume, lei dos cossenos); (3) derive em relação a t com a regra da cadeia; (4) **só então** substitua os valores do instante. Substituir antes de derivar transforma variável em constante e zera a taxa.

- **Cone de 10 m de altura e 4 m de raio, enchendo a $25\pi$ m³/min.** Semelhança: $r = \tfrac{2h}{5}$, $V = \tfrac{\pi}{3}r^2h = \tfrac{4\pi}{75}h^3$, $\tfrac{dV}{dt} = \tfrac{4\pi}{25}h^2\tfrac{dh}{dt}$. Em $h = 5$: $25\pi = 4\pi\tfrac{dh}{dt}$, $\tfrac{dh}{dt} = \tfrac{25}{4}$ m/min.
- **Ponteiros de 16 cm e 8 cm às 2 h.** $D^2 = 16^2 + 8^2 - 2\cdot16\cdot8\cos\theta$, $\theta = \tfrac{\pi}{3}$ às 2 h, $D = 8\sqrt3$. O ângulo diminui a $\tfrac{2\pi}{60} - \tfrac{2\pi}{720} = \tfrac{11\pi}{360}$ rad/min. $2D\,D' = 256\operatorname{sen}\theta\,\theta'$ dá $D' = -\tfrac{11\pi}{45}$ cm/min (a distância diminui).
- **Cilindro de volume constante**, diâmetro 20 cm, altura 40 cm, altura crescendo 2 cm/min: $0 = 2rhr' + r^2h'$, $r' = -\tfrac{rh'}{2h} = -\tfrac14$ cm/min.
- **Esfera inscrita num cubo** com diagonal crescendo 3 mm/s: $d = a\sqrt3$, $a' = \sqrt3$; $V = \tfrac{\pi a^3}{6}$, $V' = \tfrac{\pi a^2}{2}a'$. Com aresta $4\sqrt3$ mm (lida como "4 3"), $V' = 24\sqrt3\,\pi$ mm³/s.

**Verificação:** derivar $V(h(t))$ com SymPy e substituir $h = 5$ dá $dh/dt = 25/4$.
