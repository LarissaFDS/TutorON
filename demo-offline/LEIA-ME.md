# Demonstração offline para a apresentação

Abra **TutorON-apresentacao-offline.html** com dois cliques no navegador. Copie
somente esse HTML para outro computador ou pendrive: todos os textos, estilos,
fontes, foto e vídeos estão dentro dele. Não precisa instalar nada, iniciar o
servidor, conectar à internet ou ter um modelo local.

Roteiro sugerido:

1. **Tirar dúvida:** escolha a disciplina e uma das nove perguntas preparadas;
   clique em **Pedir ajuda**. Fórmulas e respostas são exibidas como no TutorON.
2. **Foto e novas pistas:** clique em **Usar foto de exemplo**, confira a leitura
   e confirme. Clique duas vezes em **Ainda não consegui** para ver como o tutor
   muda a explicação da mesma dúvida. **Recomeçar este exemplo** volta ao início.
3. **Aprender com desenhos:** escolha recursão, Karnaugh ou BFS e reproduza o vídeo.
   Se o computador não reproduzir vídeo, abra **Ver quadro final como imagem**.
4. **Reiniciar demonstração** prepara a próxima apresentação.

Os exemplos são registros reais de 21 e 22/10/2026, preservados sem edição em
`backend/web/demo/demo.json`. O modo offline reproduz esses registros: não recebe
perguntas livres, não lê novas fotos e não gera novas respostas ou animações.
As avaliações “Ajudou / Não ajudou / Tem erro” são apenas visuais e não são salvas.
As animações são evidências do protótipo de outubro, não uma avaliação do fluxo atual.

Para regenerar após mudar os dados ou a interface, na raiz do projeto:

```powershell
.venv\Scripts\python scripts\demo_apresentacao_offline.py
```

Os arquivos `apresentacao.html` e `apresentacao.js` são fontes para a geração;
leve para a apresentação o **TutorON-apresentacao-offline.html** gerado.
O arquivo anterior `TutorON-demo.html` foi preservado.

Verificação de 03/11/2026: as nove perguntas, as três rodadas da foto, o feedback
visual e a reinicialização foram conferidos no navegador. As três animações
reproduziram, e as imagens de reserva carregaram. Nenhuma fórmula apresentou
erro de renderização. A inspeção do HTML confirmou dez mídias e vinte fontes
embutidas, sem referências externas; a política da página bloqueia conexões.
A prévia foi testada por HTTP local; a abertura por `file://` não foi automatizada.
