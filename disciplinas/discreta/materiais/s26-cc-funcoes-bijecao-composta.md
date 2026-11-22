---
id: discreta-cc-funcoes-bijecao-composta
titulo: Função bijetora, função mal definida, composta com inversa e termo geral de sequência (provas de CC)
assunto: discreta-05-funcoes
tipo: resolucao
resolucao: sim
questao: Prova 1 2020.2 e 2021.1 (Q4, Q5); Reavaliação 1 2020.2 (Q4); Prova 1 de 2017 (Q6 a Q8)
fonte: Provas do Prof. Bruno Pimentel (2020.2 e 2021.1) e Prova Escrita 01 do Prof. Lucas Amorim (2017)
curso: Ciência da Computação (UFAL), turmas de 2017 (Prof. Lucas Amorim) e 2020.2/2021.1 (Prof. Bruno Pimentel)
fontes_catalogo: ufal-cc-discreta-provas-bruno,ufal-cc-discreta-prova-lucas-2017
autoria: Profs. Bruno Pimentel e Lucas Amorim (IC-UFAL), enunciados parafraseados; resolução da equipe TutorON com auxílio de IA
licenca: Não declarada (provas do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia os enunciados e traz resolução própria; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Resolução da equipe TutorON, não é gabarito do professor. Status da resolução: validada.

**Antes de perguntar se é bijetora, confira se é função.** Em $\{a,b,c,d\}\to\{a,b,c,d\}$:
- $f(a)=b,\ f(b)=a,\ f(d)=d$: $f(c)$ não foi definido, então f **não é função** de todo o conjunto e não pode ser bijeção;
- $f(a)=b,\ f(b)=b,\ f(c)=d,\ f(d)=c$: a e b têm a mesma imagem, então não é injetiva; também não é sobrejetiva (a fica sem pré-imagem).

O mesmo cuidado vale para $g(x)=1/x$ "de $\mathbb{N}$ em $\mathbb{N}$": $g(0)$ não existe e $g(2)=1/2\notin\mathbb{N}$. Antes de compor, diga que g não é função de $\mathbb{N}$ em $\mathbb{N}$. Já $f(x)=x+1$ dá $(f\circ f)(x)=x+2$, injetiva e não sobrejetiva em $\mathbb{N}$ (0 e 1 ficam sem pré-imagem).

**Existe?** De $A=\{1,\dots,5\}$ em $B=\{a,b,c,d\}$ não há função injetiva (5 > 4, casa dos pombos); de B em A não há sobrejetiva nem bijetiva.

**Composta com inversa:** $(f\circ g^{-1})(y)=f(g^{-1}(y))$. Ache $g^{-1}$ isolando x:
- $g(x)=2x-5$, $f(x)=x^2+x$: $g^{-1}(2)=7/2$ e $f(7/2)=63/4$;
- $g(x)=3x+4$, $f(x)=x^2+2x$: $g^{-1}(2)=-2/3$ e $f(-2/3)=-8/9$;
- $g(x)=x-2$, $f(x)=x^2+2x$: $f(g^{-1}(2))=f(4)=24$ e $g^{-1}(f(1))=g^{-1}(3)=5$.

A ordem importa: $f\circ g^{-1}$ aplica $g^{-1}$ primeiro.

**Termo geral:** 5, 95, 995, 9995, … é $a_n=10^n-5$ para $n\ge1$.

**Verificação:** as compostas foram calculadas com frações exatas em Python, a não injetividade por contagem de imagens e o termo geral comparado com os quatro primeiros termos.
