---
id: iec-conversao-bases-ip
titulo: Conversão decimal → binário → hexadecimal (divisões sucessivas e grupos de 4 bits); endereço IP 200.17.114.17
assunto: iec-05-numeracao-conversoes
tipo: prova
questao: 1
semestre: 2016.1
resolucao: sim
fonte: Fotos da Reavaliação AB1 de Introdução à Engenharia de Computação (ECOM006), UFAL, 2016.1, Q1
fontes_catalogo: ufal-iec-reav-ab1-2016
autoria: Enunciados: reavaliação da disciplina (professor não identificado na prova), parafraseados pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Método (Apêndice A de Tanenbaum):**
- Decimal → binário: **divisões sucessivas por 2**; os restos, lidos de baixo para cima, são os bits.
- Binário → hexadecimal: separe em **grupos de 4 bits** a partir da direita (octal: grupos de 3) e troque cada grupo pelo dígito (0–9, A–F).
- Volta para decimal: soma de potências, $\sum b_i 2^i$.

Exemplo: 156. $156/2=78$ resto 0; $78/2=39$ r 0; $39/2=19$ r 1; $19/2=9$ r 1; $9/2=4$ r 1; $4/2=2$ r 0; $2/2=1$ r 0; $1/2=0$ r 1. Lendo de baixo: $10011100_2$. Grupos 1001 1100 = $9C_{16}$; em octal 10 011 100 = $234_8$.

**Enunciado (Reavaliação AB1, Q1):** escrever o IP 200.17.114.17 em binário e em hexadecimal. Cada número é um **octeto** (8 bits, 0 a 255), convertido separadamente e completado com zeros à esquerda:

| decimal | binário | hex |
|---|---|---|
| 200 | 11001000 | C8 |
| 17 | 00010001 | 11 |
| 114 | 01110010 | 72 |
| 17 | 00010001 | 11 |

Resposta: 11001000.00010001.01110010.00010001 e C8.11.72.11 (0xC8117211).

**Verificação:** de volta, $C8_{16}=12\cdot16+8=200$, $72_{16}=7\cdot16+2=114$, $11_{16}=17$ e $10011100_2=128+16+8+4=156$.
