# Relatório: Ciência da Computação, lote 3 de 4 (23/11/2026)

Decisão da equipe para este lote: disciplina criada entra como `MVP`, sem aviso. As sete deste lote já
existiam como `MVP` no `dev` e continuam assim (nenhuma foi criada). Liberar não é revisar: nenhum bloco
está marcado com `revisao_humana: feita` nem `revisao_professor: sim`, e nenhuma nota escrita por IA
entrou na busca.

| # | Item | PR | Merge dev / main | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|
| 1 | Lógica Aplicada à Computação (`logica`) | — | — | nada novo | — | o complemento de CC de 22/11/2026 já usou as fotos das provas da Profa. Roberta Lopes (2019), as fichas práticas, os arquivos .pl e as apostilas de Prolog (assunto `logica-14-programacao-logica-prolog`); fotos com nome de aluno e livros protegidos seguem fora; bloco `logica-roberta-prova1-complexidade-negacao` continua `pendente_professor` |
| 2 | Computação, Sociedade e Ética (`etica`) | — | — | nada novo | — | as três avaliações de 2020.2 (reavaliações AB1 e AB2, Avaliação Final) já são a fonte dos blocos e01–e09; ementa não conferida; propriedade intelectual sem bloco |
| 3 | Estrutura de Dados (`ed`) | — | — | nada novo | — | questões do Huxley já usadas (3 blocos `ed-cc-*`); slides do Prof. Márcio, dicas de AVL e heap e o PDF "Estrutura de Dados Peixoto" (é o livro de Shaffer, 3.2, já `shaffer-dsaa-3-2`) ficam só como evidência; Makefile, Huffman e livros protegidos fora; POO e containers da ementa de CC sem bloco |
| 4 | Banco de Dados (`bd`) | — | — | nada novo | — | Lista 2 de SQL já usada (2 blocos `bd-cc-*`); slides, revisão AB2, exercícios e trabalhos registrados em `ufal-cc-bd-materiais`; `dump_hospital.sql` não versionado (nomes de pessoas) |
| 5 | Redes de Computadores (`redes`) | — | — | nada novo | — | a disciplina foi criada com este mesmo material (provas do Prof. Leandro Sales de 2012, 2017 e 2020.1 PLE, blocos r01–r12); fotos com nomes de alunos e respostas de alunos fora; Redes 2 sem material; o topo do `CURADORIA.md` ainda diz "em validação" |
| 6 | Probabilidade e Estatística (`prob`) | — | — | nada novo | — | provas de 2013 do Prof. Heitor já usadas (4 blocos `prob-cc-*`); AT1 com nomes de alunos e o arquivo de idades fora do acervo; demais provas e slides só como evidência |
| 7 | Sistemas Operacionais (`so`) | — | — | nada novo | — | o complemento de CC de 22/11/2026 conferiu arquivo por arquivo (slides do Prof. Aquino, livro e caderno do Prof. Maziero, provas e listas): nada novo |

Suíte completa: 2227 passaram, 30 pulados. Bateria de relevância: 647/647. `ruff check --select E9,F63,F7,F82 .`: sem erros.

Itens 1 a 7: comparei cada arquivo da pasta com o `CURADORIA.md`, o `fontes.json` e os blocos da
disciplina, pelo nome, pelo semestre, pelo professor e, no caso do PDF de ED sem nome de autor, pelo
conteúdo da primeira página. Todo o material deste lote já tinha sido curado na fila CC anterior
(22/11/2026). Não houve PR por item, porque nada novo entraria. Este relatório entra numa PR própria.

## Aguardando decisão
- Revisão humana e do professor dos blocos das sete disciplinas (nenhum está marcado como revisado).
- O `CURADORIA.md` de `redes` ainda diz "em validação" no topo, mas o cadastro diz `MVP`. Não mexi para
  não abrir PR só de texto.
- Ementa oficial de Ética (COMP361) não conferida.
- PR #104 (Sistemas Digitais) não foi tocada.
- O site não foi atualizado por mim: não há acesso ao Render nem ao PC do servidor.
