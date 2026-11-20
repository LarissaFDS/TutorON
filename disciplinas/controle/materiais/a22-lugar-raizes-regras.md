---
id: controle-anot-lugar-raizes-regras
titulo: Regras de construção do lugar das raízes com o exemplo (s+2)/(s²+2s+3): eixo real, assíntotas, ângulos de partida ±144,7°, chegada 180°, ponto de ramificação −2−√3 e ganho K = 2+2√3
assunto: controle-07-lugar-raizes
tipo: resolucao
resolucao: sim
fonte: Anotações "Método Lugar das raízes" (11 nov. 2026), p. 3–9
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: corrigida
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: corrigida.

**Condições:** $1 + KG(s) = 0$, $K > 0$: **módulo** $|KG(s)| = 1$ e **fase** $\angle G(s) = 180^\circ(2l + 1)$. O lugar é o conjunto dos $s$ que satisfazem a fase; $p_i$, $z_j$ são polos e zeros de $G$ de **malha aberta**.

**Exemplo:** $G = \frac{s + 2}{s^2 + 2s + 3}$: polos $-1 \pm j\sqrt2$, zero $-2$ ($n = 2$, $m = 1$).
1. Marque $\times$ nos polos e $\circ$ nos zeros.
2. **Eixo real:** pertence ao lugar o trecho **à esquerda de um número ímpar** de polos e zeros reais. Aqui: $(-\infty, -2]$.
3. **Assíntotas:** $n - m = 1$, ângulo $\frac{180^\circ(2l + 1)}{n - m} = 180^\circ$. Um ramo vai ao zero, outro a $-\infty$.
4. **Partida** de $p_1$: $\theta_{p_1} = 180^\circ + \angle(p_1 - z_1) - \angle(p_1 - p_2) = 180^\circ + 54{,}7^\circ - 90^\circ = 144{,}7^\circ$; $p_2$: $-144{,}7^\circ$. **Chegada** no zero: $180^\circ$.
5. **Ramificação:** $\frac{d}{ds}\Big[\frac{1}{G}\Big] = 0 \Rightarrow s^2 + 4s + 1 = 0$, $s = -2 \pm \sqrt3$. $-0{,}27$ não está no lugar; **$-3{,}73$ está** (ponto de chegada ao eixo real). A condição é só necessária: confira se o ponto pertence ao lugar.
6. **Ganho no ponto:** $K = \frac{1}{|G(s_0)|}$: $K = 2 + 2\sqrt3 \approx 5{,}46$ (polo duplo em $-3{,}73$).

O lugar sai dos polos complexos, faz um arco pela esquerda e se junta no eixo real em $-3{,}73$; daí um ramo vai a $-2$ e outro a $-\infty$.

**Correções:** a raiz descartada é $-2 + \sqrt3 \approx -0{,}27$ (as anotações escrevem "0,26" sem o sinal); o ângulo de partida exato é $144{,}7^\circ$ (anotado como $145^\circ$, arredondado).

**Verificação:** `numpy.roots` de $s^2 + (2 + K)s + 3 + 2K$ com $K = 5{,}464$ dá polo duplo em $-3{,}732$.
