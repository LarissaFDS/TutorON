---
id: circ-davi-primeira-ordem-ab2-q2-q3
titulo: RC com chave e RL com indutor em curto: duas questões de prova resolvidas
assunto: circ-07-primeira-ordem
tipo: material_estudo
resolucao: sim
fonte: Prova AB2 do Prof. Davi (2017), questões 2 e 3, e resolução fotografada
autoria: Prof. Davi Bibiano Brito (IC/UFAL), material de aula e provas de Circuitos Elétricos (2017); resolução da equipe TutorON, conferida por código
licenca: Não declarada (slides e provas do professor; fotos de resoluções sem identificação de aluno); arquivos fora do repositório
publicacao_transcricao: não declarada: conteúdo parafraseado, sem copiar slides, enunciados ou fotos; nomes e e-mails omitidos; confirmação da equipe pendente
fontes_catalogo: ufal-circ-davi-2017
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Material do Prof. Davi (IC/UFAL), parafraseado; resolução da equipe TutorON conferida por código, não é gabarito oficial. Status da resolução: corrigida.

**Q2 (paráfrase).** Nó P: uma fonte de $12$ V (+ em cima) em série com $4$ kΩ vai de P à referência. De P ao nó de saída Q, $12$ kΩ em paralelo com um capacitor de $100$ µF; de Q à referência, $8$ kΩ ($v_o$). Antes de $t = 0$, uma chave fechada liga P à referência por uma fonte de $6$ V, que fixa $v_P = 6$ V; em $t = 0$ ela abre.

Antes: $v_C(0^-) = 6 \cdot \dfrac{12}{12 + 8} = 3{,}6$ V (o ramo de $12$ V não muda $v_P$). Depois: $v_C(\infty) = 12 \cdot \dfrac{12}{24} = 6$ V; $R_{Th} = 12\text{k} \parallel (4\text{k} + 8\text{k}) = 6$ kΩ, $\tau = 0{,}6$ s. Então $v_C(t) = 6 - 2{,}4e^{-t/0{,}6}$ V e, pela LKT, $v_o = \tfrac{2}{3}(12 - v_C)$:
$$v_o(t) = 4 + 1{,}6\,e^{-5t/3}\ \text{V},\quad t > 0 .$$

**Q3 (paráfrase).** Uma fonte de $5$ mA alimenta, antes da chave, um indutor de $1$ mH que está em curto sobre a rede de resistores: $i_L(0^-) = 5$ mA. Depois da chave, o indutor vê $1\text{k} \parallel [(1\text{k} + 1\text{k}) \parallel 2\text{k} + 2\text{k}] = 750$ Ω (redução da resolução fotografada), e $\tau = L/R = 1\text{ mH}/750\ \Omega \approx 1{,}33$ µs. Logo $i(t) = 5\,e^{-7{,}5\times 10^{5}t}$ mA.

**Correções:** na Q2 a foto escreve o expoente como $-1{,}6t$; o certo é $-t/0{,}6 = -\tfrac{5}{3}t$ (o valor numérico de $v_o$ e $v_C$ nos instantes $0$ e $\infty$ confere). Na Q3, a foto chama a constante de tempo de "1,3 ms"; é $1{,}33$ **µs** (o expoente $7{,}5 \times 10^5$ escrito está certo).

**Verificação:** Q2: $v_o(0^+) = \tfrac23(12 - 3{,}6) = 5{,}6 = 4 + 1{,}6$ V e $v_o(\infty) = 12\cdot 8/24 = 4$ V. Q3: $1/\tau = 750/10^{-3} = 7{,}5 \times 10^5$ s⁻¹.
