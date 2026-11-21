---
id: so-fat-cluster-ext2-tamanho-maximo
titulo: FAT e cluster — arquivo de 1024 bytes em clusters de 2048 bytes não fragmenta; tamanho máximo de arquivo no ext2 com ponteiros diretos e indiretos
assunto: so-06-arquivos
tipo: prova
questao: Prova 2, questão 10; caderno, cap. 6 (lista 6 da turma, questão 17)
resolucao: sim
fonte: Prova 2 do Prof. André Aquino (UFAL), fotos da turma com gabarito; Lista 6 da turma (2021) sobre o caderno do Prof. Maziero
fontes_catalogo: ufal-aquino-prova2-fotos,turma-listas-2021,maziero-caderno-2014,ufal-aquino-slides-so
autoria: Prova do Prof. André Aquino (UFAL) e exercício do Prof. Maziero; resoluções de alunos conferidas e corrigidas pela equipe TutorON
licenca: Não declarada (prova); caderno sob CC BY-NC-SA 3.0; paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Prova 2 e caderno do Prof. Maziero. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**FAT (alocação encadeada com a tabela de ponteiros separada dos dados):** a FAT tem uma entrada por cluster com o número do próximo cluster do arquivo (ou marcas de fim, livre e defeituoso). O diretório guarda o primeiro cluster.

**Prova 2, questão 10** (setor de 512 bytes, cluster de 2048 bytes, arquivo final de 1024 bytes): o arquivo ocupa $\lceil 1024 / 2048 \rceil = 1$ cluster. A menor unidade alocada é o cluster, que é contíguo (4 setores seguidos); com um só cluster não há cadeia a fragmentar. Resposta: "**possui tamanho que não permite que seu conteúdo esteja fragmentado**" (gabarito da turma conferido). Erros nas outras alternativas: o arquivo ocupa 2 setores, mas **dentro** do mesmo cluster; e a FAT **permite** fragmentação em arquivos maiores. A sobra de 1024 bytes no cluster é **fragmentação interna**.

**ext2 (caderno):** i-node com 12 ponteiros diretos, 1 indireto, 1 duplamente e 1 triplamente indireto; blocos de 1024 bytes e ponteiros de 64 bits (8 bytes). Ponteiros por bloco: $p = 1024 / 8 = 128$. Tamanho máximo:
$$T = 1024 \times (12 + 128 + 128^2 + 128^3) = 12\,288 + 131\,072 + 16\,777\,216 + 2\,147\,483\,648 = 2\,164\,404\,224 \text{ bytes}$$
(em palavras: mil e vinte e quatro vezes a soma de 12, 128, 128 ao quadrado e 128 ao cubo), cerca de **2,16 × 10⁹ bytes ≈ 2,02 GiB**.

**Correção:** a lista da turma fez a mesma soma, mas chamou cada parcela de **bits** e no fim dividiu por 8, dando 270 550 528 bytes; as parcelas já são **bytes** (número de blocos × 1024 bytes). A resposta certa é 2 164 404 224 bytes.

**Verificação:** a parcela tripla domina ($128^3 \times 1024 = 2^{31}$ bytes = 2 GiB), então o total tem de passar um pouco de 2 GiB; com 8 vezes menos o resultado ficaria abaixo de 300 MB, incompatível com a parcela tripla.
