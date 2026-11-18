---
id: ed-prof-huffman
titulo: Huffman — conceitos, exemplo da aula e regras do projeto (sem implementação completa)
assunto: ed-12-huffman
tipo: material_estudo
resolucao: sim
fonte: Notion da turma, página "Huffman / Exemplo com Árvore Binária", e PDF "Preparatório para os Projetos – AB 2" (Márcio Ribeiro, 16/04/2025)
fontes_catalogo: ufal-ed-notion,ufal-ed-prof-preparatorio
autoria: Márcio Ribeiro (UFAL, Instituto de Computação), slides da disciplina; parafraseado pela equipe TutorON; exemplo das anotações da turma conferido pela equipe
licenca: Não declarada (material do professor); o PDF não está no repositório
publicacao_transcricao: não autorizada: o bloco parafraseia, não transcreve
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Huffman (1952): código de prefixo de tamanho variável; símbolos mais frequentes ganham códigos mais curtos. Status da resolução: validada (conferida pela equipe TutorON; não é gabarito do professor).

Montagem: cada símbolo vira um nó com sua frequência, todos numa fila de prioridade (min-heap). Repita: tire os dois de menor frequência e crie um pai com a soma, até restar um nó. Esquerda = 0, direita = 1. Nenhum código é prefixo de outro porque os símbolos ficam só nas folhas.

Exemplo da aula, conferido por código: frequências a 5, b 9, c 12, d 13, e 16, f 45. Códigos: f 0, c 100, d 101, a 1100, b 1101, e 111, com o menor à esquerda em cada junção. Total de 224 bits, contra 300 com 3 bits fixos. Com outra regra de desempate os códigos mudam, mas os comprimentos e o total ficam iguais.

O projeto (Entrega 1 da AB2) é avaliado; aqui só entram os conceitos. Regras do PDF do professor:
- compactar e descompactar qualquer arquivo em C;
- cabeçalho .huff obrigatório, no formato "visto em sala" (o formato não está no acervo);
- `void*` obrigatório nas estruturas de dados;
- documentação no estilo JavaDoc;
- equipes de 3 a 5, nota individual, projeto no GitHub.

Pontos de depuração: tratar arquivo vazio e arquivo com um único símbolo, ler e escrever em modo binário (`"rb"`, `"wb"`), lixo de bits no último byte e liberar a árvore.

O TutorON não entrega implementação completa do projeto: explica, pergunta e ajuda a depurar o código do aluno.
