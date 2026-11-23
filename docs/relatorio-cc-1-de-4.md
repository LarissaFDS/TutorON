# Relatório: Ciência da Computação, lote 1 de 4 (23/11/2026)

Decisão da equipe para este lote: disciplina criada entra como `MVP`, sem aviso. As seis deste lote já
existiam como `MVP` e continuam assim. Liberar não é revisar: nenhum bloco está marcado com
`revisao_humana: feita` nem `revisao_professor: sim`, e nenhuma nota escrita por IA entrou na busca.

| # | Item | PR | Merge dev / main | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|
| 0 | Correção da grade de períodos | #151 | dev: sim; main: sim (#152) | — (código) | pytest 2227 ok, 30 pulados; relevância 647/647; ruff ok; CI verde | conferir a janela no site depois do deploy (sem acesso ao servidor) |
| 1 | Programação 1 (`prog1`) | — | — | nada novo | — | o complemento de CC de 21/11/2026 já usou o livro de Evaristo, o "Guia funcional", `dicas-terminal.pdf` e os 92 arquivos de `c_descomplicado/` (blocos s17–s23); pendências antigas: código COMP359 e PPC de CC em vigor, professor e turma |
| 2 | Cálculo Diferencial e Integral (`calc1`) | — | — | nada novo | — | o complemento de 22/11/2026 já leu todo o banco de provas avulsas (2003 a 2013); entraram as 4ª provas de 2006 e 2007 |
| 3 | Teoria da Computação (`lfa`) | — | — | nada novo | — | o complemento de 22/11/2026 já cobriu a pasta (3 blocos `lfa-cc-*`; o resto registrado como sem bloco); pendência antiga: problema da correspondência de Post sem bloco |
| 4 | Ciência de Dados (`cd`) | — | — | nada novo | — | provas e listas de 2020.1, 2020.2 e 2021.1 e o projeto já usados (c01–c14); ementa de COMP401 não conferida |
| 5 | Sistemas Distribuídos (`sd_dist`) | — | — | nada novo | — | provas de 2017, 2020.1 e 2020.2, resumos e seminários já avaliados (d01–d18); segurança em SD e relógios sem bloco |
| 6 | Segurança de Sistemas Computacionais (`seguranca`) | — | — | nada novo | — | provas, listas, slides, PSI e trabalho já avaliados (s01–s15, só defesa); nenhum código de exploração no acervo; ementa de COMP403 não conferida |

## Item 0: disciplinas fora da janela de períodos

- **Antes:** `clp`, `am`, `cd`, `compevol`, `pln`, `seguranca`, `ihc` (nenhum período de nenhum curso).
- **Depois:** nenhuma. Em cada curso, toda disciplina disponível fica num período ou no grupo
  "Eletivas, ênfases e outras" (teste `backend/tests/test_cursos_eletivas.py`). As sete receberam
  `"cursos": {"cc": "eletiva"}` (são de ênfase ou eletivas de CC segundo o `LEIA-ME.md` do lote).

Itens 1 a 6: comparei cada arquivo da pasta com o `CURADORIA.md`, o `fontes.json` e os blocos da
disciplina. Todo o material deste lote já tinha sido curado nas filas anteriores (mesmos nomes,
semestres e quantidades de arquivos). Não houve PR, porque nada novo entraria. A `situacao` das seis
continua `MVP`.

## Aguardando decisão
- Revisão humana e do professor dos blocos das seis disciplinas (nenhum está marcado como revisado).
- Os `CURADORIA.md` de `cd`, `sd_dist` e `seguranca` ainda dizem "em validação" no topo, mas o
  cadastro diz `MVP`; o de `cd` ainda diz "Sem ligação em `cursos.json`", o que a correção do item 0
  resolve pelo grupo de eletivas. Não mexi para não abrir PR só de texto.
- Ementas oficiais não conferidas: COMP359 (P1), COMP401 (CD), COMP403 (Segurança).
- O site não foi atualizado por mim: não há acesso ao Render nem ao PC do servidor.
