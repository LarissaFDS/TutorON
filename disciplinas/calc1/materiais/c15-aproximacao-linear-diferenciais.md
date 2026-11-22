---
id: calc1-aproximacao-linear
titulo: Aproximação linear (linearização) e diferenciais para estimar raiz, potência e seno: (63)^(2/3), sen 60°30', variação do volume de um cone, área de triângulo isósceles 3,2; 3,2; 2
assunto: calc1-06-taxas-aproximacao-linear
tipo: prova
questao: vários
semestre: 2014–2015
resolucao: sim
fonte: Provas de Cálculo 1, IM-UFAL | 3ª Avaliação (01.11.2014), Q2a e Q2b; 4ª prova (foto), Q3a; Avaliação Final (03.12.2015), Q3a; Questões para teste de escrita (Prof. José Lucyan, 09.06.2015), Q2
fontes_catalogo: ufal-im-calc1-provas-fotos,ufal-im-calc1-provas-pdf,ufal-calc1-listas-simulados
autoria: Enunciados: provas de Cálculo 1 do Instituto de Matemática da UFAL (professor não impresso nas provas), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova ou material da disciplina); fotos e PDFs originais não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

Como usar a aproximação linear para estimar uma raiz, uma potência ou um seno sem calculadora:

**Linearização:** perto de a, $f(x) \approx L(x) = f(a) + f'(a)(x - a)$. Escolha a onde f e f' são fáceis de calcular. Diferencial: $dy = f'(x)\,dx$. Ângulos sempre em **radianos**.

- $(63)^{2/3}$: $f(x) = x^{2/3}$, $a = 64$, $f(64) = 16$, $f'(64) = \tfrac23\cdot\tfrac14 = \tfrac16$. $L(63) = 16 - \tfrac16 = \tfrac{95}{6}$.
- $\operatorname{sen}60^\circ30'$: $30' = \tfrac{\pi}{360}$ rad; $\operatorname{sen}(\tfrac{\pi}{3} + \tfrac{\pi}{360}) \approx \tfrac{\sqrt3}{2} + \tfrac12\cdot\tfrac{\pi}{360}$.
- Cone de altura 2 m com raio de 1 m para 1,05 m: $V = \tfrac{\pi}{3}r^2h$, $dV = \tfrac{2\pi}{3}rh\,dr = \tfrac{2\pi}{3}\cdot1\cdot2\cdot0{,}05 = \tfrac{\pi}{15}$ m³ (cuidado: 100 cm = 1 m).
- Triângulo isósceles de lados 3,2; 3,2 e 2: altura $\sqrt{3{,}2^2 - 1} = \sqrt{9{,}24}$, área $= \sqrt{9{,}24}$. Com $\sqrt{x}$ em $a = 9$: $\sqrt{9{,}24} \approx 3 + \tfrac{0{,}24}{6} = 3{,}04$.

Erro comum: usar $30'$ como 0,5 (graus) na fórmula da derivada, que só vale em radianos.

**Verificação:** $63^{2/3} \approx 15{,}8332$ e $\tfrac{95}{6} \approx 15{,}8333$; $\operatorname{sen}(60{,}5^\circ) \approx 0{,}87036$ contra $0{,}87039$; $\sqrt{9{,}24} \approx 3{,}0397$.
