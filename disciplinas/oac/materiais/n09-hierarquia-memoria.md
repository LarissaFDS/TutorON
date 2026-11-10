---
id: oac-nota-hierarquia-memoria
titulo: Nota — hierarquia de memória: localidade, caches, mapeamento e tempo médio de acesso
assunto: oac-15-hierarquia-memoria
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: pattersonhennessy-cod-riscv,cs61c-berkeley
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Hierarquia de memória (Patterson & Hennessy, cap. 5). Tópico fundamental do livro; confirmado nas anotações da turma do cap. 5 (bloco oac-notion-cap5-memoria).

Localidade temporal (o mesmo dado volta a ser usado) e espacial (dados vizinhos são usados em seguida) justificam a hierarquia: registradores → caches → memória principal → disco, cada nível maior, mais lento e mais barato por byte.

Termos: acerto (hit), falta (miss), taxa de faltas, penalidade de falta, bloco (linha).

Cache diretamente mapeada: endereço = tag | índice | offset. Com blocos de 2ᵇ bytes e 2ⁿ linhas: offset = b bits, índice = n bits, tag = restante. Linha = (endereço do bloco) mod (número de linhas). Associativa por conjunto de k vias: o índice escolhe o conjunto e o bloco pode ficar em qualquer uma das k vias; totalmente associativa: um único conjunto.
Exemplo da equipe: endereço de 32 bits, cache de 16 KiB com blocos de 16 bytes, diretamente mapeada → 1024 linhas; offset = 4 bits, índice = 10 bits, tag = 18 bits.

Tempo médio de acesso (AMAT) = tempo de acerto + taxa de faltas × penalidade. Ex.: 1 ciclo + 0,05 × 100 ciclos = 6 ciclos.
Ciclos de stall de memória = acessos × taxa de faltas × penalidade.

Tipos de falta (3 Cs): compulsória, de capacidade, de conflito. Escrita: write-through (com buffer) × write-back (bit sujo).

Memória virtual: páginas, tabela de páginas, TLB (cache de traduções) e falta de página tratada pelo sistema operacional.
