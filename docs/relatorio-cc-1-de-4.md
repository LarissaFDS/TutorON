# Relatório: Ciência da Computação, lote 1 de 4 (23/11/2026)

Decisão da equipe para este lote: disciplina criada entra como `MVP`, sem aviso. As seis deste lote já
existiam como `MVP` e continuam assim. Liberar não é revisar: nenhum bloco está marcado com
`revisao_humana: feita` nem `revisao_professor: sim`, e nenhuma nota escrita por IA entrou na busca.

| # | Item | PR | Merge dev / main | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|
| 0 | Correção da grade de períodos | (esta PR) | em andamento | — (código) | pytest 2227 ok, 30 pulados; relevância 647/647; ruff ok | conferir a janela no site depois do deploy (sem acesso ao servidor) |

## Item 0: disciplinas fora da janela de períodos

- **Antes:** `clp`, `am`, `cd`, `compevol`, `pln`, `seguranca`, `ihc` (nenhum período de nenhum curso).
- **Depois:** nenhuma. Em cada curso, toda disciplina disponível fica num período ou no grupo
  "Eletivas, ênfases e outras" (teste `backend/tests/test_cursos_eletivas.py`). As sete receberam
  `"cursos": {"cc": "eletiva"}` (são de ênfase ou eletivas de CC segundo o `LEIA-ME.md` do lote).

## Aguardando decisão
- O site não foi atualizado por mim: não há acesso ao Render nem ao PC do servidor.
