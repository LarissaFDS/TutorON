---
id: sd-nota-aritmeticos
titulo: Nota — somador ripple-carry, subtrator, comparador de magnitude, incrementador e ULA
assunto: sd-05-circuitos-aritmeticos
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: wikibooks-digital-circuits,kuphaldt-lec-vol4,mit-ocw-6004
autoria: Equipe TutorON, redigida com auxílio de IA; revisada pela responsável pela curadoria em 21/10/2026
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Circuitos aritméticos

Somador completo: S = A ⊕ B ⊕ Cin; Cout = AB + ACin + BCin. Somador de n bits (ripple-carry): n somadores completos em cascata, com o Cout de cada bit no Cin do seguinte. O resultado tem n + 1 bits (com o vai-um). O atraso é proporcional a n; o carry-lookahead acelera calculando os vai-uns em paralelo, com gᵢ = aᵢbᵢ e pᵢ = aᵢ ⊕ bᵢ.

Subtrator: A − B = A + B' + 1. Somador + inversores em B + Cin = 1. Somador/subtrator: cada bᵢ passa por uma XOR com o sinal sub, e Cin = sub.

Overflow: sem sinal, o vai-um final; com sinal, V = Cₙ ⊕ Cₙ₋₁.

Comparador:
- Igualdade: eᵢ = (aᵢ ⊕ bᵢ)' e A = B = e₃e₂e₁e₀.
- Magnitude (do bit mais significativo para o menos): A > B = a₃b₃' + e₃a₂b₂' + e₃e₂a₁b₁' + e₃e₂e₁a₀b₀'; A < B é análogo, com a e b trocados. Alternativa: calcular A − B e olhar o vai-um e o zero.
- Em cascata: comparadores de 4 bits encadeados com entradas "igual, maior e menor vindos do estágio anterior".

Combinações frequentes em lista e prova:
- |A − B|: comparador (A ≥ B) seleciona por MUX entre A − B e B − A.
- MAX(0, X − Y): subtrai e, se o sinal do resultado for 1, a saída é 0 (MUX ou AND com o sinal negado).
- (A + B)/2: soma de n + 1 bits deslocada 1 à direita, ou seja, descartar o bit menos significativo.
- Incrementador: somador com B = 0 e Cin = 1 (ou meios somadores em cadeia); serve de contador i + 1 no projeto RTL.
- Saturação (clamp em [Y1, Y2]): dois comparadores e dois MUX.

ULA: calcula várias operações (soma, subtração, AND, OR…) e um MUX escolhe o resultado pelo código de operação.
