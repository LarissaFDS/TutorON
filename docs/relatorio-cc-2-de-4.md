# Relatório: Ciência da Computação, lote 2 de 4 (23/11/2026)

Decisão da equipe para este lote: disciplina criada entra como `MVP`, sem aviso. As seis deste lote já
existiam como `MVP` no `dev` e continuam assim (nenhuma foi criada). Liberar não é revisar: nenhum bloco
está marcado com `revisao_humana: feita` nem `revisao_professor: sim`, e nenhuma nota escrita por IA
entrou na busca.

| # | Item | PR | Merge dev / main | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|
| 1 | Matemática Discreta (`discreta`) | — | — | nada novo | — | o complemento de CC de 22/11/2026 já usou as 8 provas do Prof. Bruno (2020.1 a 2021.1), as 4 fotos da prova de 2017, as revisões da monitoria (blocos s24–s30); slides e listas da UFCG (`ufcg-discreta-leandro`) e o livro de Evaristo já estavam; o RSA em Python (com chave privada de exemplo) segue fora do repositório |
| 2 | OAC (`oac`) | — | — | nada novo | — | o complemento de CC de 22/11/2026 já avaliou as provas de 2016.2 e 2017 e a reavaliação de 2017.1 (3 blocos `oac-cc-*`); arquivos do MARS registrados como fora do repositório |
| 3 | Projeto de Software (`projsw`) | — | — | nada novo | — | o único arquivo (notas de aula de Programação II da UFCG) já é a fonte dos blocos da disciplina |
| 4 | Teoria dos Grafos (`grafos`) | — | — | nada novo | — | listas 2020.1 e 2020.2, provas de 2016.2 e 2018.1, slides da UFCG, `ETG.pdf` (Feofiloff), listas resolvidas por alunos e POSCOMP 2002–2013 já registrados em `fontes.json`; pendências antigas: conferir questões do POSCOMP com o gabarito, hipergrafos e matróides sem bloco, questão 4.4 da lista |
| 5 | Conceitos de Linguagens de Programação (`clp`) | — | — | nada novo | — | provas AB1 2013.1, AB2 2011.2 e final 2012.2 já usadas (c01–c14); fotos com nome e matrícula, trabalhos e anotações de alunos ficam fora; Paradigmas (CCOM036) sem material |
| 6 | Processamento de Linguagem Natural (`pln`) | — | — | nada novo | — | as listas 1 a 6 de 2021.1 já usadas (p01–p13); ementa oficial não conferida |

Itens 1 a 6: comparei cada arquivo da pasta com o `CURADORIA.md`, o `fontes.json` e os blocos da
disciplina, pelo nome, pelo semestre e pela quantidade de arquivos. Todo o material deste lote já tinha
sido curado na fila CC anterior (22/11/2026). Não houve PR por item, porque nada novo entraria. Este
relatório entra numa PR própria.

## Aguardando decisão
- Revisão humana e do professor dos blocos das seis disciplinas (nenhum está marcado como revisado).
- Os `CURADORIA.md` de `grafos` e `clp` ainda dizem "em validação" no topo, mas o cadastro diz `MVP`; o
  de `clp` ainda diz "Sem ligação em `cursos.json`", o que o grupo de eletivas (PR #151) já resolve. Não
  mexi para não abrir PR só de texto.
- Ementas oficiais não conferidas: PLN (eletiva de CC).
- PR #104 (Sistemas Digitais) não foi tocada.
- O site não foi atualizado por mim: não há acesso ao Render nem ao PC do servidor.
