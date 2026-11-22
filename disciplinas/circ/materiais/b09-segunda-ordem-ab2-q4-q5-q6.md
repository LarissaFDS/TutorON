---
id: circ-davi-segunda-ordem-ab2-q4-q5-q6
titulo: RLC paralelo subamortecido, série superamortecido e série crítico: três questões de prova
assunto: circ-08-segunda-ordem
tipo: material_estudo
resolucao: sim
fonte: Prova AB2 do Prof. Davi (2017), questões 4, 5 e 6, e resolução fotografada
autoria: Prof. Davi Bibiano Brito (IC/UFAL), material de aula e provas de Circuitos Elétricos (2017); resolução da equipe TutorON, conferida por código
licenca: Não declarada (slides e provas do professor; fotos de resoluções sem identificação de aluno); arquivos fora do repositório
publicacao_transcricao: não declarada: conteúdo parafraseado, sem copiar slides, enunciados ou fotos; nomes e e-mails omitidos; confirmação da equipe pendente
fontes_catalogo: ufal-circ-davi-2017
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Material do Prof. Davi (IC/UFAL), parafraseado; resolução da equipe TutorON conferida por código, não é gabarito oficial. Status da resolução: validada.

**Q4, RLC paralelo (paráfrase).** Fonte de $1$ A, $8$ Ω e $0{,}04$ F em paralelo; em $t = 0$ uma chave liga também um indutor de $1$ H (descarregado). $v_C(0) = 8$ V, $i_L(0) = 0$ e, pela LKC, $C\,v'(0) = 1 - 8/8 - 0 = 0$. $\alpha = \dfrac{1}{2RC} = 1{,}5625$ s⁻¹, $\omega_0 = 5$ rad/s: **subamortecido**, $\omega_d = \sqrt{\omega_0^2 - \alpha^2} \approx 4{,}75$ rad/s. Valor final $0$ (o indutor curto-circuita).
$$v_C(t) = e^{-1{,}5625t}\left(8\cos 4{,}75t + 2{,}63\sin 4{,}75t\right)\ \text{V}.$$

**Q5, RLC série (paráfrase).** Fonte de $12$ V ligada em $t = 0$ a $1$ kΩ, $100$ mH e $1$ µF descarregados. $\alpha = R/2L = 5000$ s⁻¹, $\omega_0 = 1/\sqrt{LC} \approx 3162$ rad/s: **superamortecido**, $s_{1,2} = -5000 \pm \sqrt{15}\cdot 10^3$, isto é, $-1127$ e $-8873$ s⁻¹. Com $v_C(0) = 0$ e $v_C'(0) = 0$:
$$v_C(t) = 12 - 13{,}75\,e^{-1127t} + 1{,}75\,e^{-8873t}\ \text{V}.$$

**Q6, RLC série (paráfrase).** Antes da chave, $20$ V com $5$ Ω alimentam um ramo de $5$ Ω, $1$ H e uma fonte de $10$ V que soma com a de $20$ V: $i(0^-) = (20 + 10)/10 = 3$ A e $v_C(0^-) = 5$ V. Depois, o laço tem $10$ Ω, $1$ H e $0{,}04$ F: $\alpha = \omega_0 = 5$, **crítico**. A LKT dá $i'(0) = 10 + 5 - 10\cdot 3 = -15$ A/s, e
$$i(t) = 3\,e^{-5t}\ \text{A}.$$

As três resoluções fotografadas conferem com `dsolve`.

**Verificação:** Q4: $v(0) = 8$ e $v'(0) = -1{,}5625\cdot 8 + 4{,}75\cdot 2{,}63 \approx 0$. Q5: $12 - 13{,}75 + 1{,}75 = 0$. Q6: $i(0) = 3$ A, $i'(0) = -15$ A/s, $i(\infty) = 0$.
