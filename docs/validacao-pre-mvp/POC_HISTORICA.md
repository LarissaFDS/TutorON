# TutorON — PoC de RAG simulada em PAA

> **Comece por [PASSO_A_PASSO.md](PASSO_A_PASSO.md)**: como abrir, testar, atualizar o acervo e preparar o treinamento. Execute `iniciar_validacao.bat` para abrir a comparação A/B. Detalhes técnicos em [docs/ACERVO_LOCAL.md](docs/ACERVO_LOCAL.md); resultados e pendências em [RELATORIO_QUINTA.md](RELATORIO_QUINTA.md). A PoC documentada abaixo foi preservada nos caminhos originais.

**A pergunta que esta PoC responde:** adicionar contexto acadêmico específico de PAA melhora de forma perceptível a qualidade das respostas do TutorON em comparação com um prompt genérico?

A recuperação é simulada à mão: para cada pergunta, os trechos que uma RAG deveria encontrar já estão escolhidos em `materiais/`. O fluxo simulado é:

```
pergunta → [recuperação simulada: materiais/cXX] → contexto + pergunta → Gemini → resposta
```

Isto **não** é a implementação da RAG. Não há banco vetorial, embeddings nem pipeline.

---

## 1. Como rodar (5 minutos)

### Opção A: com chave da API do Gemini (recomendado)

```bash
pip install google-genai
export GEMINI_API_KEY="sua-chave"      # gere em https://aistudio.google.com/apikey
python run_demo.py                     # 4 questões × 2 cenários = 8 chamadas
python run_demo.py --controle --juiz   # versão completa (ver seção 3)
```

O relatório sai em `resultados/<data-hora>/relatorio.html`. Abra no navegador e apresente direto dele.

Outras opções: `--model gemini-2.5-pro` (o padrão é `gemini-2.5-flash`; se o nome não existir mais, o script escolhe automaticamente um modelo *flash* disponível), `--questoes Q1,Q4`.

### Opção B: sem chave, usando o Google AI Studio na mão

```bash
python run_demo.py --dry-run          # gera prompts_gerados/Q1_generico.txt, Q1_estruturado.txt, ...
```
1. Para cada arquivo, abra um **chat novo** no AI Studio com o mesmo modelo e temperatura 0.2.
2. No cenário estruturado, cole o bloco `SYSTEM INSTRUCTION` em *System instructions* e o bloco `PROMPT` no chat. No genérico, cole só o prompt.
3. Salve cada resposta em `respostas_manuais/Q1_generico.md`, `respostas_manuais/Q1_estruturado.md`, etc.
4. Rode `python run_demo.py --importar respostas_manuais` para gerar o mesmo relatório.

### Checagem do próprio kit
`python teste_checkpoints.py` confere se o checklist automático reconhece as formas usuais de escrita (LaTeX, markdown). `python run_demo.py --mock` testa o pipeline com respostas falsas, marcadas como MOCK.

---

## 2. A demonstração: 4 questões reais da disciplina

Todas foram tiradas das provas e listas do Prof. Rian Gabriel Pinheiro que estão no projeto. Os trechos de contexto são transcrições fiéis, com a fonte no cabeçalho de cada arquivo em `materiais/`.

| # | Pergunta do aluno | Contexto (recuperação simulada) | O que ela testa |
|---|---|---|---|
| Q1 | Explicar e provar a corretude do **Algoritmo X** (maior elemento por divisão e conquista) | c01 enunciado da 1ª prova · c02 **resolução corrigida com nota 2,0** · c03 variantes em outras 3 provas | **Aderência à disciplina**: o gabarito segue Teorema → Caso base (`inicio = fim`) → Hipótese de indução → Passo indutivo, com **indução forte no tamanho do vetor**. |
| Q2 | Quantos asteriscos `ASTERISCO(n)` imprime, **mostrando a recorrência** | c04 enunciados das provas · c05 resolução da Lista 2 · c06 método de iteração da Lista 2 | **Aderência ao enunciado**: a resolução da lista dá só a fórmula fechada, mas a prova pede a recorrência. Resposta esperada: A(0)=0, A(n)=2A(n−1)+n ⇒ 2ⁿ⁺¹−n−2 (1, 4, 11, 26). |
| Q3 | Por que o força bruta do **COMPOSTO** não é polinomial se faz O(n) divisões | c07 Prova Final 2024 · c08 resolução da Lista 7 | **Vocabulário da disciplina**: tamanho da entrada em bits, b = log n ⇒ n = 2ᵇ, "pseudo-polinomial". Também mede **extrapolação**: citar o AKS está correto, mas o material não traz isso. |
| Q4 | Definir as classes **P, NP e NP-completo** | c09 resolução da Lista 7 (**contém uma definição imprecisa de NP**) · c10 enunciados de três 4ªs provas | **Risco de alucinação induzida pelo contexto**: a resolução de aluno diz que NP é "o conjunto dos problemas em que ninguém conseguiu comprovar se são polinomiais". O prompt estruturado instrui a corrigir e avisar. É o teste mais importante para uma RAG que vai indexar resoluções de alunos. |

