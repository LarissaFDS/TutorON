---
id: ga-parabola-reta-secante
titulo: Parábola de foco (0, 0) e diretriz y = −2: quantos pontos uma reta tem em comum com ela (enunciado corrigido: nem toda reta não vertical corta em dois pontos)
assunto: ga-07-parabola
tipo: prova
questao: 2a
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | 2ª Avaliação (11.03.2017), Q2a
fontes_catalogo: ufal-ga-provas-2017
autoria: Enunciado: Instituto de Matemática da UFAL (professor não impresso na prova), parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Questão de prova (enunciado parafraseado). Status da resolução: corrigida (resolução da equipe TutorON, conferida com SymPy; não é gabarito do professor).

Parábola de foco F(0, 0) e diretriz $y = -2$. Pela definição, $x^2 + y^2 = (y + 2)^2$, ou seja, $x^2 = 4(y + 1)$: vértice (0, −1), $p = 1$.

**Divergência.** O enunciado pede para mostrar que toda reta não perpendicular à diretriz "toda" (corta) a parábola em dois pontos. Como escrito, é falso. Contraexemplo: a reta $y = -5$ não é perpendicular à diretriz e não corta a parábola, pois $x^2 = -16$ não tem solução real.

**Correções da equipe.** O que vale:
- Reta perpendicular à diretriz (vertical, $x = x_0$): corta em **exatamente um** ponto, $(x_0, \tfrac{x_0^2}{4} - 1)$.
- Reta não vertical $y = mx + k$: $x^2 - 4mx - 4(1 + k) = 0$, com discriminante $16(m^2 + 1 + k)$. Dois pontos se $k > -1 - m^2$; um (reta tangente) se $k = -1 - m^2$; nenhum se $k < -1 - m^2$.
- Leitura possível do que se queria: toda reta não vertical **que passa pelo foco** corta em dois pontos, porque aí $k = 0 > -1 - m^2$.

Esta correção não é gabarito do professor; o enunciado pretendido precisa ser confirmado com ele.

**Verificação:** com $m = 0$ e $k = -1$ (tangente no vértice), $x^2 = 0$ dá um só ponto; com $k = 0$, $x = \pm2$, e os pontos (±2, 0) estão a 2 do foco e a 2 da diretriz.
