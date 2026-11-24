---
id: fis3-prova1-q1-gauss-cilindro
titulo: Prova 1 de Física 3, Q1 — Lei de Gauss num cilindro maciço infinito com densidade ρ uniforme: E = ρr/(2ε₀) dentro e E = ρR²/(2ε₀r) fora
assunto: fis3-01-lei-de-gauss
tipo: prova
questao: 1
resolucao: sim
fonte: Prova 1 de Física 3 (Instituto de Física, UFAL; Prof. Alexandre de Morais Carvalho; 19/08/2025; arquivo prova1_fsica_3.pdf), questão 1 | enunciado parafraseado
curso: Engenharia de Computação (UFAL), ECOM022 Física 3, 4º período; 2025
fontes_catalogo: ufal-fis3-prova1-2025
autoria: Enunciado: Prof. Alexandre de Morais Carvalho (IF-UFAL); resolução da equipe TutorON, conferida com SymPy e comparada com a resolução manuscrita que veio com a prova
licenca: Não declarada (prova da disciplina); PDF não versionado
publicacao_transcricao: não autorizada; enunciado parafraseado
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Prova 1 de Física 3 (IF-UFAL, Prof. Alexandre de Morais Carvalho, 2025), questão 1, parafraseada. Status da resolução: pendente de confirmação do professor (sem gabarito oficial; a resolução manuscrita que veio com a prova, de autoria não identificada, chega ao mesmo resultado). A resolução é da equipe TutorON e não é gabarito do professor. Prova é atividade avaliativa: o tutor guia, não entrega.

**Enunciado.** Cilindro maciço muito longo (infinito), raio $R$, carga uniforme no volume com densidade $\rho$ (C/m³). Pede-se o módulo do campo $E(r)$ (a) dentro, $r < R$, e (b) fora, $r > R$, usando a Lei de Gauss.

**Simetria.** Por ser infinito e uniforme, o campo é **radial** (perpendicular ao eixo) e só depende de $r$. Superfície gaussiana: cilindro coaxial de raio $r$ e comprimento $L$. Nas tampas, $\vec E$ é paralelo à superfície e o fluxo é zero; na lateral, $\vec E$ é normal e tem módulo constante: $\Phi = E(r)\cdot 2\pi rL$.

**(a) Dentro ($r < R$).** A carga envolvida é só a do cilindro de raio $r$: $q_{env} = \rho\,\pi r^2L$. Pela Lei de Gauss, $E\cdot 2\pi rL = \rho\pi r^2L/\varepsilon_0$, então
$$E(r) = \frac{\rho\,r}{2\varepsilon_0}\quad(r < R),$$
que cresce linearmente a partir de zero no eixo.

**(b) Fora ($r > R$).** A gaussiana envolve todo o cilindro de raio $R$: $q_{env} = \rho\,\pi R^2L$, e
$$E(r) = \frac{\rho\,R^2}{2\varepsilon_0\,r}\quad(r > R),$$
o mesmo campo de uma linha com densidade linear $\lambda = \rho\pi R^2$. Em $r = R$ as duas expressões dão $\frac{\rho R}{2\varepsilon_0}$: o campo é contínuo.

Erros comuns: usar o volume inteiro dentro (a carga envolvida depende de $r$); escrever $1/r^2$ como numa esfera (aqui é $1/r$); esquecer que o $L$ se cancela.

**Verificação:** `test_prova1_q1_gauss_cilindro` refaz as duas expressões pela Lei de Gauss e confere a continuidade em $r = R$ e o divergente $\nabla\cdot\vec E = \rho/\varepsilon_0$ dentro e $0$ fora.
