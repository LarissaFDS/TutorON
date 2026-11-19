---
id: sinais-anot-funcao-transferencia
titulo: Função de transferência G(s) = Y(s)/U(s) com condições iniciais nulas: polos e zeros; exemplo de circuito Y/U = (s + 0,5)/(s² + 3s + 2,25)
assunto: sinais-10-funcao-transferencia
tipo: resolucao
resolucao: sim
fonte: Anotações manuscritas "Representação por função de transferência" (19 jun. 2026)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sinais e Sistemas 2026.1; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.1); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), informada em 18/11/2026; enunciados de livros e de provas parafraseados; fotos e figuras coladas não foram copiadas
fontes_catalogo: ufal-sinais-anotacoes-otavio-2026-1
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.1), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Definição:** $G(s) = \frac{Y(s)}{U(s)}$ com **condições iniciais nulas**; também $G(s) = \mathcal{L}\{g(t)\}$ (resposta ao impulso). Para a EDO $\sum a_iy^{(i)} = \sum b_ku^{(k)}$: $G(s) = \frac{B(s)}{A(s)}$. **Polos**: raízes de $A(s)$ (polinômio característico). **Zeros**: raízes de $B(s)$. Estritamente própria: grau de $B$ menor que o de $A$.

**Exemplo (circuito descrito):** fonte de tensão $u(t)$ em série com 2,5 Ω e 1 H; a corrente $y(t)$ alimenta 2 Ω em paralelo com 1 F (tensão $v_C$). Equações: $u = 2{,}5y + \dot y + v_C$ e $y = \frac{v_C}{2} + \dot v_C$. Com CI nulas: $V_C = \frac{Y}{s + 0{,}5}$ e
$$U = \left(s + 2{,}5 + \frac{1}{s + 0{,}5}\right)Y \Rightarrow G(s) = \frac{Y(s)}{U(s)} = \frac{s + 0{,}5}{s^2 + 3s + 2{,}25}.$$
Zero em $-0{,}5$; polo duplo em $-1{,}5$, pois $s^2 + 3s + 2{,}25 = (s + 1{,}5)^2$.

O exercício "para fazer" seguinte (circuito com fonte de corrente e fonte dependente $4v_L$) não tem resolução nas anotações e não entrou.

**Verificação:** resolvendo as duas equações em $s$ com SymPy sai a mesma $G(s)$; ganho DC $G(0) = 0{,}5/2{,}25 = 2/9$, igual a $1/(2{,}5 + 2)$ (em CC o indutor é curto e o capacitor aberto: $u/(2{,}5 + 2)$).
