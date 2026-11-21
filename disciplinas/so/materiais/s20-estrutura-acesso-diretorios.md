---
id: so-estrutura-arquivos-acesso-diretorios
titulo: Estrutura de arquivos (sequência de bytes, registros, árvore), métodos de acesso, atributos, diretórios, atalhos e semânticas de compartilhamento
assunto: so-06-arquivos
tipo: prova
questao: Prova 2, questão 7; variante da AB2, questões 6 e 7; caderno, cap. 6
resolucao: sim
fonte: Prova 2 do Prof. André Aquino (UFAL), fotos da turma com gabarito; resolução da turma de uma variante da AB2; Lista 6 da turma (2021) e resolução de aluna (2017) sobre o caderno do Prof. Maziero
fontes_catalogo: ufal-aquino-prova2-fotos,turma-resolucao-ab2-variante,turma-respostas-so,turma-listas-2021,turma-resumos-2017,ufal-aquino-slides-so
autoria: Prova do Prof. André Aquino (UFAL); resoluções de alunos parafraseadas, conferidas e corrigidas pela equipe TutorON
licenca: Não declarada (prova); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
Prova 2 do Prof. André Aquino. Status da resolução: corrigida. A resolução é da equipe TutorON e não é gabarito do professor.

**Prova 2, questão 7** (estrutura interna de um arquivo):
- I. "Organizado como árvore, fornece a máxima flexibilidade": **falsa**. A máxima flexibilidade é da **sequência de bytes** (o SO não impõe nada; a aplicação interpreta).
- II. "Organizado em registros, usa registros de tamanho fixo": **verdadeira** (modelo dos sistemas antigos de cartões).
- III. "Organizado em árvore, usa registros de tamanhos variáveis": **verdadeira** (árvore de registros com chave, de mainframes).
- IV. "Pode ser sequência de bytes, de registros ou árvore": **verdadeira**.
Resposta: **somente II, III e IV** (gabarito da turma conferido). **Correção:** a resolução da variante da AB2 justificou I como falsa dizendo que a árvore "tem tamanho limitado"; o motivo é outro: a flexibilidade máxima é a do arquivo sem estrutura.

**Métodos de acesso:** sequencial (lê na ordem, com um ponteiro que avança; simples, mas não é o mais rápido para chegar a um ponto distante), direto ou aleatório (posição informada, como `lseek`), indexado (por chave).

**Atributos:** nome, tipo, tamanho, datas, proprietário, permissões, localização dos dados.

**Diretórios:** um nível, dois níveis (um por usuário), árvore e grafo acíclico (com atalhos). **Atalho rígido** (*hard link*): outra entrada de diretório para o mesmo i-node; **simbólico**: arquivo que guarda o caminho de outro, e fica "quebrado" se o alvo for removido.

**Semânticas de compartilhamento:** UNIX (toda escrita é vista logo por todos), de sessão (as mudanças só aparecem para quem abrir depois do `close`), imutável (arquivo compartilhado não muda) e transacional.

**Verificação:** com I falsa e II, III, IV verdadeiras, só uma alternativa da questão 7 contém exatamente II, III e IV.
