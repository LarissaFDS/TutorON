---
id: iec-sistemas-numeracao-negativos
titulo: Bases 2, 8, 10 e 16 e os quatro sistemas de números negativos (sinal-magnitude, complemento de 1, complemento de 2, excesso)
assunto: iec-05-numeracao-conversoes
tipo: material_estudo
resolucao: sim
fonte: Slides do Apêndice A (Números binários), Tanenbaum, Pearson, slides 2 a 8
fontes_catalogo: pearson-tanenbaum-slides
autoria: Slides da editora Pearson, usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Protegido (© 2014 Pearson, todos os direitos reservados): só paráfrase
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Bases:** decimal usa 10 dígitos (0–9); binário, 2 (0, 1); octal, 8 (0–7); hexadecimal, 16 (0–9 e A=10, B=11, C=12, D=13, E=14, F=15). O valor é a soma de cada dígito vezes a base elevada à posição: $2A_{16}=2\cdot16+10=42$.

Conversões diretas: binário ↔ octal em grupos de **3** bits; binário ↔ hexadecimal em grupos de **4** bits, contados a partir da vírgula. Decimal → binário: subtraindo a maior potência de 2 possível (pela definição) ou por divisões sucessivas (só inteiros).

**Números negativos com $m$ bits** (exemplo: $-6$ com 8 bits):
- **Sinal-magnitude:** o bit da esquerda é o sinal: 10000110.
- **Complemento de 1:** inverta todos os bits de +6 (00000110): 11111001. Tem dois zeros (+0 e −0).
- **Complemento de 2:** complemento de 1 mais 1: 11111010. Um só zero; intervalo de $-2^{m-1}$ a $2^{m-1}-1$ (−128 a 127 em 8 bits).
- **Excesso $2^{m-1}$:** guarda o número somado a 128: $-6+128=122=01111010$. É o complemento de 2 com o primeiro bit invertido.

**Verificação:** 11111010 em complemento de 2 vale $-128+122=-6$; 01111010 em excesso 128 vale $122-128=-6$.
