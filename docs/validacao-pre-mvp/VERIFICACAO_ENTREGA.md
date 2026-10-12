# Verificação da entrega

- Branch: codex/paa-acervo-validacao.
- Pipeline novo: 22 testes passaram, incluindo regressões de números de questão em linha separada, aprovações por hash, persistência de suspeitas, bloqueio de votos duplicados e repetição limitada de respostas truncadas.
- Backend existente: 43 testes passaram, sem alterações em seu código.
- PoC: teste_checkpoints.py passou; reconheceu o caso da definição incorreta de NP.
- HTTP real em base temporária: listagem, comparação cega, gravação, duplicata e origem externa verificados (200, 400 e 403 conforme esperado).
- Navegador: comparação real A/B aberta e conferida; não foram inseridos votos técnicos na base dos alunos.
- PowerShell padrão do Windows: preparação, testes e exportação do dataset executados.
- git diff --check passou (somente avisos de conversão futura LF/CRLF).
- Hashes: snapshot inicial de 55 arquivos e 60 documentos de entrada conferidos, sem divergências.

Testes de fallback Gemini usam falhas simuladas; não houve chamada real à API externa. Pareceres, OCR e respostas locais não substituem validação do professor. O arquivo RELATORIO_QUINTA.md contém os números da rodada final, inclusive falhas de visão.
