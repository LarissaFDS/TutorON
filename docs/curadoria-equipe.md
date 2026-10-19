# Material da equipe (`materiais/Equipe/`): revisão antes de ir para os alunos

Os arquivos de `materiais/Equipe/*.md` foram escritos pela equipe TutorON. Eles **não** são do professor. Cada um começa com um cabeçalho:

```
---
id: e01
titulo: Mochila 0/1
assunto: b2-04-programacao-dinamica
autoria: Equipe TutorON (não é material do professor)
revisado: false
---
```

## O que `revisado: false` faz

- **Busca de produção (site):** o material **fica fora**. O bloco existe no acervo e no índice, mas `acervo/retrieval.search` o descarta a cada consulta.
- **Para medir na matriz:** passe `python eval/matriz.py gerar --incluir-nao-revisados ...`. A flag liga `ACERVO_USAR_NAO_REVISADOS=1` só naquele processo.
- **Interruptor global:** `ACERVO_USAR_NAO_REVISADOS=1` no `.env` liga o material também no site. O padrão é desligado (`backend/config.py`, `acervo_usar_nao_revisados`). **Não use em produção** sem revisão.

## Como marcar um arquivo como revisado

1. **Ler o arquivo inteiro.** Um professor, monitor ou membro da equipe que domine o assunto confere:
   - recorrência e casos base;
   - o rastreio da tabela;
   - a complexidade;
   - que nada é atribuído ao professor.

   Os testes de `tests_acervo/test_equipe_pd.py` já conferem as contas, mas não substituem essa leitura.
2. **Trocar o cabeçalho** para `revisado: true`. Se o texto mudou, rode `python -m pytest tests_acervo/test_equipe_pd.py`.
3. **Atualizar o acervo:**

   ```bash
   python -m acervo equipe
   ```

   O comando reescreve `02-acervo/itens.json` e `indice.csv`. A busca relê o `itens.json` a cada consulta, então o bloco passa a valer na hora.
4. **Reindexar só se o corpo do texto mudou.** O índice guarda o `sha256` do corpo, não do cabeçalho. Trocar apenas `revisado` dispensa reindexar. Se o corpo mudou:

   ```bash
   python -m acervo indexar --embeddings
   ```

   Sem reindexar, o bloco com hash diferente é ignorado.
5. **Abrir um PR** com o `.md`, o `02-acervo/itens.json` e o `indice.csv`. O nome de quem revisou vai na descrição.

Para tirar um material de circulação, volte o cabeçalho para `revisado: false` e rode `python -m acervo equipe`.
