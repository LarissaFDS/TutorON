---
id: oac-nota-desempenho
titulo: Nota — desempenho: tempo de CPU, CPI, CPI médio, speedup, MIPS e Lei de Amdahl
assunto: oac-02-desempenho
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: ufal-oac-resumo-formulas,ufal-oac-anotacoes-manuscritas,ufal-oac-lista-cap1
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Desempenho do processador (Patterson & Hennessy, seções 1.6, 1.7 e 1.10). Reúne as fórmulas do resumo e das anotações dos alunos.

Definições: CPI = ciclos de clock por instrução (média). Ciclos de clock = Instruções × CPI. Frequência (taxa de clock, Hz) = 1 / Tempo de ciclo. Desempenho = 1 / Tempo de execução.

Tempo de CPU = Ciclos × Tempo de ciclo = Ciclos / Frequência = (Instruções × CPI) / Frequência.

CPI médio com várias classes: CPI_médio = Σ (frequência relativa da classe × CPI da classe). Ex.: 50% A (CPI 5), 30% B (CPI 2), 20% C (CPI 10) → 0,5×5 + 0,3×2 + 0,2×10 = 5,1. O CPI médio pode ser fracionário: não arredonde.

Speedup = Tempo antigo / Tempo novo = Desempenho novo / Desempenho antigo. "X é n vezes mais rápido que Y" quer dizer Tempo_Y / Tempo_X = n.

Frequência para atingir um tempo novo: f_novo = (Instruções × CPI_novo) / Tempo_novo.

Lei de Amdahl: Tempo novo = Tempo afetado / melhoria + Tempo não afetado. Speedup = 1 / ((1 − F) + F / S), com F a fração melhorada e S o fator. Ex.: F = 0,8 e S = 4 → 1 / (0,2 + 0,2) = 2,5. Mesmo com S infinito, o speedup não passa de 1 / (1 − F).

MIPS = Instruções / (Tempo × 10⁶) = Frequência / (CPI × 10⁶). Falácia: o MIPS não serve para comparar arquiteturas diferentes (o mesmo programa tem números de instruções diferentes) e varia de programa para programa no mesmo processador.

Comparar processadores: compare tempos, nunca só a frequência ou só o CPI. Um processador de clock menor pode ser mais rápido se tiver CPI menor ou executar menos instruções.

Potência dinâmica ∝ ½ × carga capacitiva × tensão² × frequência (power wall, seção 1.7).
