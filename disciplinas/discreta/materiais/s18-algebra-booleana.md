---
id: discreta-algebra-booleana
titulo: Álgebra booleana — axiomas, dualidade e prova de identidades
assunto: discreta-10-estruturas-algebricas-booleanas
tipo: material_estudo
resolucao: sim
fonte: Slides de Álgebra Booleana do Prof. Leandro Balby Marinho (UFCG)
fontes_catalogo: ufcg-discreta-leandro
autoria: Prof. Leandro Balby Marinho (UFCG), parafraseado pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Uma **álgebra booleana** [B, +, ·, ', 0, 1] tem duas operações binárias, um complemento e dois elementos distintos 0 e 1, com os axiomas (para todos x, y, z de B):
- comutatividade: x + y = y + x e x · y = y · x;
- associatividade: (x + y) + z = x + (y + z) e (x · y) · z = x · (y · z);
- distributividade: x + (y · z) = (x + y) · (x + z) e x · (y + z) = x · y + x · z;
- neutros: x + 0 = x e x · 1 = x;
- complemento: x + x' = 1 e x · x' = 0.

Modelos: a lógica ({F, V}, ∨, ∧, ¬), os conjuntos (𝒫(S), ∪, ∩, complemento, ∅, S) e os bits ({0, 1}, OR, AND, NOT).

**Dualidade**: trocando + por ·, e 0 por 1, em uma identidade válida, obtém-se outra identidade válida. Ex.: de x + 0 = x sai x · 1 = x.

Consequências (provadas a partir dos axiomas):
- idempotência: x + x = x;
- absorção: x + x · y = x;
- De Morgan: (x + y)' = x' · y';
- complemento duplo: (x')' = x.

**Como provar uma identidade pelos axiomas** (cite o axioma em cada passo). Ex.: x + x = x.
x + x = (x + x) · 1 (neutro) = (x + x) · (x + x') (complemento) = x + x · x' (distributividade) = x + 0 (complemento) = x (neutro). ∎

Em {0, 1}, também se pode provar por tabela-verdade, testando todas as combinações. Isso **não** vale como prova para uma álgebra booleana qualquer, a não ser que o enunciado peça só o caso {0, 1}. A simplificação de circuitos e os mapas de Karnaugh são estudados em Sistemas Digitais.

Status da resolução: validada (conferida por código pela equipe TutorON).

**Verificação:** idempotência, absorção, De Morgan e distributividade conferidas por código em {0, 1} e em 𝒫({1, 2, 3}).
