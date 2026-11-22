# Relatório da fila da noite: Ciência da Computação, parte 1 (22/11/2026)

| # | Disciplina | PR | Merge dev / main | Blocos novos | Testes e bateria de relevância | Pendências |
|---|---|---|---|---|---|---|
| 0 | Lógica | #110 (outra sessão) | dev: sim | ver PR #110 | ver PR #110 | ver PR #110 |
| 1 | Matemática Discreta | #112 | dev: sim; main: #113 | 7 (`s24`–`s30`) | pytest 1614 ok, 8 pulados (dev + calc1); relevância 456/456; ruff ok | revisão humana dos blocos |
| 2 | Cálculo 1 | #111 | dev: sim; main: #113 | 4 (`c24`–`c27`) | testes de calc1 e da busca ok; relevância 447/447; ruff ok | c25 é `corrigida` (o enunciado chama de máximo um ponto que é mínimo) |
| 3 | Geometria Analítica | #114 | dev: sim; main: #116 | 4 (`g30`–`g33`) | suíte ok; relevância ok; ruff ok | g31 é `corrigida` (P2 = P3 na prova final: os pontos não definem plano); a ementa de CCOM05 inclui matrizes, determinantes e sistemas |
| 4 | Probabilidade e Estatística | #115 | dev: sim; main: #116 | 4 (`a19`–`a22`) | suíte ok; relevância ok; ruff ok | a19 é `corrigida` (três erros no gabarito; P(C > 2300) = 0,64); a atividade AT1 tem nomes de alunos e ficou fora |
| 5 | Estrutura de Dados | #117 | dev: sim; main: PR final | 3 (`s24`–`s26`) | suíte ok; relevância ok; ruff ok | POO e containers da ementa de CCOM009 não têm bloco; o projeto Huffman (avaliativo) ficou fora |
| 6 | Banco de Dados | #118 | dev: sim; main: PR final | 2 (`b12`, `b13`) | pytest 1659 ok; relevância 486/486; ruff ok | `pendente_professor`, como as demais resoluções de bd; o dump do hospital não foi versionado nem usado |
| 7 | OAC | #119 | dev: sim; main: PR final | 3 (`v01`–`v03`) | pytest 1658 ok, 8 pulados; relevância 486/486 (489/489 depois do merge de dev); ruff ok | as provas de 2017 usam MIPS, e o acervo usa RISC-V |
| 8 | PAA | #120 e PR seguinte | dev: sim; main: sim | 2 (`e06`, `e07`, `revisado: false`) | suíte ok; relevância 486/486 | entraram depois de ajustar dois testes, com autorização (ver abaixo) |

Programação 1 foi pulada (PR #109, já em dev).

## Aguardando decisão
- **PAA:** `e06` e `e07` estão em `materiais/Equipe/` com `revisado: false`, fora da busca até a revisão humana. Com autorização da responsável, `test_equipe_pd.py` passou a aplicar o padrão de PD só aos arquivos `e*_pd_*`, e o instantâneo do ranking léxico de PAA foi regenerado.
- **Ementas:** GA (matrizes e sistemas em CCOM05), ED (POO e containers em CCOM009) e PAA (árvores B, TSP e FFT no material da turma) têm diferenças registradas no `CURADORIA.md` de cada uma. Nenhuma pediu disciplina separada.
- **OAC:** confirmar se blocos com MIPS (provas de 2017) servem para a turma atual, que usa RISC-V.
- **Revisão:** nenhum bloco novo tem `revisao_humana: feita`, e todos esperam revisão humana, a começar pelos `corrigida` (c25, g31, a19) e pelos `pendente_professor` de BD.
- **Fora do repositório:**
  - fotos de provas e provas com nome de aluno (Discreta, PAA);
  - a atividade AT1 de Probabilidade, que tem nomes de alunos;
  - o dump SQL do hospital (BD);
  - o código RSA de aluno com chave privada;
  - o projeto Huffman (ED);
  - os livros protegidos (Cormen, Navathe, Heuser, Tenenbaum, Goodrich);
  - os PDFs das provas.
- O site não foi atualizado: não há acesso ao PC do servidor.
