---
id: iec-somadores
titulo: Meio-somador, somador completo e somador paralelo de 4 bits
assunto: iec-09-circuitos-combinacionais
tipo: material_estudo
resolucao: sim
fonte: Notas de aula Circuitos Combinacionais (ES572), Profa. Grace S. Deaecto (FEM-Unicamp, 2013), páginas 40 a 47
fontes_catalogo: unicamp-deaecto-combinacionais
autoria: Profa. Grace S. Deaecto (Unicamp), usadas na disciplina; parafraseadas pela equipe TutorON com auxílio de IA
licenca: Não declarada (material da professora)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Meio-somador** (entradas $A$ e $B$; saídas soma $S$ e carry $C_{out}$):

| A | B | S | Cout |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

$S=\overline{A}B+A\overline{B}=A\oplus B$ e $C_{out}=AB$: uma XOR e uma AND.

**Somador completo** (soma também o carry que entra, $C_{in}$): $S=A\oplus B\oplus C_{in}$ e $C_{out}=AB+(A\oplus B)C_{in}$. $S$ vale 1 com um número ímpar de 1s; $C_{out}$ vale 1 com pelo menos dois 1s. Monta-se com dois meio-somadores e uma OR.

**Somador paralelo de 4 bits:** quatro somadores completos; o $C_{out}$ de cada estágio liga no $C_{in}$ do seguinte, e o primeiro $C_{in}$ vale 0. Exemplo $0110+0111$ (6 + 7): bit 0: 0+1 = 1, carry 0; bit 1: 1+1 = 0, carry 1; bit 2: 1+1+1 = 1, carry 1; bit 3: 0+0+1 = 1, carry 0. Resultado $1101$ = 13.

Tanenbaum usa o mesmo somador dentro da **ULA de 1 bit**, que também faz AND e OR e escolhe a operação por um decodificador.

**Verificação:** o somador completo foi testado nas 8 combinações ($A+B+C_{in}=2C_{out}+S$) e o somador de 4 bits nos 256 pares de entradas (Python).
