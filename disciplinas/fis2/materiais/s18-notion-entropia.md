---
id: fis2-notion-entropia
titulo: Anotações da turma (Notion) — entropia, variação de entropia, expansão livre e Segunda Lei
assunto: fis2-09-entropia-segunda-lei
tipo: material_estudo
resolucao: nao
fonte: Notion da turma, página "Entropia e a Segunda Lei da Termodinâmica" (texto lido; imagens com fórmulas não versionadas, transcritas e conferidas pela equipe)
fontes_catalogo: ufal-fis2-notion
autoria: Anotações de alunos da turma de Física 2 (UFAL), revisadas e reescritas pela equipe TutorON com auxílio de IA
licenca: Não declarada (anotações de alunos no Notion da turma); imagens fora do repositório
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio as anotações e corrige os erros indicados no fim
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Variação de entropia num processo **reversível**: $\Delta S = \int_i^f \dfrac{dQ}{T}$ (J/K, T em kelvin). Isotérmico reversível: $\Delta S = Q/T$; o sinal de ΔS é o sinal de Q.

A entropia é função de estado: ΔS depende só dos estados inicial e final. Para gás ideal:
$$\Delta S = nR\ln\frac{V_f}{V_i} + nC_V\ln\frac{T_f}{T_i}$$

Processo irreversível: a integral de dQ/T ao longo do processo real **não** dá ΔS. Escolha um processo reversível que ligue os mesmos estados e calcule ΔS nele.

Como calcular a variação de entropia numa expansão livre: o gás ideal vai de $V_i$ a $V_f$ no vácuo, com Q = 0, W = 0 e $T_f = T_i$. O caminho real tem Q = 0, mas ΔS não é zero. Use uma expansão **isotérmica reversível** entre os mesmos estados: $Q = W = nRT\ln(V_f/V_i)$, logo $\Delta S = nR\ln(V_f/V_i) > 0$. Ex.: 1 mol dobrando o volume: ΔS = 8,31 × ln 2 ≈ 5,76 J/K.

Segunda Lei: num sistema fechado, a entropia **aumenta** num processo irreversível e **permanece constante** num processo reversível; nunca diminui ($\Delta S \ge 0$). A anotação escreve "irreversível" nos dois casos.

Força associada à entropia (elástico): de $dE = -F\,dx + T\,dS$ com dE ≈ 0, $F = T\,dS/dx$.

Visão estatística: $S = k\ln W$ (W = multiplicidade da configuração; k = constante de Boltzmann). Para N grande, use Stirling: $\ln N! \approx N\ln N - N$.

Correções da equipe: "permanece constante se o processo for irreversível" → reversível; procedimento do caminho reversível explicitado.
