---
id: so-paginacao-bits-endereco-traducao
titulo: Paginação — quantos bits têm o endereço lógico e o físico (8 páginas de 4096 endereços, 64 quadros), número da página e deslocamento, tradução com tabela de páginas, TLB
assunto: so-05-memoria
tipo: prova
questao: Prova 2, questões 4 e 5; variante da AB2, questão 1; caderno, cap. 5 (tabela de páginas de 500 bytes)
resolucao: sim
fonte: Prova 2 do Prof. André Aquino (UFAL), fotos da turma com gabarito; resolução da turma de uma variante da AB2; Lista 4 da turma (2021) sobre o caderno do Prof. Maziero
fontes_catalogo: ufal-aquino-prova2-fotos,turma-resolucao-ab2-variante,turma-listas-2021,maziero-caderno-2014,ufal-aquino-slides-so
autoria: Provas do Prof. André Aquino (UFAL); resoluções de alunos parafraseadas e conferidas pela equipe TutorON
licenca: Não declarada (provas); caderno sob CC BY-NC-SA 3.0; paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Prova 2 e variante da AB2 do Prof. André Aquino. Status da resolução: pendente_professor. A resolução é da equipe TutorON e não é gabarito do professor.

**Método:** endereço = (número da página, deslocamento). Com páginas de $2^d$ endereços, o deslocamento tem $d$ bits. Com $2^p$ páginas no espaço lógico, o número da página tem $p$ bits; com $2^q$ quadros na memória física, o número do quadro tem $q$ bits. Lógico: $p + d$ bits; físico: $q + d$ bits (página e quadro têm o mesmo tamanho).

**Prova 2, questão 4** (8 páginas de 4096 endereços; 64 quadros): $4096 = 2^{12}$ → deslocamento 12 bits; $8 = 2^3$ → página 3 bits; $64 = 2^6$ → quadro 6 bits. Lógico $3 + 12 =$ **15 bits**; físico $6 + 12 =$ **18 bits** (alternativa "15 e 18", gabarito da turma conferido).

**Prova 2, questão 5** (endereço virtual de 16 bits, páginas de 2 KB): $2\,\text{KB} = 2^{11}$ → deslocamento **11 bits**; página $16 - 11 =$ **5 bits** (32 páginas). O número de páginas do processo (o WSL de 4 páginas) não muda a divisão dos bits.

**Tradução com tabela** (caderno, páginas de 500 bytes, conta em decimal): página = endereço div 500, deslocamento = endereço mod 500, físico = quadro × 500 + deslocamento. 414 → página 0, deslocamento 414; 741 → página 1, deslocamento 241; 1995 → página 3, deslocamento 495; 4000 → página 8, deslocamento 0; 6633 → página 13, deslocamento 133. **Pendente:** a tabela de páginas do caderno é uma figura que não está no material; a lista da turma dá os quadros 2, 5, 5, 0 e 1, o que daria os físicos 1414, 2741, 2995, 0 e 633, mas não dá os endereços físicos nem diz se alguma página é inválida (falta de página). Confira com a tabela do caderno.

**TLB:** cache de traduções página → quadro dentro da MMU; evita ler a tabela de páginas na memória a cada acesso. Precisa ser limpa (ou marcada por espaço de endereçamento) a cada troca de contexto entre processos, porque a mesma página lógica aponta para outro quadro.

**Verificação:** $2^{15} = 8 \times 4096$ endereços lógicos e $2^{18} = 64 \times 4096$ físicos; para 6633, $13 \times 500 + 133 = 6633$.
