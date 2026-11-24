---
id: fis3-prova1-q2-potencial-coroa
titulo: Prova 1 de Física 3, Q2 — potencial no eixo de uma coroa circular com σ uniforme (R = 13,0 cm, raio interno 0,200R, σ = 6,20 pC/cm², z = 2,00R): somar anéis dá V ≈ 103 V
assunto: fis3-02-potencial-eletrico
tipo: prova
questao: 2
resolucao: sim
fonte: Prova 1 de Física 3 (Instituto de Física, UFAL; Prof. Alexandre de Morais Carvalho; 19/08/2025; arquivo prova1_fsica_3.pdf), questão 2 | enunciado parafraseado
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
Prova 1 de Física 3 (IF-UFAL, Prof. Alexandre de Morais Carvalho, 2025), questão 2, parafraseada. Status da resolução: pendente de confirmação do professor (sem gabarito oficial; a resolução manuscrita que veio com a prova, de autoria não identificada, chega ao mesmo resultado). A resolução é da equipe TutorON e não é gabarito do professor. Prova é atividade avaliativa: o tutor guia, não entrega.

**Enunciado.** Coroa circular de raio externo $R = 13{,}0$ cm, raio interno $r_i = 0{,}200R$ e densidade superficial uniforme $\sigma = 6{,}20$ pC/cm². Com $V = 0$ no infinito, achar o potencial no ponto $P$ do eixo central a $z = 2{,}00R$ do centro.

**Ideia: dividir em anéis.** Um anel de raio $r'$ e espessura $dr'$ tem carga $dq = \sigma\,2\pi r'\,dr'$, toda à mesma distância $\sqrt{z^2 + r'^2}$ de $P$. Potencial é escalar, então basta somar:
$$V = \frac{1}{4\pi\varepsilon_0}\int_{r_i}^{R}\frac{\sigma\,2\pi r'\,dr'}{\sqrt{z^2 + r'^2}} = \frac{\sigma}{2\varepsilon_0}\left(\sqrt{z^2 + R^2} - \sqrt{z^2 + r_i^2}\right).$$
(É o potencial de um disco de raio $R$ menos o de um disco de raio $r_i$.)

**Números em SI.** $\sigma = 6{,}20\times10^{-12}$ C/cm² $= 6{,}20\times10^{-8}$ C/m²; $R = 0{,}130$ m, $r_i = 0{,}026$ m, $z = 0{,}260$ m. Os parênteses dão $R(\sqrt5 - \sqrt{4{,}04}) \approx 0{,}0294$ m e $\frac{\sigma}{2\varepsilon_0} \approx 3{,}50\times10^{3}$ V/m, logo
$$V(P) \approx 1{,}03\times10^{2}\ \text{V}.$$

Erros comuns: converter pC/cm² para C/m² multiplicando por $10^{-4}$ em vez de $10^{4}$; tratar o potencial como vetor; usar a carga total como se estivesse num ponto (perto da coroa isso não vale).

**Verificação:** `test_prova1_q2_potencial_coroa` faz a integral com SymPy, confere a forma fechada e o valor numérico (≈ 102,9 V).
