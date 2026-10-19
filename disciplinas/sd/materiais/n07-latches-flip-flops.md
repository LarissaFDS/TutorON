---
id: sd-nota-latches-flip-flops
titulo: Nota — latch SR e D, flip-flop D, JK e T, borda de clock e diagrama de tempo
assunto: sd-07-latches-flip-flops
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: wikibooks-digital-circuits,kuphaldt-lec-vol4,wikilivros-eletronica-digital
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
Latches e flip-flops

Latch SR (com NOR): S = 1 seta (Q = 1); R = 1 reseta (Q = 0); S = R = 0 mantém; S = R = 1 é proibido. É sensível a nível.

Latch D (com enable/clock C): enquanto C = 1, Q segue D (transparente); com C = 0, mantém o último valor. Problema: durante todo o nível alto, mudanças de D passam para Q.

Flip-flop D (disparado por borda): só copia D no instante da borda ativa (normalmente a de subida, indicada pelo triângulo no símbolo; com bolinha, a de descida). Entre bordas, Q não muda. É o elemento de memória dos registradores e das máquinas de estados síncronas. Equação característica: Q+ = D.

Como desenhar Q de um flip-flop D a partir do diagrama de tempo:
1. Marque cada borda de subida do clock.
2. Em cada borda, leia D imediatamente antes dela.
3. Q passa a esse valor na borda e fica constante até a próxima borda.
4. Pulsos de D entre duas bordas são ignorados; antes da primeira borda, Q é desconhecido, salvo reset.
No latch D, ao contrário, Q acompanha D durante todo o nível alto do clock.

Outros flip-flops (equações características):
- JK: Q+ = JQ' + K'Q (00 mantém, 01 reseta, 10 seta, 11 inverte).
- T: Q+ = T ⊕ Q (T = 1 inverte); base dos contadores.

Restrições de tempo: setup (D estável antes da borda), hold (D estável depois da borda) e atraso clock-to-Q. Período mínimo do clock ≥ t_clk→Q + atraso da lógica combinacional + t_setup.

Reset síncrono (atua na borda) e assíncrono (atua na hora, independente do clock) colocam a máquina num estado inicial conhecido.