### Os prompts
- **Cenário 1 (genérico):** só a pergunta, sem instrução de sistema.
- **Cenário 2 (estruturado + contexto):** instrução de sistema com o papel de tutor da disciplina e 6 regras (seguir o material, responder ao enunciado, citar `[cXX]`, desconfiar de resoluções de alunos, não inventar critérios do professor, formato de prova), depois `CONTEXTO ACADÊMICO`, depois `PERGUNTA DO ALUNO`. O texto completo está em `prompts.py` e aparece expandível no relatório.
- **Controle (opcional, `--controle`):** a mesma instrução do cenário 2, **sem** o contexto. Serve para separar o ganho que vem do *prompt bem escrito* do ganho que vem do *material da disciplina*. Sem esse controle, a equipe não consegue afirmar que foi o contexto que fez a diferença.

Mesmo modelo e mesma temperatura (0.2) em todos os cenários.

---

## 3. Como analisar

O relatório traz três camadas de evidência. Use todas.

**a) Checklist automático (objetivo).** Para cada questão há de 4 a 7 itens tirados do material, como "usa indução forte", "escreve A(n)=2A(n−1)+n", "NÃO repete a definição errada de NP". O resumo no topo mostra a cobertura por cenário. O checklist funciona por expressões regulares: ele indica tendências, mas quem decide é a leitura humana.

**b) Juiz cego (`--juiz`).** O próprio Gemini recebe o material, a pergunta e as duas respostas **anônimas e em ordem aleatória**. Ele dá notas de 1 a 5 nos 7 critérios da PoC (precisão, clareza, aderência à disciplina, aderência ao enunciado, uso do material, especificidade e ausência de alucinação) e lista as afirmações problemáticas. Ressalva: um modelo avaliando o próprio modelo tem viés. Trate como segunda opinião.

**c) Leitura humana (decisiva).** Ideal: dois membros da equipe leem cada par de respostas sem saber qual é qual e anotam no campo *Notas da equipe* do relatório. Perguntas-guia:

| Critério | Pergunta |
|---|---|
| Precisão | Há algum erro técnico? |
| Clareza | Um aluno de PAA entenderia e conseguiria reproduzir na prova? |
| Aderência à disciplina | A resposta segue a estrutura e a notação do gabarito e das listas? |
| Aderência ao enunciado | Faz exatamente o que a prova pede ("mostre a recorrência", "prove")? |
| Uso do material | Cita e usa algo que só existe no material (`[c02]`, os valores 1, 4, 11, 26, "pseudo-polinomial")? |
| Resposta genérica | Traz material de livro-texto que não foi pedido? |
| Alucinação | Inventa algo sobre a disciplina ou repete o erro de c09? |

### O que esperar (hipóteses a confirmar, não resultados)
- **Q1 e Q2:** é onde a diferença deve aparecer mais. O genérico tende a dar uma prova correta, mas em outro formato (indução fraca, invariante, "por construção") e a responder só "Θ(2ⁿ)" ou a fórmula sem a recorrência.
- **Q3:** as duas respostas devem estar corretas. O ganho esperado está no vocabulário ("pseudo-polinomial") e no foco. Se o genérico citar o AKS, isso é correto, mas fora do escopo.
- **Q4:** o teste decisivo é se o cenário 2 **copia** o erro de c09 ou **corrige e avisa**. Se copiar, isso também é um achado valioso: significa que a futura RAG precisa de curadoria dos materiais e não pode confiar só no prompt.

