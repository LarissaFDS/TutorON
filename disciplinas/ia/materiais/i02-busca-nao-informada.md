---
id: ia-busca-nao-informada-profundidade-largura-aprofundamento-iterativo-completude-otimalidade
titulo: Busca não informada (cega): busca em profundidade com retrocesso, busca em largura, aprofundamento iterativo (BPAI, IDS); completude, otimalidade, admissibilidade e complexidade
assunto: ia-02-busca-e-jogos
tipo: material_estudo
questao: slide 05 (Métodos de Busca), parte 1
resolucao: sim
fonte: Slides de Inteligência Artificial do Prof. Jacson R. C. Silva (Departamento de Computação, CCA-UFES), usados na turma da UFAL
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufes-jeiks-slides
autoria: Slides do Prof. Jacson R. C. Silva (UFES), usados como material da turma da UFAL; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), slide 05 (Métodos de Busca), parte 1 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Problema como busca:** estado inicial, ações (sucessores) e teste de objetivo. A busca **guiada por dados** parte do estado inicial; a **guiada por objetivos** parte do objetivo.

**Busca em profundidade:** expande o nó mais fundo primeiro e, num beco sem saída, faz **retrocesso cronológico**. Sucessores entram **na frente** da lista (pilha). Na árvore A(B(D(H,I),E),C(F,G)) a ordem é A, B, D, H, I, E, C, F, G.

**Busca em largura:** examina um nível inteiro antes do seguinte. Sucessores entram **atrás** (fila). Ordem: A, B, C, D, E, F, G, H, I.

**Aprofundamento iterativo (BPAI, IDS):** profundidade limitada com limite 0, 1, 2, ... Junta a memória pequena da profundidade com a completude da largura.

Contagem com fator de ramificação $b$ e profundidade $d$:
- profundidade, todos os nós: $1+b+\dots+b^d = \dfrac{b^{d+1}-1}{b-1}$; com $b=10$ e $d=4$, **11.111** nós;
- BPAI, com nós revisitados: $(d+1)+d\,b+(d-1)b^2+\dots+b^d$; com $b=10$ e $d=4$, **12.345** nós. O custo extra é pequeno e o tempo é $O(b^d)$.

**Propriedades:**
- **completude:** sempre acha um objetivo, se houver;
- **otimalidade:** acha a melhor solução;
- **admissibilidade:** acha a melhor solução pelo melhor caminho;
- **complexidade** de tempo e de espaço.

A largura é completa e ótima com custos iguais, mas gasta memória $O(b^d)$; a profundidade gasta $O(b\,d)$, mas pode se perder em caminhos infinitos (use limite de profundidade).

**Verificação:** `test_ordens_profundidade_largura` e `test_contagem_bpai` conferem as ordens de visita e os totais 11.111 e 12.345.
