# Rodar a matriz no servidor, em duas rodadas

São duas rodadas, cada uma num checkout e numa pasta de resultados própria:

- **Rodada 1, baseline.** Só o #21. Mede o TutorON como ele é hoje, com o prompt antigo congelado e o candidato.
- **Rodada 2, integração.** #21 + #23 + #24. Mede o efeito do corte de relevância e da curadoria de PD. Roda só `atual_rag` e `novo_rag`, nas 3 perguntas do aluno.

Custo estimado com `--intervalo 4`:

| Rodada | Chamadas Gemini | Tempo |
|---|---|---|
| 1 | 90 (30 gerações e 60 julgamentos) | ~30 min |
| 2 | 36 | ~12 min |

O `preflight.py` recalcula esses números para o `--intervalo` escolhido.

> **Cota:** se a chave do `.env` é a mesma do site, a matriz gasta a cota dos alunos e pode empurrar o site para o modelo lite. Rode fora do horário de uso ou com outra chave.
>
> **Chave:** nunca cole a chave em comando, issue ou chat. Ela fica só no `.env`. O preflight só diz se ela existe.

## 0. Preparar uma cópia separada do site

Rode a matriz numa **worktree separada**: trocar de branch na pasta do site mudaria o código e o índice em produção. Supondo que o site rode em `~/TutorON`:

```bash
cd ~/TutorON
git fetch origin
git worktree add ~/TutorON-eval origin/feat/eval-harness
cp ~/TutorON/.env ~/TutorON-eval/.env
cd ~/TutorON-eval
```

O Ollama (com o `bge-m3`) é o mesmo do site. Nada mais é compartilhado.

## Rodada 1: baseline, só o #21

```bash
cd ~/TutorON-eval
git checkout --detach origin/feat/eval-harness
git status --short
python eval/preflight.py --rodada 1 --intervalo 4
```

O `git status` deve sair vazio. Siga só se o preflight terminar em "pronto para rodar". Ele falha nestes casos:
- falta a chave;
- o `bge-m3` está fora do ar;
- o índice está sem vetores;
- o #23 ou o #24 está no checkout;
- o `04-rag/indice.json` foi alterado.

```bash
python eval/matriz.py gerar --saida eval/results/rodada1 --perguntas A1,A2,A3 --intervalo 4
python eval/matriz.py julgar --saida eval/results/rodada1 --juiz gemini-3.8-flash
python eval/matriz.py julgar --saida eval/results/rodada1 --juiz gemini-3.7-flash
python eval/matriz.py relatorio --saida eval/results/rodada1
python eval/folha_cega.py --saida eval/results/rodada1
python eval/decidir.py --rodada1 eval/results/rodada1/resumo.json
```

- **Dois juízes:** o `gemini-3.8-flash` também é o modelo forte avaliado. O segundo juiz serve para medir a autopreferência, e o relatório escolhe sozinho o juiz neutro.
- **Interrupções:** se algum comando parar (429, queda de rede), rode o mesmo comando de novo. Ele retoma de onde parou.
- **Decisão:** o `decidir.py` já dá as decisões (a), (b) e (c). A (d) precisa da rodada 2.

## Rodada 2: integração #21 + #23 + #24

### 2.1 Checkout e preflight

```bash
cd ~/TutorON-eval
git checkout --detach origin/feat/eval-harness
git merge --no-edit origin/feat/rag-corte-relevancia origin/feat/curadoria-pd
python eval/preflight.py --rodada 2 --intervalo 4
```

O merge é só local: **não faça push**.

Nesta etapa é normal o preflight avisar "0 materiais da equipe no índice". Ele deve dar FALHA apenas se faltar a chave, o `bge-m3`, ou o #23/#24 no checkout.

### 2.2 Backup do índice (antes de reindexar)

```bash
BACKUP=~/backups-tutoron/indice-$(date +%Y%m%d-%H%M)
mkdir -p "$BACKUP"
cp -a 04-rag 02-acervo "$BACKUP"/
ls "$BACKUP"
```

Para **restaurar** o índice anterior (o backup fica fora do repositório, em `~/backups-tutoron`), a partir de `~/TutorON-eval`:

