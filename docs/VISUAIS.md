# Visuais na própria conversa

Há duas entradas separadas. Em **Tirar dúvida**, o tipo de ajuda começa em **O tutor escolhe**, inclusive ao abrir links antigos com `?visual=1`. Depois da ajuda em texto, **Quer entender visualmente?** usa a pergunta, a tentativa e a explicação já recebida para gerar um vídeo na própria conversa. O aluno pode escolher outro tipo de ajuda manualmente.

Na aba **Aprender com desenhos** (`/visuais`), o aluno escreve uma pergunta livre e pode adicionar código, enunciado ou tentativa. **Explicar com um desenho** pede uma pista visual diretamente, sem gerar uma resposta textual antes. A disciplina é automática por padrão, com correção manual opcional.

Os sete temas anteriores ficam abaixo do formulário como recomendações opcionais: robô/DP, fluxo residual, Karnaugh, circuito/tabela-verdade, BFS, certificados em grafos e reduções. Nenhum é selecionado por padrão. Clicar abre o exemplo controlado; **Usar como ponto de partida** copia uma pergunta editável para o formulário livre, sem enviar. As recomendações não aparecem no formulário de **Tirar dúvida** e não alteram seu tipo de ajuda.

A foto já conferida e o código/tentativa colados acompanham o pedido visual em campos separados. A animação direta não precisa gerar antes uma resposta textual. Depois de uma resposta, a ajuda já recebida também acompanha o planejamento do desenho.

## Disciplina opcional

O padrão é **Identificar automaticamente**. O servidor procura sinais do enunciado e, quando necessário, da tentativa/foto confirmada para escolher entre PAA e Sistemas Digitais. A disciplina identificada aparece junto à resposta. Você pode escolher manualmente para corrigir.

O identificador é conservador e usa regras de vocabulário; não é um classificador universal. Se a dúvida for vaga ou misturar sinais das duas disciplinas, o servidor pede esclarecimento ou escolha manual, sem consultar silenciosamente um acervo aleatório. Clientes antigos que omitem a disciplina continuam com PAA como antes. A foto é primeiro transcrita e conferida; a inferência da disciplina ocorre ao enviar a pergunta com essa leitura.

## Como a animação se adapta

O planejador recebe o enunciado atual, a tentativa/código, a foto confirmada e a ajuda textual, quando houver. Ele produz dados JSON para um renderizador Manim, nunca código executável. Os formatos anteriores de árvore, vetor, grafo, tabela, grade, fluxo, Karnaugh, circuito e redução continuam disponíveis para problemas com dados adequados.

Para dúvidas conceituais sem valores, o formato **esquema** monta de dois a quatro blocos e relações com conteúdo da dúvida. Não precisa inventar números para preencher uma grade. Se uma primeira proposta falha, a reformulação simplifica a representação para blocos da mesma dúvida. Uma lacuna é normalizada para “Você completa ?”, impedindo que uma resposta escrita naquele campo apareça como se estivesse em branco. O layout respeita os níveis de dependência para não desenhar entradas independentes como uma sequência.

O roteiro é validado e revisado antes de renderizar. A revisão visual distingue dados de entrada, conceitos e lacunas de resultados calculados; continua recusando erros técnicos e soluções completas. Tanto a revisão quanto o planejador podem errar. Isso não garante um desenho correto para qualquer assunto.

Se as duas propostas falharem, o sistema explica que não conseguiu montar o desenho e pede que o aluno detalhe a relação ou o passo. **Não substitui a dúvida por um vídeo de tema fixo.**

## Onde ficou o catálogo anterior

A aba **Aprender com desenhos** foi mantida como uma área separada. Os exemplos controlados acompanham o formulário livre em `/visuais`; a rota técnica `/demo/visuais` também continua disponível. Não são usados como alternativa automática quando uma pergunta livre falha.

Os scripts e as evidências da demonstração anterior foram preservados. O arquivo offline alterado pelo usuário não foi modificado.

## Verificação

A bateria real adicional usou perguntas abertas de robô/DP, pilha de chamadas e registrador de estado, sem seleção de tema. As três propostas finais chegaram a vídeos em cerca de 10–11 segundos no modelo local sem raciocínio. Os roteiros e quadros finais foram inspecionados: são pistas parciais, não validação de aprendizagem nem cobertura de todos os temas.

Evidências da evolução e dos bloqueios ficam em `eval/results/visual-contextual-v1/`. Os ensaios iniciais foram mantidos, incluindo propostas rejeitadas. A implementação usa o modo JSON documentado pelo [Ollama](https://docs.ollama.com/capabilities/structured-outputs) e valida o conteúdo antes do Manim.
