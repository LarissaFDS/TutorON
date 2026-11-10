---
id: sd-nota-conversores-memorias
titulo: Nota — conversores D/A e A/D, teorema da amostragem e memórias ROM/RAM
assunto: sd-12-conversores-memorias
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor); tópicos das ementas oficiais CCOM019 e ECOM019 (UFAL, 2011)
fontes_catalogo: ufal-ppc-cc-2011,ufal-ppc-ecomp-2011,kuphaldt-lec-vol4,wikilivros-eletronica-digital
autoria: Equipe TutorON, redigida com auxílio de IA; exemplo conferido por código; revisada pela responsável pela curadoria em 21/10/2026
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
Conversores e memórias

Conversor D/A (digital → analógico): a saída é proporcional ao valor binário de entrada. Saída = resolução × valor, em que a resolução (tamanho do degrau) é a saída para o valor 1. Com n bits há 2ⁿ níveis; o fundo de escala é resolução × (2ⁿ − 1). Exemplo: se 10100₂ = 20 dá 10 mA, o degrau é 0,5 mA e 11101₂ = 29 dá 14,5 mA. Implementações: resistores ponderados ou rede R-2R.

Conversor A/D (analógico → digital): transforma a tensão em um código de n bits. Resolução = faixa / 2ⁿ, e o erro de quantização é de até meio degrau (com arredondamento). Tipos: flash (comparadores em paralelo, rápido e caro), aproximações sucessivas (um bit por ciclo, usando um D/A interno) e rampa/contador.

Teorema da amostragem (Nyquist): para reconstruir um sinal de frequência máxima f_max, amostre com f_a > 2·f_max; abaixo disso ocorre aliasing.

Memórias:
- Organização: 2ᵏ palavras × m bits; k linhas de endereço, m linhas de dados. Capacidade = 2ᵏ × m bits (1 K × 8 = 1024 palavras de 8 bits).
- Internamente, um decodificador de endereço seleciona a palavra.
- ROM: só leitura no uso normal; implementa qualquer tabela-verdade (endereço = entradas, dado = saídas).
- RAM: leitura e escrita (sinal de escrita/leitura); SRAM (latches, rápida) e DRAM (capacitores, precisa de refresh).
- Banco de registradores: pequena memória rápida com portas de leitura e escrita, usada em processadores.
- Em projeto RTL, a memória entra no bloco operacional: a FSM gera o endereço (por exemplo, base + i) e o sinal de leitura, e o dado lido vai para um registrador.

Atenção: estes tópicos constam nas ementas oficiais de 2011, mas não apareceram nas listas e provas recentes recebidas, exceto a questão do D/A na Prova 1.
