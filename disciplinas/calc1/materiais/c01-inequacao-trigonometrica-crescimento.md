---
id: calc1-inequacao-trig-crescimento
titulo: Inequações na derivada: intervalos onde f(x) = −cos x + sen x + ln 99 é crescente (sen x + cos x > 0)
assunto: calc1-01-funcoes-inequacoes-modulo
tipo: exercicio
questao: exercício
semestre: 2013–2014
resolucao: sim
fonte: Material de apoio de Cálculo 1 (UFAL): dica "estudem as inequações" e exercício de intervalos de crescimento
fontes_catalogo: ufal-calc1-dicas-apoio
autoria: Material de apoio da turma, autoria não identificada, parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exercício do material de apoio (enunciado parafraseado). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

O material de apoio insiste: muita questão de derivada termina numa **inequação** de ensino médio. Exemplo: em que intervalos $f(x) = -\cos x + \operatorname{sen} x + \ln 99$ é crescente?

1. Domínio: todos os reais. $f'(x) = \operatorname{sen} x + \cos x$ (a constante $\ln 99$ tem derivada 0).
2. Crescente onde $f'(x) > 0$, ou seja, $\operatorname{sen} x + \cos x > 0$.
3. Técnica (fator auxiliar): $\operatorname{sen} x + \cos x = \sqrt2\,\operatorname{sen}\!\left(x + \tfrac{\pi}{4}\right)$ (raiz de 2 vezes seno de x mais pi sobre 4).
4. $\operatorname{sen}(x + \tfrac{\pi}{4}) > 0 \iff 2k\pi < x + \tfrac{\pi}{4} < \pi + 2k\pi$, isto é, $x \in \left(-\tfrac{\pi}{4} + 2k\pi,\ \tfrac{3\pi}{4} + 2k\pi\right)$, $k$ inteiro.

Caminho sugerido pelo material: separar os casos $\cos x > 0$ (dividir por $\cos x$ mantém o sinal: $\operatorname{tg} x > -1$), $\cos x < 0$ (inverte: $\operatorname{tg} x < -1$) e $\cos x = 0$ (conferir direto). Os dois caminhos dão o mesmo conjunto.

**Módulo em inequação:** $|x - a| < r \iff a - r < x < a + r$; com produto ou quociente, faça o quadro de sinais com as raízes de cada fator.

Erro comum: dividir a inequação por $\cos x$ sem olhar o sinal.

**Verificação:** em $x = 0$, $f'(0) = 1 > 0$ (dentro do intervalo); em $x = \pi$, $f'(\pi) = -1 < 0$ (fora).
