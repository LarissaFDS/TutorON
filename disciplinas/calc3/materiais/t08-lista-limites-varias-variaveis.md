---
id: calc3-lista-limites-varias-variaveis
titulo: Exercícios resolvidos de limites em várias variáveis — caminhos, continuidade, |x|/(|x|+|y|) e (1+x)^(y/x)
assunto: calc3-08-limites-derivadas-parciais
tipo: gabarito
questao: 1, 2, 6 e 8
resolucao: sim
fonte: Exercicios_Limites_Derivadas.pdf (página do Notion "Cálculo 3"; resolução manuscrita escaneada), páginas de limites
autoria: Resolução manuscrita anexada ao Notion da turma (autoria não identificada no arquivo); paráfrase e revisão da equipe TutorON
licenca: Não declarada (material de turma); o PDF não está no repositório
publicacao_transcricao: não autorizada até agora; o bloco parafraseia a resolução e não reproduz o manuscrito
fontes_catalogo: ufal-calc3-notion-resolucoes
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Resolução manuscrita da turma, parafraseada. Status da resolução: corrigida (um passo do exercício 6 foi reescrito; a conclusão do original se mantém). Conferida com SymPy.

Ex. 1. Uma função com $f(x, 0) = 3$ ao longo do eixo x e $f(0, y) = 5$ ao longo do eixo y não tem limite em (0, 0): dois caminhos, dois valores.

Ex. 2. Se $f$ é contínua em (2, 3) e $f(2, y) = y^3$, então $f(2, 3) = \lim_{y \to 3} f(2, y) = 27$: continuidade permite calcular o valor pelo limite ao longo de qualquer caminho.

Ex. 6. $\lim_{(x,y)\to(0,0)} \dfrac{|x|}{|x| + |y|}$. Ao longo de $y = mx$: $\dfrac{|x|}{|x| + |m||x|} = \dfrac{1}{1 + |m|}$.
- **Correção:** o original escreveu $\dfrac{1}{1+m}$, esquecendo o módulo em m. O valor certo é $\dfrac{1}{1+|m|}$ (com m = −1 o original daria divisão por zero; o correto dá 1/2).
- Conclusão (mantida): o valor depende de m (m = 0 dá 1, m = 1 dá 1/2), então o limite **não existe**.

Ex. 8. $\lim_{(x,y)\to(0,2)} (1+x)^{y/x}$. Escreva $(1+x)^{y/x} = \left[(1+x)^{1/x}\right]^{y}$. Quando $x \to 0$, $(1+x)^{1/x} \to e$, e $y \to 2$: o limite é $e^2$ (por continuidade da exponencial; a expressão não está definida em x = 0, o que não impede o limite).

**Verificação:** no ex. 8, em $x = 10^{-6}$, $y = 2$, $(1+x)^{y/x} \approx 7{,}389 \approx e^2$; no ex. 6, com m = −1, $|x|/(|x|+|-x|) = 1/2$.
