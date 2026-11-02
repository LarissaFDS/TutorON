---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações de alunos no Notion da turma); imagens e arquivos anexos não estão no repositório
publicacao_transcricao: não se aplica: o bloco resume com texto próprio as anotações; trechos de código curtos foram conferidos
revisao_humana: pendente
fontes_catalogo: ufal-oac-notion
id: oac-notion-cap6-paralelismo
titulo: Anotações da turma (Notion) — cap. 6: Amdahl, speedup, SISD/SIMD/MIMD, multithreading, SMP, GPU e roofline
assunto: oac-16-paralelismo
tipo: material_estudo
fonte: Notion da turma, página "Capítulo 6" e subpágina "Perplexity" (resumos feitos com assistente de IA para a lista do cap. 6)
autoria: Alunos da turma de OAC (UFAL), com assistente de IA; revisão da equipe TutorON
status_resolucao: corrigida
---
Resumo da turma para o cap. 6. Status da resolução: corrigida (contagem do Ex. 1 e princípios de DSA; ver abaixo).

Speedup S = T1 / Tp; eficiência E = S / P. Amdahl: S = 1 / ((1 − f) + f / P), f = fração paralelizável. Gustafson (problema cresce com P): S = (1 − f) + f P.
Para E ≥ 0,9: f ≥ (P − 1/0,9) / (P − 1); P = 10 → f ≥ 0,988; P = 100 → f ≥ 0,9989.
Flynn: SISD (CPU escalar), SIMD (mesma instrução em vários dados: extensões vetoriais, GPU), MIMD (multicore, cluster).
Multithreading: grão grosso (troca de thread só em eventos longos, como falta na cache), grão fino (troca a cada ciclo), SMT (várias threads emitem no mesmo ciclo).
SMP: um só espaço de endereços, comunicação por variáveis compartilhadas e barreiras, exige coerência de cache. Sem memória compartilhada: troca de mensagens. Código com sum[] compartilhado e barreira é SMP.
GPU otimiza vazão (SIMT); CPU, latência.
Cinco princípios das arquiteturas de domínio específico (DSA), como no livro e na subpágina Perplexity: (1) memórias dedicadas para reduzir movimentação de dados; (2) gastar os recursos poupados de otimizações de microarquitetura em mais unidades aritméticas ou memórias maiores; (3) usar a forma de paralelismo mais simples que serve ao domínio; (4) reduzir tamanho e tipo dos dados ao mínimo necessário; (5) usar linguagem de programação do domínio. Correção da equipe: a lista da página principal (especializar o datapath, otimizar energia, co-projeto HW/SW) não é a do livro.
Roofline: eixo x = intensidade aritmética (FLOP/byte); à esquerda do joelho o limite é a banda de memória, à direita o pico de FLOP/s.

Correção da equipe no Ex. 1 (somar 10 escalares e duas matrizes 10 × 10): as anotações contam 9 somas para os escalares. O exemplo do livro conta 10 somas sequenciais e 100 paralelizáveis: T1 = 110 t. Com 10 processadores: 10 t + 100 t / 10 = 20 t, S = 5,5 (55% do ideal). Com 100: 10 t + 1 t = 11 t, S = 10 (10% do ideal).
