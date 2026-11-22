---
id: ed-ufcg-rubro-negra
titulo: Árvore rubro-negra — propriedades, altura e exemplo de inserção (UFCG)
assunto: ed-15-arvores-balanceadas
tipo: material_estudo
resolucao: sim
fonte: Slides de Estrutura de Dados da UFCG (DSC), Prof. Adalberto Cajueiro, 2013, aula "Árvore Rubro-Negra"; referência dos slides: Cormen et al., Algoritmos, cap. 14 (1ª ed.)
fontes_catalogo: ufcg-ed-cajueiro-slides
autoria: Conteúdo dos slides do Prof. Adalberto Cajueiro (UFCG), parafraseado e reescrito em C pela equipe TutorON com auxílio de IA
licenca: Não declarada nos slides
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio e código C novo; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Árvore rubro-negra: ABB em que cada nó é vermelho ou preto e valem cinco regras. (1) Todo nó tem cor. (2) As folhas NIL (os ponteiros nulos) são pretas. (3) A raiz é preta. (4) Os dois filhos de um nó vermelho são pretos: nunca há dois vermelhos seguidos. (5) Todo caminho de um nó até as folhas NIL abaixo dele passa pelo mesmo número de nós pretos; esse número, sem contar o próprio nó, é a altura negra bh(x). Status da resolução: validada (conferida pela equipe TutorON com programa C; não é gabarito do professor).

Consequência: com n chaves, a altura é no máximo $2\log_2(n+1)$, logo busca, inserção e remoção custam O(log n) no pior caso. O motivo: pela regra 4, pelo menos metade dos nós de qualquer caminho da raiz até uma folha é preta. Os slides resumem como "a altura de um filho nunca passa do dobro da do outro"; o exato é que o caminho mais longo até uma folha NIL tem no máximo o dobro de nós do mais curto.

Comparação com a AVL: a AVL é mais rigidamente balanceada (busca um pouco mais rápida); a rubro-negra faz no máximo duas rotações por inserção e é a escolha de muitas bibliotecas.

Exemplo da aula, inserindo 8, 4, 2 (todo nó novo entra vermelho):
- 8 entra vermelho e é raiz: pinta de preto. Antes: 8 vermelho. Depois: 8 preto.
- 4 entra vermelho à esquerda de 8; pai preto: nada a fazer.
- 2 entra vermelho à esquerda de 4. Antes: 8 preto, 4 vermelho, 2 vermelho (dois vermelhos seguidos; tio NIL, preto; linha reta). Conserto: 4 vira preto, 8 vira vermelho e gira à direita em 8. Depois: raiz 4 preta, filhos 2 e 8 vermelhos.

Para conferir uma árvore pronta, verifique as cinco regras: calcule a altura negra de cada subárvore recursivamente e veja se a esquerda e a direita dão o mesmo valor em todo nó.

Remoção: tirar um nó vermelho não muda nenhuma altura negra. Tirar um nó preto pode quebrar a regra 5; o conserto olha a cor do irmão e dos sobrinhos e usa recoloração e até três rotações. Detalhes em Cormen et al., seção sobre remoção em árvores rubro-negras.
