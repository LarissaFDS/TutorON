---
id: logica-prolog-fatos-regras-consultas
titulo: Prolog: fatos, regras, consultas e o erro do ponto e vírgula
assunto: logica-14-programacao-logica-prolog
tipo: material_estudo
resolucao: sim
fonte: Arquivos first.pl e prolog1.pl da pasta Prolog e fichas práticas 2 e 3 (turma de Ciência da Computação, UFAL)
curso: Ciência da Computação (UFAL), turma da Profa. Roberta Lopes, COMP360
fontes_catalogo: cc-prolog-turma
autoria: Material de Prolog da turma de Ciência da Computação (UFAL), autoria dos arquivos não identificada; exemplos próprios da equipe TutorON escritos com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: corrigida (resolução da equipe TutorON, não é gabarito do professor; código executado no SWI-Prolog 11).

Um programa Prolog é uma **base de conhecimento** de cláusulas de Horn: **fatos** (`humano(pedro).`), **regras** (`cabeça :- corpo.`, lida "cabeça é verdade se o corpo é verdade") e **consultas** (`?- area(sala, A).`). A vírgula no corpo é "e" ($\land$); toda cláusula termina com ponto final. A regra `p :- q, r.` é a fórmula $q\land r\to p$ (em palavras: se q e r, então p), e as variáveis (maiúsculas) são quantificadas universalmente.

Exemplo do material (área de cômodos), já corrigido:

```prolog
largura(sala,4).
comprimento(sala,5).
largura(quarto,3).
comprimento(quarto,3).
area(X,A) :- largura(X,L), comprimento(X,C), A is L*C.
```

A consulta `?- area(X,A).` responde `X = sala, A = 20` e, pedindo outra solução com `;`, `X = quarto, A = 9`.

**Correção:** no arquivo original a linha `comprimento(quarto,3);` termina com ponto e vírgula. Em Prolog `;` é "ou": o leitor junta essa linha com a regra seguinte num só termo `(... ; ...) :- ...` e o SWI-Prolog recusa com "No permission to modify static procedure (;)/2". Troque `;` por `.`.

Na pergunta da turma, ajude o aluno a ler a mensagem de erro e achar a linha, em vez de reescrever o programa inteiro.

**Verificação:** o programa corrigido foi carregado no SWI-Prolog 11 e respondeu sala-20 e quarto-9; a versão com `;` reproduziu o erro citado.