Um resultado honesto pode ser: "o contexto ajuda muito em Q1/Q2, pouco em Q3, e em Q4 depende do prompt". Esse resultado continua justificando a RAG, com requisitos mais claros.

---

## 4. Conclusão: o que a PoC permite afirmar e os próximos passos

**Critério de decisão sugerido:** a abordagem se justifica se o cenário 2 superar o genérico em **aderência à disciplina e ao enunciado** em pelo menos 3 das 4 questões, **sem perder precisão**, e se esse ganho **não** aparecer só no controle (ou seja, se vier do contexto e não apenas do prompt).

**O que a PoC não prova:** que a recuperação automática vai encontrar os trechos certos, porque aqui eles foram escolhidos à mão. Com 4 questões e uma execução, também não há significância estatística. É uma demonstração qualitativa.

### Achados sobre a base, já observados ao montar a PoC (independem do Gemini)
1. **Parte do acervo não tem texto extraível.** `prova_1_A.pdf`, `prova_21.pdf`, `prova_2_A.pdf` e `Respostas_prova_2_PAA.pdf` são digitalizações que retornam 0 palavras. Todas as fotos de WhatsApp e os gabaritos manuscritos também. Sem OCR, a RAG não enxerga esse material, e ele inclui justamente os gabaritos corrigidos pelo professor, que são o conteúdo mais valioso.
2. **Resoluções de alunos contêm erros** (caso c09). O material precisa de metadados de confiabilidade: prova ou enunciado, resolução corrigida pelo professor com nota, resolução de aluno sem revisão.
3. **Há muita repetição de questões entre semestres** (Algoritmo X em 4 provas, ASTERISCO em 3, "Defina P, NP" em 3). Isso favorece bastante a RAG: a pergunta do aluno costuma ter um "gêmeo" na base.

### Próximos passos para virar uma RAG real (não implementados agora)
1. **Ingestão e OCR:** extrair texto de PDFs e imagens (OCR com suporte a manuscrito e fórmulas; o próprio Gemini multimodal é uma opção) e revisar por amostragem.
2. **Chunking por questão:** um chunk por questão ou resolução, como em `materiais/`, com metadados `fonte`, `tipo`, `tópico`, `semestre` e `confiabilidade`. O formato destes arquivos já é o esquema proposto.
3. **Indexação:** embeddings (por exemplo, `gemini-embedding`) em um índice simples (pgvector, Chroma ou até FAISS local para começar) combinados com busca por palavra-chave, porque nomes como "ASTERISCO" e "Algoritmo X" são exatos.
4. **Recuperação e ranqueamento:** top-k com preferência por gabaritos corrigidos pelo professor e diversidade de fontes (enunciado + resolução).
5. **Avaliação contínua:** transformar este kit em um conjunto de testes. As questões de `questoes.json`, com o checklist, viram casos de regressão, acrescidos de uma métrica de recuperação ("o chunk certo apareceu no top-k?"). Sem nenhum código novo, basta trocar a recuperação manual pela automática e comparar com esta linha de base.

---

## Estrutura

```
materiais/            10 trechos da base (simulam o que a RAG recuperaria), com a fonte no cabeçalho
questoes.json         as 4 questões: pergunta, ids de contexto e checklist
prompts.py            prompt genérico, prompt estruturado e controle
run_demo.py           executa, avalia e gera o relatório HTML
teste_checkpoints.py  sanidade do checklist
respostas_manuais/    (opção B) cole aqui as respostas do AI Studio
resultados/           relatórios gerados
```

Interface e organização do restante do repositório:

```
acervo/               pipeline do acervo local; acervo/web/ tem a página de validação com alunos
design/               design system (tokens, componentes, renderizador de respostas); regras em DESIGN.md
frontend/             CLI que conversa com o backend FastAPI
backend/              API FastAPI; check_supabase.py e smoke_check.py são checagens manuais
01-extraido … 07-validacao-alunos/   dados do pipeline, na ordem em que são produzidos
```

Antes de criar ou mudar uma tela, leia [DESIGN.md](DESIGN.md).
