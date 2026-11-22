---
id: circ-davi-primeira-ordem-teoria
titulo: Capacitor, indutor e circuitos RC e RL de primeira ordem: resposta natural e ao degrau
assunto: circ-07-primeira-ordem
tipo: material_estudo
resolucao: nao
fonte: Slides do Prof. Davi, aulas 6 e 7 (indutância, capacitância, RL e RC)
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

**Elementos.** Capacitor: $i = C\,\dfrac{dv}{dt}$, energia $\tfrac12 Cv^2$; sua **tensão** não muda de forma instantânea e, em regime CC, ele é um circuito aberto. Indutor: $v = L\,\dfrac{di}{dt}$, energia $\tfrac12 Li^2$; sua **corrente** não muda de forma instantânea e, em regime CC, ele é um curto. Capacitores em paralelo somam; indutores em série somam.

**Constante de tempo.** Reduza o resto do circuito a um Thévenin visto pelo elemento: $\tau = R_{Th}C$ (RC) ou $\tau = L/R_{Th}$ (RL), em segundos.

**Resposta geral** (fonte constante depois da chave):
$$x(t) = x(\infty) + \left[x(0^+) - x(\infty)\right]e^{-t/\tau},\quad t > 0,$$
com $x = v_C$ ou $i_L$. Receita: (1) circuito antes da chave em regime CC: $v_C(0^-)$ ou $i_L(0^-)$; (2) continuidade: $v_C(0^+) = v_C(0^-)$, $i_L(0^+) = i_L(0^-)$; (3) circuito depois da chave em regime CC: $x(\infty)$; (4) $R_{Th}$ e $\tau$; (5) as outras grandezas saem de $x(t)$ por LKC e LKT.

**Resposta natural**: sem fonte depois da chave, $x(\infty) = 0$ e $x(t) = x(0)e^{-t/\tau}$. **Resposta ao degrau**: fonte constante, $x(\infty) \neq 0$. Em $5\tau$ resta menos de $1\%$ do transitório. Chaveamento sequencial: a condição final de um intervalo é a inicial do seguinte.

**Integrador com amp-op**: entrada por $R$, capacitor $C$ na realimentação: $v_o(t) = -\dfrac{1}{RC}\displaystyle\int_0^t v_s\,dt + v_o(0)$.

**Verificação:** em $x(t)$, $t = 0$ dá $x(0^+)$ e $t \to \infty$ dá $x(\infty)$; a derivada em $0^+$ é $-[x(0^+) - x(\infty)]/\tau$.