```bash
rm -rf 04-rag 02-acervo
cp -a "$BACKUP"/04-rag "$BACKUP"/02-acervo .
```

Para voltar ao índice versionado, o mesmo vale: `git checkout -- 04-rag 02-acervo`.

### 2.3 Reindexar e calibrar

```bash
python -m acervo indexar --embeddings
python eval/preflight.py --rodada 2 --pos-indexacao --intervalo 4
python eval/diagnostico.py --saida eval/results/rodada2 calibrar
```

- **Reindexar:** os vetores dos 53 blocos antigos são reaproveitados pelo hash do texto. Só os 5 materiais da equipe passam pelo `bge-m3`.
- **Preflight `--pos-indexacao`:** agora ele **exige** os 5 materiais da equipe com vetor.
- **Calibrar:** o `calibrar` recomenda um limiar e grava a tabela em `eval/results/rodada2/diagnostico-calibrar.md`. Anote o valor como `LIMIAR` abaixo.
- **`.env` intocado:** o limiar entra por variável de ambiente só nos comandos da matriz. Assim o site não muda.

### 2.4 Gerar, julgar e decidir

```bash
export ACERVO_SIMILARIDADE_MINIMA=LIMIAR
python eval/matriz.py gerar --saida eval/results/rodada2 --perguntas A1,A2,A3 --condicoes atual_rag,novo_rag --incluir-nao-revisados --intervalo 4
python eval/matriz.py julgar --saida eval/results/rodada2 --juiz gemini-3.8-flash
python eval/matriz.py julgar --saida eval/results/rodada2 --juiz gemini-3.7-flash
python eval/matriz.py relatorio --saida eval/results/rodada2
python eval/decidir.py --rodada1 eval/results/rodada1/resumo.json --rodada2 eval/results/rodada2/resumo.json
unset ACERVO_SIMILARIDADE_MINIMA
```

- **`--incluir-nao-revisados`:** obrigatório nesta rodada. Os 5 materiais da equipe ainda estão com `revisado: false`, e a produção os ignora até alguém revisar (como marcar como revisado: `docs/curadoria-equipe.md`, no #24). Sem a flag, a rodada 2 mediria o acervo sem a curadoria.
- **Juízes:** use os **mesmos dois juízes** da rodada 1. O efeito da curadoria (d) é a diferença rodada 2 − rodada 1, pergunta a pergunta, com o mesmo juiz.

## Devolver os resultados

```bash
tar czf resultados-matriz.tgz eval/results/rodada1 eval/results/rodada2 eval/results/decisao.md
```

- **O que vai no pacote:** respostas, notas, relatórios e a decisão. Não há chave nesses arquivos.
- **Folha cega:** envie `rodada1/folha_cega.md` ao aluno. O `folha_cega_mapa.json` fica com a equipe.
- **Não faça commit** do `04-rag/indice.json` reindexado. Ele só entra no repositório depois que o #24 for revisado e mesclado.

Para apagar a cópia de avaliação:

```bash
cd ~/TutorON
git worktree remove --force ~/TutorON-eval
```

## Como ler a decisão

| Saída do `decidir.py` | O que fazer |
|---|---|
| (a) #25 "SAI DO RASCUNHO" | `novo_rag` ≥ genérico e a, b, d ≥ 4 nas 3 originais, nos dois modelos: tirar o #25 de rascunho. Se só passa "com a curadoria", mesclar junto com o #24. |
| (b) roteamento "ABRIR" | forte − lite ≥ 0,5 no braço que vai a produção: abrir o PR de roteamento (esperar o forte em perguntas de raciocínio). |
| (c) H4 "CONFIRMADA" | RAG (com − sem) ≤ −0,3 com o prompt atual: o #23, com o limiar calibrado, vira prioridade. |
| (d) curadoria | Diferença rodada 2 − rodada 1 em `atual_rag` e `novo_rag`. "Ajudou" se ≥ 0,3; "piorou" se ≤ −0,3. |

Os limiares (0,5; −0,3; 4; 0,3) são **heurísticos** e ficam no topo do `eval/decidir.py`. Com 3 perguntas, cada número tem n ≤ 3. Quem confirma é a folha cega do aluno.
